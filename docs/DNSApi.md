# mailinabox_api.DNSApi

All URIs are relative to *https://box.example.com/admin*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_dns_custom_a_record**](DNSApi.md#add_dns_custom_a_record) | **POST** /dns/custom/{qname} | Add DNS custom A record
[**add_dns_custom_record**](DNSApi.md#add_dns_custom_record) | **POST** /dns/custom/{qname}/{rtype} | Add DNS custom record
[**add_dns_secondary_nameserver**](DNSApi.md#add_dns_secondary_nameserver) | **POST** /dns/secondary-nameserver | Add DNS secondary nameserver
[**get_dns_custom_a_records_for_q_name**](DNSApi.md#get_dns_custom_a_records_for_q_name) | **GET** /dns/custom/{qname} | Get DNS custom A records
[**get_dns_custom_records**](DNSApi.md#get_dns_custom_records) | **GET** /dns/custom | Get DNS custom records
[**get_dns_custom_records_for_q_name_and_type**](DNSApi.md#get_dns_custom_records_for_q_name_and_type) | **GET** /dns/custom/{qname}/{rtype} | Get DNS custom records
[**get_dns_dump**](DNSApi.md#get_dns_dump) | **GET** /dns/dump | Get DNS dump
[**get_dns_secondary_nameserver**](DNSApi.md#get_dns_secondary_nameserver) | **GET** /dns/secondary-nameserver | Get DNS secondary nameserver
[**get_dns_zonefile**](DNSApi.md#get_dns_zonefile) | **GET** /dns/zonefile/{zone} | Get DNS zonefile
[**get_dns_zones**](DNSApi.md#get_dns_zones) | **GET** /dns/zones | Get DNS zones
[**remove_dns_custom_a_record**](DNSApi.md#remove_dns_custom_a_record) | **DELETE** /dns/custom/{qname} | Remove DNS custom A record
[**remove_dns_custom_record**](DNSApi.md#remove_dns_custom_record) | **DELETE** /dns/custom/{qname}/{rtype} | Remove DNS custom record
[**update_dns**](DNSApi.md#update_dns) | **POST** /dns/update | Update DNS
[**update_dns_custom_a_record**](DNSApi.md#update_dns_custom_a_record) | **PUT** /dns/custom/{qname} | Update DNS custom A record
[**update_dns_custom_record**](DNSApi.md#update_dns_custom_record) | **PUT** /dns/custom/{qname}/{rtype} | Update DNS custom record


# **add_dns_custom_a_record**
> str add_dns_custom_a_record(qname, body)

Add DNS custom A record

Adds a custom DNS A record for the specified query name.

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
    qname = 'qname_example' # str | DNS query name.
body = 1.2.3.4 # str | 

    try:
        # Add DNS custom A record
        api_response = api_instance.add_dns_custom_a_record(qname, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DNSApi->add_dns_custom_a_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qname** | **str**| DNS query name. | 
 **body** | **str**|  | 

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

# **add_dns_custom_record**
> str add_dns_custom_record(qname, rtype, body)

Add DNS custom record

Adds a custom DNS record for the specified query name and type.

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
    qname = 'qname_example' # str | DNS record query name
rtype = mailinabox_api.DNSRecordType() # DNSRecordType | Record type
body = 1.2.3.4 # str | 

    try:
        # Add DNS custom record
        api_response = api_instance.add_dns_custom_record(qname, rtype, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DNSApi->add_dns_custom_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qname** | **str**| DNS record query name | 
 **rtype** | [**DNSRecordType**](.md)| Record type | 
 **body** | **str**|  | 

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

Add DNS secondary nameserver

Adds one or more secondary nameservers. 

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
        # Add DNS secondary nameserver
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

# **get_dns_custom_a_records_for_q_name**
> DNSCustomRecordsResponse get_dns_custom_a_records_for_q_name(qname)

Get DNS custom A records

Returns all custom A records for the specified query name.

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
    qname = 'qname_example' # str | DNS query name.

    try:
        # Get DNS custom A records
        api_response = api_instance.get_dns_custom_a_records_for_q_name(qname)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DNSApi->get_dns_custom_a_records_for_q_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qname** | **str**| DNS query name. | 

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

# **get_dns_custom_records**
> DNSCustomRecordsResponse get_dns_custom_records()

Get DNS custom records

Returns all custom DNS records.

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
        # Get DNS custom records
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

# **get_dns_custom_records_for_q_name_and_type**
> DNSCustomRecordsResponse get_dns_custom_records_for_q_name_and_type(qname, rtype)

Get DNS custom records

Returns all custom records for the specified query name and type.

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
    qname = 'qname_example' # str | DNS record query name
rtype = mailinabox_api.DNSRecordType() # DNSRecordType | Record type

    try:
        # Get DNS custom records
        api_response = api_instance.get_dns_custom_records_for_q_name_and_type(qname, rtype)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DNSApi->get_dns_custom_records_for_q_name_and_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qname** | **str**| DNS record query name | 
 **rtype** | [**DNSRecordType**](.md)| Record type | 

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

Get DNS dump

Returns all DNS records.

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
        # Get DNS dump
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

Get DNS secondary nameserver

Returns a list of nameserver hostnames. 

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
        # Get DNS secondary nameserver
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

# **get_dns_zonefile**
> str get_dns_zonefile(zone)

Get DNS zonefile

Returns a DNS zone file for a hostname.

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
    zone = 'zone_example' # str | Hostname

    try:
        # Get DNS zonefile
        api_response = api_instance.get_dns_zonefile(zone)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DNSApi->get_dns_zonefile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | **str**| Hostname | 

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

# **get_dns_zones**
> DNSZonesResponse get_dns_zones()

Get DNS zones

Returns an array of all managed top-level domains.

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
        # Get DNS zones
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

# **remove_dns_custom_a_record**
> str remove_dns_custom_a_record(qname, body)

Remove DNS custom A record

Removes a DNS custom A record for the specified domain & value.

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
    qname = 'qname_example' # str | DNS query name.
body = 1.2.3.4 # str | 

    try:
        # Remove DNS custom A record
        api_response = api_instance.remove_dns_custom_a_record(qname, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DNSApi->remove_dns_custom_a_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qname** | **str**| DNS query name. | 
 **body** | **str**|  | 

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

# **remove_dns_custom_record**
> str remove_dns_custom_record(qname, rtype, body)

Remove DNS custom record

Removes a DNS custom record for the specified domain, type & value.

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
    qname = 'qname_example' # str | DNS record query name
rtype = mailinabox_api.DNSRecordType() # DNSRecordType | Record type
body = 1.2.3.4 # str | 

    try:
        # Remove DNS custom record
        api_response = api_instance.remove_dns_custom_record(qname, rtype, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DNSApi->remove_dns_custom_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qname** | **str**| DNS record query name | 
 **rtype** | [**DNSRecordType**](.md)| Record type | 
 **body** | **str**|  | 

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

Update DNS

Updates the DNS. Involves creating zone files and restarting `nsd`.

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
        # Update DNS
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

# **update_dns_custom_a_record**
> str update_dns_custom_a_record(qname, body)

Update DNS custom A record

Updates an existing DNS custom A record value for the specified qname.

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
    qname = 'qname_example' # str | DNS query name.
body = 1.2.3.4 # str | 

    try:
        # Update DNS custom A record
        api_response = api_instance.update_dns_custom_a_record(qname, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DNSApi->update_dns_custom_a_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qname** | **str**| DNS query name. | 
 **body** | **str**|  | 

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

# **update_dns_custom_record**
> str update_dns_custom_record(qname, rtype, body)

Update DNS custom record

Updates an existing DNS custom record value for the specified qname and type.

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
    qname = 'qname_example' # str | DNS record query name
rtype = mailinabox_api.DNSRecordType() # DNSRecordType | Record type
body = 1.2.3.4 # str | 

    try:
        # Update DNS custom record
        api_response = api_instance.update_dns_custom_record(qname, rtype, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DNSApi->update_dns_custom_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qname** | **str**| DNS record query name | 
 **rtype** | [**DNSRecordType**](.md)| Record type | 
 **body** | **str**|  | 

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

