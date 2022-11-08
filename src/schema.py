import json
from src.exceptions import DatabaseAlreadyExistsInSchemaError

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

    