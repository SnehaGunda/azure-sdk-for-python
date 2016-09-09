# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import ServiceClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.lab_operations import LabOperations
from .operations.artifact_source_operations import ArtifactSourceOperations
from .operations.artifact_operations import ArtifactOperations
from .operations.cost_operations import CostOperations
from .operations.custom_image_operations import CustomImageOperations
from .operations.formula_operations import FormulaOperations
from .operations.gallery_image_operations import GalleryImageOperations
from .operations.policy_set_operations import PolicySetOperations
from .operations.policy_operations import PolicyOperations
from .operations.schedule_operations import ScheduleOperations
from .operations.virtual_machine_operations import VirtualMachineOperations
from .operations.virtual_network_operations import VirtualNetworkOperations
from . import models


class DevTestLabsClientConfiguration(AzureConfiguration):
    """Configuration for DevTestLabsClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param accept_language: Gets or sets the preferred language for the
     response.
    :type accept_language: str
    :param long_running_operation_retry_timeout: Gets or sets the retry
     timeout in seconds for Long Running Operations. Default value is 30.
    :type long_running_operation_retry_timeout: int
    :param generate_client_request_id: When set to true a unique
     x-ms-client-request-id value is generated and included in each request.
     Default is true.
    :type generate_client_request_id: bool
    :param str base_url: Service URL
    :param str filepath: Existing config
    """

    def __init__(
            self, credentials, subscription_id, api_version='2016-05-15', accept_language='en-US', long_running_operation_retry_timeout=30, generate_client_request_id=True, base_url=None, filepath=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if api_version is not None and not isinstance(api_version, str):
            raise TypeError("Optional parameter 'api_version' must be str.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not isinstance(subscription_id, str):
            raise TypeError("Parameter 'subscription_id' must be str.")
        if accept_language is not None and not isinstance(accept_language, str):
            raise TypeError("Optional parameter 'accept_language' must be str.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(DevTestLabsClientConfiguration, self).__init__(base_url, filepath)

        self.add_user_agent('devtestlabsclient/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.api_version = api_version
        self.subscription_id = subscription_id
        self.accept_language = accept_language
        self.long_running_operation_retry_timeout = long_running_operation_retry_timeout
        self.generate_client_request_id = generate_client_request_id


class DevTestLabsClient(object):
    """The DevTest Labs Client.

    :ivar config: Configuration for client.
    :vartype config: DevTestLabsClientConfiguration

    :ivar lab: Lab operations
    :vartype lab: .operations.LabOperations
    :ivar artifact_source: ArtifactSource operations
    :vartype artifact_source: .operations.ArtifactSourceOperations
    :ivar artifact: Artifact operations
    :vartype artifact: .operations.ArtifactOperations
    :ivar cost: Cost operations
    :vartype cost: .operations.CostOperations
    :ivar custom_image: CustomImage operations
    :vartype custom_image: .operations.CustomImageOperations
    :ivar formula: Formula operations
    :vartype formula: .operations.FormulaOperations
    :ivar gallery_image: GalleryImage operations
    :vartype gallery_image: .operations.GalleryImageOperations
    :ivar policy_set: PolicySet operations
    :vartype policy_set: .operations.PolicySetOperations
    :ivar policy: Policy operations
    :vartype policy: .operations.PolicyOperations
    :ivar schedule: Schedule operations
    :vartype schedule: .operations.ScheduleOperations
    :ivar virtual_machine: VirtualMachine operations
    :vartype virtual_machine: .operations.VirtualMachineOperations
    :ivar virtual_network: VirtualNetwork operations
    :vartype virtual_network: .operations.VirtualNetworkOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param accept_language: Gets or sets the preferred language for the
     response.
    :type accept_language: str
    :param long_running_operation_retry_timeout: Gets or sets the retry
     timeout in seconds for Long Running Operations. Default value is 30.
    :type long_running_operation_retry_timeout: int
    :param generate_client_request_id: When set to true a unique
     x-ms-client-request-id value is generated and included in each request.
     Default is true.
    :type generate_client_request_id: bool
    :param str base_url: Service URL
    :param str filepath: Existing config
    """

    def __init__(
            self, credentials, subscription_id, api_version='2016-05-15', accept_language='en-US', long_running_operation_retry_timeout=30, generate_client_request_id=True, base_url=None, filepath=None):

        self.config = DevTestLabsClientConfiguration(credentials, subscription_id, api_version, accept_language, long_running_operation_retry_timeout, generate_client_request_id, base_url, filepath)
        self._client = ServiceClient(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.lab = LabOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.artifact_source = ArtifactSourceOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.artifact = ArtifactOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.cost = CostOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.custom_image = CustomImageOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.formula = FormulaOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.gallery_image = GalleryImageOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.policy_set = PolicySetOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.policy = PolicyOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.schedule = ScheduleOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.virtual_machine = VirtualMachineOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.virtual_network = VirtualNetworkOperations(
            self._client, self.config, self._serialize, self._deserialize)
