# coding: utf-8

"""
    INCAS TA2-UIUC Datatypes

    This API document is defined based on INCAS Common Datatypes version 0.0.7.  # noqa: E501

    OpenAPI spec version: 1.2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from uiuc_incas_client.models.message import Message  # noqa: F401,E501

class UiucMessageDB(Message):
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
        'uiuc_message_id': 'str',
        'enrichments': 'dict(str, Enrichment)'
    }
    if hasattr(Message, "swagger_types"):
        swagger_types.update(Message.swagger_types)

    attribute_map = {
        'uiuc_message_id': 'uiucMessageId',
        'enrichments': 'enrichments'
    }
    if hasattr(Message, "attribute_map"):
        attribute_map.update(Message.attribute_map)

    def __init__(self, uiuc_message_id=None, enrichments=None, *args, **kwargs):  # noqa: E501
        """UiucMessageDB - a model defined in Swagger"""  # noqa: E501
        self._uiuc_message_id = None
        self._enrichments = None
        self.discriminator = None
        if uiuc_message_id is not None:
            self.uiuc_message_id = uiuc_message_id
        if enrichments is not None:
            self.enrichments = enrichments
        Message.__init__(self, *args, **kwargs)

    @property
    def uiuc_message_id(self):
        """Gets the uiuc_message_id of this UiucMessageDB.  # noqa: E501


        :return: The uiuc_message_id of this UiucMessageDB.  # noqa: E501
        :rtype: str
        """
        return self._uiuc_message_id

    @uiuc_message_id.setter
    def uiuc_message_id(self, uiuc_message_id):
        """Sets the uiuc_message_id of this UiucMessageDB.


        :param uiuc_message_id: The uiuc_message_id of this UiucMessageDB.  # noqa: E501
        :type: str
        """

        self._uiuc_message_id = uiuc_message_id

    @property
    def enrichments(self):
        """Gets the enrichments of this UiucMessageDB.  # noqa: E501


        :return: The enrichments of this UiucMessageDB.  # noqa: E501
        :rtype: dict(str, Enrichment)
        """
        return self._enrichments

    @enrichments.setter
    def enrichments(self, enrichments):
        """Sets the enrichments of this UiucMessageDB.


        :param enrichments: The enrichments of this UiucMessageDB.  # noqa: E501
        :type: dict(str, Enrichment)
        """

        self._enrichments = enrichments

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
        if issubclass(UiucMessageDB, dict):
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
        if not isinstance(other, UiucMessageDB):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
