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


class MfaStatusResponseEnabledMfa(object):
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
    openapi_types = {"id": "str", "type": "str", "label": "str"}

    attribute_map = {"id": "id", "type": "type", "label": "label"}

    def __init__(
        self, id=None, type=None, label=None, local_vars_configuration=None
    ):  # noqa: E501
        """MfaStatusResponseEnabledMfa - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._type = None
        self._label = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if label is not None:
            self.label = label

    @property
    def id(self):
        """Gets the id of this MfaStatusResponseEnabledMfa.  # noqa: E501


        :return: The id of this MfaStatusResponseEnabledMfa.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MfaStatusResponseEnabledMfa.


        :param id: The id of this MfaStatusResponseEnabledMfa.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this MfaStatusResponseEnabledMfa.  # noqa: E501


        :return: The type of this MfaStatusResponseEnabledMfa.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MfaStatusResponseEnabledMfa.


        :param type: The type of this MfaStatusResponseEnabledMfa.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def label(self):
        """Gets the label of this MfaStatusResponseEnabledMfa.  # noqa: E501


        :return: The label of this MfaStatusResponseEnabledMfa.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this MfaStatusResponseEnabledMfa.


        :param label: The label of this MfaStatusResponseEnabledMfa.  # noqa: E501
        :type: str
        """

        self._label = label

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
        if not isinstance(other, MfaStatusResponseEnabledMfa):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MfaStatusResponseEnabledMfa):
            return True

        return self.to_dict() != other.to_dict()