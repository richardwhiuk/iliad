iliad
=====

iliad is a internet server software, primarily focusing on HTTP.

It's currently under development, so there isn't much to see here.

Getting Started
---------------

iliad can be run by simply `python iliad.py`

To run a http server, specify http on the command line - e.g. `python iliad.py http`. Currently it will be bind to \*:8080 by default

Configuration
-------------

In order for iliad to do anything useful, you need to do some basic configuration.

This is done using environment variables

`ILIAD_DATABASE` = `iliad.mysql:\\username:password@host:port\database`

Requirements
------------

* [jinja2](http://jinja.pocoo.org "jinja2")
* [markdown](http://packages.python.org/Markdown "markdown")
* [MySQLdb](http://mysql-python.sourceforge.net/MySQLdb.html "MySQLdb")
* [py-prefork-server](https://github.com/crustymonkey/py-prefork-server "py-prefork-server")


