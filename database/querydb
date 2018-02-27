# Import libraries
import pandas as pd
import sys

from sqlalchemy import create_engine, MetaData, Table, select, engine
from sqlalchemy import create_engine

print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)

# there are multiple approaches to connect to DB
# Parameters
ServerName = "DAVID-THINK"
Database = "BizIntel"
Driver = "driver=SQL Server Native Client 11.0"

# Create the connection
engine = create_engine('mssql+pyodbc://' + ServerName + '/' + Database + "?" + Driver)

df = pd.read_sql_query("SELECT top 5 * FROM data", engine)
