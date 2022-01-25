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

class MediaResource(object):
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
        'account_type': 'str',
        'account_id': 'str',
        'user_names': 'list[str]',
        'hashed_user_names': 'list[str]',
        'account_status': 'str',
        'display_names': 'list[str]',
        'verified': 'bool',
        'url': 'str'
    }

    attribute_map = {
        'account_type': 'accountType',
        'account_id': 'accountId',
        'user_names': 'userNames',
        'hashed_user_names': 'hashedUserNames',
        'account_status': 'accountStatus',
        'display_names': 'displayNames',
        'verified': 'verified',
        'url': 'url'
    }

    def __init__(self, account_type=None, account_id=None, user_names=None, hashed_user_names=None, account_status=None, display_names=None, verified=None, url=None):  # noqa: E501
        """MediaResource - a model defined in Swagger"""  # noqa: E501
        self._account_type = None
        self._account_id = None
        self._user_names = None
        self._hashed_user_names = None
        self._account_status = None
        self._display_names = None
        self._verified = None
        self._url = None
        self.discriminator = None
        if account_type is not None:
            self.account_type = account_type
        if account_id is not None:
            self.account_id = account_id
        if user_names is not None:
            self.user_names = user_names
        if hashed_user_names is not None:
            self.hashed_user_names = hashed_user_names
        if account_status is not None:
            self.account_status = account_status
        if display_names is not None:
            self.display_names = display_names
        if verified is not None:
            self.verified = verified
        if url is not None:
            self.url = url

    @property
    def account_type(self):
        """Gets the account_type of this MediaResource.  # noqa: E501


        :return: The account_type of this MediaResource.  # noqa: E501
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """Sets the account_type of this MediaResource.


        :param account_type: The account_type of this MediaResource.  # noqa: E501
        :type: str
        """
        allowed_values = ["MEDIA_UNSPECIFIED", "News", "Reddit", "Twitter", "Webpage"]  # noqa: E501
        if account_type not in allowed_values:
            raise ValueError(
                "Invalid value for `account_type` ({0}), must be one of {1}"  # noqa: E501
                .format(account_type, allowed_values)
            )

        self._account_type = account_type

    @property
    def account_id(self):
        """Gets the account_id of this MediaResource.  # noqa: E501


        :return: The account_id of this MediaResource.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this MediaResource.


        :param account_id: The account_id of this MediaResource.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def user_names(self):
        """Gets the user_names of this MediaResource.  # noqa: E501


        :return: The user_names of this MediaResource.  # noqa: E501
        :rtype: list[str]
        """
        return self._user_names

    @user_names.setter
    def user_names(self, user_names):
        """Sets the user_names of this MediaResource.


        :param user_names: The user_names of this MediaResource.  # noqa: E501
        :type: list[str]
        """

        self._user_names = user_names

    @property
    def hashed_user_names(self):
        """Gets the hashed_user_names of this MediaResource.  # noqa: E501


        :return: The hashed_user_names of this MediaResource.  # noqa: E501
        :rtype: list[str]
        """
        return self._hashed_user_names

    @hashed_user_names.setter
    def hashed_user_names(self, hashed_user_names):
        """Sets the hashed_user_names of this MediaResource.


        :param hashed_user_names: The hashed_user_names of this MediaResource.  # noqa: E501
        :type: list[str]
        """

        self._hashed_user_names = hashed_user_names

    @property
    def account_status(self):
        """Gets the account_status of this MediaResource.  # noqa: E501


        :return: The account_status of this MediaResource.  # noqa: E501
        :rtype: str
        """
        return self._account_status

    @account_status.setter
    def account_status(self, account_status):
        """Sets the account_status of this MediaResource.


        :param account_status: The account_status of this MediaResource.  # noqa: E501
        :type: str
        """

        self._account_status = account_status

    @property
    def display_names(self):
        """Gets the display_names of this MediaResource.  # noqa: E501


        :return: The display_names of this MediaResource.  # noqa: E501
        :rtype: list[str]
        """
        return self._display_names

    @display_names.setter
    def display_names(self, display_names):
        """Sets the display_names of this MediaResource.


        :param display_names: The display_names of this MediaResource.  # noqa: E501
        :type: list[str]
        """

        self._display_names = display_names

    @property
    def verified(self):
        """Gets the verified of this MediaResource.  # noqa: E501


        :return: The verified of this MediaResource.  # noqa: E501
        :rtype: bool
        """
        return self._verified

    @verified.setter
    def verified(self, verified):
        """Sets the verified of this MediaResource.


        :param verified: The verified of this MediaResource.  # noqa: E501
        :type: bool
        """

        self._verified = verified

    @property
    def url(self):
        """Gets the url of this MediaResource.  # noqa: E501


        :return: The url of this MediaResource.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this MediaResource.


        :param url: The url of this MediaResource.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(MediaResource, dict):
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
        if not isinstance(other, MediaResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
