# coding: utf-8

"""
    Mail-in-a-Box

    Mail-in-a-Box API HTTP specification.  # noqa: E501

    The version of the OpenAPI document: 0.46.0
    Contact: contact@mailinabox.email
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import mailinaboxapi
from mailinaboxapi.models.mail_alias_upsert_request import (
    MailAliasUpsertRequest,
)  # noqa: E501
from mailinaboxapi.rest import ApiException


class TestMailAliasUpsertRequest(unittest.TestCase):
    """MailAliasUpsertRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MailAliasUpsertRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mailinaboxapi.models.mail_alias_upsert_request.MailAliasUpsertRequest()  # noqa: E501
        if include_optional:
            return MailAliasUpsertRequest(
                update_if_exists=1,
                address="user@example.com",
                forwards_to="email1@example.com, example2@example.com",
                permitted_senders="email1@example.com, example2@example.com",
            )
        else:
            return MailAliasUpsertRequest(
                update_if_exists=1,
                address="user@example.com",
                forwards_to="email1@example.com, example2@example.com",
                permitted_senders="email1@example.com, example2@example.com",
            )

    def testMailAliasUpsertRequest(self):
        """Test MailAliasUpsertRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
