# coding: utf-8

"""
    INCAS TA2-UIUC Datatypes

    This API document is defined based on INCAS Common Datatypes version 0.0.3.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class MessageIdResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'global_id': 'str',
        'media_id': 'str'
    }

    attribute_map = {
        'global_id': 'globalId',
        'media_id': 'mediaId'
    }

    def __init__(self, global_id=None, media_id=None):  # noqa: E501
        """MessageIdResponse - a model defined in Swagger"""  # noqa: E501
        self._global_id = None
        self._media_id = None
        self.discriminator = None
        if global_id is not None:
            self.global_id = global_id
        if media_id is not None:
            self.media_id = media_id

    @property
    def global_id(self):
        """Gets the global_id of this MessageIdResponse.  # noqa: E501


        :return: The global_id of this MessageIdResponse.  # noqa: E501
        :rtype: str
        """
        return self._global_id

    @global_id.setter
    def global_id(self, global_id):
        """Sets the global_id of this MessageIdResponse.


        :param global_id: The global_id of this MessageIdResponse.  # noqa: E501
        :type: str
        """

        self._global_id = global_id

    @property
    def media_id(self):
        """Gets the media_id of this MessageIdResponse.  # noqa: E501


        :return: The media_id of this MessageIdResponse.  # noqa: E501
        :rtype: str
        """
        return self._media_id

    @media_id.setter
    def media_id(self, media_id):
        """Sets the media_id of this MessageIdResponse.


        :param media_id: The media_id of this MessageIdResponse.  # noqa: E501
        :type: str
        """

        self._media_id = media_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(MessageIdResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MessageIdResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
