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


class MailUserRemovePrivilegeRequest(object):
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
    openapi_types = {"email": "str", "privilege": "MailUserPrivilege"}

    attribute_map = {"email": "email", "privilege": "privilege"}

    def __init__(
        self, email=None, privilege=None, local_vars_configuration=None
    ):  # noqa: E501
        """MailUserRemovePrivilegeRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._email = None
        self._privilege = None
        self.discriminator = None

        self.email = email
        self.privilege = privilege

    @property
    def email(self):
        """Gets the email of this MailUserRemovePrivilegeRequest.  # noqa: E501

        Email format.  # noqa: E501

        :return: The email of this MailUserRemovePrivilegeRequest.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this MailUserRemovePrivilegeRequest.

        Email format.  # noqa: E501

        :param email: The email of this MailUserRemovePrivilegeRequest.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and email is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `email`, must not be `None`"
            )  # noqa: E501

        self._email = email

    @property
    def privilege(self):
        """Gets the privilege of this MailUserRemovePrivilegeRequest.  # noqa: E501


        :return: The privilege of this MailUserRemovePrivilegeRequest.  # noqa: E501
        :rtype: MailUserPrivilege
        """
        return self._privilege

    @privilege.setter
    def privilege(self, privilege):
        """Sets the privilege of this MailUserRemovePrivilegeRequest.


        :param privilege: The privilege of this MailUserRemovePrivilegeRequest.  # noqa: E501
        :type: MailUserPrivilege
        """
        if (
            self.local_vars_configuration.client_side_validation and privilege is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `privilege`, must not be `None`"
            )  # noqa: E501

        self._privilege = privilege

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
        if not isinstance(other, MailUserRemovePrivilegeRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MailUserRemovePrivilegeRequest):
            return True

        return self.to_dict() != other.to_dict()
