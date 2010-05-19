"""
sample vertical

website: http://example.org
repository: http://github.com/JohnDoe/sample
"""

from tiddlyweb.util import merge_config

from tiddlywebplugins.sample.config import config as sample_config


__version__ = '0.1.0'


def init(config):
    import tiddlywebwiki

    merge_config(config, sample_config)

    tiddlywebwiki.init(config)
