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

from mailinaboxapi.configuration import Configuration


class MailAliasUpsertRequest(object):
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
    openapi_types = {
        'update_if_exists': 'int',
        'address': 'str',
        'forwards_to': 'str',
        'permitted_senders': 'str'
    }

    attribute_map = {
        'update_if_exists': 'update_if_exists',
        'address': 'address',
        'forwards_to': 'forwards_to',
        'permitted_senders': 'permitted_senders'
    }

    def __init__(self, update_if_exists=None, address=None, forwards_to=None, permitted_senders=None, local_vars_configuration=None):  # noqa: E501
        """MailAliasUpsertRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._update_if_exists = None
        self._address = None
        self._forwards_to = None
        self._permitted_senders = None
        self.discriminator = None

        self.update_if_exists = update_if_exists
        self.address = address
        self.forwards_to = forwards_to
        self.permitted_senders = permitted_senders

    @property
    def update_if_exists(self):
        """Gets the update_if_exists of this MailAliasUpsertRequest.  # noqa: E501

        Set to `1` when updating an alias.  # noqa: E501

        :return: The update_if_exists of this MailAliasUpsertRequest.  # noqa: E501
        :rtype: int
        """
        return self._update_if_exists

    @update_if_exists.setter
    def update_if_exists(self, update_if_exists):
        """Sets the update_if_exists of this MailAliasUpsertRequest.

        Set to `1` when updating an alias.  # noqa: E501

        :param update_if_exists: The update_if_exists of this MailAliasUpsertRequest.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and update_if_exists is None:  # noqa: E501
            raise ValueError("Invalid value for `update_if_exists`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                update_if_exists is not None and update_if_exists > 1):  # noqa: E501
            raise ValueError("Invalid value for `update_if_exists`, must be a value less than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                update_if_exists is not None and update_if_exists < 0):  # noqa: E501
            raise ValueError("Invalid value for `update_if_exists`, must be a value greater than or equal to `0`")  # noqa: E501

        self._update_if_exists = update_if_exists

    @property
    def address(self):
        """Gets the address of this MailAliasUpsertRequest.  # noqa: E501

        Email format.  # noqa: E501

        :return: The address of this MailAliasUpsertRequest.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this MailAliasUpsertRequest.

        Email format.  # noqa: E501

        :param address: The address of this MailAliasUpsertRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and address is None:  # noqa: E501
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def forwards_to(self):
        """Gets the forwards_to of this MailAliasUpsertRequest.  # noqa: E501

        If adding a regular or catch-all alias, the format needs to be `email1@example.com`. Multiple address can be separated by newlines or commas.  If adding a domain alias, the format needs to be `@example.com`.   # noqa: E501

        :return: The forwards_to of this MailAliasUpsertRequest.  # noqa: E501
        :rtype: str
        """
        return self._forwards_to

    @forwards_to.setter
    def forwards_to(self, forwards_to):
        """Sets the forwards_to of this MailAliasUpsertRequest.

        If adding a regular or catch-all alias, the format needs to be `email1@example.com`. Multiple address can be separated by newlines or commas.  If adding a domain alias, the format needs to be `@example.com`.   # noqa: E501

        :param forwards_to: The forwards_to of this MailAliasUpsertRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and forwards_to is None:  # noqa: E501
            raise ValueError("Invalid value for `forwards_to`, must not be `None`")  # noqa: E501

        self._forwards_to = forwards_to

    @property
    def permitted_senders(self):
        """Gets the permitted_senders of this MailAliasUpsertRequest.  # noqa: E501

        Mail users that can send mail claiming to be from any address on the alias domain. Multiple address can be separated by newlines or commas.  Leave empty to allow any mail user listed in `forwards_to` to send mail claiming to be from any address on the alias domain.   # noqa: E501

        :return: The permitted_senders of this MailAliasUpsertRequest.  # noqa: E501
        :rtype: str
        """
        return self._permitted_senders

    @permitted_senders.setter
    def permitted_senders(self, permitted_senders):
        """Sets the permitted_senders of this MailAliasUpsertRequest.

        Mail users that can send mail claiming to be from any address on the alias domain. Multiple address can be separated by newlines or commas.  Leave empty to allow any mail user listed in `forwards_to` to send mail claiming to be from any address on the alias domain.   # noqa: E501

        :param permitted_senders: The permitted_senders of this MailAliasUpsertRequest.  # noqa: E501
        :type: str
        """

        self._permitted_senders = permitted_senders

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
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
        if not isinstance(other, MailAliasUpsertRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MailAliasUpsertRequest):
            return True

        return self.to_dict() != other.to_dict()
