#---------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#---------------------------------------------------------------------------------------------

from azure.cli.core.help_files import helps #pylint: disable=unused-import

#pylint: disable=line-too-long

helps['docbuilder'] = """
    type: group
    short-summary: Helps build and update CLI documentation
"""

helps['docbuilder review-sheet'] = """
    type: group
    short-summary: Review sheets allow quick auditing of CLI documentation
"""

helps['docbuilder review-sheet generate'] = """
    type: command
    short-summary: Create a new review sheet to review and complete
    parameters:
        - name: --group -g
          type: string
"""


helps['docbuilder review-sheet import'] = """
    type: command
    short-summary: Process a completed review sheet and modifies nnecessary help files
"""
