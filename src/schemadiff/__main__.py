import click
from src.config import configuration
from src.schemadiff.schemadiff import SchemaDiff

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
def schema_diff(ctx) -> None:
    schema_diff = SchemaDiff(connection_string=ctx.obj['connection_string'], database=ctx.obj['dbconfig']['database'])
    schema_diff.diff()

if __name__ == '__main__':
    cli()