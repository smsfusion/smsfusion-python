# coding: utf-8

"""
    SMS Fusion API

    This is the SMS Fusion API

    OpenAPI spec version: 1.0.0
    Contact: support@smsfusion.com.au
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.sms_api import SMSApi


class TestSMSApi(unittest.TestCase):
    """ SMSApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.sms_api.SMSApi()

    def tearDown(self):
        pass

    def test_send_sms(self):
        """
        Test case for send_sms

        Send an SMS
        """
        pass


if __name__ == '__main__':
    unittest.main()