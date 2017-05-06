# swagger_client
This is the SMS Fusion API

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen
For more information, please visit [https://www.smsfusion.com.au/help/](https://www.smsfusion.com.au/help/)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/smsfusion/smsfusion-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/smsfusion/smsfusion-python.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
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

## Documentation for API Endpoints

All URIs are relative to *https://api.smsfusion.com.au/*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*HLRApi* | [**get_hlr**](docs/HLRApi.md#get_hlr) | **GET** /hlr/ | HLR number lookup
*HLRApi* | [**get_hlr_callback**](docs/HLRApi.md#get_hlr_callback) | **GET** /hlr-callback/ | HLR number lookup with results going to a callback URL
*SMSApi* | [**send_sms**](docs/SMSApi.md#send_sms) | **GET** /sms/ | Send an SMS


## Documentation For Models

 - [HLRCallback](docs/HLRCallback.md)
 - [HLRError](docs/HLRError.md)
 - [HLRResult](docs/HLRResult.md)
 - [OutOfCredit](docs/OutOfCredit.md)
 - [SMSResult](docs/SMSResult.md)


## Documentation For Authorization


## api_key

- **Type**: API key
- **API key parameter name**: key
- **Location**: URL query string


## Author

support@smsfusion.com.au

