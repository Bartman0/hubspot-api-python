# coding: utf-8

"""
    Timeline events

    This feature allows an app to create and configure custom events that can show up in the timelines of certain CRM object like contacts, companies, tickets, or deals. You'll find multiple use cases for this API in the sections below.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.crm.timeline.configuration import Configuration


class TimelineEventResponse(object):
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
        "id": "str",
        "event_template_id": "str",
        "email": "str",
        "object_id": "str",
        "utk": "str",
        "domain": "str",
        "timestamp": "datetime",
        "tokens": "dict(str, str)",
        "extra_data": "object",
        "timeline_i_frame": "TimelineEventIFrame",
        "object_type": "str",
        "created_at": "datetime",
    }

    attribute_map = {
        "id": "id",
        "event_template_id": "eventTemplateId",
        "email": "email",
        "object_id": "objectId",
        "utk": "utk",
        "domain": "domain",
        "timestamp": "timestamp",
        "tokens": "tokens",
        "extra_data": "extraData",
        "timeline_i_frame": "timelineIFrame",
        "object_type": "objectType",
        "created_at": "createdAt",
    }

    def __init__(
        self,
        id=None,
        event_template_id=None,
        email=None,
        object_id=None,
        utk=None,
        domain=None,
        timestamp=None,
        tokens=None,
        extra_data=None,
        timeline_i_frame=None,
        object_type=None,
        created_at=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """TimelineEventResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._event_template_id = None
        self._email = None
        self._object_id = None
        self._utk = None
        self._domain = None
        self._timestamp = None
        self._tokens = None
        self._extra_data = None
        self._timeline_i_frame = None
        self._object_type = None
        self._created_at = None
        self.discriminator = None

        self.id = id
        self.event_template_id = event_template_id
        if email is not None:
            self.email = email
        if object_id is not None:
            self.object_id = object_id
        if utk is not None:
            self.utk = utk
        if domain is not None:
            self.domain = domain
        if timestamp is not None:
            self.timestamp = timestamp
        self.tokens = tokens
        if extra_data is not None:
            self.extra_data = extra_data
        if timeline_i_frame is not None:
            self.timeline_i_frame = timeline_i_frame
        self.object_type = object_type
        if created_at is not None:
            self.created_at = created_at

    @property
    def id(self):
        """Gets the id of this TimelineEventResponse.  # noqa: E501

        Identifier for the event. This should be unique to the app and event template. If you use the same ID for different CRM objects, the last to be processed will win and the first will not have a record. You can also use `{{uuid}}` anywhere in the ID to generate a unique string, guaranteeing uniqueness.  # noqa: E501

        :return: The id of this TimelineEventResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TimelineEventResponse.

        Identifier for the event. This should be unique to the app and event template. If you use the same ID for different CRM objects, the last to be processed will win and the first will not have a record. You can also use `{{uuid}}` anywhere in the ID to generate a unique string, guaranteeing uniqueness.  # noqa: E501

        :param id: The id of this TimelineEventResponse.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and id is None
        ):  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def event_template_id(self):
        """Gets the event_template_id of this TimelineEventResponse.  # noqa: E501

        The event template ID.  # noqa: E501

        :return: The event_template_id of this TimelineEventResponse.  # noqa: E501
        :rtype: str
        """
        return self._event_template_id

    @event_template_id.setter
    def event_template_id(self, event_template_id):
        """Sets the event_template_id of this TimelineEventResponse.

        The event template ID.  # noqa: E501

        :param event_template_id: The event_template_id of this TimelineEventResponse.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation
            and event_template_id is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `event_template_id`, must not be `None`"
            )  # noqa: E501

        self._event_template_id = event_template_id

    @property
    def email(self):
        """Gets the email of this TimelineEventResponse.  # noqa: E501

        The email address used for contact-specific events. This can be used to identify existing contacts, create new ones, or change the email for an existing contact (if paired with the `objectId`).  # noqa: E501

        :return: The email of this TimelineEventResponse.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this TimelineEventResponse.

        The email address used for contact-specific events. This can be used to identify existing contacts, create new ones, or change the email for an existing contact (if paired with the `objectId`).  # noqa: E501

        :param email: The email of this TimelineEventResponse.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def object_id(self):
        """Gets the object_id of this TimelineEventResponse.  # noqa: E501

        The CRM object identifier. This is required for every event other than contacts (where utk or email can be used).  # noqa: E501

        :return: The object_id of this TimelineEventResponse.  # noqa: E501
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this TimelineEventResponse.

        The CRM object identifier. This is required for every event other than contacts (where utk or email can be used).  # noqa: E501

        :param object_id: The object_id of this TimelineEventResponse.  # noqa: E501
        :type: str
        """

        self._object_id = object_id

    @property
    def utk(self):
        """Gets the utk of this TimelineEventResponse.  # noqa: E501

        Use the `utk` parameter to associate an event with a contact by `usertoken`. This is recommended if you don't know a user's email, but have an identifying user token in your cookie.  # noqa: E501

        :return: The utk of this TimelineEventResponse.  # noqa: E501
        :rtype: str
        """
        return self._utk

    @utk.setter
    def utk(self, utk):
        """Sets the utk of this TimelineEventResponse.

        Use the `utk` parameter to associate an event with a contact by `usertoken`. This is recommended if you don't know a user's email, but have an identifying user token in your cookie.  # noqa: E501

        :param utk: The utk of this TimelineEventResponse.  # noqa: E501
        :type: str
        """

        self._utk = utk

    @property
    def domain(self):
        """Gets the domain of this TimelineEventResponse.  # noqa: E501

        The event domain (often paired with utk).  # noqa: E501

        :return: The domain of this TimelineEventResponse.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this TimelineEventResponse.

        The event domain (often paired with utk).  # noqa: E501

        :param domain: The domain of this TimelineEventResponse.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def timestamp(self):
        """Gets the timestamp of this TimelineEventResponse.  # noqa: E501

        The time the event occurred. If not passed in, the curren time will be assumed. This is used to determine where an event is shown on a CRM object's timeline.  # noqa: E501

        :return: The timestamp of this TimelineEventResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this TimelineEventResponse.

        The time the event occurred. If not passed in, the curren time will be assumed. This is used to determine where an event is shown on a CRM object's timeline.  # noqa: E501

        :param timestamp: The timestamp of this TimelineEventResponse.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def tokens(self):
        """Gets the tokens of this TimelineEventResponse.  # noqa: E501

        A collection of token keys and values associated with the template tokens.  # noqa: E501

        :return: The tokens of this TimelineEventResponse.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._tokens

    @tokens.setter
    def tokens(self, tokens):
        """Sets the tokens of this TimelineEventResponse.

        A collection of token keys and values associated with the template tokens.  # noqa: E501

        :param tokens: The tokens of this TimelineEventResponse.  # noqa: E501
        :type: dict(str, str)
        """
        if (
            self.local_vars_configuration.client_side_validation and tokens is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `tokens`, must not be `None`"
            )  # noqa: E501

        self._tokens = tokens

    @property
    def extra_data(self):
        """Gets the extra_data of this TimelineEventResponse.  # noqa: E501

        Additional event-specific data that can be interpreted by the template's markdown.  # noqa: E501

        :return: The extra_data of this TimelineEventResponse.  # noqa: E501
        :rtype: object
        """
        return self._extra_data

    @extra_data.setter
    def extra_data(self, extra_data):
        """Sets the extra_data of this TimelineEventResponse.

        Additional event-specific data that can be interpreted by the template's markdown.  # noqa: E501

        :param extra_data: The extra_data of this TimelineEventResponse.  # noqa: E501
        :type: object
        """

        self._extra_data = extra_data

    @property
    def timeline_i_frame(self):
        """Gets the timeline_i_frame of this TimelineEventResponse.  # noqa: E501


        :return: The timeline_i_frame of this TimelineEventResponse.  # noqa: E501
        :rtype: TimelineEventIFrame
        """
        return self._timeline_i_frame

    @timeline_i_frame.setter
    def timeline_i_frame(self, timeline_i_frame):
        """Sets the timeline_i_frame of this TimelineEventResponse.


        :param timeline_i_frame: The timeline_i_frame of this TimelineEventResponse.  # noqa: E501
        :type: TimelineEventIFrame
        """

        self._timeline_i_frame = timeline_i_frame

    @property
    def object_type(self):
        """Gets the object_type of this TimelineEventResponse.  # noqa: E501

        The ObjectType associated with the EventTemplate.  # noqa: E501

        :return: The object_type of this TimelineEventResponse.  # noqa: E501
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this TimelineEventResponse.

        The ObjectType associated with the EventTemplate.  # noqa: E501

        :param object_type: The object_type of this TimelineEventResponse.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and object_type is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `object_type`, must not be `None`"
            )  # noqa: E501

        self._object_type = object_type

    @property
    def created_at(self):
        """Gets the created_at of this TimelineEventResponse.  # noqa: E501


        :return: The created_at of this TimelineEventResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this TimelineEventResponse.


        :param created_at: The created_at of this TimelineEventResponse.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

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
        if not isinstance(other, TimelineEventResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TimelineEventResponse):
            return True

        return self.to_dict() != other.to_dict()
