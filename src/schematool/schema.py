import json
from src.exceptions.exceptions import DatabaseAlreadyExistsInSchemaError
from src.exceptions.exceptions import SchemaAlreadyExistsInDatabaseError
from src.exceptions.exceptions import SchemaDoesNotExistInDatabaseError
from src.exceptions.exceptions import TableAlreadyExistsInSchemaError
from src.exceptions.exceptions import TableDoesNotExistInSchemaError

class Schema:
    def __init__(self, schema_file: str = 'src/config/testschema.json'):
        self.schema_file = schema_file
        self.schema_config = self._get_schema(schema_file)

    def _get_schema(self, schema_file: str) -> dict:
        with open(schema_file, 'r') as f:
            return json.load(f)

    def print_schema(self) -> None:
        print(json.dumps(self.schema_config,
                         indent=4, sort_keys=True))

    def _write_schema(self, schema: dict) -> None:
        with open(self.schema_file, 'w') as f:
            json.dump(schema, f, indent=4, sort_keys=True)

    def _get_next_id(self) -> int:
        return len(self.schema_config.keys()) + 1

    def add_database(self, database: str) -> None:
        # Check if database already exists
        if database in self.schema_config.keys():
            raise DatabaseAlreadyExistsInSchemaError(f'Database {database} already exists')
        self.schema_config[database] = {
            "id": self._get_next_id(),
            "database": database,
            "schemas": {
                "public": {
                    "tables": {}
                }
            }
        }
        self._write_schema(self.schema_config)

    def drop_database(self, database: str) -> None:
        if database in self.schema_config.keys():
            del self.schema_config[database]
            self._write_schema(self.schema_config)

    def add_schema(self, database: str, schema_name: str) -> None:
        if schema_name in self.schema_config[database]['schemas'].keys():
            raise SchemaAlreadyExistsInDatabaseError(f'Schema {schema_name} already exists')
        self.schema_config[database]['schemas'][schema_name] = {
            "tables": {}
        }
        self._write_schema(self.schema_config)

    def drop_schema(self, database: str, schema_name: str) -> None:
        if schema_name not in self.schema_config[database]['schemas'].keys():
            raise SchemaDoesNotExistInDatabaseError(f'Schema {schema_name} does not exist')
        del self.schema_config[database]['schemas'][schema_name]
        self._write_schema(self.schema_config)

    def add_table(self, database: str, schema_name: str, table_name: str) -> None:
        if table_name in self.schema_config[database]['schemas'][schema_name]['tables'].keys():
            raise TableAlreadyExistsInSchemaError(f'Table {table_name} already exists')
        self.schema_config[database]['schemas'][schema_name]['tables'][table_name] = {
            "columns": {}
        }
        self._write_schema(self.schema_config)

    def drop_table(self, database: str, schema_name: str, table_name: str) -> None:
        if table_name not in self.schema_config[database]['schemas'][schema_name]['tables'].keys():
            raise TableDoesNotExistInSchemaError(f'Table {table_name} does not exist')
        del self.schema_config[database]['schemas'][schema_name]['tables'][table_name]
        self._write_schema(self.schema_config)

    def add_column(self, database: str, schema_name: str, table_name: str, column_name: str, column_type: str) -> None:
        self.schema_config[database]['schemas'][schema_name]['tables'][table_name]['columns'][column_name] = {
            "type": Dtypes.types[column_type]
        }
        self._write_schema(self.schema_config)

    def drop_column(self, database: str, schema_name: str, table_name: str, column_name: str) -> None:
        del self.schema_config[database]['schemas'][schema_name]['tables'][table_name]['columns'][column_name]
        self._write_schema(self.schema_config)

    
class Dtypes:
    types = {
        'int': 'INT',
        'float': 'FLOAT',
        'varchar': 'VARCHAR',
        'bool': 'BOOLEAN',
        'serial': 'SERIAL',
        'timestamp': 'TIMESTAMP'
    }


