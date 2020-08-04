# mailinaboxapi.WebApi

All URIs are relative to *https://box.example.com/admin*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_web_domains**](WebApi.md#get_web_domains) | **GET** /web/domains | 
[**update_web**](WebApi.md#update_web) | **POST** /web/update | 


# **get_web_domains**
> list[WebDomain] get_web_domains()



Retrieve all static web domains.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import mailinaboxapi
from mailinaboxapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://box.example.com/admin
# See configuration.py for a list of all supported configuration parameters.
configuration = mailinaboxapi.Configuration(
    host = "https://box.example.com/admin"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = mailinaboxapi.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mailinaboxapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailinaboxapi.WebApi(api_client)
    
    try:
        api_response = api_instance.get_web_domains()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebApi->get_web_domains: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[WebDomain]**](WebDomain.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_web**
> str update_web()



Update static websites, used for updating domain root directories.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import mailinaboxapi
from mailinaboxapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://box.example.com/admin
# See configuration.py for a list of all supported configuration parameters.
configuration = mailinaboxapi.Configuration(
    host = "https://box.example.com/admin"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = mailinaboxapi.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mailinaboxapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailinaboxapi.WebApi(api_client)
    
    try:
        api_response = api_instance.update_web()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebApi->update_web: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

