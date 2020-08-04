# mailinabox_api.DNSApi

All URIs are relative to *https://box.example.com/admin*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_dns_custom_record**](DNSApi.md#add_dns_custom_record) | **POST** /dns/custom/{domain}/{type} | 
[**add_dns_custom_record_for_type_a**](DNSApi.md#add_dns_custom_record_for_type_a) | **POST** /dns/custom/{domain} | 
[**add_dns_secondary_nameserver**](DNSApi.md#add_dns_secondary_nameserver) | **POST** /dns/secondary-nameserver | 
[**get_dns_custom_records**](DNSApi.md#get_dns_custom_records) | **GET** /dns/custom | 
[**get_dns_custom_records_for_domain_and_type**](DNSApi.md#get_dns_custom_records_for_domain_and_type) | **GET** /dns/custom/{domain}/{type} | 
[**get_dns_custom_records_for_domain_and_type_a**](DNSApi.md#get_dns_custom_records_for_domain_and_type_a) | **GET** /dns/custom/{domain} | 
[**get_dns_dump**](DNSApi.md#get_dns_dump) | **GET** /dns/dump | 
[**get_dns_secondary_nameserver**](DNSApi.md#get_dns_secondary_nameserver) | **GET** /dns/secondary-nameserver | 
[**get_dns_zones**](DNSApi.md#get_dns_zones) | **GET** /dns/zones | 
[**remove_dns_custom_record**](DNSApi.md#remove_dns_custom_record) | **DELETE** /dns/custom/{domain}/{type} | 
[**remove_dns_custom_record_for_type_a**](DNSApi.md#remove_dns_custom_record_for_type_a) | **DELETE** /dns/custom/{domain} | 
[**update_dns**](DNSApi.md#update_dns) | **POST** /dns/update | 
[**update_dns_custom_record**](DNSApi.md#update_dns_custom_record) | **PUT** /dns/custom/{domain}/{type} | 
[**update_dns_custom_record_for_type_a**](DNSApi.md#update_dns_custom_record_for_type_a) | **PUT** /dns/custom/{domain} | 


# **add_dns_custom_record**
> str add_dns_custom_record(domain, type, body)



Add a custom DNS record.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import mailinabox_api
from mailinabox_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://box.example.com/admin
# See configuration.py for a list of all supported configuration parameters.
configuration = mailinabox_api.Configuration(
    host = "https://box.example.com/admin"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = mailinabox_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mailinabox_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailinabox_api.DNSApi(api_client)
    domain = 'domain_example' # str | DNS record domain
type = mailinabox_api.DNSRecordType() # DNSRecordType | Record type
body = 'body_example' # str | The value of the DNS record.

    try:
        api_response = api_instance.add_dns_custom_record(domain, type, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DNSApi->add_dns_custom_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| DNS record domain | 
 **type** | [**DNSRecordType**](.md)| Record type | 
 **body** | **str**| The value of the DNS record. | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_dns_custom_record_for_type_a**
> str add_dns_custom_record_for_type_a(domain, body)



Add a custom DNS A record.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import mailinabox_api
from mailinabox_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://box.example.com/admin
# See configuration.py for a list of all supported configuration parameters.
configuration = mailinabox_api.Configuration(
    host = "https://box.example.com/admin"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = mailinabox_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mailinabox_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailinabox_api.DNSApi(api_client)
    domain = 'domain_example' # str | DNS record domain.
body = 'body_example' # str | The value of the DNS record.

    try:
        api_response = api_instance.add_dns_custom_record_for_type_a(domain, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DNSApi->add_dns_custom_record_for_type_a: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| DNS record domain. | 
 **body** | **str**| The value of the DNS record. | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_dns_secondary_nameserver**
> str add_dns_secondary_nameserver(hostnames)



Add secondary nameservers.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import mailinabox_api
from mailinabox_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://box.example.com/admin
# See configuration.py for a list of all supported configuration parameters.
configuration = mailinabox_api.Configuration(
    host = "https://box.example.com/admin"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = mailinabox_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mailinabox_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailinabox_api.DNSApi(api_client)
    hostnames = 'hostnames_example' # str | Hostnames separated with commas or spaces.

    try:
        api_response = api_instance.add_dns_secondary_nameserver(hostnames)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DNSApi->add_dns_secondary_nameserver: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostnames** | **str**| Hostnames separated with commas or spaces. | 

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

# **get_dns_custom_records**
> DNSCustomRecordsResponse get_dns_custom_records()



Retrieve all custom DNS records.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import mailinabox_api
from mailinabox_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://box.example.com/admin
# See configuration.py for a list of all supported configuration parameters.
configuration = mailinabox_api.Configuration(
    host = "https://box.example.com/admin"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = mailinabox_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mailinabox_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailinabox_api.DNSApi(api_client)
    
    try:
        api_response = api_instance.get_dns_custom_records()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DNSApi->get_dns_custom_records: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DNSCustomRecordsResponse**](DNSCustomRecordsResponse.md)

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

# **get_dns_custom_records_for_domain_and_type**
> DNSCustomRecordsResponse get_dns_custom_records_for_domain_and_type(domain, type)



Get DNS records for domain and type.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import mailinabox_api
from mailinabox_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://box.example.com/admin
# See configuration.py for a list of all supported configuration parameters.
configuration = mailinabox_api.Configuration(
    host = "https://box.example.com/admin"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = mailinabox_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mailinabox_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailinabox_api.DNSApi(api_client)
    domain = 'domain_example' # str | DNS record domain
type = mailinabox_api.DNSRecordType() # DNSRecordType | Record type

    try:
        api_response = api_instance.get_dns_custom_records_for_domain_and_type(domain, type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DNSApi->get_dns_custom_records_for_domain_and_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| DNS record domain | 
 **type** | [**DNSRecordType**](.md)| Record type | 

### Return type

[**DNSCustomRecordsResponse**](DNSCustomRecordsResponse.md)

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

# **get_dns_custom_records_for_domain_and_type_a**
> DNSCustomRecordsResponse get_dns_custom_records_for_domain_and_type_a(domain)



Get DNS A records for domain.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import mailinabox_api
from mailinabox_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://box.example.com/admin
# See configuration.py for a list of all supported configuration parameters.
configuration = mailinabox_api.Configuration(
    host = "https://box.example.com/admin"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = mailinabox_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mailinabox_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailinabox_api.DNSApi(api_client)
    domain = 'domain_example' # str | DNS record domain.

    try:
        api_response = api_instance.get_dns_custom_records_for_domain_and_type_a(domain)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DNSApi->get_dns_custom_records_for_domain_and_type_a: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| DNS record domain. | 

### Return type

[**DNSCustomRecordsResponse**](DNSCustomRecordsResponse.md)

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

# **get_dns_dump**
> DNSDumpResponse get_dns_dump()



Retrieve all DNS records.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import mailinabox_api
from mailinabox_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://box.example.com/admin
# See configuration.py for a list of all supported configuration parameters.
configuration = mailinabox_api.Configuration(
    host = "https://box.example.com/admin"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = mailinabox_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mailinabox_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailinabox_api.DNSApi(api_client)
    
    try:
        api_response = api_instance.get_dns_dump()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DNSApi->get_dns_dump: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DNSDumpResponse**](DNSDumpResponse.md)

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

# **get_dns_secondary_nameserver**
> DNSSecondaryNameserverResponse get_dns_secondary_nameserver()



Retrieve secondary nameservers.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import mailinabox_api
from mailinabox_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://box.example.com/admin
# See configuration.py for a list of all supported configuration parameters.
configuration = mailinabox_api.Configuration(
    host = "https://box.example.com/admin"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = mailinabox_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mailinabox_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailinabox_api.DNSApi(api_client)
    
    try:
        api_response = api_instance.get_dns_secondary_nameserver()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DNSApi->get_dns_secondary_nameserver: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DNSSecondaryNameserverResponse**](DNSSecondaryNameserverResponse.md)

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

# **get_dns_zones**
> DNSZonesResponse get_dns_zones()



Retrieve DNS zones.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import mailinabox_api
from mailinabox_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://box.example.com/admin
# See configuration.py for a list of all supported configuration parameters.
configuration = mailinabox_api.Configuration(
    host = "https://box.example.com/admin"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = mailinabox_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mailinabox_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailinabox_api.DNSApi(api_client)
    
    try:
        api_response = api_instance.get_dns_zones()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DNSApi->get_dns_zones: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DNSZonesResponse**](DNSZonesResponse.md)

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

# **remove_dns_custom_record**
> str remove_dns_custom_record(domain, type, body)



Remove a custom DNS record.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import mailinabox_api
from mailinabox_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://box.example.com/admin
# See configuration.py for a list of all supported configuration parameters.
configuration = mailinabox_api.Configuration(
    host = "https://box.example.com/admin"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = mailinabox_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mailinabox_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailinabox_api.DNSApi(api_client)
    domain = 'domain_example' # str | DNS record domain
type = mailinabox_api.DNSRecordType() # DNSRecordType | Record type
body = 'body_example' # str | The value of the DNS record.

    try:
        api_response = api_instance.remove_dns_custom_record(domain, type, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DNSApi->remove_dns_custom_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| DNS record domain | 
 **type** | [**DNSRecordType**](.md)| Record type | 
 **body** | **str**| The value of the DNS record. | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_dns_custom_record_for_type_a**
> str remove_dns_custom_record_for_type_a(domain, body)



Remove a custom DNS A record.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import mailinabox_api
from mailinabox_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://box.example.com/admin
# See configuration.py for a list of all supported configuration parameters.
configuration = mailinabox_api.Configuration(
    host = "https://box.example.com/admin"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = mailinabox_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mailinabox_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailinabox_api.DNSApi(api_client)
    domain = 'domain_example' # str | DNS record domain.
body = 'body_example' # str | The value of the DNS record.

    try:
        api_response = api_instance.remove_dns_custom_record_for_type_a(domain, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DNSApi->remove_dns_custom_record_for_type_a: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| DNS record domain. | 
 **body** | **str**| The value of the DNS record. | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dns**
> str update_dns(force)



Update DNS, which involves creating zone files and restarting `nsd`.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import mailinabox_api
from mailinabox_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://box.example.com/admin
# See configuration.py for a list of all supported configuration parameters.
configuration = mailinabox_api.Configuration(
    host = "https://box.example.com/admin"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = mailinabox_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mailinabox_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailinabox_api.DNSApi(api_client)
    force = 56 # int | Force an update even if mailinabox detects no changes are required.

    try:
        api_response = api_instance.update_dns(force)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DNSApi->update_dns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **force** | **int**| Force an update even if mailinabox detects no changes are required. | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dns_custom_record**
> str update_dns_custom_record(domain, type, body)



Update a custom DNS record.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import mailinabox_api
from mailinabox_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://box.example.com/admin
# See configuration.py for a list of all supported configuration parameters.
configuration = mailinabox_api.Configuration(
    host = "https://box.example.com/admin"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = mailinabox_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mailinabox_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailinabox_api.DNSApi(api_client)
    domain = 'domain_example' # str | DNS record domain
type = mailinabox_api.DNSRecordType() # DNSRecordType | Record type
body = 'body_example' # str | The value of the DNS record.

    try:
        api_response = api_instance.update_dns_custom_record(domain, type, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DNSApi->update_dns_custom_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| DNS record domain | 
 **type** | [**DNSRecordType**](.md)| Record type | 
 **body** | **str**| The value of the DNS record. | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dns_custom_record_for_type_a**
> str update_dns_custom_record_for_type_a(domain, body)



Update a custom DNS A record.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import mailinabox_api
from mailinabox_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://box.example.com/admin
# See configuration.py for a list of all supported configuration parameters.
configuration = mailinabox_api.Configuration(
    host = "https://box.example.com/admin"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = mailinabox_api.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mailinabox_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mailinabox_api.DNSApi(api_client)
    domain = 'domain_example' # str | DNS record domain.
body = 'body_example' # str | The value of the DNS record.

    try:
        api_response = api_instance.update_dns_custom_record_for_type_a(domain, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DNSApi->update_dns_custom_record_for_type_a: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| DNS record domain. | 
 **body** | **str**| The value of the DNS record. | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

