# applications
This repository hosts common applications related to Web/Database/Security.


-----------------------------------
Application 1

Database wrapper for executing secure CRUD operation to SQLITE database.
Application 1:
database wrapper written in python accepts database filename(directoty/filename) and table name creates one for the user.
Provide following methods and attributes:
Attributes:
  - filename: specify current directory/databasefilename.
  - table: specify current tablename
Methods:
  - create_database(): Create a new database file.
  - sql_noparam(query): execute SQL queries which accepts no params.
  - sql_do(query,params): execute SQL queries which accepts paramets.
  - create_table(columns): Create table in current database.
  - insert(columns): Insert columns in current Table.
  - delete(id): delete record with ID=id.
  - update(id,columns): update record at row with row id=id and update columns with new values.
  - retrieve_row(id): retreieve row with Row id=id 
  - retrieve_rows(): retrieve all rows in table
  - def countrecs(): Count total records.
