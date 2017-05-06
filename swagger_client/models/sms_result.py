# coding: utf-8

"""
    SMS Fusion API

    This is the SMS Fusion API

    OpenAPI spec version: 1.0.0
    Contact: support@smsfusion.com.au
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class SMSResult(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, success=None, cost=None, count=None, failure=None):
        """
        SMSResult - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'success': 'int',
            'cost': 'float',
            'count': 'int',
            'failure': 'list[str]'
        }

        self.attribute_map = {
            'id': 'id',
            'success': 'success',
            'cost': 'cost',
            'count': 'count',
            'failure': 'failure'
        }

        self._id = id
        self._success = success
        self._cost = cost
        self._count = count
        self._failure = failure

    @property
    def id(self):
        """
        Gets the id of this SMSResult.
        Unique ID for response

        :return: The id of this SMSResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SMSResult.
        Unique ID for response

        :param id: The id of this SMSResult.
        :type: str
        """

        self._id = id

    @property
    def success(self):
        """
        Gets the success of this SMSResult.
        Count of queued SMS

        :return: The success of this SMSResult.
        :rtype: int
        """
        return self._success

    @success.setter
    def success(self, success):
        """
        Sets the success of this SMSResult.
        Count of queued SMS

        :param success: The success of this SMSResult.
        :type: int
        """

        self._success = success

    @property
    def cost(self):
        """
        Gets the cost of this SMSResult.
        Cost of the SMS

        :return: The cost of this SMSResult.
        :rtype: float
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """
        Sets the cost of this SMSResult.
        Cost of the SMS

        :param cost: The cost of this SMSResult.
        :type: float
        """

        self._cost = cost

    @property
    def count(self):
        """
        Gets the count of this SMSResult.
        Total count of SMS queued

        :return: The count of this SMSResult.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this SMSResult.
        Total count of SMS queued

        :param count: The count of this SMSResult.
        :type: int
        """

        self._count = count

    @property
    def failure(self):
        """
        Gets the failure of this SMSResult.
        List of failed numbers

        :return: The failure of this SMSResult.
        :rtype: list[str]
        """
        return self._failure

    @failure.setter
    def failure(self, failure):
        """
        Sets the failure of this SMSResult.
        List of failed numbers

        :param failure: The failure of this SMSResult.
        :type: list[str]
        """

        self._failure = failure

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, SMSResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
