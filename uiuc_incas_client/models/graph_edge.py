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

class GraphEdge(object):
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
        'edge_type': 'str',
        'action_type': 'str',
        'src_id': 'str',
        'dst_id': 'str',
        'distance': 'float',
        'weight': 'float'
    }

    attribute_map = {
        'edge_type': 'edgeType',
        'action_type': 'actionType',
        'src_id': 'srcId',
        'dst_id': 'dstId',
        'distance': 'distance',
        'weight': 'weight'
    }

    def __init__(self, edge_type=None, action_type=None, src_id=None, dst_id=None, distance=None, weight=None):  # noqa: E501
        """GraphEdge - a model defined in Swagger"""  # noqa: E501
        self._edge_type = None
        self._action_type = None
        self._src_id = None
        self._dst_id = None
        self._distance = None
        self._weight = None
        self.discriminator = None
        self.edge_type = edge_type
        if action_type is not None:
            self.action_type = action_type
        if src_id is not None:
            self.src_id = src_id
        if dst_id is not None:
            self.dst_id = dst_id
        if distance is not None:
            self.distance = distance
        if weight is not None:
            self.weight = weight

    @property
    def edge_type(self):
        """Gets the edge_type of this GraphEdge.  # noqa: E501

        For discriminator  # noqa: E501

        :return: The edge_type of this GraphEdge.  # noqa: E501
        :rtype: str
        """
        return self._edge_type

    @edge_type.setter
    def edge_type(self, edge_type):
        """Sets the edge_type of this GraphEdge.

        For discriminator  # noqa: E501

        :param edge_type: The edge_type of this GraphEdge.  # noqa: E501
        :type: str
        """
        if edge_type is None:
            raise ValueError("Invalid value for `edge_type`, must not be `None`")  # noqa: E501

        self._edge_type = edge_type

    @property
    def action_type(self):
        """Gets the action_type of this GraphEdge.  # noqa: E501


        :return: The action_type of this GraphEdge.  # noqa: E501
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """Sets the action_type of this GraphEdge.


        :param action_type: The action_type of this GraphEdge.  # noqa: E501
        :type: str
        """

        self._action_type = action_type

    @property
    def src_id(self):
        """Gets the src_id of this GraphEdge.  # noqa: E501


        :return: The src_id of this GraphEdge.  # noqa: E501
        :rtype: str
        """
        return self._src_id

    @src_id.setter
    def src_id(self, src_id):
        """Sets the src_id of this GraphEdge.


        :param src_id: The src_id of this GraphEdge.  # noqa: E501
        :type: str
        """

        self._src_id = src_id

    @property
    def dst_id(self):
        """Gets the dst_id of this GraphEdge.  # noqa: E501


        :return: The dst_id of this GraphEdge.  # noqa: E501
        :rtype: str
        """
        return self._dst_id

    @dst_id.setter
    def dst_id(self, dst_id):
        """Sets the dst_id of this GraphEdge.


        :param dst_id: The dst_id of this GraphEdge.  # noqa: E501
        :type: str
        """

        self._dst_id = dst_id

    @property
    def distance(self):
        """Gets the distance of this GraphEdge.  # noqa: E501


        :return: The distance of this GraphEdge.  # noqa: E501
        :rtype: float
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        """Sets the distance of this GraphEdge.


        :param distance: The distance of this GraphEdge.  # noqa: E501
        :type: float
        """

        self._distance = distance

    @property
    def weight(self):
        """Gets the weight of this GraphEdge.  # noqa: E501


        :return: The weight of this GraphEdge.  # noqa: E501
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this GraphEdge.


        :param weight: The weight of this GraphEdge.  # noqa: E501
        :type: float
        """

        self._weight = weight

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
        if issubclass(GraphEdge, dict):
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
        if not isinstance(other, GraphEdge):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
