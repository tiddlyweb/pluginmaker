AUTHOR = 'John Doe'
AUTHOR_EMAIL = 'johndoe@example.org'
NAME = 'tiddlywebplugins.sample'
DESCRIPTION = 'a sample TiddlyWeb vertical'
VERSION = '0.1'


import os

from setuptools import setup, find_packages


setup(
    namespace_packages = ['tiddlywebplugins'],
    name = NAME,
    version = VERSION,
    description = DESCRIPTION,
    long_description = open(os.path.join(os.path.dirname(__file__), 'README')).read(),
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,
    url = 'http://pypi.python.org/pypi/%s' % NAME,
    platforms = 'Posix; MacOS X; Windows',
    packages = find_packages(exclude=['test']),
    scripts = ['sample'],
    install_requires = ['tiddlywebwiki'],
    include_package_data = True,
    zip_safe = False
)
