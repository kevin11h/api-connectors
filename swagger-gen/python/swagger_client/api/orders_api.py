# coding: utf-8

"""
    Bybit API

    ## REST API for the Bybit Exchange. Base URI: [https://api-testnet.bybit.com]    # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@bybit.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class OrdersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def linearorder_cancel(self, **kwargs):  # noqa: E501
        """Cancel Active Order  # noqa: E501

        This will cancel linear active order  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.linearorder_cancel(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object order_id:
        :param str order_link_id:
        :param str symbol:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.linearorder_cancel_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.linearorder_cancel_with_http_info(**kwargs)  # noqa: E501
            return data

    def linearorder_cancel_with_http_info(self, **kwargs):  # noqa: E501
        """Cancel Active Order  # noqa: E501

        This will cancel linear active order  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.linearorder_cancel_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object order_id:
        :param str order_link_id:
        :param str symbol:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['order_id', 'order_link_id', 'symbol']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method linearorder_cancel" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'order_id' in params:
            form_params.append(('order_id', params['order_id']))  # noqa: E501
        if 'order_link_id' in params:
            form_params.append(('order_link_id', params['order_link_id']))  # noqa: E501
        if 'symbol' in params:
            form_params.append(('symbol', params['symbol']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey', 'apiSignature', 'timestamp']  # noqa: E501

        return self.api_client.call_api(
            '/private/linear/order/cancel', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
