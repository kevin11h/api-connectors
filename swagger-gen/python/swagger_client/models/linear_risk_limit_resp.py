# coding: utf-8

"""
    Bybit API

    ## REST API for the Bybit Exchange. Base URI: [https://api.bybit.com]    # noqa: E501

    OpenAPI spec version: 0.2.6
    Contact: support@bybit.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class LinearRiskLimitResp(object):
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
        'created_at': 'str',
        'id': 'int',
        'is_lowest_risk': 'int',
        'limit': 'int',
        'maintain_margin': 'float',
        'section': 'list[str]',
        'starting_margin': 'float',
        'symbol': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'created_at': 'created_at',
        'id': 'id',
        'is_lowest_risk': 'is_lowest_risk',
        'limit': 'limit',
        'maintain_margin': 'maintain_margin',
        'section': 'section',
        'starting_margin': 'starting_margin',
        'symbol': 'symbol',
        'updated_at': 'updated_at'
    }

    def __init__(self, created_at=None, id=None, is_lowest_risk=None, limit=None, maintain_margin=None, section=None, starting_margin=None, symbol=None, updated_at=None):  # noqa: E501
        """LinearRiskLimitResp - a model defined in Swagger"""  # noqa: E501

        self._created_at = None
        self._id = None
        self._is_lowest_risk = None
        self._limit = None
        self._maintain_margin = None
        self._section = None
        self._starting_margin = None
        self._symbol = None
        self._updated_at = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if id is not None:
            self.id = id
        if is_lowest_risk is not None:
            self.is_lowest_risk = is_lowest_risk
        if limit is not None:
            self.limit = limit
        if maintain_margin is not None:
            self.maintain_margin = maintain_margin
        if section is not None:
            self.section = section
        if starting_margin is not None:
            self.starting_margin = starting_margin
        if symbol is not None:
            self.symbol = symbol
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def created_at(self):
        """Gets the created_at of this LinearRiskLimitResp.  # noqa: E501


        :return: The created_at of this LinearRiskLimitResp.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this LinearRiskLimitResp.


        :param created_at: The created_at of this LinearRiskLimitResp.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def id(self):
        """Gets the id of this LinearRiskLimitResp.  # noqa: E501


        :return: The id of this LinearRiskLimitResp.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LinearRiskLimitResp.


        :param id: The id of this LinearRiskLimitResp.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def is_lowest_risk(self):
        """Gets the is_lowest_risk of this LinearRiskLimitResp.  # noqa: E501


        :return: The is_lowest_risk of this LinearRiskLimitResp.  # noqa: E501
        :rtype: int
        """
        return self._is_lowest_risk

    @is_lowest_risk.setter
    def is_lowest_risk(self, is_lowest_risk):
        """Sets the is_lowest_risk of this LinearRiskLimitResp.


        :param is_lowest_risk: The is_lowest_risk of this LinearRiskLimitResp.  # noqa: E501
        :type: int
        """

        self._is_lowest_risk = is_lowest_risk

    @property
    def limit(self):
        """Gets the limit of this LinearRiskLimitResp.  # noqa: E501


        :return: The limit of this LinearRiskLimitResp.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this LinearRiskLimitResp.


        :param limit: The limit of this LinearRiskLimitResp.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def maintain_margin(self):
        """Gets the maintain_margin of this LinearRiskLimitResp.  # noqa: E501


        :return: The maintain_margin of this LinearRiskLimitResp.  # noqa: E501
        :rtype: float
        """
        return self._maintain_margin

    @maintain_margin.setter
    def maintain_margin(self, maintain_margin):
        """Sets the maintain_margin of this LinearRiskLimitResp.


        :param maintain_margin: The maintain_margin of this LinearRiskLimitResp.  # noqa: E501
        :type: float
        """

        self._maintain_margin = maintain_margin

    @property
    def section(self):
        """Gets the section of this LinearRiskLimitResp.  # noqa: E501


        :return: The section of this LinearRiskLimitResp.  # noqa: E501
        :rtype: list[str]
        """
        return self._section

    @section.setter
    def section(self, section):
        """Sets the section of this LinearRiskLimitResp.


        :param section: The section of this LinearRiskLimitResp.  # noqa: E501
        :type: list[str]
        """

        self._section = section

    @property
    def starting_margin(self):
        """Gets the starting_margin of this LinearRiskLimitResp.  # noqa: E501


        :return: The starting_margin of this LinearRiskLimitResp.  # noqa: E501
        :rtype: float
        """
        return self._starting_margin

    @starting_margin.setter
    def starting_margin(self, starting_margin):
        """Sets the starting_margin of this LinearRiskLimitResp.


        :param starting_margin: The starting_margin of this LinearRiskLimitResp.  # noqa: E501
        :type: float
        """

        self._starting_margin = starting_margin

    @property
    def symbol(self):
        """Gets the symbol of this LinearRiskLimitResp.  # noqa: E501


        :return: The symbol of this LinearRiskLimitResp.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this LinearRiskLimitResp.


        :param symbol: The symbol of this LinearRiskLimitResp.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

    @property
    def updated_at(self):
        """Gets the updated_at of this LinearRiskLimitResp.  # noqa: E501


        :return: The updated_at of this LinearRiskLimitResp.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this LinearRiskLimitResp.


        :param updated_at: The updated_at of this LinearRiskLimitResp.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

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
        if issubclass(LinearRiskLimitResp, dict):
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
        if not isinstance(other, LinearRiskLimitResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
