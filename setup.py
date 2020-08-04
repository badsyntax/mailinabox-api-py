# coding: utf-8

"""
    Mail-in-a-Box

    Mail-in-a-Box API HTTP specification.  # noqa: E501

    The version of the OpenAPI document: 0.46.0
    Contact: contact@mailinabox.email
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301
from pathlib import Path  # noqa E402


def get_long_description():
    return (CURRENT_DIR / "README.md").read_text(encoding="utf8")


NAME = "mailinabox-api"
VERSION = "0.0.3"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Mail-in-a-Box",
    author="Richard Willis",
    author_email="willis.rh@gmail.com",
    url="https://github.com/badsyntax/mailinabox-api-py",
    keywords=["mailinabox", "mail-in-a-box", "Mail-in-a-Box"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="CC0 1.0 Universal",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
)
