# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .abstract_frequency_details import AbstractFrequencyDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CustomFrequencyDetails(AbstractFrequencyDetails):
    """
    Frequency details model to set cron-based frequency
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CustomFrequencyDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.CustomFrequencyDetails.model_type` attribute
        of this class is ``CUSTOM`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this CustomFrequencyDetails.
            Allowed values for this property are: "HOURLY", "DAILY", "MONTHLY", "WEEKLY", "MONTHLY_RULE", "CUSTOM"
        :type model_type: str

        :param frequency:
            The value to assign to the frequency property of this CustomFrequencyDetails.
            Allowed values for this property are: "HOURLY", "DAILY", "MONTHLY", "WEEKLY", "CUSTOM"
        :type frequency: str

        :param custom_expression:
            The value to assign to the custom_expression property of this CustomFrequencyDetails.
        :type custom_expression: str

        """
        self.swagger_types = {
            'model_type': 'str',
            'frequency': 'str',
            'custom_expression': 'str'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'frequency': 'frequency',
            'custom_expression': 'customExpression'
        }

        self._model_type = None
        self._frequency = None
        self._custom_expression = None
        self._model_type = 'CUSTOM'

    @property
    def custom_expression(self):
        """
        Gets the custom_expression of this CustomFrequencyDetails.
        This holds the complete cron expression for this schedule, for example, 10 0/5 * * * ? that fires every 5 minutes, at 10 seconds after the minute (i.e. 10:00:10 am, 10:05:10 am, etc.)


        :return: The custom_expression of this CustomFrequencyDetails.
        :rtype: str
        """
        return self._custom_expression

    @custom_expression.setter
    def custom_expression(self, custom_expression):
        """
        Sets the custom_expression of this CustomFrequencyDetails.
        This holds the complete cron expression for this schedule, for example, 10 0/5 * * * ? that fires every 5 minutes, at 10 seconds after the minute (i.e. 10:00:10 am, 10:05:10 am, etc.)


        :param custom_expression: The custom_expression of this CustomFrequencyDetails.
        :type: str
        """
        self._custom_expression = custom_expression

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
