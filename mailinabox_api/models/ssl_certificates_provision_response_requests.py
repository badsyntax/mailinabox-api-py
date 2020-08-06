# coding: utf-8

"""
    Mail-in-a-Box

    Mail-in-a-Box API HTTP specification.  # noqa: E501

    The version of the OpenAPI document: 0.47.0
    Contact: contact@mailinabox.email
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mailinabox_api.configuration import Configuration


class SSLCertificatesProvisionResponseRequests(object):
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
    openapi_types = {"log": "list[str]", "result": "str", "domains": "list[str]"}

    attribute_map = {"log": "log", "result": "result", "domains": "domains"}

    def __init__(
        self, log=None, result=None, domains=None, local_vars_configuration=None
    ):  # noqa: E501
        """SSLCertificatesProvisionResponseRequests - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._log = None
        self._result = None
        self._domains = None
        self.discriminator = None

        self.log = log
        self.result = result
        self.domains = domains

    @property
    def log(self):
        """Gets the log of this SSLCertificatesProvisionResponseRequests.  # noqa: E501


        :return: The log of this SSLCertificatesProvisionResponseRequests.  # noqa: E501
        :rtype: list[str]
        """
        return self._log

    @log.setter
    def log(self, log):
        """Sets the log of this SSLCertificatesProvisionResponseRequests.


        :param log: The log of this SSLCertificatesProvisionResponseRequests.  # noqa: E501
        :type: list[str]
        """
        if (
            self.local_vars_configuration.client_side_validation and log is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `log`, must not be `None`"
            )  # noqa: E501

        self._log = log

    @property
    def result(self):
        """Gets the result of this SSLCertificatesProvisionResponseRequests.  # noqa: E501


        :return: The result of this SSLCertificatesProvisionResponseRequests.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this SSLCertificatesProvisionResponseRequests.


        :param result: The result of this SSLCertificatesProvisionResponseRequests.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and result is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `result`, must not be `None`"
            )  # noqa: E501
        allowed_values = ["installed", "error", "skipped"]  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and result not in allowed_values
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `result` ({0}), must be one of {1}".format(  # noqa: E501
                    result, allowed_values
                )
            )

        self._result = result

    @property
    def domains(self):
        """Gets the domains of this SSLCertificatesProvisionResponseRequests.  # noqa: E501


        :return: The domains of this SSLCertificatesProvisionResponseRequests.  # noqa: E501
        :rtype: list[str]
        """
        return self._domains

    @domains.setter
    def domains(self, domains):
        """Sets the domains of this SSLCertificatesProvisionResponseRequests.


        :param domains: The domains of this SSLCertificatesProvisionResponseRequests.  # noqa: E501
        :type: list[str]
        """
        if (
            self.local_vars_configuration.client_side_validation and domains is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `domains`, must not be `None`"
            )  # noqa: E501

        self._domains = domains

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
        if not isinstance(other, SSLCertificatesProvisionResponseRequests):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SSLCertificatesProvisionResponseRequests):
            return True

        return self.to_dict() != other.to_dict()
