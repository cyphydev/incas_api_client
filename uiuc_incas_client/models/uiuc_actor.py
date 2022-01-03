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
from uiuc_incas_client.models.actor import Actor  # noqa: F401,E501

class UiucActor(Actor):
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
        'enrichments': 'list[ActorEnrichment]'
    }
    if hasattr(Actor, "swagger_types"):
        swagger_types.update(Actor.swagger_types)

    attribute_map = {
        'enrichments': 'enrichments'
    }
    if hasattr(Actor, "attribute_map"):
        attribute_map.update(Actor.attribute_map)

    def __init__(self, enrichments=None, *args, **kwargs):  # noqa: E501
        """UiucActor - a model defined in Swagger"""  # noqa: E501
        self._enrichments = None
        self.discriminator = None
        if enrichments is not None:
            self.enrichments = enrichments
        Actor.__init__(self, *args, **kwargs)

    @property
    def enrichments(self):
        """Gets the enrichments of this UiucActor.  # noqa: E501


        :return: The enrichments of this UiucActor.  # noqa: E501
        :rtype: list[ActorEnrichment]
        """
        return self._enrichments

    @enrichments.setter
    def enrichments(self, enrichments):
        """Sets the enrichments of this UiucActor.


        :param enrichments: The enrichments of this UiucActor.  # noqa: E501
        :type: list[ActorEnrichment]
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
        if issubclass(UiucActor, dict):
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
        if not isinstance(other, UiucActor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
