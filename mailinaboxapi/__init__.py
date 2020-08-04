# coding: utf-8

# flake8: noqa

"""
    Mail-in-a-Box

    Mail-in-a-Box API HTTP specification.  # noqa: E501

    The version of the OpenAPI document: 0.46.0
    Contact: contact@mailinabox.email
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "0.0.0-SNAPSHOT.5"

# import apis into sdk package
from mailinaboxapi.api.dns_api import DNSApi
from mailinaboxapi.api.mail_api import MailApi
from mailinaboxapi.api.ssl_api import SSLApi
from mailinaboxapi.api.system_api import SystemApi
from mailinaboxapi.api.user_api import UserApi
from mailinaboxapi.api.web_api import WebApi

# import ApiClient
from mailinaboxapi.api_client import ApiClient
from mailinaboxapi.configuration import Configuration
from mailinaboxapi.exceptions import OpenApiException
from mailinaboxapi.exceptions import ApiTypeError
from mailinaboxapi.exceptions import ApiValueError
from mailinaboxapi.exceptions import ApiKeyError
from mailinaboxapi.exceptions import ApiException

# import models into sdk package
from mailinaboxapi.models.dns_custom_record import DNSCustomRecord
from mailinaboxapi.models.dns_custom_records_response import DNSCustomRecordsResponse
from mailinaboxapi.models.dns_dump_domain_record import DNSDumpDomainRecord
from mailinaboxapi.models.dns_dump_domain_records import DNSDumpDomainRecords
from mailinaboxapi.models.dns_dump_domains import DNSDumpDomains
from mailinaboxapi.models.dns_dump_response import DNSDumpResponse
from mailinaboxapi.models.dns_record_type import DNSRecordType
from mailinaboxapi.models.dns_secondary_nameserver_add_request import (
    DNSSecondaryNameserverAddRequest,
)
from mailinaboxapi.models.dns_secondary_nameserver_response import (
    DNSSecondaryNameserverResponse,
)
from mailinaboxapi.models.dns_update_request import DNSUpdateRequest
from mailinaboxapi.models.dns_zones_response import DNSZonesResponse
from mailinaboxapi.models.mail_alias import MailAlias
from mailinaboxapi.models.mail_alias_by_domain import MailAliasByDomain
from mailinaboxapi.models.mail_alias_remove_request import MailAliasRemoveRequest
from mailinaboxapi.models.mail_alias_upsert_request import MailAliasUpsertRequest
from mailinaboxapi.models.mail_aliases_response_format import MailAliasesResponseFormat
from mailinaboxapi.models.mail_user import MailUser
from mailinaboxapi.models.mail_user_add_privilege_request import (
    MailUserAddPrivilegeRequest,
)
from mailinaboxapi.models.mail_user_add_request import MailUserAddRequest
from mailinaboxapi.models.mail_user_by_domain import MailUserByDomain
from mailinaboxapi.models.mail_user_privilege import MailUserPrivilege
from mailinaboxapi.models.mail_user_remove_privilege_request import (
    MailUserRemovePrivilegeRequest,
)
from mailinaboxapi.models.mail_user_remove_request import MailUserRemoveRequest
from mailinaboxapi.models.mail_user_set_password_request import (
    MailUserSetPasswordRequest,
)
from mailinaboxapi.models.mail_user_status import MailUserStatus
from mailinaboxapi.models.mail_users_response import MailUsersResponse
from mailinaboxapi.models.mail_users_response_format import MailUsersResponseFormat
from mailinaboxapi.models.me_auth_status import MeAuthStatus
from mailinaboxapi.models.me_response import MeResponse
from mailinaboxapi.models.sslcsr_generate_request import SSLCSRGenerateRequest
from mailinaboxapi.models.ssl_certificate_install_request import (
    SSLCertificateInstallRequest,
)
from mailinaboxapi.models.ssl_certificates_provision_response import (
    SSLCertificatesProvisionResponse,
)
from mailinaboxapi.models.ssl_certificates_provision_response_requests import (
    SSLCertificatesProvisionResponseRequests,
)
from mailinaboxapi.models.ssl_status import SSLStatus
from mailinaboxapi.models.ssl_status_response import SSLStatusResponse
from mailinaboxapi.models.ssl_status_type import SSLStatusType
from mailinaboxapi.models.status_entry import StatusEntry
from mailinaboxapi.models.status_entry_extra import StatusEntryExtra
from mailinaboxapi.models.status_entry_type import StatusEntryType
from mailinaboxapi.models.system_backup_config_response import (
    SystemBackupConfigResponse,
)
from mailinaboxapi.models.system_backup_config_update_request import (
    SystemBackupConfigUpdateRequest,
)
from mailinaboxapi.models.system_backup_status import SystemBackupStatus
from mailinaboxapi.models.system_backup_status_response import (
    SystemBackupStatusResponse,
)
from mailinaboxapi.models.system_privacy_status import SystemPrivacyStatus
from mailinaboxapi.models.system_privacy_update_request import (
    SystemPrivacyUpdateRequest,
)
from mailinaboxapi.models.system_status_response import SystemStatusResponse
from mailinaboxapi.models.web_domain import WebDomain
