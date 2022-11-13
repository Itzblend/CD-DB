import psycopg
import json

class DBTool():
    def __init__(self, connection_string: str, database: str = 'postgres'):
        self.conn = psycopg.connect(f'{connection_string}/{database}')
        self.database = database
        self.cursor = self.conn.cursor()

    def query(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def commit(self):
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def read_database_schema(self):
        self.cursor.execute("select * from information_schema.columns WHERE table_schema not in ('pg_catalog', 'information_schema')")
        result = self.cursor.fetchall()
        result_columns = [c[0] for c in self.cursor.description]

        schema_map = {
            str(self.database): {
                'database': str(self.database),
                'id': None,
                'schemas': {}
            }              
        }
        
        for row in result:
            schema = row[result_columns.index('table_schema')]
            table = row[result_columns.index('table_name')]
            column = row[result_columns.index('column_name')]
            dtype = row[result_columns.index('data_type')]
            column_default = row[result_columns.index('column_default')]
            if schema not in schema_map[str(self.database)]['schemas']:
                schema_map[str(self.database)]['schemas'][schema] = {
                    'tables': {}
                }
            if table not in schema_map[str(self.database)]['schemas'][schema]['tables']:
                schema_map[str(self.database)]['schemas'][schema]['tables'][table] = {
                    'columns': {}
                }
            schema_map[str(self.database)]['schemas'][schema]['tables'][table]['columns'][column] = {
                'type': dtype,
                'default': column_default
            }

        print(json.dumps(schema_map, indent=4))