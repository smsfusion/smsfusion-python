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


class HLRCallback(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, msisdn=None, status=None, country=None, operator=None, mccmnc=None, duration=None, message=None, extended=None, cost=None):
        """
        HLRCallback - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'msisdn': 'int',
            'status': 'str',
            'country': 'str',
            'operator': 'str',
            'mccmnc': 'int',
            'duration': 'str',
            'message': 'str',
            'extended': 'str',
            'cost': 'float'
        }

        self.attribute_map = {
            'id': 'id',
            'msisdn': 'msisdn',
            'status': 'status',
            'country': 'country',
            'operator': 'operator',
            'mccmnc': 'mccmnc',
            'duration': 'duration',
            'message': 'message',
            'extended': 'extended',
            'cost': 'cost'
        }

        self._id = id
        self._msisdn = msisdn
        self._status = status
        self._country = country
        self._operator = operator
        self._mccmnc = mccmnc
        self._duration = duration
        self._message = message
        self._extended = extended
        self._cost = cost

    @property
    def id(self):
        """
        Gets the id of this HLRCallback.
        Unique ID for response

        :return: The id of this HLRCallback.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this HLRCallback.
        Unique ID for response

        :param id: The id of this HLRCallback.
        :type: str
        """

        self._id = id

    @property
    def msisdn(self):
        """
        Gets the msisdn of this HLRCallback.
        The MSISDN of the number queried

        :return: The msisdn of this HLRCallback.
        :rtype: int
        """
        return self._msisdn

    @msisdn.setter
    def msisdn(self, msisdn):
        """
        Sets the msisdn of this HLRCallback.
        The MSISDN of the number queried

        :param msisdn: The msisdn of this HLRCallback.
        :type: int
        """

        self._msisdn = msisdn

    @property
    def status(self):
        """
        Gets the status of this HLRCallback.
        Short status code of the response

        :return: The status of this HLRCallback.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this HLRCallback.
        Short status code of the response

        :param status: The status of this HLRCallback.
        :type: str
        """
        allowed_values = ["valid", "invalid", "unknown"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def country(self):
        """
        Gets the country of this HLRCallback.
        ISO 3166-2 country code

        :return: The country of this HLRCallback.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this HLRCallback.
        ISO 3166-2 country code

        :param country: The country of this HLRCallback.
        :type: str
        """

        self._country = country

    @property
    def operator(self):
        """
        Gets the operator of this HLRCallback.
        The operator attached to the MSISDN

        :return: The operator of this HLRCallback.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """
        Sets the operator of this HLRCallback.
        The operator attached to the MSISDN

        :param operator: The operator of this HLRCallback.
        :type: str
        """

        self._operator = operator

    @property
    def mccmnc(self):
        """
        Gets the mccmnc of this HLRCallback.
        MCC and MNC of MSDISDN

        :return: The mccmnc of this HLRCallback.
        :rtype: int
        """
        return self._mccmnc

    @mccmnc.setter
    def mccmnc(self, mccmnc):
        """
        Sets the mccmnc of this HLRCallback.
        MCC and MNC of MSDISDN

        :param mccmnc: The mccmnc of this HLRCallback.
        :type: int
        """

        self._mccmnc = mccmnc

    @property
    def duration(self):
        """
        Gets the duration of this HLRCallback.
        If the response code is temporary or permenant

        :return: The duration of this HLRCallback.
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """
        Sets the duration of this HLRCallback.
        If the response code is temporary or permenant

        :param duration: The duration of this HLRCallback.
        :type: str
        """
        allowed_values = ["perm", "temp"]
        if duration not in allowed_values:
            raise ValueError(
                "Invalid value for `duration` ({0}), must be one of {1}"
                .format(duration, allowed_values)
            )

        self._duration = duration

    @property
    def message(self):
        """
        Gets the message of this HLRCallback.
        Full status code of the response

        :return: The message of this HLRCallback.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this HLRCallback.
        Full status code of the response

        :param message: The message of this HLRCallback.
        :type: str
        """

        self._message = message

    @property
    def extended(self):
        """
        Gets the extended of this HLRCallback.
        Extended explanation of the status code

        :return: The extended of this HLRCallback.
        :rtype: str
        """
        return self._extended

    @extended.setter
    def extended(self, extended):
        """
        Sets the extended of this HLRCallback.
        Extended explanation of the status code

        :param extended: The extended of this HLRCallback.
        :type: str
        """

        self._extended = extended

    @property
    def cost(self):
        """
        Gets the cost of this HLRCallback.
        Cost of the response

        :return: The cost of this HLRCallback.
        :rtype: float
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """
        Sets the cost of this HLRCallback.
        Cost of the response

        :param cost: The cost of this HLRCallback.
        :type: float
        """

        self._cost = cost

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
        if not isinstance(other, HLRCallback):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
