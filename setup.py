#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    import ez_setup
    ez_setup.use_setuptools()
    from setuptools import setup, find_packages

VERSION = __import__('scanredirect').__version__

import os
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-scanredirect',
    version = VERSION,
    description='Django app thats adds URL rules to redirect scripts looking for webapps exploits to their own IP ',
    packages=['scanredirect'],
    include_package_data=True,
    author='Cooperative Quinode',
    author_email='contact@quinode.fr',
    license='BSD',
    zip_safe=False,
    install_requires = [],
    long_description = open('README.rst').read(),
    url = 'https://github.com/quinode/scanredirect/',
    download_url = 'https://github.com/quinode/scanredirect/tarball/master',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        'Natural Language :: English',
        'Natural Language :: French',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],

)

