import click
from . import run

@click.command(context_settings={'show_default': True})
@click.option('--config', default='config.ini', help='Configuration file.', type=click.Path())
@click.option('--db', default='db.sqlite', help='Sqlite database file.', type=click.Path())
@click.option('--template-path', help='Path to custom templates.', type=click.Path())
@click.option('--update/--no-update', default=True, help="Update feeds in database")
@click.option('--sync/--no-sync', default=True, help="Sync database feed list to config file")
@click.option('--no-out', is_flag=True)
def main(config, db, update, sync, template_path, no_out):
    run(config, db, update, sync, template_path, not no_out)

if __name__ == '__main__':
    main()
