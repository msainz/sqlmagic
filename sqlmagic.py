"""
Author: Aiyesha Ma & Marcos Sainz
Tested on IPython version 0.13.1

This SQL cell magic allows you to open multiple connections to several
databases and then reference the connections by name inside IPython

This code can be put in any Python module, it does not require IPython
itself to be running already.  It only creates the magics subclass but
doesn't instantiate it yet.

Adapted from:
    - https://gist.github.com/pfmoore/3872878
    - https://gist.github.com/bmabey/4585890

Load using:

import sqlmagic
reload(sqlmagic) # useful if you plan to be modifying this file
ip = get_ipython()
ip.register_magics(sqlmagic.SQLMagic)

Now you can do:

%connect {"name": "connection_name", "params": {"host": "host", "db": "database_name", "user": "user", "password": "password"}}

%%sql connection_name
select * from foo

"""
from IPython.core.magic import (Magics, magics_class, cell_magic, line_magic)

import MySQLdb
import json

# The class MUST call this class decorator at creation time
@magics_class
class SQLMagic(Magics):
    connections = {}

    @line_magic
    def connect(self, line):
        "Connect to a database"
        args = json.loads(line)
        connection_name = args['name'].strip()
        params = args['params']
        pwd = params['password'] if 'password' in params else ''
        self.connections[connection_name] = MySQLdb.connect(
                host=params['host'],
                user=params['user'],
                passwd=pwd , 
                db=params['db'])
        print "Connected successfully"

    @cell_magic
    def sql(self, line, cell):
        "Run a SQL query"
        c = self.connections[line.strip()].cursor()
        c.execute(cell)
        return c.fetchall()


