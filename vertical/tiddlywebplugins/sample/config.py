from tiddlywebplugins.instancer.util import get_tiddler_locations

from tiddlywebplugins.sample.instance import store_contents


PACKAGE_NAME = 'tiddlywebplugins.sample'


config = {
    'instance_tiddlers': get_tiddler_locations(store_contents, PACKAGE_NAME),
    'bag_create_policy': 'ANY',
    'recipe_create_policy': 'ANY',
}
