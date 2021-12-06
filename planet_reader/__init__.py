from reader import make_reader
from jinja2 import Environment, PackageLoader, ChoiceLoader, FileSystemLoader, select_autoescape
from configparser import ConfigParser
import itertools


def sync_feed_list(config, reader):
    feeds_in_config = set(feed['rss_url'] for feed in filter_active_feeds(config))
    feeds_in_database = set(item.url for item in reader.get_feeds())

    feeds_to_add = feeds_in_config - feeds_in_database
    feeds_to_disable = feeds_in_database - feeds_in_config

    for feed in feeds_to_disable:
        reader.disable_feed_updates(feed)
    for feed in feeds_to_add:
        reader.add_feed(feed)


def filter_active_feeds(config):
    for feed, item in config.items():
        if feed in ('Planet', config.default_section):
            continue
        if item.get('link') is None:
            continue
        yield dict(rss_url=feed, **item)

def template_env(path=None):
    loaders = []
    if path:
        loaders.append(FileSystemLoader(path))
    loaders.append(PackageLoader(__package__))
    env = Environment(
        ChoiceLoader(loaders),
        autoescape=select_autoescape()
    )
    env.filters['take'] = itertools.islice
    return env

def run(config_path, db_path, update, sync, template_path, out):
    config= ConfigParser(interpolation=None)
    config.read(config_path)
    reader = make_reader(db_path)

    planet_config = dict(config['Planet'])
    config.remove_section('Planet')

    if sync:
        sync_feed_list(config, reader)

    if update:
        reader.update_feeds()

    env = template_env(template_path)
    template = env.get_template("layout.j2")
    output = template.render(
            planet_config = planet_config,
            feeds = filter_active_feeds(config),
            posts = reader.get_entries(),
    )
    if out:
        print(output)
