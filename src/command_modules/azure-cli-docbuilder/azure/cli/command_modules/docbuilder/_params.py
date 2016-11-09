#---------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#---------------------------------------------------------------------------------------------

from azure.cli.core.commands import register_cli_argument

from azure.cli.core.cloud import get_clouds
from azure.cli.core.context import get_contexts

# pylint: disable=line-too-long

register_cli_argument('docbuilder review-sheet generate', 'root_group', options_list=('--group', '-g'), help='Root command group to generate sheet for, such as "network dns"')
register_cli_argument('docbuilder review-sheet generate', 'exclude_prompts', action='store_true', help='Will generate sample output, but not content prompts for importing')
