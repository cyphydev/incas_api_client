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

class ActorSegmentsBatchValidationResponse(object):
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
        'ok': 'dict(str, ActorSegmentCollection)',
        'id_invalid': 'dict(str, ActorSegmentCollection)',
        'value_invalid': 'dict(str, ActorSegmentCollection)',
        'value_not_found': 'dict(str, ActorSegmentCollection)',
        'value_existed': 'dict(str, ActorSegmentCollection)'
    }

    attribute_map = {
        'ok': 'ok',
        'id_invalid': 'idInvalid',
        'value_invalid': 'valueInvalid',
        'value_not_found': 'valueNotFound',
        'value_existed': 'valueExisted'
    }

    def __init__(self, ok=None, id_invalid=None, value_invalid=None, value_not_found=None, value_existed=None):  # noqa: E501
        """ActorSegmentsBatchValidationResponse - a model defined in Swagger"""  # noqa: E501
        self._ok = None
        self._id_invalid = None
        self._value_invalid = None
        self._value_not_found = None
        self._value_existed = None
        self.discriminator = None
        if ok is not None:
            self.ok = ok
        if id_invalid is not None:
            self.id_invalid = id_invalid
        if value_invalid is not None:
            self.value_invalid = value_invalid
        if value_not_found is not None:
            self.value_not_found = value_not_found
        if value_existed is not None:
            self.value_existed = value_existed

    @property
    def ok(self):
        """Gets the ok of this ActorSegmentsBatchValidationResponse.  # noqa: E501


        :return: The ok of this ActorSegmentsBatchValidationResponse.  # noqa: E501
        :rtype: dict(str, ActorSegmentCollection)
        """
        return self._ok

    @ok.setter
    def ok(self, ok):
        """Sets the ok of this ActorSegmentsBatchValidationResponse.


        :param ok: The ok of this ActorSegmentsBatchValidationResponse.  # noqa: E501
        :type: dict(str, ActorSegmentCollection)
        """

        self._ok = ok

    @property
    def id_invalid(self):
        """Gets the id_invalid of this ActorSegmentsBatchValidationResponse.  # noqa: E501


        :return: The id_invalid of this ActorSegmentsBatchValidationResponse.  # noqa: E501
        :rtype: dict(str, ActorSegmentCollection)
        """
        return self._id_invalid

    @id_invalid.setter
    def id_invalid(self, id_invalid):
        """Sets the id_invalid of this ActorSegmentsBatchValidationResponse.


        :param id_invalid: The id_invalid of this ActorSegmentsBatchValidationResponse.  # noqa: E501
        :type: dict(str, ActorSegmentCollection)
        """

        self._id_invalid = id_invalid

    @property
    def value_invalid(self):
        """Gets the value_invalid of this ActorSegmentsBatchValidationResponse.  # noqa: E501


        :return: The value_invalid of this ActorSegmentsBatchValidationResponse.  # noqa: E501
        :rtype: dict(str, ActorSegmentCollection)
        """
        return self._value_invalid

    @value_invalid.setter
    def value_invalid(self, value_invalid):
        """Sets the value_invalid of this ActorSegmentsBatchValidationResponse.


        :param value_invalid: The value_invalid of this ActorSegmentsBatchValidationResponse.  # noqa: E501
        :type: dict(str, ActorSegmentCollection)
        """

        self._value_invalid = value_invalid

    @property
    def value_not_found(self):
        """Gets the value_not_found of this ActorSegmentsBatchValidationResponse.  # noqa: E501


        :return: The value_not_found of this ActorSegmentsBatchValidationResponse.  # noqa: E501
        :rtype: dict(str, ActorSegmentCollection)
        """
        return self._value_not_found

    @value_not_found.setter
    def value_not_found(self, value_not_found):
        """Sets the value_not_found of this ActorSegmentsBatchValidationResponse.


        :param value_not_found: The value_not_found of this ActorSegmentsBatchValidationResponse.  # noqa: E501
        :type: dict(str, ActorSegmentCollection)
        """

        self._value_not_found = value_not_found

    @property
    def value_existed(self):
        """Gets the value_existed of this ActorSegmentsBatchValidationResponse.  # noqa: E501


        :return: The value_existed of this ActorSegmentsBatchValidationResponse.  # noqa: E501
        :rtype: dict(str, ActorSegmentCollection)
        """
        return self._value_existed

    @value_existed.setter
    def value_existed(self, value_existed):
        """Sets the value_existed of this ActorSegmentsBatchValidationResponse.


        :param value_existed: The value_existed of this ActorSegmentsBatchValidationResponse.  # noqa: E501
        :type: dict(str, ActorSegmentCollection)
        """

        self._value_existed = value_existed

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
        if issubclass(ActorSegmentsBatchValidationResponse, dict):
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
        if not isinstance(other, ActorSegmentsBatchValidationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
