#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:copyright: (c) 2018 by LaunchDarkly
:license: Apche 2.0, see LICENSE for more details.
"""
import os
import sys

from setuptools import setup
from setuptools.command.install import install

# relayCommander version
VERSION = "1.1.2"

def readme():
    """print long description"""
    with open('README.md') as f:
        return f.read()


class VerifyVersionCommand(install):
    """Custom command to verify that the git tag matches our version"""
    description = 'verify that the git tag matches our version'

    def run(self):
        tag = os.getenv('CIRCLE_TAG')

        if tag != VERSION:
            info = "Git tag: {0} does not match the version of this app: {1}".format(
                tag, VERSION
            )
            sys.exit(info)

setup(
    name="rc",
    version=VERSION,
    description="CLI to Update LD Relay in Disaster Scenarios",
    long_description=readme(),
    url="https://github.com/launchdarkly/relayCommander",
    author="Launch Darkly Solutions Engineering Team",
    author_email="sales@launchdarkly.com",
    license="Apache 2.0",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords='launchdarkly api redis relay',
    packages=['relay_commander', 'lib/api-client-python'],
    install_requires=[
        'click',
        'requests',
        'redis',
        'jinja2'
    ],
    python_requires='>=3',
    cmdclass={
        'verify': VerifyVersionCommand,
    },
    entry_points='''
        [console_scripts]
        rc=relay_commander.rc:cli
    '''
)