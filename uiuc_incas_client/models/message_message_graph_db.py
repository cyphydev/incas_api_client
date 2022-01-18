# coding: utf-8

"""
    INCAS TA2-UIUC Datatypes

    This API document is defined based on INCAS Common Datatypes version 0.0.6.  # noqa: E501

    OpenAPI spec version: 1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from uiuc_incas_client.models.base_graph import BaseGraph  # noqa: F401,E501

class MessageMessageGraphDB(BaseGraph):
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
        'enrichment_name': 'str',
        'edges': 'dict(str, GraphEdge)'
    }
    if hasattr(BaseGraph, "swagger_types"):
        swagger_types.update(BaseGraph.swagger_types)

    attribute_map = {
        'enrichment_name': 'enrichmentName',
        'edges': 'edges'
    }
    if hasattr(BaseGraph, "attribute_map"):
        attribute_map.update(BaseGraph.attribute_map)

    def __init__(self, enrichment_name=None, edges=None, *args, **kwargs):  # noqa: E501
        """MessageMessageGraphDB - a model defined in Swagger"""  # noqa: E501
        self._enrichment_name = None
        self._edges = None
        self.discriminator = None
        if enrichment_name is not None:
            self.enrichment_name = enrichment_name
        if edges is not None:
            self.edges = edges
        BaseGraph.__init__(self, *args, **kwargs)

    @property
    def enrichment_name(self):
        """Gets the enrichment_name of this MessageMessageGraphDB.  # noqa: E501

        The type of enrichment used to construct the msg2msg graph.  # noqa: E501

        :return: The enrichment_name of this MessageMessageGraphDB.  # noqa: E501
        :rtype: str
        """
        return self._enrichment_name

    @enrichment_name.setter
    def enrichment_name(self, enrichment_name):
        """Sets the enrichment_name of this MessageMessageGraphDB.

        The type of enrichment used to construct the msg2msg graph.  # noqa: E501

        :param enrichment_name: The enrichment_name of this MessageMessageGraphDB.  # noqa: E501
        :type: str
        """

        self._enrichment_name = enrichment_name

    @property
    def edges(self):
        """Gets the edges of this MessageMessageGraphDB.  # noqa: E501


        :return: The edges of this MessageMessageGraphDB.  # noqa: E501
        :rtype: dict(str, GraphEdge)
        """
        return self._edges

    @edges.setter
    def edges(self, edges):
        """Sets the edges of this MessageMessageGraphDB.


        :param edges: The edges of this MessageMessageGraphDB.  # noqa: E501
        :type: dict(str, GraphEdge)
        """

        self._edges = edges

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
        if issubclass(MessageMessageGraphDB, dict):
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
        if not isinstance(other, MessageMessageGraphDB):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
