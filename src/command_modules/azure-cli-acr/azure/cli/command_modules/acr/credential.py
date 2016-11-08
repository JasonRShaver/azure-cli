#---------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#---------------------------------------------------------------------------------------------

from azure.cli.core.commands import cli_command

from ._factory import get_acr_service_client
from ._utils import get_resource_group_name_by_registry_name
from ._format import output_format

import azure.cli.core._logging as _logging
logger = _logging.get_az_logger(__name__)

def acr_credential_show(registry_name, resource_group_name=None):
    '''Get login credentials for a container registry.
    :param str registry_name: The name of container registry
    :param str resource_group_name: The name of resource group
    '''
    if resource_group_name is None:
        resource_group_name = get_resource_group_name_by_registry_name(registry_name)

    client = get_acr_service_client().registries

    return client.get_credentials(resource_group_name, registry_name)

def acr_credential_renew(registry_name, resource_group_name=None):
    '''Regenerate login credentials for a container registry.
    :param str registry_name: The name of container registry
    :param str resource_group_name: The name of resource group
    '''
    if resource_group_name is None:
        resource_group_name = get_resource_group_name_by_registry_name(registry_name)

    client = get_acr_service_client().registries

    return client.regenerate_credentials(resource_group_name, registry_name)

cli_command('acr credential show', acr_credential_show, table_transformer=output_format)
cli_command('acr credential renew', acr_credential_renew, table_transformer=output_format)
