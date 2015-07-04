#!/usr/bin/env python

from setuptools import setup
import sys
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ["-v", "granary/test"]

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(
    name='granary',
    version = '0.7',
    packages=[
        'granary',
        'granary.test'
    ],
    license='http://opensource.org/licenses/MIT',
    author='Andreas M. Antonopoulos',
    author_email='andreas@thirdkey.solutions',
    url='https:/thirdkey.solutions',
    description='A library and interactive shell for encrypted versatile and resilient seed generation storage and recovery',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    cmdclass={'test': PyTest},
    entry_points={
        'console_scripts': [
            'granary=granary.shell:main',
        ],
    },
    
    install_requires=[
        'bitcoin',
        'mnemonic',
        'pbkdf2',
        'python-gnupg',
        'cmd2',
        'pycrypto',
    ],
    tests_require=[
        'mock',
        'pytest',
    ],
    test_suite='granary.test',
)
