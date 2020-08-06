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
from mailinabox_api.models.system_backup_config_response import (
    SystemBackupConfigResponse,
)  # noqa: E501
from mailinabox_api.rest import ApiException


class TestSystemBackupConfigResponse(unittest.TestCase):
    """SystemBackupConfigResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SystemBackupConfigResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mailinabox_api.models.system_backup_config_response.SystemBackupConfigResponse()  # noqa: E501
        if include_optional:
            return SystemBackupConfigResponse(
                enc_pw_file="/home/user-data/backup/secret_key.txt",
                file_target_directory="/home/user-data/backup/encrypted",
                min_age_in_days=3,
                ssh_pub_key="ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDb root@box.example.com\n",
                target="s3://s3.eu-central-1.amazonaws.com/box-example-com",
                target_user="0",
                target_pass="0",
            )
        else:
            return SystemBackupConfigResponse(
                enc_pw_file="/home/user-data/backup/secret_key.txt",
                file_target_directory="/home/user-data/backup/encrypted",
                min_age_in_days=3,
                ssh_pub_key="ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDb root@box.example.com\n",
                target="s3://s3.eu-central-1.amazonaws.com/box-example-com",
            )

    def testSystemBackupConfigResponse(self):
        """Test SystemBackupConfigResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
