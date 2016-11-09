#---------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#---------------------------------------------------------------------------------------------

# pylint: disable=no-self-use,too-few-public-methods
from __future__ import print_function
from azure.cli.core.help_files import helps #pylint: disable=unused-import
from azure.cli.core.commands import cli_command #pylint: disable=unused-import
from azure.cli.core.application import Configuration
from azure.cli.core._help import ArgumentGroupRegistry
from azure.cli.core.parser import AzCliCommandParser

import os
import azure.cli.core.application as application
import azure.cli.core._help as _help
import azure.cli.core.commands as commands


def generate_review_sheet(root_group, exclude_prompts=False):

    config = Configuration([])
    cmd_table = commands.get_command_table()
    cmd_list = cmd_table.keys()
    filtered_cmd_listed = [cmd_name for cmd_name in cmd_table.keys() if root_group is None or cmd_name.split()[0] in root_group]

    my_application = application.Application(config)
    my_application.parser.load_command_table(cmd_table)

    for cmd in filtered_cmd_listed:
        print('\n================================================================================')
        print('=== CURRENT HELP === $ az {} -h'.format(cmd))
        print('================================================================================')

        cmd_string = 'az {} -h'.format(cmd)
        os.system(cmd_string)
        
        print('\n********************************************************************************')
   
        # need to do this recursively and not just one level
        my_subparser = my_application.parser._get_subparser(cmd.split())
        this_parser = my_subparser.choices[cmd.split()[1]]
        help_file = _help.CommandHelpFile(' '.join(cmd.split()), this_parser)
        help_file.load(this_parser)

        print('*** {}:short: {}'.format(cmd, help_file.short_summary or None))
        print('*** Change to : ')
        print('***')
        print('*** {}:long: {}'.format(cmd, help_file.long_summary or None))
        print('*** Change to : ')
        print('***')
        print('*** {}:examples: {}'.format(cmd, help_file.examples or None))
        print('*** Change to : ')
        print('***')

        for thisparam in help_file.parameters:
            if (thisparam.group_name == 'Global Arguments'):
                continue
            if (thisparam.group_name == 'Resource Id Arguments'):
                continue

            print ('*** {}:{}:short: {}'.format(cmd, thisparam.name, thisparam.short_summary or None))
            print('*** Change to : ')
            print('***')
            print ('*** {}:{}:long: {}'.format(cmd, thisparam.name, thisparam.long_summary or None))
            print('*** Change to : ')
            print('***')

        print('********************************************************************************', flush=True) #pylint: disable=line-too-long

def import_review_sheet():
    print("Not implemented")


cli_command('docbuilder review-sheet generate', generate_review_sheet)
cli_command('docbuilder review-sheet import', import_review_sheet)
