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


class SystemBackupStatus(object):
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
        "date": "datetime",
        "date_delta": "str",
        "date_str": "str",
        "deleted_in": "str",
        "full": "bool",
        "size": "int",
        "volumes": "int",
    }

    attribute_map = {
        "date": "date",
        "date_delta": "date_delta",
        "date_str": "date_str",
        "deleted_in": "deleted_in",
        "full": "full",
        "size": "size",
        "volumes": "volumes",
    }

    def __init__(
        self,
        date=None,
        date_delta=None,
        date_str=None,
        deleted_in=None,
        full=None,
        size=None,
        volumes=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """SystemBackupStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._date = None
        self._date_delta = None
        self._date_str = None
        self._deleted_in = None
        self._full = None
        self._size = None
        self._volumes = None
        self.discriminator = None

        self.date = date
        self.date_delta = date_delta
        self.date_str = date_str
        if deleted_in is not None:
            self.deleted_in = deleted_in
        self.full = full
        self.size = size
        self.volumes = volumes

    @property
    def date(self):
        """Gets the date of this SystemBackupStatus.  # noqa: E501


        :return: The date of this SystemBackupStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this SystemBackupStatus.


        :param date: The date of this SystemBackupStatus.  # noqa: E501
        :type: datetime
        """
        if (
            self.local_vars_configuration.client_side_validation and date is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `date`, must not be `None`"
            )  # noqa: E501

        self._date = date

    @property
    def date_delta(self):
        """Gets the date_delta of this SystemBackupStatus.  # noqa: E501


        :return: The date_delta of this SystemBackupStatus.  # noqa: E501
        :rtype: str
        """
        return self._date_delta

    @date_delta.setter
    def date_delta(self, date_delta):
        """Sets the date_delta of this SystemBackupStatus.


        :param date_delta: The date_delta of this SystemBackupStatus.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and date_delta is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `date_delta`, must not be `None`"
            )  # noqa: E501

        self._date_delta = date_delta

    @property
    def date_str(self):
        """Gets the date_str of this SystemBackupStatus.  # noqa: E501


        :return: The date_str of this SystemBackupStatus.  # noqa: E501
        :rtype: str
        """
        return self._date_str

    @date_str.setter
    def date_str(self, date_str):
        """Sets the date_str of this SystemBackupStatus.


        :param date_str: The date_str of this SystemBackupStatus.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and date_str is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `date_str`, must not be `None`"
            )  # noqa: E501

        self._date_str = date_str

    @property
    def deleted_in(self):
        """Gets the deleted_in of this SystemBackupStatus.  # noqa: E501


        :return: The deleted_in of this SystemBackupStatus.  # noqa: E501
        :rtype: str
        """
        return self._deleted_in

    @deleted_in.setter
    def deleted_in(self, deleted_in):
        """Sets the deleted_in of this SystemBackupStatus.


        :param deleted_in: The deleted_in of this SystemBackupStatus.  # noqa: E501
        :type: str
        """

        self._deleted_in = deleted_in

    @property
    def full(self):
        """Gets the full of this SystemBackupStatus.  # noqa: E501


        :return: The full of this SystemBackupStatus.  # noqa: E501
        :rtype: bool
        """
        return self._full

    @full.setter
    def full(self, full):
        """Sets the full of this SystemBackupStatus.


        :param full: The full of this SystemBackupStatus.  # noqa: E501
        :type: bool
        """
        if (
            self.local_vars_configuration.client_side_validation and full is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `full`, must not be `None`"
            )  # noqa: E501

        self._full = full

    @property
    def size(self):
        """Gets the size of this SystemBackupStatus.  # noqa: E501


        :return: The size of this SystemBackupStatus.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this SystemBackupStatus.


        :param size: The size of this SystemBackupStatus.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation and size is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `size`, must not be `None`"
            )  # noqa: E501

        self._size = size

    @property
    def volumes(self):
        """Gets the volumes of this SystemBackupStatus.  # noqa: E501


        :return: The volumes of this SystemBackupStatus.  # noqa: E501
        :rtype: int
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this SystemBackupStatus.


        :param volumes: The volumes of this SystemBackupStatus.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation and volumes is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `volumes`, must not be `None`"
            )  # noqa: E501

        self._volumes = volumes

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
        if not isinstance(other, SystemBackupStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SystemBackupStatus):
            return True

        return self.to_dict() != other.to_dict()
