# coding: utf-8

"""
    Mail-in-a-Box

    Mail-in-a-Box API HTTP specification.  # Introduction This API is documented in [**OpenAPI format**](http://spec.openapis.org/oas/v3.0.3). ([View the full HTTP specification](https://raw.githubusercontent.com/mail-in-a-box/mailinabox/api-spec/api/mailinabox.yml).)  All endpoints are relative to `https://{host}/admin` and are secured with [`Basic Access` authentication](https://en.wikipedia.org/wiki/Basic_access_authentication). If you have multi-factor authentication enabled, authentication with a `user:password` combination will fail unless a valid OTP is supplied via the `x-auth-token` header. Authentication via a `user:user_key` pair is possible without the header being present.   # noqa: E501

    The version of the OpenAPI document: 0.51.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import mailinabox_api
from mailinabox_api.api.mail_api import MailApi  # noqa: E501
from mailinabox_api.rest import ApiException


class TestMailApi(unittest.TestCase):
    """MailApi unit test stubs"""

    def setUp(self):
        self.api = mailinabox_api.api.mail_api.MailApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_mail_user(self):
        """Test case for add_mail_user

        Add mail user  # noqa: E501
        """
        pass

    def test_add_mail_user_privilege(self):
        """Test case for add_mail_user_privilege

        Add mail user privilege  # noqa: E501
        """
        pass

    def test_get_mail_aliases(self):
        """Test case for get_mail_aliases

        Get mail aliases  # noqa: E501
        """
        pass

    def test_get_mail_domains(self):
        """Test case for get_mail_domains

        Get mail domains  # noqa: E501
        """
        pass

    def test_get_mail_user_privileges(self):
        """Test case for get_mail_user_privileges

        Get mail user privileges  # noqa: E501
        """
        pass

    def test_get_mail_users(self):
        """Test case for get_mail_users

        Get mail users  # noqa: E501
        """
        pass

    def test_remove_mail_alias(self):
        """Test case for remove_mail_alias

        Remove mail alias  # noqa: E501
        """
        pass

    def test_remove_mail_user(self):
        """Test case for remove_mail_user

        Remove mail user  # noqa: E501
        """
        pass

    def test_remove_mail_user_privilege(self):
        """Test case for remove_mail_user_privilege

        Remove mail user privilege  # noqa: E501
        """
        pass

    def test_set_mail_user_password(self):
        """Test case for set_mail_user_password

        Set mail user password  # noqa: E501
        """
        pass

    def test_upsert_mail_alias(self):
        """Test case for upsert_mail_alias

        Upsert mail alias  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
