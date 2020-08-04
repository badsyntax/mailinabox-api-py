# mailinaboxapi.SystemApi

All URIs are relative to *https://box.example.com/admin*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_system_backup_config**](SystemApi.md#get_system_backup_config) | **GET** /system/backup/config | 
[**get_system_backup_status**](SystemApi.md#get_system_backup_status) | **GET** /system/backup/status | 
[**get_system_privacy_status**](SystemApi.md#get_system_privacy_status) | **GET** /system/privacy | 
[**get_system_reboot_status**](SystemApi.md#get_system_reboot_status) | **GET** /system/reboot | 
[**get_system_status**](SystemApi.md#get_system_status) | **POST** /system/status | 
[**get_system_updates**](SystemApi.md#get_system_updates) | **GET** /system/updates | 
[**get_system_upstream_version**](SystemApi.md#get_system_upstream_version) | **POST** /system/latest-upstream-version | 
[**get_system_version**](SystemApi.md#get_system_version) | **GET** /system/version | 
[**reboot_system**](SystemApi.md#reboot_system) | **POST** /system/reboot | 
[**update_system_backup_config**](SystemApi.md#update_system_backup_config) | **POST** /system/backup/config | 
[**update_system_packages**](SystemApi.md#update_system_packages) | **POST** /system/update-packages | 
[**update_system_privacy**](SystemApi.md#update_system_privacy) | **POST** /system/privacy | 


# **get_system_backup_config**
> SystemBackupConfigResponse get_system_backup_config()



Retrieve backup config.

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
    api_instance = mailinaboxapi.SystemApi(api_client)
    
    try:
        api_response = api_instance.get_system_backup_config()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SystemApi->get_system_backup_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemBackupConfigResponse**](SystemBackupConfigResponse.md)

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

# **get_system_backup_status**
> SystemBackupStatusResponse get_system_backup_status()



Retrieve backup status.  If the list of backups is empty, this implies no backups have been made yet. 

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
    api_instance = mailinaboxapi.SystemApi(api_client)
    
    try:
        api_response = api_instance.get_system_backup_status()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SystemApi->get_system_backup_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemBackupStatusResponse**](SystemBackupStatusResponse.md)

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

# **get_system_privacy_status**
> bool get_system_privacy_status()



Retrieve new-version check status.  Response:    - `true`: Private, new-version checks will not be performed   - `false`: Not private, new-version checks will be performed 

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
    api_instance = mailinaboxapi.SystemApi(api_client)
    
    try:
        api_response = api_instance.get_system_privacy_status()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SystemApi->get_system_privacy_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**bool**

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

# **get_system_reboot_status**
> bool get_system_reboot_status()



Retrieve reboot status.  Response:    - `true`: A reboot is required   - `false`: A reboot is not required 

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
    api_instance = mailinaboxapi.SystemApi(api_client)
    
    try:
        api_response = api_instance.get_system_reboot_status()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SystemApi->get_system_reboot_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**bool**

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

# **get_system_status**
> SystemStatusResponse get_system_status()



Retrieve system status. Returns an array of statuses which can include headings. 

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
    api_instance = mailinaboxapi.SystemApi(api_client)
    
    try:
        api_response = api_instance.get_system_status()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SystemApi->get_system_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemStatusResponse**](SystemStatusResponse.md)

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

# **get_system_updates**
> str get_system_updates()



Retrieve system updates.

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
    api_instance = mailinaboxapi.SystemApi(api_client)
    
    try:
        api_response = api_instance.get_system_updates()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SystemApi->get_system_updates: %s\n" % e)
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

# **get_system_upstream_version**
> str get_system_upstream_version()



Retrieve Mail-in-a-Box upstream version.

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
    api_instance = mailinaboxapi.SystemApi(api_client)
    
    try:
        api_response = api_instance.get_system_upstream_version()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SystemApi->get_system_upstream_version: %s\n" % e)
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

# **get_system_version**
> str get_system_version()



Retrieve installed Mail-in-a-Box version.

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
    api_instance = mailinaboxapi.SystemApi(api_client)
    
    try:
        api_response = api_instance.get_system_version()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SystemApi->get_system_version: %s\n" % e)
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

# **reboot_system**
> str reboot_system()



Reboot system.

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
    api_instance = mailinaboxapi.SystemApi(api_client)
    
    try:
        api_response = api_instance.reboot_system()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SystemApi->reboot_system: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

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

# **update_system_backup_config**
> str update_system_backup_config(target, target_user, target_pass, min_age)



Update backup config.

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
    api_instance = mailinaboxapi.SystemApi(api_client)
    target = 'target_example' # str | 
target_user = 'target_user_example' # str | 
target_pass = 'target_pass_example' # str | 
min_age = 56 # int | 

    try:
        api_response = api_instance.update_system_backup_config(target, target_user, target_pass, min_age)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SystemApi->update_system_backup_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target** | **str**|  | 
 **target_user** | **str**|  | 
 **target_pass** | **str**|  | 
 **min_age** | **int**|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_system_packages**
> str update_system_packages()



Update system packages.

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
    api_instance = mailinaboxapi.SystemApi(api_client)
    
    try:
        api_response = api_instance.update_system_packages()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SystemApi->update_system_packages: %s\n" % e)
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

# **update_system_privacy**
> str update_system_privacy(value)



Update new-version check status.  Request:    - `value: private`: Disable new version checks   - `value: off`: Enable new version checks 

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
    api_instance = mailinaboxapi.SystemApi(api_client)
    value = mailinaboxapi.SystemPrivacyStatus() # SystemPrivacyStatus | 

    try:
        api_response = api_instance.update_system_privacy(value)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SystemApi->update_system_privacy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | [**SystemPrivacyStatus**](SystemPrivacyStatus.md)|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

