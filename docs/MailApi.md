# mailinabox_api.MailApi

All URIs are relative to *https://box.example.com/admin*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_mail_user**](MailApi.md#add_mail_user) | **POST** /mail/users/add | Add mail user
[**add_mail_user_privilege**](MailApi.md#add_mail_user_privilege) | **POST** /mail/users/privileges/add | Add mail user privilege
[**get_mail_aliases**](MailApi.md#get_mail_aliases) | **GET** /mail/aliases | Get mail aliases
[**get_mail_domains**](MailApi.md#get_mail_domains) | **GET** /mail/domains | Get mail domains
[**get_mail_user_privileges**](MailApi.md#get_mail_user_privileges) | **GET** /mail/users/privileges | Get mail user privileges
[**get_mail_users**](MailApi.md#get_mail_users) | **GET** /mail/users | Get mail users
[**remove_mail_alias**](MailApi.md#remove_mail_alias) | **POST** /mail/aliases/remove | Remove mail alias
[**remove_mail_user**](MailApi.md#remove_mail_user) | **POST** /mail/users/remove | Remove mail user
[**remove_mail_user_privilege**](MailApi.md#remove_mail_user_privilege) | **POST** /mail/users/privileges/remove | Remove mail user privilege
[**set_mail_user_password**](MailApi.md#set_mail_user_password) | **POST** /mail/users/password | Set mail user password
[**upsert_mail_alias**](MailApi.md#upsert_mail_alias) | **POST** /mail/aliases/add | Upsert mail alias


# **add_mail_user**
> str add_mail_user(email, password, privileges)

Add mail user

Adds a new mail user.

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
    api_instance = mailinabox_api.MailApi(api_client)
    email = 'email_example' # str | Email format.
password = 'password_example' # str | 
privileges = mailinabox_api.MailUserPrivilege() # MailUserPrivilege | 

    try:
        # Add mail user
        api_response = api_instance.add_mail_user(email, password, privileges)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MailApi->add_mail_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | [**str**](str.md)| Email format. | 
 **password** | **str**|  | 
 **privileges** | [**MailUserPrivilege**](MailUserPrivilege.md)|  | 

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

# **add_mail_user_privilege**
> str add_mail_user_privilege(email, privilege)

Add mail user privilege

Adds a privilege to an existing mail user.

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
    api_instance = mailinabox_api.MailApi(api_client)
    email = 'email_example' # str | Email format.
privilege = mailinabox_api.MailUserPrivilege() # MailUserPrivilege | 

    try:
        # Add mail user privilege
        api_response = api_instance.add_mail_user_privilege(email, privilege)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MailApi->add_mail_user_privilege: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | [**str**](str.md)| Email format. | 
 **privilege** | [**MailUserPrivilege**](MailUserPrivilege.md)|  | 

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

# **get_mail_aliases**
> list[MailAliasByDomain] get_mail_aliases(format=format)

Get mail aliases

Returns all mail aliases.

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
    api_instance = mailinabox_api.MailApi(api_client)
    format = mailinabox_api.MailAliasesResponseFormat() # MailAliasesResponseFormat | The format of the response. (optional)

    try:
        # Get mail aliases
        api_response = api_instance.get_mail_aliases(format=format)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MailApi->get_mail_aliases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | [**MailAliasesResponseFormat**](.md)| The format of the response. | [optional] 

### Return type

[**list[MailAliasByDomain]**](MailAliasByDomain.md)

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

# **get_mail_domains**
> str get_mail_domains()

Get mail domains

Returns all mail domains.

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
    api_instance = mailinabox_api.MailApi(api_client)
    
    try:
        # Get mail domains
        api_response = api_instance.get_mail_domains()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MailApi->get_mail_domains: %s\n" % e)
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

# **get_mail_user_privileges**
> MailUserPrivilege get_mail_user_privileges(email=email)

Get mail user privileges

Returns all privileges for an existing mail user.

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
    api_instance = mailinabox_api.MailApi(api_client)
    email = 'email_example' # str | The email you want to get privileges for. (optional)

    try:
        # Get mail user privileges
        api_response = api_instance.get_mail_user_privileges(email=email)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MailApi->get_mail_user_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | [**str**](.md)| The email you want to get privileges for. | [optional] 

### Return type

[**MailUserPrivilege**](MailUserPrivilege.md)

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

# **get_mail_users**
> MailUsersResponse get_mail_users(format=format)

Get mail users

Returns all mail users.

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
    api_instance = mailinabox_api.MailApi(api_client)
    format = mailinabox_api.MailUsersResponseFormat() # MailUsersResponseFormat | The format of the response. (optional)

    try:
        # Get mail users
        api_response = api_instance.get_mail_users(format=format)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MailApi->get_mail_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | [**MailUsersResponseFormat**](.md)| The format of the response. | [optional] 

### Return type

[**MailUsersResponse**](MailUsersResponse.md)

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

# **remove_mail_alias**
> str remove_mail_alias(address)

Remove mail alias

Removes a mail alias.

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
    api_instance = mailinabox_api.MailApi(api_client)
    address = 'address_example' # str | Email format.

    try:
        # Remove mail alias
        api_response = api_instance.remove_mail_alias(address)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MailApi->remove_mail_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | [**str**](str.md)| Email format. | 

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

# **remove_mail_user**
> str remove_mail_user(email)

Remove mail user

Removes an existing mail user.

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
    api_instance = mailinabox_api.MailApi(api_client)
    email = 'email_example' # str | Email format.

    try:
        # Remove mail user
        api_response = api_instance.remove_mail_user(email)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MailApi->remove_mail_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | [**str**](str.md)| Email format. | 

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

# **remove_mail_user_privilege**
> str remove_mail_user_privilege(email, privilege)

Remove mail user privilege

Removes a privilege from an existing mail user.

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
    api_instance = mailinabox_api.MailApi(api_client)
    email = 'email_example' # str | Email format.
privilege = mailinabox_api.MailUserPrivilege() # MailUserPrivilege | 

    try:
        # Remove mail user privilege
        api_response = api_instance.remove_mail_user_privilege(email, privilege)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MailApi->remove_mail_user_privilege: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | [**str**](str.md)| Email format. | 
 **privilege** | [**MailUserPrivilege**](MailUserPrivilege.md)|  | 

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

# **set_mail_user_password**
> str set_mail_user_password(email, password)

Set mail user password

Sets a password for an existing mail user.

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
    api_instance = mailinabox_api.MailApi(api_client)
    email = 'email_example' # str | Email format.
password = 'password_example' # str | 

    try:
        # Set mail user password
        api_response = api_instance.set_mail_user_password(email, password)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MailApi->set_mail_user_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | [**str**](str.md)| Email format. | 
 **password** | **str**|  | 

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

# **upsert_mail_alias**
> str upsert_mail_alias(update_if_exists, address, forwards_to, permitted_senders)

Upsert mail alias

Adds or updates a mail alias. If updating, you need to set `update_if_exists: 1`. 

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
    api_instance = mailinabox_api.MailApi(api_client)
    update_if_exists = 56 # int | Set to `1` when updating an alias.
address = 'address_example' # str | Email format.
forwards_to = 'forwards_to_example' # str | If adding a regular or catch-all alias, the format needs to be `email1@example.com`. Multiple address can be separated by newlines or commas.  If adding a domain alias, the format needs to be `@example.com`. 
permitted_senders = 'permitted_senders_example' # str | Mail users that can send mail claiming to be from any address on the alias domain. Multiple address can be separated by newlines or commas.  Leave empty to allow any mail user listed in `forwards_to` to send mail claiming to be from any address on the alias domain. 

    try:
        # Upsert mail alias
        api_response = api_instance.upsert_mail_alias(update_if_exists, address, forwards_to, permitted_senders)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MailApi->upsert_mail_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_if_exists** | **int**| Set to &#x60;1&#x60; when updating an alias. | 
 **address** | [**str**](str.md)| Email format. | 
 **forwards_to** | **str**| If adding a regular or catch-all alias, the format needs to be &#x60;email1@example.com&#x60;. Multiple address can be separated by newlines or commas.  If adding a domain alias, the format needs to be &#x60;@example.com&#x60;.  | 
 **permitted_senders** | **str**| Mail users that can send mail claiming to be from any address on the alias domain. Multiple address can be separated by newlines or commas.  Leave empty to allow any mail user listed in &#x60;forwards_to&#x60; to send mail claiming to be from any address on the alias domain.  | 

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

