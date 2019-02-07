import click
from flask.cli import with_appcontext
from flask_migrate import upgrade

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    upgrade()
    click.echo('Initialized the database.')


def init_app(app):
    app.cli.add_command(init_db_command)
