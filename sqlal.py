# -*- coding:utf-8 -*-
"""Operate Local SQL Server by sqlalchemy."""
import sqlalchemy as sa
import urllib
#import gab_models as gab

connection_string = "DRIVER={SQL Server};SERVER=localhost;\
                   UID=sa;PWD=Zaq12wsxcde34rfv!;Database=ASP20010;\
                   Trusted_Connection=Yes;Port=1433;"
connection_string = urllib.parse.quote_plus(connection_string)
connection_string = "mssql+pyodbc:///?odbc_connect=%s" % connection_string

engine = sa.create_engine(connection_string)
connection = engine.connect()
rows = connection.execute("USE ASP20010 select * from PERSON;")
for row in rows:
    print(row)
connection.close()
