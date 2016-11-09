#---------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#---------------------------------------------------------------------------------------------

# pylint: disable=no-self-use,too-few-public-methods
from __future__ import print_function
from azure.cli.core.help_files import helps #pylint: disable=unused-import
from azure.cli.core.commands import cli_command #pylint: disable=unused-import
from azure.cli.core.application import Configuration

#from azure.cli.core.application import APPLICATION, Application
import os
import azure.cli.core.application as application

def dump_help():
    '''How to deploy an ARM template using Azure CLI.'''
    print("""
***********************
ARM Template Deployment
***********************

Could this be helpful?  Let us know!
====================================

1. First Step
2. Second Step

And you're done!
""")

from azure.cli.core._help import ArgumentGroupRegistry
#import azure.cli.core._help as helpcore

def generate_review_sheet(root_group, exclude_prompts=False):
    #cmd_table = APPLICATION.configuration.get_command_table()
    #print(cmd_table)
    cmd_set_names = root_group

    config = Configuration([root_group])
    application.APPLICATION = application.Application(config)
    cmd_table = config.get_command_table()
    cmd_list = sorted([cmd_name for cmd_name in cmd_table.keys() if cmd_set_names is None or cmd_name.split()[0] in cmd_set_names])

    #cmd_list = cmd_table.keys()

    for cmd in cmd_list:
        print('\n================================================================================')
        print('=== CURRENT HELP === $ az {} -h'.format(cmd))
        print('================================================================================')

        cmd_string = 'az {} -h'.format(cmd)
        os.system(cmd_string)

        print('\n********************************************************************************')
   
        #whateverthisis = [p.group_name for p in cmd_table[cmd].arguments if p.group_name]
        group_registry = ArgumentGroupRegistry(root_group)

        #cmd_name = [x for x in cmd_table.keys() if cmd == x][0]
        for arg in cmd_table[cmd].arguments:
            this_arg = cmd_table[cmd].arguments[arg]
            print('\n++++++++++ {} + {} ++++++++++'.format(cmd, this_arg.name))


            print(cmd_table[cmd].arguments[arg])
            #arghelp = cmd_table[cmd].arguments[arg].name
            print('+++ Currently + {}'.format(arghelp))
            print('+++ Change to + ')

        print('\n********************************************************************************', flush=True) #pylint: disable=line-too-long

    print("DONE")

def import_review_sheet():
    print("""
test
""")


cli_command('docbuilder review-sheet generate', generate_review_sheet)
cli_command('docbuilder review-sheet import', import_review_sheet)
