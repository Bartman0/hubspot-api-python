# coding: utf-8

"""
    Blog Post endpoints

    \"Use these endpoints for interacting with Blog Posts, Blog Authors, and Blog Tags\"  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.cms.blogs.tags.configuration import Configuration


class Tag(object):
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
    openapi_types = {"id": "str", "name": "str", "deleted_at": "datetime", "created_at": "datetime", "updated_at": "datetime"}

    attribute_map = {"id": "id", "name": "name", "deleted_at": "deletedAt", "created_at": "createdAt", "updated_at": "updatedAt"}

    def __init__(self, id=None, name=None, deleted_at=None, created_at=None, updated_at=None, local_vars_configuration=None):  # noqa: E501
        """Tag - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._deleted_at = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.deleted_at = deleted_at
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this Tag.  # noqa: E501

        The unique ID of the Blog Tag.  # noqa: E501

        :return: The id of this Tag.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Tag.

        The unique ID of the Blog Tag.  # noqa: E501

        :param id: The id of this Tag.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Tag.  # noqa: E501

        The name of the tag.  # noqa: E501

        :return: The name of this Tag.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Tag.

        The name of the tag.  # noqa: E501

        :param name: The name of this Tag.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def deleted_at(self):
        """Gets the deleted_at of this Tag.  # noqa: E501

        The timestamp (ISO8601 format) when this Blog Tag was deleted.  # noqa: E501

        :return: The deleted_at of this Tag.  # noqa: E501
        :rtype: datetime
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """Sets the deleted_at of this Tag.

        The timestamp (ISO8601 format) when this Blog Tag was deleted.  # noqa: E501

        :param deleted_at: The deleted_at of this Tag.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and deleted_at is None:  # noqa: E501
            raise ValueError("Invalid value for `deleted_at`, must not be `None`")  # noqa: E501

        self._deleted_at = deleted_at

    @property
    def created_at(self):
        """Gets the created_at of this Tag.  # noqa: E501

        The timestamp (ISO8601 format) when this Blog Tag was created.  # noqa: E501

        :return: The created_at of this Tag.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Tag.

        The timestamp (ISO8601 format) when this Blog Tag was created.  # noqa: E501

        :param created_at: The created_at of this Tag.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Tag.  # noqa: E501

        The timestamp (ISO8601 format) when this Blog Tag was last updated.  # noqa: E501

        :return: The updated_at of this Tag.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Tag.

        The timestamp (ISO8601 format) when this Blog Tag was last updated.  # noqa: E501

        :param updated_at: The updated_at of this Tag.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_at is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(lambda item: (item[0], item[1].to_dict()) if hasattr(item[1], "to_dict") else item, value.items()))
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
        if not isinstance(other, Tag):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Tag):
            return True

        return self.to_dict() != other.to_dict()
