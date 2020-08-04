# coding: utf-8

"""
    Mail-in-a-Box

    Mail-in-a-Box API HTTP specification.  # noqa: E501

    The version of the OpenAPI document: 0.46.0
    Contact: contact@mailinabox.email
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mailinabox_api.configuration import Configuration


class SSLCertificateInstallRequest(object):
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
    openapi_types = {"domain": "str", "cert": "str", "chain": "str"}

    attribute_map = {"domain": "domain", "cert": "cert", "chain": "chain"}

    def __init__(
        self, domain=None, cert=None, chain=None, local_vars_configuration=None
    ):  # noqa: E501
        """SSLCertificateInstallRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._domain = None
        self._cert = None
        self._chain = None
        self.discriminator = None

        self.domain = domain
        self.cert = cert
        self.chain = chain

    @property
    def domain(self):
        """Gets the domain of this SSLCertificateInstallRequest.  # noqa: E501

        Hostname format.  # noqa: E501

        :return: The domain of this SSLCertificateInstallRequest.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this SSLCertificateInstallRequest.

        Hostname format.  # noqa: E501

        :param domain: The domain of this SSLCertificateInstallRequest.  # noqa: E501
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
    def cert(self):
        """Gets the cert of this SSLCertificateInstallRequest.  # noqa: E501

        TLS/SSL certificate.  # noqa: E501

        :return: The cert of this SSLCertificateInstallRequest.  # noqa: E501
        :rtype: str
        """
        return self._cert

    @cert.setter
    def cert(self, cert):
        """Sets the cert of this SSLCertificateInstallRequest.

        TLS/SSL certificate.  # noqa: E501

        :param cert: The cert of this SSLCertificateInstallRequest.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and cert is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `cert`, must not be `None`"
            )  # noqa: E501

        self._cert = cert

    @property
    def chain(self):
        """Gets the chain of this SSLCertificateInstallRequest.  # noqa: E501

        TLS/SSL intermediate chain (if provided, else empty string).  # noqa: E501

        :return: The chain of this SSLCertificateInstallRequest.  # noqa: E501
        :rtype: str
        """
        return self._chain

    @chain.setter
    def chain(self, chain):
        """Sets the chain of this SSLCertificateInstallRequest.

        TLS/SSL intermediate chain (if provided, else empty string).  # noqa: E501

        :param chain: The chain of this SSLCertificateInstallRequest.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and chain is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `chain`, must not be `None`"
            )  # noqa: E501

        self._chain = chain

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
        if not isinstance(other, SSLCertificateInstallRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SSLCertificateInstallRequest):
            return True

        return self.to_dict() != other.to_dict()