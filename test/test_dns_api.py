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

import mailinaboxapi
from mailinaboxapi.api.dns_api import DNSApi  # noqa: E501
from mailinaboxapi.rest import ApiException


class TestDNSApi(unittest.TestCase):
    """DNSApi unit test stubs"""

    def setUp(self):
        self.api = mailinaboxapi.api.dns_api.DNSApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_dns_custom_record(self):
        """Test case for add_dns_custom_record

        """
        pass

    def test_add_dns_custom_record_for_type_a(self):
        """Test case for add_dns_custom_record_for_type_a

        """
        pass

    def test_add_dns_secondary_nameserver(self):
        """Test case for add_dns_secondary_nameserver

        """
        pass

    def test_get_dns_custom_records(self):
        """Test case for get_dns_custom_records

        """
        pass

    def test_get_dns_custom_records_for_domain_and_type(self):
        """Test case for get_dns_custom_records_for_domain_and_type

        """
        pass

    def test_get_dns_custom_records_for_domain_and_type_a(self):
        """Test case for get_dns_custom_records_for_domain_and_type_a

        """
        pass

    def test_get_dns_dump(self):
        """Test case for get_dns_dump

        """
        pass

    def test_get_dns_secondary_nameserver(self):
        """Test case for get_dns_secondary_nameserver

        """
        pass

    def test_get_dns_zones(self):
        """Test case for get_dns_zones

        """
        pass

    def test_remove_dns_custom_record(self):
        """Test case for remove_dns_custom_record

        """
        pass

    def test_remove_dns_custom_record_for_type_a(self):
        """Test case for remove_dns_custom_record_for_type_a

        """
        pass

    def test_update_dns(self):
        """Test case for update_dns

        """
        pass

    def test_update_dns_custom_record(self):
        """Test case for update_dns_custom_record

        """
        pass

    def test_update_dns_custom_record_for_type_a(self):
        """Test case for update_dns_custom_record_for_type_a

        """
        pass


if __name__ == "__main__":
    unittest.main()
