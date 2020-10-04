import click
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
import db.testdb as cool


@click.command()
def cli():
    """Example script."""
    click.echo('Hello World2!')

if __name__ == "__main__":
    # cli()
    print(cool.User.__tablename__)