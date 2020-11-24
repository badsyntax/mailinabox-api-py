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
from mailinabox_api.models.system_backup_status_response import (
    SystemBackupStatusResponse,
)  # noqa: E501
from mailinabox_api.rest import ApiException


class TestSystemBackupStatusResponse(unittest.TestCase):
    """SystemBackupStatusResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SystemBackupStatusResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # model = mailinabox_api.models.system_backup_status_response.SystemBackupStatusResponse()  # noqa: E501
        if include_optional:
            return SystemBackupStatusResponse(
                backups=[
                    mailinabox_api.models.system_backup_status.SystemBackupStatus(
                        date=datetime.datetime.strptime(
                            "2013-10-20 19:20:30.00", "%Y-%m-%d %H:%M:%S.%f"
                        ),
                        date_delta="15 hours, 40 minutes",
                        date_str="2020-08-01 03:37:06 BST",
                        deleted_in="approx. 6 days",
                        full=False,
                        size=125332,
                        volumes=1,
                    )
                ],
                unmatched_file_size=0,
                error="Something is wrong with the backup",
            )
        else:
            return SystemBackupStatusResponse(
                unmatched_file_size=0,
            )

    def testSystemBackupStatusResponse(self):
        """Test SystemBackupStatusResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
