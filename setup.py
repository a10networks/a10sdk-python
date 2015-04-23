#!/usr/bin/env python
# flake8: noqa

from setuptools import setup, find_packages

setup(
    name = "a10sdk",
    version = "4.0.1.214",
    packages = find_packages(),

    author = "A10 Networks",
    author_email = "support@a10networks.com",
    description = "A10 Networks ACOS Python SDK",
    license = "Apache",
    keywords = "a10 axapi acos adc slb load balancer",
    url = "https://github.com/a10networks/a10sdk-python",

    long_description = open('README.md').read(),

    classifiers = [
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet',
    ],
)
