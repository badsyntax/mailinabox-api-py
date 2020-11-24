# coding: utf-8

"""
    Mail-in-a-Box

    Mail-in-a-Box API HTTP specification.  # Introduction This API is documented in [**OpenAPI format**](http://spec.openapis.org/oas/v3.0.3). ([View the full HTTP specification](https://raw.githubusercontent.com/mail-in-a-box/mailinabox/api-spec/api/mailinabox.yml).)  All endpoints are relative to `https://{host}/admin` and are secured with [`Basic Access` authentication](https://en.wikipedia.org/wiki/Basic_access_authentication). If you have multi-factor authentication enabled, authentication with a `user:password` combination will fail unless a valid OTP is supplied via the `x-auth-token` header. Authentication via a `user:user_key` pair is possible without the header being present.   # noqa: E501

    The version of the OpenAPI document: 0.51.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import mailinabox_api
from mailinabox_api.models.mfa_enable_request import MfaEnableRequest  # noqa: E501
from mailinabox_api.rest import ApiException


class TestMfaEnableRequest(unittest.TestCase):
    """MfaEnableRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MfaEnableRequest
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # model = mailinabox_api.models.mfa_enable_request.MfaEnableRequest()  # noqa: E501
        if include_optional:
            return MfaEnableRequest(secret="0", code="0", label="0")
        else:
            return MfaEnableRequest(
                secret="0",
                code="0",
            )

    def testMfaEnableRequest(self):
        """Test MfaEnableRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
