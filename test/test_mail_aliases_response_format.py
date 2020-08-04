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
from mailinaboxapi.models.mail_aliases_response_format import MailAliasesResponseFormat  # noqa: E501
from mailinaboxapi.rest import ApiException

class TestMailAliasesResponseFormat(unittest.TestCase):
    """MailAliasesResponseFormat unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MailAliasesResponseFormat
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mailinaboxapi.models.mail_aliases_response_format.MailAliasesResponseFormat()  # noqa: E501
        if include_optional :
            return MailAliasesResponseFormat(
            )
        else :
            return MailAliasesResponseFormat(
        )

    def testMailAliasesResponseFormat(self):
        """Test MailAliasesResponseFormat"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
