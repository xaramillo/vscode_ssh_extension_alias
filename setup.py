#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="Luis Xaramillo",
    author_email='xaramillo@solariabiodata.com.mx',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description=" Python alias package to installation of lastest version of ssh sync of VS Code extension.",
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='vscode_ssh_extension_alias',
    name='vscode_ssh_extension_alias',
    packages=find_packages(include=['vscode_ssh_extension_alias', 'vscode_ssh_extension_alias.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/xaramillo/vscode_ssh_extension_alias',
    version='0.1.0',
    zip_safe=False,
)
