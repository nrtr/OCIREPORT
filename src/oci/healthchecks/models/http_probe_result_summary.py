# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HttpProbeResultSummary(object):
    """
    The results returned by running an HTTP probe.  All times and durations are
    returned in milliseconds. All times are relative to the POSIX epoch
    (1970-01-01T00:00Z). Time properties conform to W3C Resource Timing.
    For more information, see
    `PerformanceResourceTiming`__
    interface.

    __ https://w3c.github.io/resource-timing/#sec-resource-timing
    """

    #: A constant which can be used with the error_category property of a HttpProbeResultSummary.
    #: This constant has a value of "NONE"
    ERROR_CATEGORY_NONE = "NONE"

    #: A constant which can be used with the error_category property of a HttpProbeResultSummary.
    #: This constant has a value of "DNS"
    ERROR_CATEGORY_DNS = "DNS"

    #: A constant which can be used with the error_category property of a HttpProbeResultSummary.
    #: This constant has a value of "TRANSPORT"
    ERROR_CATEGORY_TRANSPORT = "TRANSPORT"

    #: A constant which can be used with the error_category property of a HttpProbeResultSummary.
    #: This constant has a value of "NETWORK"
    ERROR_CATEGORY_NETWORK = "NETWORK"

    #: A constant which can be used with the error_category property of a HttpProbeResultSummary.
    #: This constant has a value of "SYSTEM"
    ERROR_CATEGORY_SYSTEM = "SYSTEM"

    #: A constant which can be used with the protocol property of a HttpProbeResultSummary.
    #: This constant has a value of "HTTP"
    PROTOCOL_HTTP = "HTTP"

    #: A constant which can be used with the protocol property of a HttpProbeResultSummary.
    #: This constant has a value of "HTTPS"
    PROTOCOL_HTTPS = "HTTPS"

    def __init__(self, **kwargs):
        """
        Initializes a new HttpProbeResultSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this HttpProbeResultSummary.
        :type key: str

        :param probe_configuration_id:
            The value to assign to the probe_configuration_id property of this HttpProbeResultSummary.
        :type probe_configuration_id: str

        :param start_time:
            The value to assign to the start_time property of this HttpProbeResultSummary.
        :type start_time: float

        :param target:
            The value to assign to the target property of this HttpProbeResultSummary.
        :type target: str

        :param vantage_point_name:
            The value to assign to the vantage_point_name property of this HttpProbeResultSummary.
        :type vantage_point_name: str

        :param is_timed_out:
            The value to assign to the is_timed_out property of this HttpProbeResultSummary.
        :type is_timed_out: bool

        :param is_healthy:
            The value to assign to the is_healthy property of this HttpProbeResultSummary.
        :type is_healthy: bool

        :param error_category:
            The value to assign to the error_category property of this HttpProbeResultSummary.
            Allowed values for this property are: "NONE", "DNS", "TRANSPORT", "NETWORK", "SYSTEM", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type error_category: str

        :param error_message:
            The value to assign to the error_message property of this HttpProbeResultSummary.
        :type error_message: str

        :param protocol:
            The value to assign to the protocol property of this HttpProbeResultSummary.
            Allowed values for this property are: "HTTP", "HTTPS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type protocol: str

        :param connection:
            The value to assign to the connection property of this HttpProbeResultSummary.
        :type connection: oci.healthchecks.models.TcpConnection

        :param dns:
            The value to assign to the dns property of this HttpProbeResultSummary.
        :type dns: oci.healthchecks.models.DNS

        :param status_code:
            The value to assign to the status_code property of this HttpProbeResultSummary.
        :type status_code: int

        :param domain_lookup_start:
            The value to assign to the domain_lookup_start property of this HttpProbeResultSummary.
        :type domain_lookup_start: float

        :param domain_lookup_end:
            The value to assign to the domain_lookup_end property of this HttpProbeResultSummary.
        :type domain_lookup_end: float

        :param connect_start:
            The value to assign to the connect_start property of this HttpProbeResultSummary.
        :type connect_start: float

        :param secure_connection_start:
            The value to assign to the secure_connection_start property of this HttpProbeResultSummary.
        :type secure_connection_start: float

        :param connect_end:
            The value to assign to the connect_end property of this HttpProbeResultSummary.
        :type connect_end: float

        :param fetch_start:
            The value to assign to the fetch_start property of this HttpProbeResultSummary.
        :type fetch_start: float

        :param request_start:
            The value to assign to the request_start property of this HttpProbeResultSummary.
        :type request_start: float

        :param response_start:
            The value to assign to the response_start property of this HttpProbeResultSummary.
        :type response_start: float

        :param response_end:
            The value to assign to the response_end property of this HttpProbeResultSummary.
        :type response_end: float

        :param duration:
            The value to assign to the duration property of this HttpProbeResultSummary.
        :type duration: float

        :param encoded_body_size:
            The value to assign to the encoded_body_size property of this HttpProbeResultSummary.
        :type encoded_body_size: int

        """
        self.swagger_types = {
            'key': 'str',
            'probe_configuration_id': 'str',
            'start_time': 'float',
            'target': 'str',
            'vantage_point_name': 'str',
            'is_timed_out': 'bool',
            'is_healthy': 'bool',
            'error_category': 'str',
            'error_message': 'str',
            'protocol': 'str',
            'connection': 'TcpConnection',
            'dns': 'DNS',
            'status_code': 'int',
            'domain_lookup_start': 'float',
            'domain_lookup_end': 'float',
            'connect_start': 'float',
            'secure_connection_start': 'float',
            'connect_end': 'float',
            'fetch_start': 'float',
            'request_start': 'float',
            'response_start': 'float',
            'response_end': 'float',
            'duration': 'float',
            'encoded_body_size': 'int'
        }

        self.attribute_map = {
            'key': 'key',
            'probe_configuration_id': 'probeConfigurationId',
            'start_time': 'startTime',
            'target': 'target',
            'vantage_point_name': 'vantagePointName',
            'is_timed_out': 'isTimedOut',
            'is_healthy': 'isHealthy',
            'error_category': 'errorCategory',
            'error_message': 'errorMessage',
            'protocol': 'protocol',
            'connection': 'connection',
            'dns': 'dns',
            'status_code': 'statusCode',
            'domain_lookup_start': 'domainLookupStart',
            'domain_lookup_end': 'domainLookupEnd',
            'connect_start': 'connectStart',
            'secure_connection_start': 'secureConnectionStart',
            'connect_end': 'connectEnd',
            'fetch_start': 'fetchStart',
            'request_start': 'requestStart',
            'response_start': 'responseStart',
            'response_end': 'responseEnd',
            'duration': 'duration',
            'encoded_body_size': 'encodedBodySize'
        }

        self._key = None
        self._probe_configuration_id = None
        self._start_time = None
        self._target = None
        self._vantage_point_name = None
        self._is_timed_out = None
        self._is_healthy = None
        self._error_category = None
        self._error_message = None
        self._protocol = None
        self._connection = None
        self._dns = None
        self._status_code = None
        self._domain_lookup_start = None
        self._domain_lookup_end = None
        self._connect_start = None
        self._secure_connection_start = None
        self._connect_end = None
        self._fetch_start = None
        self._request_start = None
        self._response_start = None
        self._response_end = None
        self._duration = None
        self._encoded_body_size = None

    @property
    def key(self):
        """
        Gets the key of this HttpProbeResultSummary.
        A value identifying this specific probe result. The key is only unique within
        the results of its probe configuration. The key may be reused after 90 days.


        :return: The key of this HttpProbeResultSummary.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this HttpProbeResultSummary.
        A value identifying this specific probe result. The key is only unique within
        the results of its probe configuration. The key may be reused after 90 days.


        :param key: The key of this HttpProbeResultSummary.
        :type: str
        """
        self._key = key

    @property
    def probe_configuration_id(self):
        """
        Gets the probe_configuration_id of this HttpProbeResultSummary.
        The OCID of the monitor or on-demand probe responsible for creating this result.


        :return: The probe_configuration_id of this HttpProbeResultSummary.
        :rtype: str
        """
        return self._probe_configuration_id

    @probe_configuration_id.setter
    def probe_configuration_id(self, probe_configuration_id):
        """
        Sets the probe_configuration_id of this HttpProbeResultSummary.
        The OCID of the monitor or on-demand probe responsible for creating this result.


        :param probe_configuration_id: The probe_configuration_id of this HttpProbeResultSummary.
        :type: str
        """
        self._probe_configuration_id = probe_configuration_id

    @property
    def start_time(self):
        """
        Gets the start_time of this HttpProbeResultSummary.
        The date and time the probe was executed, expressed in milliseconds since the
        POSIX epoch. This field is defined by the PerformanceResourceTiming interface
        of the W3C Resource Timing specification. For more information, see
        `Resource Timing`__.

        __ https://w3c.github.io/resource-timing/#sec-resource-timing


        :return: The start_time of this HttpProbeResultSummary.
        :rtype: float
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this HttpProbeResultSummary.
        The date and time the probe was executed, expressed in milliseconds since the
        POSIX epoch. This field is defined by the PerformanceResourceTiming interface
        of the W3C Resource Timing specification. For more information, see
        `Resource Timing`__.

        __ https://w3c.github.io/resource-timing/#sec-resource-timing


        :param start_time: The start_time of this HttpProbeResultSummary.
        :type: float
        """
        self._start_time = start_time

    @property
    def target(self):
        """
        Gets the target of this HttpProbeResultSummary.
        The target hostname or IP address of the probe.


        :return: The target of this HttpProbeResultSummary.
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """
        Sets the target of this HttpProbeResultSummary.
        The target hostname or IP address of the probe.


        :param target: The target of this HttpProbeResultSummary.
        :type: str
        """
        self._target = target

    @property
    def vantage_point_name(self):
        """
        Gets the vantage_point_name of this HttpProbeResultSummary.
        The name of the vantage point that executed the probe.


        :return: The vantage_point_name of this HttpProbeResultSummary.
        :rtype: str
        """
        return self._vantage_point_name

    @vantage_point_name.setter
    def vantage_point_name(self, vantage_point_name):
        """
        Sets the vantage_point_name of this HttpProbeResultSummary.
        The name of the vantage point that executed the probe.


        :param vantage_point_name: The vantage_point_name of this HttpProbeResultSummary.
        :type: str
        """
        self._vantage_point_name = vantage_point_name

    @property
    def is_timed_out(self):
        """
        Gets the is_timed_out of this HttpProbeResultSummary.
        True if the probe did not complete before the configured `timeoutInSeconds` value.


        :return: The is_timed_out of this HttpProbeResultSummary.
        :rtype: bool
        """
        return self._is_timed_out

    @is_timed_out.setter
    def is_timed_out(self, is_timed_out):
        """
        Sets the is_timed_out of this HttpProbeResultSummary.
        True if the probe did not complete before the configured `timeoutInSeconds` value.


        :param is_timed_out: The is_timed_out of this HttpProbeResultSummary.
        :type: bool
        """
        self._is_timed_out = is_timed_out

    @property
    def is_healthy(self):
        """
        Gets the is_healthy of this HttpProbeResultSummary.
        True if the probe result is determined to be healthy based on probe
        type-specific criteria.  For HTTP probes, a probe result is considered
        healthy if the HTTP response code is greater than or equal to 200 and
        less than 300.


        :return: The is_healthy of this HttpProbeResultSummary.
        :rtype: bool
        """
        return self._is_healthy

    @is_healthy.setter
    def is_healthy(self, is_healthy):
        """
        Sets the is_healthy of this HttpProbeResultSummary.
        True if the probe result is determined to be healthy based on probe
        type-specific criteria.  For HTTP probes, a probe result is considered
        healthy if the HTTP response code is greater than or equal to 200 and
        less than 300.


        :param is_healthy: The is_healthy of this HttpProbeResultSummary.
        :type: bool
        """
        self._is_healthy = is_healthy

    @property
    def error_category(self):
        """
        Gets the error_category of this HttpProbeResultSummary.
        The category of error if an error occurs executing the probe.
        The `errorMessage` field provides a message with the error details.
        * NONE - No error
        * DNS - DNS errors
        * TRANSPORT - Transport-related errors, for example a \"TLS certificate expired\" error.
        * NETWORK - Network-related errors, for example a \"network unreachable\" error.
        * SYSTEM - Internal system errors.

        Allowed values for this property are: "NONE", "DNS", "TRANSPORT", "NETWORK", "SYSTEM", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The error_category of this HttpProbeResultSummary.
        :rtype: str
        """
        return self._error_category

    @error_category.setter
    def error_category(self, error_category):
        """
        Sets the error_category of this HttpProbeResultSummary.
        The category of error if an error occurs executing the probe.
        The `errorMessage` field provides a message with the error details.
        * NONE - No error
        * DNS - DNS errors
        * TRANSPORT - Transport-related errors, for example a \"TLS certificate expired\" error.
        * NETWORK - Network-related errors, for example a \"network unreachable\" error.
        * SYSTEM - Internal system errors.


        :param error_category: The error_category of this HttpProbeResultSummary.
        :type: str
        """
        allowed_values = ["NONE", "DNS", "TRANSPORT", "NETWORK", "SYSTEM"]
        if not value_allowed_none_or_none_sentinel(error_category, allowed_values):
            error_category = 'UNKNOWN_ENUM_VALUE'
        self._error_category = error_category

    @property
    def error_message(self):
        """
        Gets the error_message of this HttpProbeResultSummary.
        The error information indicating why a probe execution failed.


        :return: The error_message of this HttpProbeResultSummary.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this HttpProbeResultSummary.
        The error information indicating why a probe execution failed.


        :param error_message: The error_message of this HttpProbeResultSummary.
        :type: str
        """
        self._error_message = error_message

    @property
    def protocol(self):
        """
        Gets the protocol of this HttpProbeResultSummary.
        Allowed values for this property are: "HTTP", "HTTPS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The protocol of this HttpProbeResultSummary.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this HttpProbeResultSummary.

        :param protocol: The protocol of this HttpProbeResultSummary.
        :type: str
        """
        allowed_values = ["HTTP", "HTTPS"]
        if not value_allowed_none_or_none_sentinel(protocol, allowed_values):
            protocol = 'UNKNOWN_ENUM_VALUE'
        self._protocol = protocol

    @property
    def connection(self):
        """
        Gets the connection of this HttpProbeResultSummary.

        :return: The connection of this HttpProbeResultSummary.
        :rtype: oci.healthchecks.models.TcpConnection
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        """
        Sets the connection of this HttpProbeResultSummary.

        :param connection: The connection of this HttpProbeResultSummary.
        :type: oci.healthchecks.models.TcpConnection
        """
        self._connection = connection

    @property
    def dns(self):
        """
        Gets the dns of this HttpProbeResultSummary.

        :return: The dns of this HttpProbeResultSummary.
        :rtype: oci.healthchecks.models.DNS
        """
        return self._dns

    @dns.setter
    def dns(self, dns):
        """
        Sets the dns of this HttpProbeResultSummary.

        :param dns: The dns of this HttpProbeResultSummary.
        :type: oci.healthchecks.models.DNS
        """
        self._dns = dns

    @property
    def status_code(self):
        """
        Gets the status_code of this HttpProbeResultSummary.
        The HTTP response status code.


        :return: The status_code of this HttpProbeResultSummary.
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """
        Sets the status_code of this HttpProbeResultSummary.
        The HTTP response status code.


        :param status_code: The status_code of this HttpProbeResultSummary.
        :type: int
        """
        self._status_code = status_code

    @property
    def domain_lookup_start(self):
        """
        Gets the domain_lookup_start of this HttpProbeResultSummary.
        The time immediately before the vantage point starts the domain name lookup for
        the resource.


        :return: The domain_lookup_start of this HttpProbeResultSummary.
        :rtype: float
        """
        return self._domain_lookup_start

    @domain_lookup_start.setter
    def domain_lookup_start(self, domain_lookup_start):
        """
        Sets the domain_lookup_start of this HttpProbeResultSummary.
        The time immediately before the vantage point starts the domain name lookup for
        the resource.


        :param domain_lookup_start: The domain_lookup_start of this HttpProbeResultSummary.
        :type: float
        """
        self._domain_lookup_start = domain_lookup_start

    @property
    def domain_lookup_end(self):
        """
        Gets the domain_lookup_end of this HttpProbeResultSummary.
        The time immediately before the vantage point finishes the domain name lookup for
        the resource.


        :return: The domain_lookup_end of this HttpProbeResultSummary.
        :rtype: float
        """
        return self._domain_lookup_end

    @domain_lookup_end.setter
    def domain_lookup_end(self, domain_lookup_end):
        """
        Sets the domain_lookup_end of this HttpProbeResultSummary.
        The time immediately before the vantage point finishes the domain name lookup for
        the resource.


        :param domain_lookup_end: The domain_lookup_end of this HttpProbeResultSummary.
        :type: float
        """
        self._domain_lookup_end = domain_lookup_end

    @property
    def connect_start(self):
        """
        Gets the connect_start of this HttpProbeResultSummary.
        The time immediately before the vantage point starts establishing the connection
        to the server to retrieve the resource.


        :return: The connect_start of this HttpProbeResultSummary.
        :rtype: float
        """
        return self._connect_start

    @connect_start.setter
    def connect_start(self, connect_start):
        """
        Sets the connect_start of this HttpProbeResultSummary.
        The time immediately before the vantage point starts establishing the connection
        to the server to retrieve the resource.


        :param connect_start: The connect_start of this HttpProbeResultSummary.
        :type: float
        """
        self._connect_start = connect_start

    @property
    def secure_connection_start(self):
        """
        Gets the secure_connection_start of this HttpProbeResultSummary.
        The time immediately before the vantage point starts the handshake process to
        secure the current connection.


        :return: The secure_connection_start of this HttpProbeResultSummary.
        :rtype: float
        """
        return self._secure_connection_start

    @secure_connection_start.setter
    def secure_connection_start(self, secure_connection_start):
        """
        Sets the secure_connection_start of this HttpProbeResultSummary.
        The time immediately before the vantage point starts the handshake process to
        secure the current connection.


        :param secure_connection_start: The secure_connection_start of this HttpProbeResultSummary.
        :type: float
        """
        self._secure_connection_start = secure_connection_start

    @property
    def connect_end(self):
        """
        Gets the connect_end of this HttpProbeResultSummary.
        The time immediately after the vantage point finishes establishing the connection
        to the server to retrieve the resource.


        :return: The connect_end of this HttpProbeResultSummary.
        :rtype: float
        """
        return self._connect_end

    @connect_end.setter
    def connect_end(self, connect_end):
        """
        Sets the connect_end of this HttpProbeResultSummary.
        The time immediately after the vantage point finishes establishing the connection
        to the server to retrieve the resource.


        :param connect_end: The connect_end of this HttpProbeResultSummary.
        :type: float
        """
        self._connect_end = connect_end

    @property
    def fetch_start(self):
        """
        Gets the fetch_start of this HttpProbeResultSummary.
        The time immediately before the vantage point starts to fetch the resource.


        :return: The fetch_start of this HttpProbeResultSummary.
        :rtype: float
        """
        return self._fetch_start

    @fetch_start.setter
    def fetch_start(self, fetch_start):
        """
        Sets the fetch_start of this HttpProbeResultSummary.
        The time immediately before the vantage point starts to fetch the resource.


        :param fetch_start: The fetch_start of this HttpProbeResultSummary.
        :type: float
        """
        self._fetch_start = fetch_start

    @property
    def request_start(self):
        """
        Gets the request_start of this HttpProbeResultSummary.
        The time immediately before the vantage point starts requesting the resource from
        the server.


        :return: The request_start of this HttpProbeResultSummary.
        :rtype: float
        """
        return self._request_start

    @request_start.setter
    def request_start(self, request_start):
        """
        Sets the request_start of this HttpProbeResultSummary.
        The time immediately before the vantage point starts requesting the resource from
        the server.


        :param request_start: The request_start of this HttpProbeResultSummary.
        :type: float
        """
        self._request_start = request_start

    @property
    def response_start(self):
        """
        Gets the response_start of this HttpProbeResultSummary.
        The time immediately after the vantage point's HTTP parser receives the first byte
        of the response.


        :return: The response_start of this HttpProbeResultSummary.
        :rtype: float
        """
        return self._response_start

    @response_start.setter
    def response_start(self, response_start):
        """
        Sets the response_start of this HttpProbeResultSummary.
        The time immediately after the vantage point's HTTP parser receives the first byte
        of the response.


        :param response_start: The response_start of this HttpProbeResultSummary.
        :type: float
        """
        self._response_start = response_start

    @property
    def response_end(self):
        """
        Gets the response_end of this HttpProbeResultSummary.
        The time immediately after the vantage point receives the last byte of the response
        or immediately before the transport connection is closed, whichever comes first.


        :return: The response_end of this HttpProbeResultSummary.
        :rtype: float
        """
        return self._response_end

    @response_end.setter
    def response_end(self, response_end):
        """
        Sets the response_end of this HttpProbeResultSummary.
        The time immediately after the vantage point receives the last byte of the response
        or immediately before the transport connection is closed, whichever comes first.


        :param response_end: The response_end of this HttpProbeResultSummary.
        :type: float
        """
        self._response_end = response_end

    @property
    def duration(self):
        """
        Gets the duration of this HttpProbeResultSummary.
        The total duration from start of request until response is fully consumed or the
        connection is closed.


        :return: The duration of this HttpProbeResultSummary.
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """
        Sets the duration of this HttpProbeResultSummary.
        The total duration from start of request until response is fully consumed or the
        connection is closed.


        :param duration: The duration of this HttpProbeResultSummary.
        :type: float
        """
        self._duration = duration

    @property
    def encoded_body_size(self):
        """
        Gets the encoded_body_size of this HttpProbeResultSummary.
        The size, in octets, of the payload body prior to removing any applied
        content-codings.


        :return: The encoded_body_size of this HttpProbeResultSummary.
        :rtype: int
        """
        return self._encoded_body_size

    @encoded_body_size.setter
    def encoded_body_size(self, encoded_body_size):
        """
        Sets the encoded_body_size of this HttpProbeResultSummary.
        The size, in octets, of the payload body prior to removing any applied
        content-codings.


        :param encoded_body_size: The encoded_body_size of this HttpProbeResultSummary.
        :type: int
        """
        self._encoded_body_size = encoded_body_size

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
