import click
from src.dbtool.db import DBTool
from src.config import configuration

@click.group()
@click.option('--database_name', '-d', required=False, help='Database name')
@click.pass_context
def cli(ctx, database_name: str = 'postgres') -> None:
    ctx.ensure_object(dict)
    config = configuration.set_config(database=database_name)
    ctx.obj['dbconfig'] = config.dbconfig
    ctx.obj['connection_string'] = f"postgresql://{config.dbconfig['user']}:{config.dbconfig['password']}@{config.dbconfig['host']}:{config.dbconfig['port']}"

@cli.command()
@click.pass_context
def test_connection(ctx) -> None:
    db = DBTool(connection_string=ctx.obj['connection_string'], database=ctx.obj['dbconfig']['database'])
    print(db.query('SELECT 1'))
    db.close()

@cli.command()
@click.pass_context
def read_database_schema(ctx) -> None:
    db = DBTool(connection_string=ctx.obj['connection_string'], database=ctx.obj['dbconfig']['database'])
    db.read_database_schema()
    db.close()

    

if __name__ == '__main__':
    cli()