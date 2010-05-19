"""
structure and contents of a default sample instance
"""

from tiddlywebwiki.instance import (instance_config, store_contents,
    store_structure)


instance_config['system_plugins'] = ['tiddlywebplugins.sample']
instance_config['twanager_plugins'] = ['tiddlywebplugins.sample']

store_contents['sample_plugins'] = ['src/plugins/index.recipe']
store_contents['sample_content'] = ['src/content/index.recipe']

store_structure['bags']['sample_plugins'] = {
    'desc': 'sample plugins',
    'policy': store_structure['bags']['system']['policy']
}

store_structure['bags']['sample_content'] = {
    'desc': 'sample content',
    'policy': {
        'read': [],
        'write': ['ANY'],
        'create': ['ANY'],
        'delete': ['NONE'],
        'manage': ['R:ADMIN'],
        'accept': ['R:ADMIN'],
        'owner': 'administrator'
    }
}

for bag in ['sample_plugins', 'sample_content']:
    store_structure['recipes']['default']['recipe'].insert(1, (bag, ''))

store_structure['recipes']['sample'] = {
    'desc': 'standard TiddlyWebWiki environment',
    'recipe': [
        ('sample_plugins', ''),
        ('sample_content', ''),
    ],
    'policy': {
        'read': [],
        'write': ['R:ADMIN'],
        'manage': ['R:ADMIN'],
        'delete': ['R:ADMIN'],
        'owner': 'administrator'
    }
}
