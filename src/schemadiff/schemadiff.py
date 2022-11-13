from src.schematool.schema import Schema
from src.dbtool.db import DBTool
from src.config import configuration


class SchemaDiff:
    def __init__(self, connection_string: str, database: str):
        schema_obj = Schema()
        db = DBTool(connection_string=connection_string, database=database)

        self.schema1 = schema_obj.schema_config
        self.schema2 = db.read_database_schema()
    
    def diff(self):
        schema_databases = [key for key in self.schema1.keys()]
        db_databases = [key for key in self.schema2.keys()]
        print(f'Databases in schema: {schema_databases}')
        print(f'Databases in database: {db_databases}')

        for path, v in dict_path(self.schema1):
            if len(path) == 8:
                print(' -> '.join(path), "=>", v)

def dict_path(my_dict, path=None):
    if path is None:
        path = []
    for k,v in my_dict.items():
        newpath = path + [k]
        if isinstance(v, dict):
            for u in dict_path(v, newpath):
                yield u
        else:
            yield newpath, v


