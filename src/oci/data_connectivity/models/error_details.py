# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ErrorDetails(object):
    """
    The details of an error that occured.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ErrorDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param code:
            The value to assign to the code property of this ErrorDetails.
        :type code: str

        :param message:
            The value to assign to the message property of this ErrorDetails.
        :type message: str

        """
        self.swagger_types = {
            'code': 'str',
            'message': 'str'
        }

        self.attribute_map = {
            'code': 'code',
            'message': 'message'
        }

        self._code = None
        self._message = None

    @property
    def code(self):
        """
        **[Required]** Gets the code of this ErrorDetails.
        A short error code that defines the error, meant for programmatic parsing. See
        `API Errors`__.

        __ https://docs.cloud.oracle.com/Content/API/References/apierrors.htm


        :return: The code of this ErrorDetails.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this ErrorDetails.
        A short error code that defines the error, meant for programmatic parsing. See
        `API Errors`__.

        __ https://docs.cloud.oracle.com/Content/API/References/apierrors.htm


        :param code: The code of this ErrorDetails.
        :type: str
        """
        self._code = code

    @property
    def message(self):
        """
        **[Required]** Gets the message of this ErrorDetails.
        A user-friendly error message.


        :return: The message of this ErrorDetails.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this ErrorDetails.
        A user-friendly error message.


        :param message: The message of this ErrorDetails.
        :type: str
        """
        self._message = message

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other