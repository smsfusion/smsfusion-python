# swagger_client.SMSApi

All URIs are relative to *https://api.smsfusion.com.au/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_sms**](SMSApi.md#send_sms) | **GET** /sms/ | Send an SMS


# **send_sms**
> SMSResult send_sms(key, num, msg, _from=_from, deliverby=deliverby, dlrcb=dlrcb, replycb=replycb, replyemail=replyemail, validity=validity, cc=cc)

Send an SMS

Send one or more SMS

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
api_instance = swagger_client.SMSApi()
key = 'key_example' # str | API Key as generated from the <a href='https://www.smsfusion.com.au/admin/api/'>admin panel</a>
num = ['num_example'] # list[str] | Comma separated list of phone numbers or <a href='https://www.smsfusion.com.au/help/msisdn/'>MSDISDN</a>'s
msg = 'msg_example' # str | Message content to send
_from = '_from_example' # str | MSISDN or vanity alphanumeric source number (optional)
deliverby = 'deliverby_example' # str | UTC encoded time to send the SMS (optional)
dlrcb = 'dlrcb_example' # str | HTTP or HTTPS callback URL for delivery reports. Timeout for callbacks is set to 30 seconds (optional)
replycb = 'replycb_example' # str | HTTP or HTTPS callback URL for replies. Timeout for callbacks is set to 30 seconds (optional)
replyemail = 'replyemail_example' # str | Email address to send replies to (optional)
validity = 56 # int | Time in minutes to keep the SMS valid for (optional)
cc = 'cc_example' # str | 2 character country code <a href='https://en.wikipedia.org/wiki/ISO_3166-2'>ISO 3166-2</a> for formatting local numbers internationally (optional)

try: 
    # Send an SMS
    api_response = api_instance.send_sms(key, num, msg, _from=_from, deliverby=deliverby, dlrcb=dlrcb, replycb=replycb, replyemail=replyemail, validity=validity, cc=cc)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSApi->send_sms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| API Key as generated from the &lt;a href&#x3D;&#39;https://www.smsfusion.com.au/admin/api/&#39;&gt;admin panel&lt;/a&gt; | 
 **num** | [**list[str]**](str.md)| Comma separated list of phone numbers or &lt;a href&#x3D;&#39;https://www.smsfusion.com.au/help/msisdn/&#39;&gt;MSDISDN&lt;/a&gt;&#39;s | 
 **msg** | **str**| Message content to send | 
 **_from** | **str**| MSISDN or vanity alphanumeric source number | [optional] 
 **deliverby** | **str**| UTC encoded time to send the SMS | [optional] 
 **dlrcb** | **str**| HTTP or HTTPS callback URL for delivery reports. Timeout for callbacks is set to 30 seconds | [optional] 
 **replycb** | **str**| HTTP or HTTPS callback URL for replies. Timeout for callbacks is set to 30 seconds | [optional] 
 **replyemail** | **str**| Email address to send replies to | [optional] 
 **validity** | **int**| Time in minutes to keep the SMS valid for | [optional] 
 **cc** | **str**| 2 character country code &lt;a href&#x3D;&#39;https://en.wikipedia.org/wiki/ISO_3166-2&#39;&gt;ISO 3166-2&lt;/a&gt; for formatting local numbers internationally | [optional] 

### Return type

[**SMSResult**](SMSResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

