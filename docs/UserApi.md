# mailinaboxapi.UserApi

All URIs are relative to *https://box.example.com/admin*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_me**](UserApi.md#get_me) | **GET** /me | 


# **get_me**
> MeResponse get_me()



Get user information, used for user authentication.  Authenticate a user by supplying the auth token as a base64 encoded string in format `email:password` using basic authentication headers.  If successful, a long-lived `api_key` is returned which can be used for subsequent requests to the API. 

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
    api_instance = mailinaboxapi.UserApi(api_client)
    
    try:
        api_response = api_instance.get_me()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->get_me: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MeResponse**](MeResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

