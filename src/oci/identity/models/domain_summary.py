# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DomainSummary(object):
    """
    As the name suggests, a `DomainSummary` object contains information about a `Domain`.
    """

    #: A constant which can be used with the type property of a DomainSummary.
    #: This constant has a value of "DEFAULT"
    TYPE_DEFAULT = "DEFAULT"

    #: A constant which can be used with the type property of a DomainSummary.
    #: This constant has a value of "SECONDARY"
    TYPE_SECONDARY = "SECONDARY"

    #: A constant which can be used with the lifecycle_state property of a DomainSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a DomainSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a DomainSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a DomainSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_details property of a DomainSummary.
    #: This constant has a value of "DEACTIVATING"
    LIFECYCLE_DETAILS_DEACTIVATING = "DEACTIVATING"

    #: A constant which can be used with the lifecycle_details property of a DomainSummary.
    #: This constant has a value of "ACTIVATING"
    LIFECYCLE_DETAILS_ACTIVATING = "ACTIVATING"

    #: A constant which can be used with the lifecycle_details property of a DomainSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_DETAILS_UPDATING = "UPDATING"

    def __init__(self, **kwargs):
        """
        Initializes a new DomainSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DomainSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DomainSummary.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this DomainSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this DomainSummary.
        :type description: str

        :param url:
            The value to assign to the url property of this DomainSummary.
        :type url: str

        :param home_region_url:
            The value to assign to the home_region_url property of this DomainSummary.
        :type home_region_url: str

        :param home_region:
            The value to assign to the home_region property of this DomainSummary.
        :type home_region: str

        :param replica_regions:
            The value to assign to the replica_regions property of this DomainSummary.
        :type replica_regions: list[oci.identity.models.ReplicatedRegionDetails]

        :param type:
            The value to assign to the type property of this DomainSummary.
            Allowed values for this property are: "DEFAULT", "SECONDARY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param license_type:
            The value to assign to the license_type property of this DomainSummary.
        :type license_type: str

        :param is_hidden_on_login:
            The value to assign to the is_hidden_on_login property of this DomainSummary.
        :type is_hidden_on_login: bool

        :param time_created:
            The value to assign to the time_created property of this DomainSummary.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DomainSummary.
            Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "INACTIVE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this DomainSummary.
            Allowed values for this property are: "DEACTIVATING", "ACTIVATING", "UPDATING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DomainSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this DomainSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'url': 'str',
            'home_region_url': 'str',
            'home_region': 'str',
            'replica_regions': 'list[ReplicatedRegionDetails]',
            'type': 'str',
            'license_type': 'str',
            'is_hidden_on_login': 'bool',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'url': 'url',
            'home_region_url': 'homeRegionUrl',
            'home_region': 'homeRegion',
            'replica_regions': 'replicaRegions',
            'type': 'type',
            'license_type': 'licenseType',
            'is_hidden_on_login': 'isHiddenOnLogin',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._url = None
        self._home_region_url = None
        self._home_region = None
        self._replica_regions = None
        self._type = None
        self._license_type = None
        self._is_hidden_on_login = None
        self._time_created = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DomainSummary.
        The OCID of the domain


        :return: The id of this DomainSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DomainSummary.
        The OCID of the domain


        :param id: The id of this DomainSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this DomainSummary.
        The OCID of the comparment containing the domain.


        :return: The compartment_id of this DomainSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DomainSummary.
        The OCID of the comparment containing the domain.


        :param compartment_id: The compartment_id of this DomainSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this DomainSummary.
        The mutable display name of the domain


        :return: The display_name of this DomainSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DomainSummary.
        The mutable display name of the domain


        :param display_name: The display_name of this DomainSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        **[Required]** Gets the description of this DomainSummary.
        The domain descripition


        :return: The description of this DomainSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DomainSummary.
        The domain descripition


        :param description: The description of this DomainSummary.
        :type: str
        """
        self._description = description

    @property
    def url(self):
        """
        **[Required]** Gets the url of this DomainSummary.
        Region agnostic domain URL.


        :return: The url of this DomainSummary.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this DomainSummary.
        Region agnostic domain URL.


        :param url: The url of this DomainSummary.
        :type: str
        """
        self._url = url

    @property
    def home_region_url(self):
        """
        **[Required]** Gets the home_region_url of this DomainSummary.
        Region specific domain URL.


        :return: The home_region_url of this DomainSummary.
        :rtype: str
        """
        return self._home_region_url

    @home_region_url.setter
    def home_region_url(self, home_region_url):
        """
        Sets the home_region_url of this DomainSummary.
        Region specific domain URL.


        :param home_region_url: The home_region_url of this DomainSummary.
        :type: str
        """
        self._home_region_url = home_region_url

    @property
    def home_region(self):
        """
        **[Required]** Gets the home_region of this DomainSummary.
        The home region for the domain.


        :return: The home_region of this DomainSummary.
        :rtype: str
        """
        return self._home_region

    @home_region.setter
    def home_region(self, home_region):
        """
        Sets the home_region of this DomainSummary.
        The home region for the domain.


        :param home_region: The home_region of this DomainSummary.
        :type: str
        """
        self._home_region = home_region

    @property
    def replica_regions(self):
        """
        **[Required]** Gets the replica_regions of this DomainSummary.
        The regions domain is replicated to.


        :return: The replica_regions of this DomainSummary.
        :rtype: list[oci.identity.models.ReplicatedRegionDetails]
        """
        return self._replica_regions

    @replica_regions.setter
    def replica_regions(self, replica_regions):
        """
        Sets the replica_regions of this DomainSummary.
        The regions domain is replicated to.


        :param replica_regions: The replica_regions of this DomainSummary.
        :type: list[oci.identity.models.ReplicatedRegionDetails]
        """
        self._replica_regions = replica_regions

    @property
    def type(self):
        """
        **[Required]** Gets the type of this DomainSummary.
        The type of the domain.

        Allowed values for this property are: "DEFAULT", "SECONDARY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this DomainSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this DomainSummary.
        The type of the domain.


        :param type: The type of this DomainSummary.
        :type: str
        """
        allowed_values = ["DEFAULT", "SECONDARY"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def license_type(self):
        """
        **[Required]** Gets the license_type of this DomainSummary.
        The License type of Domain


        :return: The license_type of this DomainSummary.
        :rtype: str
        """
        return self._license_type

    @license_type.setter
    def license_type(self, license_type):
        """
        Sets the license_type of this DomainSummary.
        The License type of Domain


        :param license_type: The license_type of this DomainSummary.
        :type: str
        """
        self._license_type = license_type

    @property
    def is_hidden_on_login(self):
        """
        **[Required]** Gets the is_hidden_on_login of this DomainSummary.
        Indicates whether domain is hidden on login screen or not.


        :return: The is_hidden_on_login of this DomainSummary.
        :rtype: bool
        """
        return self._is_hidden_on_login

    @is_hidden_on_login.setter
    def is_hidden_on_login(self, is_hidden_on_login):
        """
        Sets the is_hidden_on_login of this DomainSummary.
        Indicates whether domain is hidden on login screen or not.


        :param is_hidden_on_login: The is_hidden_on_login of this DomainSummary.
        :type: bool
        """
        self._is_hidden_on_login = is_hidden_on_login

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this DomainSummary.
        Date and time the domain was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this DomainSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DomainSummary.
        Date and time the domain was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this DomainSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this DomainSummary.
        The current state.

        Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "INACTIVE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DomainSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DomainSummary.
        The current state.


        :param lifecycle_state: The lifecycle_state of this DomainSummary.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "DELETING", "INACTIVE"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this DomainSummary.
        Any additional details about the current state of the Domain.

        Allowed values for this property are: "DEACTIVATING", "ACTIVATING", "UPDATING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_details of this DomainSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this DomainSummary.
        Any additional details about the current state of the Domain.


        :param lifecycle_details: The lifecycle_details of this DomainSummary.
        :type: str
        """
        allowed_values = ["DEACTIVATING", "ACTIVATING", "UPDATING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_details, allowed_values):
            lifecycle_details = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this DomainSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this DomainSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this DomainSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this DomainSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this DomainSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this DomainSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this DomainSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this DomainSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
