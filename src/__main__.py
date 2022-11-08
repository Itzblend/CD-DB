from src.schema import Schema
import click

@click.group()
def cli() -> None:
    pass

@cli.command()
@click.option('--database', '-d', required=True, help='Database name')
def add_database(database: str) -> None:
    schema = Schema()
    schema.add_database(database)

@cli.command()
@click.option('--database', '-d', required=True, help='Database name')
def drop_database(database: str) -> None:
    schema = Schema()
    schema.drop_database(database)


if __name__ == '__main__':
    cli()
    