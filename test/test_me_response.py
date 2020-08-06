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
from mailinabox_api.models.me_response import MeResponse  # noqa: E501
from mailinabox_api.rest import ApiException


class TestMeResponse(unittest.TestCase):
    """MeResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MeResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mailinabox_api.models.me_response.MeResponse()  # noqa: E501
        if include_optional:
            return MeResponse(
                api_key="12345abcde",
                email="user@example.com",
                privileges=["admin"],
                reason="Incorrect username or password",
                status="invalid",
            )
        else:
            return MeResponse(status="invalid",)

    def testMeResponse(self):
        """Test MeResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
