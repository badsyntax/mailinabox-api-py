# coding: utf-8

"""
    Mail-in-a-Box

    Mail-in-a-Box API HTTP specification.  # noqa: E501

    The version of the OpenAPI document: 0.47.0
    Contact: contact@mailinabox.email
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import mailinabox_api
from mailinabox_api.models.mail_user_by_domain import MailUserByDomain  # noqa: E501
from mailinabox_api.rest import ApiException


class TestMailUserByDomain(unittest.TestCase):
    """MailUserByDomain unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MailUserByDomain
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mailinabox_api.models.mail_user_by_domain.MailUserByDomain()  # noqa: E501
        if include_optional:
            return MailUserByDomain(
                domain="example.com",
                users=[
                    mailinabox_api.models.mail_user.MailUser(
                        email="user@example.com",
                        privileges=["admin"],
                        status="active",
                        mailbox="/home/user-data/mail/mailboxes/example.com/user",
                    )
                ],
            )
        else:
            return MailUserByDomain(
                domain="example.com",
                users=[
                    mailinabox_api.models.mail_user.MailUser(
                        email="user@example.com",
                        privileges=["admin"],
                        status="active",
                        mailbox="/home/user-data/mail/mailboxes/example.com/user",
                    )
                ],
            )

    def testMailUserByDomain(self):
        """Test MailUserByDomain"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
