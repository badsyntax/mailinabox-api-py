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
from mailinabox_api.models.dns_record_type import DNSRecordType  # noqa: E501
from mailinabox_api.rest import ApiException


class TestDNSRecordType(unittest.TestCase):
    """DNSRecordType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DNSRecordType
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mailinabox_api.models.dns_record_type.DNSRecordType()  # noqa: E501
        if include_optional:
            return DNSRecordType()
        else:
            return DNSRecordType()

    def testDNSRecordType(self):
        """Test DNSRecordType"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
