# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WafConfigDetails(object):
    """
    The Web Application Firewall configuration for the WAAS policy creation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new WafConfigDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param access_rules:
            The value to assign to the access_rules property of this WafConfigDetails.
        :type access_rules: list[oci.waas.models.AccessRule]

        :param address_rate_limiting:
            The value to assign to the address_rate_limiting property of this WafConfigDetails.
        :type address_rate_limiting: oci.waas.models.AddressRateLimiting

        :param captchas:
            The value to assign to the captchas property of this WafConfigDetails.
        :type captchas: list[oci.waas.models.Captcha]

        :param device_fingerprint_challenge:
            The value to assign to the device_fingerprint_challenge property of this WafConfigDetails.
        :type device_fingerprint_challenge: oci.waas.models.DeviceFingerprintChallenge

        :param human_interaction_challenge:
            The value to assign to the human_interaction_challenge property of this WafConfigDetails.
        :type human_interaction_challenge: oci.waas.models.HumanInteractionChallenge

        :param js_challenge:
            The value to assign to the js_challenge property of this WafConfigDetails.
        :type js_challenge: oci.waas.models.JsChallenge

        :param origin:
            The value to assign to the origin property of this WafConfigDetails.
        :type origin: str

        :param caching_rules:
            The value to assign to the caching_rules property of this WafConfigDetails.
        :type caching_rules: list[oci.waas.models.CachingRule]

        :param custom_protection_rules:
            The value to assign to the custom_protection_rules property of this WafConfigDetails.
        :type custom_protection_rules: list[oci.waas.models.CustomProtectionRuleSetting]

        :param origin_groups:
            The value to assign to the origin_groups property of this WafConfigDetails.
        :type origin_groups: list[str]

        :param protection_settings:
            The value to assign to the protection_settings property of this WafConfigDetails.
        :type protection_settings: oci.waas.models.ProtectionSettings

        :param whitelists:
            The value to assign to the whitelists property of this WafConfigDetails.
        :type whitelists: list[oci.waas.models.Whitelist]

        """
        self.swagger_types = {
            'access_rules': 'list[AccessRule]',
            'address_rate_limiting': 'AddressRateLimiting',
            'captchas': 'list[Captcha]',
            'device_fingerprint_challenge': 'DeviceFingerprintChallenge',
            'human_interaction_challenge': 'HumanInteractionChallenge',
            'js_challenge': 'JsChallenge',
            'origin': 'str',
            'caching_rules': 'list[CachingRule]',
            'custom_protection_rules': 'list[CustomProtectionRuleSetting]',
            'origin_groups': 'list[str]',
            'protection_settings': 'ProtectionSettings',
            'whitelists': 'list[Whitelist]'
        }

        self.attribute_map = {
            'access_rules': 'accessRules',
            'address_rate_limiting': 'addressRateLimiting',
            'captchas': 'captchas',
            'device_fingerprint_challenge': 'deviceFingerprintChallenge',
            'human_interaction_challenge': 'humanInteractionChallenge',
            'js_challenge': 'jsChallenge',
            'origin': 'origin',
            'caching_rules': 'cachingRules',
            'custom_protection_rules': 'customProtectionRules',
            'origin_groups': 'originGroups',
            'protection_settings': 'protectionSettings',
            'whitelists': 'whitelists'
        }

        self._access_rules = None
        self._address_rate_limiting = None
        self._captchas = None
        self._device_fingerprint_challenge = None
        self._human_interaction_challenge = None
        self._js_challenge = None
        self._origin = None
        self._caching_rules = None
        self._custom_protection_rules = None
        self._origin_groups = None
        self._protection_settings = None
        self._whitelists = None

    @property
    def access_rules(self):
        """
        Gets the access_rules of this WafConfigDetails.
        The access rules applied to the Web Application Firewall. Access rules allow custom content access policies to be defined and `ALLOW`, `DETECT`, or `BLOCK` actions to be taken on a request when specified criteria are met.


        :return: The access_rules of this WafConfigDetails.
        :rtype: list[oci.waas.models.AccessRule]
        """
        return self._access_rules

    @access_rules.setter
    def access_rules(self, access_rules):
        """
        Sets the access_rules of this WafConfigDetails.
        The access rules applied to the Web Application Firewall. Access rules allow custom content access policies to be defined and `ALLOW`, `DETECT`, or `BLOCK` actions to be taken on a request when specified criteria are met.


        :param access_rules: The access_rules of this WafConfigDetails.
        :type: list[oci.waas.models.AccessRule]
        """
        self._access_rules = access_rules

    @property
    def address_rate_limiting(self):
        """
        Gets the address_rate_limiting of this WafConfigDetails.
        The settings used to limit the number of requests from an IP address.


        :return: The address_rate_limiting of this WafConfigDetails.
        :rtype: oci.waas.models.AddressRateLimiting
        """
        return self._address_rate_limiting

    @address_rate_limiting.setter
    def address_rate_limiting(self, address_rate_limiting):
        """
        Sets the address_rate_limiting of this WafConfigDetails.
        The settings used to limit the number of requests from an IP address.


        :param address_rate_limiting: The address_rate_limiting of this WafConfigDetails.
        :type: oci.waas.models.AddressRateLimiting
        """
        self._address_rate_limiting = address_rate_limiting

    @property
    def captchas(self):
        """
        Gets the captchas of this WafConfigDetails.
        A list of CAPTCHA challenge settings. CAPTCHAs challenge requests to ensure a human is attempting to reach the specified URL and not a bot.


        :return: The captchas of this WafConfigDetails.
        :rtype: list[oci.waas.models.Captcha]
        """
        return self._captchas

    @captchas.setter
    def captchas(self, captchas):
        """
        Sets the captchas of this WafConfigDetails.
        A list of CAPTCHA challenge settings. CAPTCHAs challenge requests to ensure a human is attempting to reach the specified URL and not a bot.


        :param captchas: The captchas of this WafConfigDetails.
        :type: list[oci.waas.models.Captcha]
        """
        self._captchas = captchas

    @property
    def device_fingerprint_challenge(self):
        """
        Gets the device_fingerprint_challenge of this WafConfigDetails.
        The device fingerprint challenge settings. Blocks bots based on unique device fingerprint information.


        :return: The device_fingerprint_challenge of this WafConfigDetails.
        :rtype: oci.waas.models.DeviceFingerprintChallenge
        """
        return self._device_fingerprint_challenge

    @device_fingerprint_challenge.setter
    def device_fingerprint_challenge(self, device_fingerprint_challenge):
        """
        Sets the device_fingerprint_challenge of this WafConfigDetails.
        The device fingerprint challenge settings. Blocks bots based on unique device fingerprint information.


        :param device_fingerprint_challenge: The device_fingerprint_challenge of this WafConfigDetails.
        :type: oci.waas.models.DeviceFingerprintChallenge
        """
        self._device_fingerprint_challenge = device_fingerprint_challenge

    @property
    def human_interaction_challenge(self):
        """
        Gets the human_interaction_challenge of this WafConfigDetails.
        The human interaction challenge settings. Detects natural human interactions such as mouse movements, time on site, and page scrolling to identify bots.


        :return: The human_interaction_challenge of this WafConfigDetails.
        :rtype: oci.waas.models.HumanInteractionChallenge
        """
        return self._human_interaction_challenge

    @human_interaction_challenge.setter
    def human_interaction_challenge(self, human_interaction_challenge):
        """
        Sets the human_interaction_challenge of this WafConfigDetails.
        The human interaction challenge settings. Detects natural human interactions such as mouse movements, time on site, and page scrolling to identify bots.


        :param human_interaction_challenge: The human_interaction_challenge of this WafConfigDetails.
        :type: oci.waas.models.HumanInteractionChallenge
        """
        self._human_interaction_challenge = human_interaction_challenge

    @property
    def js_challenge(self):
        """
        Gets the js_challenge of this WafConfigDetails.
        The JavaScript challenge settings. Blocks bots by challenging requests from browsers that have no JavaScript support.


        :return: The js_challenge of this WafConfigDetails.
        :rtype: oci.waas.models.JsChallenge
        """
        return self._js_challenge

    @js_challenge.setter
    def js_challenge(self, js_challenge):
        """
        Sets the js_challenge of this WafConfigDetails.
        The JavaScript challenge settings. Blocks bots by challenging requests from browsers that have no JavaScript support.


        :param js_challenge: The js_challenge of this WafConfigDetails.
        :type: oci.waas.models.JsChallenge
        """
        self._js_challenge = js_challenge

    @property
    def origin(self):
        """
        Gets the origin of this WafConfigDetails.
        The key in the map of origins referencing the origin used for the Web Application Firewall. The origin must already be included in `Origins`. Required when creating the `WafConfig` resource, but is not required upon updating the configuration.


        :return: The origin of this WafConfigDetails.
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """
        Sets the origin of this WafConfigDetails.
        The key in the map of origins referencing the origin used for the Web Application Firewall. The origin must already be included in `Origins`. Required when creating the `WafConfig` resource, but is not required upon updating the configuration.


        :param origin: The origin of this WafConfigDetails.
        :type: str
        """
        self._origin = origin

    @property
    def caching_rules(self):
        """
        Gets the caching_rules of this WafConfigDetails.
        A list of caching rules applied to the web application.


        :return: The caching_rules of this WafConfigDetails.
        :rtype: list[oci.waas.models.CachingRule]
        """
        return self._caching_rules

    @caching_rules.setter
    def caching_rules(self, caching_rules):
        """
        Sets the caching_rules of this WafConfigDetails.
        A list of caching rules applied to the web application.


        :param caching_rules: The caching_rules of this WafConfigDetails.
        :type: list[oci.waas.models.CachingRule]
        """
        self._caching_rules = caching_rules

    @property
    def custom_protection_rules(self):
        """
        Gets the custom_protection_rules of this WafConfigDetails.
        A list of the custom protection rule OCIDs and their actions.


        :return: The custom_protection_rules of this WafConfigDetails.
        :rtype: list[oci.waas.models.CustomProtectionRuleSetting]
        """
        return self._custom_protection_rules

    @custom_protection_rules.setter
    def custom_protection_rules(self, custom_protection_rules):
        """
        Sets the custom_protection_rules of this WafConfigDetails.
        A list of the custom protection rule OCIDs and their actions.


        :param custom_protection_rules: The custom_protection_rules of this WafConfigDetails.
        :type: list[oci.waas.models.CustomProtectionRuleSetting]
        """
        self._custom_protection_rules = custom_protection_rules

    @property
    def origin_groups(self):
        """
        Gets the origin_groups of this WafConfigDetails.
        The map of origin groups and their keys used to associate origins to the `wafConfig`. Origin groups allow you to apply weights to groups of origins for load balancing purposes. Origins with higher weights will receive larger proportions of client requests.
        To add additional origins to your WAAS policy, update the `origins` field of a `UpdateWaasPolicy` request.


        :return: The origin_groups of this WafConfigDetails.
        :rtype: list[str]
        """
        return self._origin_groups

    @origin_groups.setter
    def origin_groups(self, origin_groups):
        """
        Sets the origin_groups of this WafConfigDetails.
        The map of origin groups and their keys used to associate origins to the `wafConfig`. Origin groups allow you to apply weights to groups of origins for load balancing purposes. Origins with higher weights will receive larger proportions of client requests.
        To add additional origins to your WAAS policy, update the `origins` field of a `UpdateWaasPolicy` request.


        :param origin_groups: The origin_groups of this WafConfigDetails.
        :type: list[str]
        """
        self._origin_groups = origin_groups

    @property
    def protection_settings(self):
        """
        Gets the protection_settings of this WafConfigDetails.
        The settings applied to protection rules.


        :return: The protection_settings of this WafConfigDetails.
        :rtype: oci.waas.models.ProtectionSettings
        """
        return self._protection_settings

    @protection_settings.setter
    def protection_settings(self, protection_settings):
        """
        Sets the protection_settings of this WafConfigDetails.
        The settings applied to protection rules.


        :param protection_settings: The protection_settings of this WafConfigDetails.
        :type: oci.waas.models.ProtectionSettings
        """
        self._protection_settings = protection_settings

    @property
    def whitelists(self):
        """
        Gets the whitelists of this WafConfigDetails.
        A list of IP addresses that bypass the Web Application Firewall.


        :return: The whitelists of this WafConfigDetails.
        :rtype: list[oci.waas.models.Whitelist]
        """
        return self._whitelists

    @whitelists.setter
    def whitelists(self, whitelists):
        """
        Sets the whitelists of this WafConfigDetails.
        A list of IP addresses that bypass the Web Application Firewall.


        :param whitelists: The whitelists of this WafConfigDetails.
        :type: list[oci.waas.models.Whitelist]
        """
        self._whitelists = whitelists

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
