# mailinaboxapi

[![Build & Publish](https://github.com/badsyntax/mailinabox-api/workflows/Build%20&%20Publish/badge.svg)](https://github.com/badsyntax/mailinabox-api/actions?query=workflow%3A%22Build+%26+Publish%22)

Python client SDK for the Mail-in-a-Box API.

- API version: 0.46.0
- Package version: 0.0.2

**NOTE:** This package is auto-generated from the Mail-In-A-Box OpenAPI spec.

## Requirements

Python 2.7 and 3.4+

## Installation & Usage

### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/badsyntax/mailinabox-api-py.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/badsyntax/mailinabox-api-py.git`)

Then import the package:
```python
import mailinaboxapi
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import mailinaboxapi
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
    api_instance = mailinaboxapi.DNSApi(api_client)
    domain = 'domain_example' # str | DNS record domain
    type = mailinaboxapi.DNSRecordType() # DNSRecordType | Record type
    body = 'body_example' # str | The value of the DNS record.

    try:
        api_response = api_instance.add_dns_custom_record(domain, type, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DNSApi->add_dns_custom_record: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *https://box.example.com/admin*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DNSApi* | [**add_dns_custom_record**](docs/DNSApi.md#add_dns_custom_record) | **POST** /dns/custom/{domain}/{type} | 
*DNSApi* | [**add_dns_custom_record_for_type_a**](docs/DNSApi.md#add_dns_custom_record_for_type_a) | **POST** /dns/custom/{domain} | 
*DNSApi* | [**add_dns_secondary_nameserver**](docs/DNSApi.md#add_dns_secondary_nameserver) | **POST** /dns/secondary-nameserver | 
*DNSApi* | [**get_dns_custom_records**](docs/DNSApi.md#get_dns_custom_records) | **GET** /dns/custom | 
*DNSApi* | [**get_dns_custom_records_for_domain_and_type**](docs/DNSApi.md#get_dns_custom_records_for_domain_and_type) | **GET** /dns/custom/{domain}/{type} | 
*DNSApi* | [**get_dns_custom_records_for_domain_and_type_a**](docs/DNSApi.md#get_dns_custom_records_for_domain_and_type_a) | **GET** /dns/custom/{domain} | 
*DNSApi* | [**get_dns_dump**](docs/DNSApi.md#get_dns_dump) | **GET** /dns/dump | 
*DNSApi* | [**get_dns_secondary_nameserver**](docs/DNSApi.md#get_dns_secondary_nameserver) | **GET** /dns/secondary-nameserver | 
*DNSApi* | [**get_dns_zones**](docs/DNSApi.md#get_dns_zones) | **GET** /dns/zones | 
*DNSApi* | [**remove_dns_custom_record**](docs/DNSApi.md#remove_dns_custom_record) | **DELETE** /dns/custom/{domain}/{type} | 
*DNSApi* | [**remove_dns_custom_record_for_type_a**](docs/DNSApi.md#remove_dns_custom_record_for_type_a) | **DELETE** /dns/custom/{domain} | 
*DNSApi* | [**update_dns**](docs/DNSApi.md#update_dns) | **POST** /dns/update | 
*DNSApi* | [**update_dns_custom_record**](docs/DNSApi.md#update_dns_custom_record) | **PUT** /dns/custom/{domain}/{type} | 
*DNSApi* | [**update_dns_custom_record_for_type_a**](docs/DNSApi.md#update_dns_custom_record_for_type_a) | **PUT** /dns/custom/{domain} | 
*MailApi* | [**add_mail_user**](docs/MailApi.md#add_mail_user) | **POST** /mail/users/add | 
*MailApi* | [**add_mail_user_privilege**](docs/MailApi.md#add_mail_user_privilege) | **POST** /mail/users/privileges/add | 
*MailApi* | [**get_mail_aliases**](docs/MailApi.md#get_mail_aliases) | **GET** /mail/aliases | 
*MailApi* | [**get_mail_domains**](docs/MailApi.md#get_mail_domains) | **GET** /mail/domains | 
*MailApi* | [**get_mail_user_privileges**](docs/MailApi.md#get_mail_user_privileges) | **GET** /mail/users/privileges | 
*MailApi* | [**get_mail_users**](docs/MailApi.md#get_mail_users) | **GET** /mail/users | 
*MailApi* | [**remove_mail_alias**](docs/MailApi.md#remove_mail_alias) | **POST** /mail/aliases/remove | 
*MailApi* | [**remove_mail_user**](docs/MailApi.md#remove_mail_user) | **POST** /mail/users/remove | 
*MailApi* | [**remove_mail_user_privilege**](docs/MailApi.md#remove_mail_user_privilege) | **POST** /mail/users/privileges/remove | 
*MailApi* | [**set_mail_user_password**](docs/MailApi.md#set_mail_user_password) | **POST** /mail/users/password | 
*MailApi* | [**upsert_mail_alias**](docs/MailApi.md#upsert_mail_alias) | **POST** /mail/aliases/add | 
*SSLApi* | [**generate_sslcsr**](docs/SSLApi.md#generate_sslcsr) | **POST** /ssl/csr/{domain} | 
*SSLApi* | [**get_ssl_status**](docs/SSLApi.md#get_ssl_status) | **GET** /ssl/status | 
*SSLApi* | [**install_ssl_certificate**](docs/SSLApi.md#install_ssl_certificate) | **POST** /ssl/install | 
*SSLApi* | [**provision_ssl_certificates**](docs/SSLApi.md#provision_ssl_certificates) | **POST** /ssl/provision | 
*SystemApi* | [**get_system_backup_config**](docs/SystemApi.md#get_system_backup_config) | **GET** /system/backup/config | 
*SystemApi* | [**get_system_backup_status**](docs/SystemApi.md#get_system_backup_status) | **GET** /system/backup/status | 
*SystemApi* | [**get_system_privacy_status**](docs/SystemApi.md#get_system_privacy_status) | **GET** /system/privacy | 
*SystemApi* | [**get_system_reboot_status**](docs/SystemApi.md#get_system_reboot_status) | **GET** /system/reboot | 
*SystemApi* | [**get_system_status**](docs/SystemApi.md#get_system_status) | **POST** /system/status | 
*SystemApi* | [**get_system_updates**](docs/SystemApi.md#get_system_updates) | **GET** /system/updates | 
*SystemApi* | [**get_system_upstream_version**](docs/SystemApi.md#get_system_upstream_version) | **POST** /system/latest-upstream-version | 
*SystemApi* | [**get_system_version**](docs/SystemApi.md#get_system_version) | **GET** /system/version | 
*SystemApi* | [**reboot_system**](docs/SystemApi.md#reboot_system) | **POST** /system/reboot | 
*SystemApi* | [**update_system_backup_config**](docs/SystemApi.md#update_system_backup_config) | **POST** /system/backup/config | 
*SystemApi* | [**update_system_packages**](docs/SystemApi.md#update_system_packages) | **POST** /system/update-packages | 
*SystemApi* | [**update_system_privacy**](docs/SystemApi.md#update_system_privacy) | **POST** /system/privacy | 
*UserApi* | [**get_me**](docs/UserApi.md#get_me) | **GET** /me | 
*WebApi* | [**get_web_domains**](docs/WebApi.md#get_web_domains) | **GET** /web/domains | 
*WebApi* | [**update_web**](docs/WebApi.md#update_web) | **POST** /web/update | 


## Documentation For Models

 - [DNSCustomRecord](docs/DNSCustomRecord.md)
 - [DNSCustomRecordsResponse](docs/DNSCustomRecordsResponse.md)
 - [DNSDumpDomainRecord](docs/DNSDumpDomainRecord.md)
 - [DNSDumpDomainRecords](docs/DNSDumpDomainRecords.md)
 - [DNSDumpDomains](docs/DNSDumpDomains.md)
 - [DNSDumpResponse](docs/DNSDumpResponse.md)
 - [DNSRecordType](docs/DNSRecordType.md)
 - [DNSSecondaryNameserverAddRequest](docs/DNSSecondaryNameserverAddRequest.md)
 - [DNSSecondaryNameserverResponse](docs/DNSSecondaryNameserverResponse.md)
 - [DNSUpdateRequest](docs/DNSUpdateRequest.md)
 - [DNSZonesResponse](docs/DNSZonesResponse.md)
 - [MailAlias](docs/MailAlias.md)
 - [MailAliasByDomain](docs/MailAliasByDomain.md)
 - [MailAliasRemoveRequest](docs/MailAliasRemoveRequest.md)
 - [MailAliasUpsertRequest](docs/MailAliasUpsertRequest.md)
 - [MailAliasesResponseFormat](docs/MailAliasesResponseFormat.md)
 - [MailUser](docs/MailUser.md)
 - [MailUserAddPrivilegeRequest](docs/MailUserAddPrivilegeRequest.md)
 - [MailUserAddRequest](docs/MailUserAddRequest.md)
 - [MailUserByDomain](docs/MailUserByDomain.md)
 - [MailUserPrivilege](docs/MailUserPrivilege.md)
 - [MailUserRemovePrivilegeRequest](docs/MailUserRemovePrivilegeRequest.md)
 - [MailUserRemoveRequest](docs/MailUserRemoveRequest.md)
 - [MailUserSetPasswordRequest](docs/MailUserSetPasswordRequest.md)
 - [MailUserStatus](docs/MailUserStatus.md)
 - [MailUsersResponse](docs/MailUsersResponse.md)
 - [MailUsersResponseFormat](docs/MailUsersResponseFormat.md)
 - [MeAuthStatus](docs/MeAuthStatus.md)
 - [MeResponse](docs/MeResponse.md)
 - [SSLCSRGenerateRequest](docs/SSLCSRGenerateRequest.md)
 - [SSLCertificateInstallRequest](docs/SSLCertificateInstallRequest.md)
 - [SSLCertificatesProvisionResponse](docs/SSLCertificatesProvisionResponse.md)
 - [SSLCertificatesProvisionResponseRequests](docs/SSLCertificatesProvisionResponseRequests.md)
 - [SSLStatus](docs/SSLStatus.md)
 - [SSLStatusResponse](docs/SSLStatusResponse.md)
 - [SSLStatusType](docs/SSLStatusType.md)
 - [StatusEntry](docs/StatusEntry.md)
 - [StatusEntryExtra](docs/StatusEntryExtra.md)
 - [StatusEntryType](docs/StatusEntryType.md)
 - [SystemBackupConfigResponse](docs/SystemBackupConfigResponse.md)
 - [SystemBackupConfigUpdateRequest](docs/SystemBackupConfigUpdateRequest.md)
 - [SystemBackupStatus](docs/SystemBackupStatus.md)
 - [SystemBackupStatusResponse](docs/SystemBackupStatusResponse.md)
 - [SystemPrivacyStatus](docs/SystemPrivacyStatus.md)
 - [SystemPrivacyUpdateRequest](docs/SystemPrivacyUpdateRequest.md)
 - [SystemStatusResponse](docs/SystemStatusResponse.md)
 - [WebDomain](docs/WebDomain.md)


## Documentation For Authorization


## basicAuth

- **Type**: HTTP basic authentication


