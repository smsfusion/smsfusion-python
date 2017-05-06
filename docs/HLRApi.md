# swagger_client.HLRApi

All URIs are relative to *https://api.smsfusion.com.au/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_hlr**](HLRApi.md#get_hlr) | **GET** /hlr/ | HLR number lookup
[**get_hlr_callback**](HLRApi.md#get_hlr_callback) | **GET** /hlr-callback/ | HLR number lookup with results going to a callback URL


# **get_hlr**
> HLRCallback get_hlr(key, num, cc=cc)

HLR number lookup

Perform HLR on number

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
swagger_client.configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.HLRApi()
key = 'key_example' # str | API Key as generated from the <a href='https://www.smsfusion.com.au/admin/api/'>admin panel</a>
num = 'num_example' # str | A single phone number or <a href='https://www.smsfusion.com.au/help/msisdn/'>MSDISDN</a>
cc = 'cc_example' # str | 2 character country code <a href='https://en.wikipedia.org/wiki/ISO_3166-2'>ISO 3166-2</a> for formatting local numbers internationally (optional)

try: 
    # HLR number lookup
    api_response = api_instance.get_hlr(key, num, cc=cc)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HLRApi->get_hlr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| API Key as generated from the &lt;a href&#x3D;&#39;https://www.smsfusion.com.au/admin/api/&#39;&gt;admin panel&lt;/a&gt; | 
 **num** | **str**| A single phone number or &lt;a href&#x3D;&#39;https://www.smsfusion.com.au/help/msisdn/&#39;&gt;MSDISDN&lt;/a&gt; | 
 **cc** | **str**| 2 character country code &lt;a href&#x3D;&#39;https://en.wikipedia.org/wiki/ISO_3166-2&#39;&gt;ISO 3166-2&lt;/a&gt; for formatting local numbers internationally | [optional] 

### Return type

[**HLRCallback**](HLRCallback.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hlr_callback**
> HLRResult get_hlr_callback(key, num, cb, cc=cc)

HLR number lookup with results going to a callback URL

Perform HLR on number with the result being sent to the callback URL provided

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
swagger_client.configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.HLRApi()
key = 'key_example' # str | API Key as generated from the <a href='https://www.smsfusion.com.au/admin/api/'>admin panel</a>
num = ['num_example'] # list[str] | Comma separated list of phone numbers or <a href='https://www.smsfusion.com.au/help/msisdn/'>MSDISDN</a>'s
cb = 'cb_example' # str | HTTP or HTTPS callback URL for each result. The result will be sent as POST with a json object included in <b>result</b>. Timeout for callbacks is set to 30 seconds
cc = 'cc_example' # str | 2 character country code <a href='https://en.wikipedia.org/wiki/ISO_3166-2'>ISO 3166-2</a> for formatting local numbers internationally (optional)

try: 
    # HLR number lookup with results going to a callback URL
    api_response = api_instance.get_hlr_callback(key, num, cb, cc=cc)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HLRApi->get_hlr_callback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| API Key as generated from the &lt;a href&#x3D;&#39;https://www.smsfusion.com.au/admin/api/&#39;&gt;admin panel&lt;/a&gt; | 
 **num** | [**list[str]**](str.md)| Comma separated list of phone numbers or &lt;a href&#x3D;&#39;https://www.smsfusion.com.au/help/msisdn/&#39;&gt;MSDISDN&lt;/a&gt;&#39;s | 
 **cb** | **str**| HTTP or HTTPS callback URL for each result. The result will be sent as POST with a json object included in &lt;b&gt;result&lt;/b&gt;. Timeout for callbacks is set to 30 seconds | 
 **cc** | **str**| 2 character country code &lt;a href&#x3D;&#39;https://en.wikipedia.org/wiki/ISO_3166-2&#39;&gt;ISO 3166-2&lt;/a&gt; for formatting local numbers internationally | [optional] 

### Return type

[**HLRResult**](HLRResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

