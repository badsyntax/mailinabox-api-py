# mailinabox_api.SSLApi

All URIs are relative to *https://box.example.com/admin*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_sslcsr**](SSLApi.md#generate_sslcsr) | **POST** /ssl/csr/{domain} | Generate SSL CSR
[**get_ssl_status**](SSLApi.md#get_ssl_status) | **GET** /ssl/status | Get SSL status
[**install_ssl_certificate**](SSLApi.md#install_ssl_certificate) | **POST** /ssl/install | Install SSL certificate
[**provision_ssl_certificates**](SSLApi.md#provision_ssl_certificates) | **POST** /ssl/provision | Provision SSL certificates


# **generate_sslcsr**
> str generate_sslcsr(domain, countrycode)

Generate SSL CSR

Generates a Certificate Signing Request (CSR) for a domain & country code. 

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
    api_instance = mailinabox_api.SSLApi(api_client)
    domain = 'domain_example' # str | Domain to generate CSR for.
countrycode = 'countrycode_example' # str | 

    try:
        # Generate SSL CSR
        api_response = api_instance.generate_sslcsr(domain, countrycode)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SSLApi->generate_sslcsr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain to generate CSR for. | 
 **countrycode** | **str**|  | 

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

# **get_ssl_status**
> SSLStatusResponse get_ssl_status()

Get SSL status

Returns the SSL status for all domains.

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
    api_instance = mailinabox_api.SSLApi(api_client)
    
    try:
        # Get SSL status
        api_response = api_instance.get_ssl_status()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SSLApi->get_ssl_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SSLStatusResponse**](SSLStatusResponse.md)

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

# **install_ssl_certificate**
> str install_ssl_certificate(domain, cert, chain)

Install SSL certificate

Installs a custom certificate. The chain certificate is optional. 

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
    api_instance = mailinabox_api.SSLApi(api_client)
    domain = 'domain_example' # str | Hostname format.
cert = 'cert_example' # str | TLS/SSL certificate.
chain = 'chain_example' # str | TLS/SSL intermediate chain (if provided, else empty string).

    try:
        # Install SSL certificate
        api_response = api_instance.install_ssl_certificate(domain, cert, chain)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SSLApi->install_ssl_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Hostname format. | 
 **cert** | **str**| TLS/SSL certificate. | 
 **chain** | **str**| TLS/SSL intermediate chain (if provided, else empty string). | 

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

# **provision_ssl_certificates**
> SSLCertificatesProvisionResponse provision_ssl_certificates()

Provision SSL certificates

Provisions certificates for all domains. 

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
    api_instance = mailinabox_api.SSLApi(api_client)
    
    try:
        # Provision SSL certificates
        api_response = api_instance.provision_ssl_certificates()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SSLApi->provision_ssl_certificates: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SSLCertificatesProvisionResponse**](SSLCertificatesProvisionResponse.md)

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

