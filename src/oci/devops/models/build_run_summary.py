# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BuildRunSummary(object):
    """
    Summary of the BuildRun.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BuildRunSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this BuildRunSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this BuildRunSummary.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this BuildRunSummary.
        :type display_name: str

        :param project_id:
            The value to assign to the project_id property of this BuildRunSummary.
        :type project_id: str

        :param build_pipeline_id:
            The value to assign to the build_pipeline_id property of this BuildRunSummary.
        :type build_pipeline_id: str

        :param build_run_source:
            The value to assign to the build_run_source property of this BuildRunSummary.
        :type build_run_source: oci.devops.models.BuildRunSource

        :param build_run_arguments:
            The value to assign to the build_run_arguments property of this BuildRunSummary.
        :type build_run_arguments: oci.devops.models.BuildRunArgumentCollection

        :param build_run_progress_summary:
            The value to assign to the build_run_progress_summary property of this BuildRunSummary.
        :type build_run_progress_summary: oci.devops.models.BuildRunProgressSummary

        :param time_created:
            The value to assign to the time_created property of this BuildRunSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this BuildRunSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this BuildRunSummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this BuildRunSummary.
        :type lifecycle_details: str

        :param commit_info:
            The value to assign to the commit_info property of this BuildRunSummary.
        :type commit_info: oci.devops.models.CommitInfo

        :param freeform_tags:
            The value to assign to the freeform_tags property of this BuildRunSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this BuildRunSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this BuildRunSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'project_id': 'str',
            'build_pipeline_id': 'str',
            'build_run_source': 'BuildRunSource',
            'build_run_arguments': 'BuildRunArgumentCollection',
            'build_run_progress_summary': 'BuildRunProgressSummary',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'commit_info': 'CommitInfo',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'project_id': 'projectId',
            'build_pipeline_id': 'buildPipelineId',
            'build_run_source': 'buildRunSource',
            'build_run_arguments': 'buildRunArguments',
            'build_run_progress_summary': 'buildRunProgressSummary',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'commit_info': 'commitInfo',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._project_id = None
        self._build_pipeline_id = None
        self._build_run_source = None
        self._build_run_arguments = None
        self._build_run_progress_summary = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._commit_info = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this BuildRunSummary.
        Unique identifier that is immutable on creation


        :return: The id of this BuildRunSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BuildRunSummary.
        Unique identifier that is immutable on creation


        :param id: The id of this BuildRunSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this BuildRunSummary.
        Compartment Identifier


        :return: The compartment_id of this BuildRunSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this BuildRunSummary.
        Compartment Identifier


        :param compartment_id: The compartment_id of this BuildRunSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this BuildRunSummary.
        BuildRun identifier which can be renamed and is not necessarily unique


        :return: The display_name of this BuildRunSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this BuildRunSummary.
        BuildRun identifier which can be renamed and is not necessarily unique


        :param display_name: The display_name of this BuildRunSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def project_id(self):
        """
        **[Required]** Gets the project_id of this BuildRunSummary.
        Project Identifier


        :return: The project_id of this BuildRunSummary.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """
        Sets the project_id of this BuildRunSummary.
        Project Identifier


        :param project_id: The project_id of this BuildRunSummary.
        :type: str
        """
        self._project_id = project_id

    @property
    def build_pipeline_id(self):
        """
        **[Required]** Gets the build_pipeline_id of this BuildRunSummary.
        Pipeline Identifier


        :return: The build_pipeline_id of this BuildRunSummary.
        :rtype: str
        """
        return self._build_pipeline_id

    @build_pipeline_id.setter
    def build_pipeline_id(self, build_pipeline_id):
        """
        Sets the build_pipeline_id of this BuildRunSummary.
        Pipeline Identifier


        :param build_pipeline_id: The build_pipeline_id of this BuildRunSummary.
        :type: str
        """
        self._build_pipeline_id = build_pipeline_id

    @property
    def build_run_source(self):
        """
        **[Required]** Gets the build_run_source of this BuildRunSummary.

        :return: The build_run_source of this BuildRunSummary.
        :rtype: oci.devops.models.BuildRunSource
        """
        return self._build_run_source

    @build_run_source.setter
    def build_run_source(self, build_run_source):
        """
        Sets the build_run_source of this BuildRunSummary.

        :param build_run_source: The build_run_source of this BuildRunSummary.
        :type: oci.devops.models.BuildRunSource
        """
        self._build_run_source = build_run_source

    @property
    def build_run_arguments(self):
        """
        Gets the build_run_arguments of this BuildRunSummary.

        :return: The build_run_arguments of this BuildRunSummary.
        :rtype: oci.devops.models.BuildRunArgumentCollection
        """
        return self._build_run_arguments

    @build_run_arguments.setter
    def build_run_arguments(self, build_run_arguments):
        """
        Sets the build_run_arguments of this BuildRunSummary.

        :param build_run_arguments: The build_run_arguments of this BuildRunSummary.
        :type: oci.devops.models.BuildRunArgumentCollection
        """
        self._build_run_arguments = build_run_arguments

    @property
    def build_run_progress_summary(self):
        """
        Gets the build_run_progress_summary of this BuildRunSummary.

        :return: The build_run_progress_summary of this BuildRunSummary.
        :rtype: oci.devops.models.BuildRunProgressSummary
        """
        return self._build_run_progress_summary

    @build_run_progress_summary.setter
    def build_run_progress_summary(self, build_run_progress_summary):
        """
        Sets the build_run_progress_summary of this BuildRunSummary.

        :param build_run_progress_summary: The build_run_progress_summary of this BuildRunSummary.
        :type: oci.devops.models.BuildRunProgressSummary
        """
        self._build_run_progress_summary = build_run_progress_summary

    @property
    def time_created(self):
        """
        Gets the time_created of this BuildRunSummary.
        The time the the BuildRun was created. An RFC3339 formatted datetime string


        :return: The time_created of this BuildRunSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this BuildRunSummary.
        The time the the BuildRun was created. An RFC3339 formatted datetime string


        :param time_created: The time_created of this BuildRunSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this BuildRunSummary.
        The time the BuildRun was updated. An RFC3339 formatted datetime string


        :return: The time_updated of this BuildRunSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this BuildRunSummary.
        The time the BuildRun was updated. An RFC3339 formatted datetime string


        :param time_updated: The time_updated of this BuildRunSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this BuildRunSummary.
        The current state of the BuildRun.


        :return: The lifecycle_state of this BuildRunSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this BuildRunSummary.
        The current state of the BuildRun.


        :param lifecycle_state: The lifecycle_state of this BuildRunSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this BuildRunSummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this BuildRunSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this BuildRunSummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this BuildRunSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def commit_info(self):
        """
        Gets the commit_info of this BuildRunSummary.

        :return: The commit_info of this BuildRunSummary.
        :rtype: oci.devops.models.CommitInfo
        """
        return self._commit_info

    @commit_info.setter
    def commit_info(self, commit_info):
        """
        Sets the commit_info of this BuildRunSummary.

        :param commit_info: The commit_info of this BuildRunSummary.
        :type: oci.devops.models.CommitInfo
        """
        self._commit_info = commit_info

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this BuildRunSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this BuildRunSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this BuildRunSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this BuildRunSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this BuildRunSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this BuildRunSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this BuildRunSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this BuildRunSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this BuildRunSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces. See `Resource Tags`__. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this BuildRunSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this BuildRunSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces. See `Resource Tags`__. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this BuildRunSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other