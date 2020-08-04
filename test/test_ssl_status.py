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

import mailinabox_api
from mailinabox_api.models.ssl_status import SSLStatus  # noqa: E501
from mailinabox_api.rest import ApiException


class TestSSLStatus(unittest.TestCase):
    """SSLStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SSLStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mailinabox_api.models.ssl_status.SSLStatus()  # noqa: E501
        if include_optional:
            return SSLStatus(
                domain="example.com",
                status="success",
                text="Signed & valid. The certificate expires in 87 days on 10/28/20.",
            )
        else:
            return SSLStatus(
                domain="example.com",
                status="success",
                text="Signed & valid. The certificate expires in 87 days on 10/28/20.",
            )

    def testSSLStatus(self):
        """Test SSLStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
