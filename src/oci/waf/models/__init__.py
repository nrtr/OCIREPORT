# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .access_control_rule import AccessControlRule
from .action import Action
from .allow_action import AllowAction
from .change_network_address_list_compartment_details import ChangeNetworkAddressListCompartmentDetails
from .change_resource_compartment_details import ChangeResourceCompartmentDetails
from .change_web_app_firewall_compartment_details import ChangeWebAppFirewallCompartmentDetails
from .change_web_app_firewall_policy_compartment_details import ChangeWebAppFirewallPolicyCompartmentDetails
from .check_action import CheckAction
from .collaborative_capability_weight import CollaborativeCapabilityWeight
from .collaborative_capability_weight_override import CollaborativeCapabilityWeightOverride
from .create_network_address_list_addresses_details import CreateNetworkAddressListAddressesDetails
from .create_network_address_list_details import CreateNetworkAddressListDetails
from .create_network_address_list_vcn_addresses_details import CreateNetworkAddressListVcnAddressesDetails
from .create_web_app_firewall_details import CreateWebAppFirewallDetails
from .create_web_app_firewall_load_balancer_details import CreateWebAppFirewallLoadBalancerDetails
from .create_web_app_firewall_policy_details import CreateWebAppFirewallPolicyDetails
from .http_response_body import HttpResponseBody
from .network_address_list import NetworkAddressList
from .network_address_list_addresses import NetworkAddressListAddresses
from .network_address_list_addresses_summary import NetworkAddressListAddressesSummary
from .network_address_list_collection import NetworkAddressListCollection
from .network_address_list_summary import NetworkAddressListSummary
from .network_address_list_vcn_addresses import NetworkAddressListVcnAddresses
from .network_address_list_vcn_addresses_summary import NetworkAddressListVcnAddressesSummary
from .private_addresses import PrivateAddresses
from .protection_capability import ProtectionCapability
from .protection_capability_collection import ProtectionCapabilityCollection
from .protection_capability_exclusions import ProtectionCapabilityExclusions
from .protection_capability_group_tag_collection import ProtectionCapabilityGroupTagCollection
from .protection_capability_group_tag_summary import ProtectionCapabilityGroupTagSummary
from .protection_capability_settings import ProtectionCapabilitySettings
from .protection_capability_summary import ProtectionCapabilitySummary
from .protection_rule import ProtectionRule
from .request_access_control import RequestAccessControl
from .request_protection import RequestProtection
from .request_rate_limiting import RequestRateLimiting
from .request_rate_limiting_configuration import RequestRateLimitingConfiguration
from .request_rate_limiting_rule import RequestRateLimitingRule
from .response_access_control import ResponseAccessControl
from .response_header import ResponseHeader
from .response_protection import ResponseProtection
from .return_http_response_action import ReturnHttpResponseAction
from .static_text_http_response_body import StaticTextHttpResponseBody
from .update_network_address_list_addresses_details import UpdateNetworkAddressListAddressesDetails
from .update_network_address_list_details import UpdateNetworkAddressListDetails
from .update_network_address_list_vcn_addresses_details import UpdateNetworkAddressListVcnAddressesDetails
from .update_web_app_firewall_details import UpdateWebAppFirewallDetails
from .update_web_app_firewall_policy_details import UpdateWebAppFirewallPolicyDetails
from .web_app_firewall import WebAppFirewall
from .web_app_firewall_collection import WebAppFirewallCollection
from .web_app_firewall_load_balancer import WebAppFirewallLoadBalancer
from .web_app_firewall_load_balancer_summary import WebAppFirewallLoadBalancerSummary
from .web_app_firewall_policy import WebAppFirewallPolicy
from .web_app_firewall_policy_collection import WebAppFirewallPolicyCollection
from .web_app_firewall_policy_rule import WebAppFirewallPolicyRule
from .web_app_firewall_policy_summary import WebAppFirewallPolicySummary
from .web_app_firewall_summary import WebAppFirewallSummary
from .work_request import WorkRequest
from .work_request_collection import WorkRequestCollection
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_log_entry_collection import WorkRequestLogEntryCollection
from .work_request_resource import WorkRequestResource

# Maps type names to classes for waf services.
waf_type_mapping = {
    "AccessControlRule": AccessControlRule,
    "Action": Action,
    "AllowAction": AllowAction,
    "ChangeNetworkAddressListCompartmentDetails": ChangeNetworkAddressListCompartmentDetails,
    "ChangeResourceCompartmentDetails": ChangeResourceCompartmentDetails,
    "ChangeWebAppFirewallCompartmentDetails": ChangeWebAppFirewallCompartmentDetails,
    "ChangeWebAppFirewallPolicyCompartmentDetails": ChangeWebAppFirewallPolicyCompartmentDetails,
    "CheckAction": CheckAction,
    "CollaborativeCapabilityWeight": CollaborativeCapabilityWeight,
    "CollaborativeCapabilityWeightOverride": CollaborativeCapabilityWeightOverride,
    "CreateNetworkAddressListAddressesDetails": CreateNetworkAddressListAddressesDetails,
    "CreateNetworkAddressListDetails": CreateNetworkAddressListDetails,
    "CreateNetworkAddressListVcnAddressesDetails": CreateNetworkAddressListVcnAddressesDetails,
    "CreateWebAppFirewallDetails": CreateWebAppFirewallDetails,
    "CreateWebAppFirewallLoadBalancerDetails": CreateWebAppFirewallLoadBalancerDetails,
    "CreateWebAppFirewallPolicyDetails": CreateWebAppFirewallPolicyDetails,
    "HttpResponseBody": HttpResponseBody,
    "NetworkAddressList": NetworkAddressList,
    "NetworkAddressListAddresses": NetworkAddressListAddresses,
    "NetworkAddressListAddressesSummary": NetworkAddressListAddressesSummary,
    "NetworkAddressListCollection": NetworkAddressListCollection,
    "NetworkAddressListSummary": NetworkAddressListSummary,
    "NetworkAddressListVcnAddresses": NetworkAddressListVcnAddresses,
    "NetworkAddressListVcnAddressesSummary": NetworkAddressListVcnAddressesSummary,
    "PrivateAddresses": PrivateAddresses,
    "ProtectionCapability": ProtectionCapability,
    "ProtectionCapabilityCollection": ProtectionCapabilityCollection,
    "ProtectionCapabilityExclusions": ProtectionCapabilityExclusions,
    "ProtectionCapabilityGroupTagCollection": ProtectionCapabilityGroupTagCollection,
    "ProtectionCapabilityGroupTagSummary": ProtectionCapabilityGroupTagSummary,
    "ProtectionCapabilitySettings": ProtectionCapabilitySettings,
    "ProtectionCapabilitySummary": ProtectionCapabilitySummary,
    "ProtectionRule": ProtectionRule,
    "RequestAccessControl": RequestAccessControl,
    "RequestProtection": RequestProtection,
    "RequestRateLimiting": RequestRateLimiting,
    "RequestRateLimitingConfiguration": RequestRateLimitingConfiguration,
    "RequestRateLimitingRule": RequestRateLimitingRule,
    "ResponseAccessControl": ResponseAccessControl,
    "ResponseHeader": ResponseHeader,
    "ResponseProtection": ResponseProtection,
    "ReturnHttpResponseAction": ReturnHttpResponseAction,
    "StaticTextHttpResponseBody": StaticTextHttpResponseBody,
    "UpdateNetworkAddressListAddressesDetails": UpdateNetworkAddressListAddressesDetails,
    "UpdateNetworkAddressListDetails": UpdateNetworkAddressListDetails,
    "UpdateNetworkAddressListVcnAddressesDetails": UpdateNetworkAddressListVcnAddressesDetails,
    "UpdateWebAppFirewallDetails": UpdateWebAppFirewallDetails,
    "UpdateWebAppFirewallPolicyDetails": UpdateWebAppFirewallPolicyDetails,
    "WebAppFirewall": WebAppFirewall,
    "WebAppFirewallCollection": WebAppFirewallCollection,
    "WebAppFirewallLoadBalancer": WebAppFirewallLoadBalancer,
    "WebAppFirewallLoadBalancerSummary": WebAppFirewallLoadBalancerSummary,
    "WebAppFirewallPolicy": WebAppFirewallPolicy,
    "WebAppFirewallPolicyCollection": WebAppFirewallPolicyCollection,
    "WebAppFirewallPolicyRule": WebAppFirewallPolicyRule,
    "WebAppFirewallPolicySummary": WebAppFirewallPolicySummary,
    "WebAppFirewallSummary": WebAppFirewallSummary,
    "WorkRequest": WorkRequest,
    "WorkRequestCollection": WorkRequestCollection,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestLogEntryCollection": WorkRequestLogEntryCollection,
    "WorkRequestResource": WorkRequestResource
}
