# SQL Magic for IPython

Author: [Aiyesha Ma](https://github.com/aiyesha) & [Marcos Sainz](https://github.com/msainz)<br>
Tested on IPython Version 0.13.1

This SQL cell magic allows you to open multiple connections to several databases and then reference the connections by name inside IPython.

This code can be put in any Python module, it does not require IPython itself to be running already.  It only creates the magics subclass but doesn't instantiate it yet.

Adapted from:
  * [https://gist.github.com/pfmoore/3872878](https://gist.github.com/pfmoore/3872878)
  * [https://gist.github.com/bmabey/4585890](https://gist.github.com/bmabey/4585890)

Load using:
```python
import sqlmagic
reload(sqlmagic) # useful if you plan to be modifying this file
ip = get_ipython()
ip.register_magics(sqlmagic.SQLMagic)
```
Now you can do the following line magic to setup a connection:
```python
%connect {"name": "connection_name", "params": {"host": "host", "db": "database_name", "user": "user", "password": "password"}}
```
And then reference and use the connection via cell magic:
```python
%%sql connection_name
select * from foo
```
