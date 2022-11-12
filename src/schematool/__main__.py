from src.schema import Schema
import click
from src.config import configuration

@click.group()
def cli() -> None:
    pass

@cli.command()
@click.option('--database_name', '-d', required=True, help='Database name')
def add_database(database_name: str) -> None:
    schema = Schema()
    schema.add_database(database_name)

@cli.command()
@click.option('--database_name', '-d', required=True, help='Database name')
def drop_database(database_name: str) -> None:
    schema = Schema()
    schema.drop_database(database_name)

@cli.command()
@click.option('--database_name', '-d', required=True, help='Database name')
@click.option('--schema_name', '-s', required=True, help='Schema name')
def add_schema(database_name: str, schema_name: str) -> None:
    schema = Schema()
    schema.add_schema(database_name, schema_name)

@cli.command()
@click.option('--database_name', '-d', required=True, help='Database name')
@click.option('--schema_name', '-s', required=True, help='Schema name')
def drop_schema(database_name: str, schema_name: str) -> None:
    schema = Schema()
    schema.drop_schema(database_name, schema_name)

@cli.command()
@click.option('--database_name', '-d', required=True, help='Database name')
@click.option('--schema_name', '-s', required=True, help='Schema name')
@click.option('--table_name', '-t', required=True, help='Table name')
def add_table(database_name: str, schema_name: str, table_name: str) -> None:
    schema = Schema()
    schema.add_table(database_name, schema_name, table_name)

@cli.command()
@click.option('--database_name', '-d', required=True, help='Database name')
@click.option('--schema_name', '-s', required=True, help='Schema name')
@click.option('--table_name', '-t', required=True, help='Table name')
def drop_table(database_name: str, schema_name: str, table_name: str) -> None:
    schema = Schema()
    schema.drop_table(database_name, schema_name, table_name)

@cli.command()
@click.option('--database_name', '-d', required=True, help='Database name')
@click.option('--schema_name', '-s', required=True, help='Schema name')
@click.option('--table_name', '-t', required=True, help='Table name')
@click.option('--column_name', '-c', required=True, help='Column name')
@click.option('--column_type', '-ct', required=True, help='Column type')
def add_column(database_name: str, schema_name: str, table_name: str, column_name: str, column_type: str) -> None:
    schema = Schema()
    schema.add_column(database_name, schema_name, table_name, column_name, column_type)

@cli.command()
@click.option('--database_name', '-d', required=True, help='Database name')
@click.option('--schema_name', '-s', required=True, help='Schema name')
@click.option('--table_name', '-t', required=True, help='Table name')
@click.option('--column_name', '-c', required=True, help='Column name')
def drop_column(database_name: str, schema_name: str, table_name: str, column_name: str) -> None:
    schema = Schema()
    schema.drop_column(database_name, schema_name, table_name, column_name)

@cli.command()
def read_config() -> None:
    config = configuration.set_config()
    print(config.dbconfig)

if __name__ == '__main__':
    cli()
    