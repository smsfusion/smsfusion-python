# coding: utf-8

"""
    SMS Fusion API

    This is the SMS Fusion API

    OpenAPI spec version: 1.0.0
    Contact: support@smsfusion.com.au
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class DefaultApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def get_hlr(self, key, num, **kwargs):
        """
        HLR number lookup
        Perform HLR on number
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_hlr(key, num, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str key: API Key as generated from the <a href='https://www.smsfusion.com.au/admin/api/'>admin panel</a> (required)
        :param str num: A single phone number or <a href='https://www.smsfusion.com.au/help/msisdn/'>MSDISDN</a> (required)
        :param str cc: 2 character country code <a href='https://en.wikipedia.org/wiki/ISO_3166-2'>ISO 3166-2</a> for formatting local numbers internationally
        :return: HLRCallback
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_hlr_with_http_info(key, num, **kwargs)
        else:
            (data) = self.get_hlr_with_http_info(key, num, **kwargs)
            return data

    def get_hlr_with_http_info(self, key, num, **kwargs):
        """
        HLR number lookup
        Perform HLR on number
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_hlr_with_http_info(key, num, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str key: API Key as generated from the <a href='https://www.smsfusion.com.au/admin/api/'>admin panel</a> (required)
        :param str num: A single phone number or <a href='https://www.smsfusion.com.au/help/msisdn/'>MSDISDN</a> (required)
        :param str cc: 2 character country code <a href='https://en.wikipedia.org/wiki/ISO_3166-2'>ISO 3166-2</a> for formatting local numbers internationally
        :return: HLRCallback
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['key', 'num', 'cc']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_hlr" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'key' is set
        if ('key' not in params) or (params['key'] is None):
            raise ValueError("Missing the required parameter `key` when calling `get_hlr`")
        # verify the required parameter 'num' is set
        if ('num' not in params) or (params['num'] is None):
            raise ValueError("Missing the required parameter `num` when calling `get_hlr`")


        collection_formats = {}

        resource_path = '/hlr/'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'key' in params:
            query_params['key'] = params['key']
        if 'num' in params:
            query_params['num'] = params['num']
        if 'cc' in params:
            query_params['cc'] = params['cc']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['api_key']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='HLRCallback',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_hlr_callback(self, key, num, cb, **kwargs):
        """
        HLR number lookup with results going to a callback URL
        Perform HLR on number with the result being sent to the callback URL provided
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_hlr_callback(key, num, cb, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str key: API Key as generated from the <a href='https://www.smsfusion.com.au/admin/api/'>admin panel</a> (required)
        :param list[str] num: Comma separated list of phone numbers or <a href='https://www.smsfusion.com.au/help/msisdn/'>MSDISDN</a>'s (required)
        :param str cb: HTTP or HTTPS callback URL for each result. The result will be sent as POST with a json object included in <b>result</b>. Timeout for callbacks is set to 30 seconds (required)
        :param str cc: 2 character country code <a href='https://en.wikipedia.org/wiki/ISO_3166-2'>ISO 3166-2</a> for formatting local numbers internationally
        :return: HLRResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_hlr_callback_with_http_info(key, num, cb, **kwargs)
        else:
            (data) = self.get_hlr_callback_with_http_info(key, num, cb, **kwargs)
            return data

    def get_hlr_callback_with_http_info(self, key, num, cb, **kwargs):
        """
        HLR number lookup with results going to a callback URL
        Perform HLR on number with the result being sent to the callback URL provided
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_hlr_callback_with_http_info(key, num, cb, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str key: API Key as generated from the <a href='https://www.smsfusion.com.au/admin/api/'>admin panel</a> (required)
        :param list[str] num: Comma separated list of phone numbers or <a href='https://www.smsfusion.com.au/help/msisdn/'>MSDISDN</a>'s (required)
        :param str cb: HTTP or HTTPS callback URL for each result. The result will be sent as POST with a json object included in <b>result</b>. Timeout for callbacks is set to 30 seconds (required)
        :param str cc: 2 character country code <a href='https://en.wikipedia.org/wiki/ISO_3166-2'>ISO 3166-2</a> for formatting local numbers internationally
        :return: HLRResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['key', 'num', 'cb', 'cc']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_hlr_callback" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'key' is set
        if ('key' not in params) or (params['key'] is None):
            raise ValueError("Missing the required parameter `key` when calling `get_hlr_callback`")
        # verify the required parameter 'num' is set
        if ('num' not in params) or (params['num'] is None):
            raise ValueError("Missing the required parameter `num` when calling `get_hlr_callback`")
        # verify the required parameter 'cb' is set
        if ('cb' not in params) or (params['cb'] is None):
            raise ValueError("Missing the required parameter `cb` when calling `get_hlr_callback`")


        collection_formats = {}

        resource_path = '/hlr-callback/'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'key' in params:
            query_params['key'] = params['key']
        if 'num' in params:
            query_params['num'] = params['num']
            collection_formats['num'] = 'csv'
        if 'cb' in params:
            query_params['cb'] = params['cb']
        if 'cc' in params:
            query_params['cc'] = params['cc']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['api_key']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='HLRResult',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)