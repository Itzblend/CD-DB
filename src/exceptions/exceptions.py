class DatabaseAlreadyExistsInSchemaError(Exception):
    pass

class SchemaAlreadyExistsInDatabaseError(Exception):
    pass

class SchemaDoesNotExistInDatabaseError(Exception):
    pass

class TableAlreadyExistsInSchemaError(Exception):
    pass

class TableDoesNotExistInSchemaError(Exception):
    pass