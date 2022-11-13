import json
import os
from collections import namedtuple

def set_config(database: str = None):
    dbconfig = {
        'host': os.getenv('DB_HOST', 'localhost'),
        'port': os.getenv('DB_PORT', '5435'),
        'user': os.getenv('DB_USER', 'postgres'),
        'password': os.getenv('DB_PASSWORD', 'password'),
        'database': database or 'postgres'
    }

    # Create namedtuple from dictionary
    config = namedtuple('config', 'dbconfig')

    return config(dbconfig=dbconfig)

