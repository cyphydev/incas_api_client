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

class MessageEnrichmentsBatchGetBody(object):
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
        'ids': 'list[str]',
        'enrichment_name': 'str',
        'provider_name': 'str',
        'version': 'str',
        'dev': 'bool'
    }

    attribute_map = {
        'ids': 'ids',
        'enrichment_name': 'enrichmentName',
        'provider_name': 'providerName',
        'version': 'version',
        'dev': 'dev'
    }

    def __init__(self, ids=None, enrichment_name=None, provider_name=None, version=None, dev=None):  # noqa: E501
        """MessageEnrichmentsBatchGetBody - a model defined in Swagger"""  # noqa: E501
        self._ids = None
        self._enrichment_name = None
        self._provider_name = None
        self._version = None
        self._dev = None
        self.discriminator = None
        self.ids = ids
        if enrichment_name is not None:
            self.enrichment_name = enrichment_name
        if provider_name is not None:
            self.provider_name = provider_name
        if version is not None:
            self.version = version
        if dev is not None:
            self.dev = dev

    @property
    def ids(self):
        """Gets the ids of this MessageEnrichmentsBatchGetBody.  # noqa: E501


        :return: The ids of this MessageEnrichmentsBatchGetBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this MessageEnrichmentsBatchGetBody.


        :param ids: The ids of this MessageEnrichmentsBatchGetBody.  # noqa: E501
        :type: list[str]
        """
        if ids is None:
            raise ValueError("Invalid value for `ids`, must not be `None`")  # noqa: E501

        self._ids = ids

    @property
    def enrichment_name(self):
        """Gets the enrichment_name of this MessageEnrichmentsBatchGetBody.  # noqa: E501


        :return: The enrichment_name of this MessageEnrichmentsBatchGetBody.  # noqa: E501
        :rtype: str
        """
        return self._enrichment_name

    @enrichment_name.setter
    def enrichment_name(self, enrichment_name):
        """Sets the enrichment_name of this MessageEnrichmentsBatchGetBody.


        :param enrichment_name: The enrichment_name of this MessageEnrichmentsBatchGetBody.  # noqa: E501
        :type: str
        """

        self._enrichment_name = enrichment_name

    @property
    def provider_name(self):
        """Gets the provider_name of this MessageEnrichmentsBatchGetBody.  # noqa: E501


        :return: The provider_name of this MessageEnrichmentsBatchGetBody.  # noqa: E501
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        """Sets the provider_name of this MessageEnrichmentsBatchGetBody.


        :param provider_name: The provider_name of this MessageEnrichmentsBatchGetBody.  # noqa: E501
        :type: str
        """

        self._provider_name = provider_name

    @property
    def version(self):
        """Gets the version of this MessageEnrichmentsBatchGetBody.  # noqa: E501


        :return: The version of this MessageEnrichmentsBatchGetBody.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this MessageEnrichmentsBatchGetBody.


        :param version: The version of this MessageEnrichmentsBatchGetBody.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def dev(self):
        """Gets the dev of this MessageEnrichmentsBatchGetBody.  # noqa: E501


        :return: The dev of this MessageEnrichmentsBatchGetBody.  # noqa: E501
        :rtype: bool
        """
        return self._dev

    @dev.setter
    def dev(self, dev):
        """Sets the dev of this MessageEnrichmentsBatchGetBody.


        :param dev: The dev of this MessageEnrichmentsBatchGetBody.  # noqa: E501
        :type: bool
        """

        self._dev = dev

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
        if issubclass(MessageEnrichmentsBatchGetBody, dict):
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
        if not isinstance(other, MessageEnrichmentsBatchGetBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
