# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CertificateSubjectAlternativeName(object):
    """
    A subject alternative name for the certificate that binds additional or alternate names to the subject of the certificate. In the certificate, the alternate subject name format is \"type:name\".
    """

    #: A constant which can be used with the type property of a CertificateSubjectAlternativeName.
    #: This constant has a value of "DNS"
    TYPE_DNS = "DNS"

    #: A constant which can be used with the type property of a CertificateSubjectAlternativeName.
    #: This constant has a value of "IP"
    TYPE_IP = "IP"

    def __init__(self, **kwargs):
        """
        Initializes a new CertificateSubjectAlternativeName object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this CertificateSubjectAlternativeName.
            Allowed values for this property are: "DNS", "IP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param value:
            The value to assign to the value property of this CertificateSubjectAlternativeName.
        :type value: str

        """
        self.swagger_types = {
            'type': 'str',
            'value': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'value': 'value'
        }

        self._type = None
        self._value = None

    @property
    def type(self):
        """
        **[Required]** Gets the type of this CertificateSubjectAlternativeName.
        The subject alternative name type. Currently only DNS domain or host names and IP addresses are supported.

        Allowed values for this property are: "DNS", "IP", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this CertificateSubjectAlternativeName.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CertificateSubjectAlternativeName.
        The subject alternative name type. Currently only DNS domain or host names and IP addresses are supported.


        :param type: The type of this CertificateSubjectAlternativeName.
        :type: str
        """
        allowed_values = ["DNS", "IP"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def value(self):
        """
        **[Required]** Gets the value of this CertificateSubjectAlternativeName.
        The subject alternative name.


        :return: The value of this CertificateSubjectAlternativeName.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this CertificateSubjectAlternativeName.
        The subject alternative name.


        :param value: The value of this CertificateSubjectAlternativeName.
        :type: str
        """
        self._value = value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
