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
from mailinaboxapi.models.status_entry_extra import StatusEntryExtra  # noqa: E501
from mailinaboxapi.rest import ApiException


class TestStatusEntryExtra(unittest.TestCase):
    """StatusEntryExtra unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test StatusEntryExtra
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mailinaboxapi.models.status_entry_extra.StatusEntryExtra()  # noqa: E501
        if include_optional:
            return StatusEntryExtra(monospace=False, text="Digest Type: 2 / SHA-256")
        else:
            return StatusEntryExtra(monospace=False, text="Digest Type: 2 / SHA-256",)

    def testStatusEntryExtra(self):
        """Test StatusEntryExtra"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()