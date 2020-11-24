# coding: utf-8

"""
    Mail-in-a-Box

    Mail-in-a-Box API HTTP specification.  # Introduction This API is documented in [**OpenAPI format**](http://spec.openapis.org/oas/v3.0.3). ([View the full HTTP specification](https://raw.githubusercontent.com/mail-in-a-box/mailinabox/api-spec/api/mailinabox.yml).)  All endpoints are relative to `https://{host}/admin` and are secured with [`Basic Access` authentication](https://en.wikipedia.org/wiki/Basic_access_authentication). If you have multi-factor authentication enabled, authentication with a `user:password` combination will fail unless a valid OTP is supplied via the `x-auth-token` header. Authentication via a `user:user_key` pair is possible without the header being present.   # noqa: E501

    The version of the OpenAPI document: 0.51.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mailinabox_api.configuration import Configuration


class MailAliasByDomain(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {"domain": "str", "aliases": "list[MailAlias]"}

    attribute_map = {"domain": "domain", "aliases": "aliases"}

    def __init__(
        self, domain=None, aliases=None, local_vars_configuration=None
    ):  # noqa: E501
        """MailAliasByDomain - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._domain = None
        self._aliases = None
        self.discriminator = None

        self.domain = domain
        self.aliases = aliases

    @property
    def domain(self):
        """Gets the domain of this MailAliasByDomain.  # noqa: E501

        Hostname format.  # noqa: E501

        :return: The domain of this MailAliasByDomain.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this MailAliasByDomain.

        Hostname format.  # noqa: E501

        :param domain: The domain of this MailAliasByDomain.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and domain is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `domain`, must not be `None`"
            )  # noqa: E501

        self._domain = domain

    @property
    def aliases(self):
        """Gets the aliases of this MailAliasByDomain.  # noqa: E501


        :return: The aliases of this MailAliasByDomain.  # noqa: E501
        :rtype: list[MailAlias]
        """
        return self._aliases

    @aliases.setter
    def aliases(self, aliases):
        """Sets the aliases of this MailAliasByDomain.


        :param aliases: The aliases of this MailAliasByDomain.  # noqa: E501
        :type: list[MailAlias]
        """
        if (
            self.local_vars_configuration.client_side_validation and aliases is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `aliases`, must not be `None`"
            )  # noqa: E501

        self._aliases = aliases

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MailAliasByDomain):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MailAliasByDomain):
            return True

        return self.to_dict() != other.to_dict()
