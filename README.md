# Applications
This repository hosts software applications geared towards Security/Web applications/Network technologies. Use of this code is strictly recommended for legitimate user only.
Publisher Name: Lalit Jagotra
Publisher Contact: lalit.jagotra@gmail.com
-----------------------------------
Database wrapper for executing secure CRUD operation to SQLITE database.
**Application 1:**
database wrapper written in python accepts database filename(directoty/filename) & table name and creates one for the user.
This wrapper Provides following methods and attributes:
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
  
 ** Application 2:**
  ProcessWebpage is **python module** used for indexing HTML code and make changes to the HTML page dynamically while updating HTML attributes, HTML tag content etc.
  - init(): initializes the object variable:
      - Type:Dict
      - Name:HTMLContent
   -  Instance attributes:
   -  Instance methods:  
       - SearchHTML(): This method is used for indexing HTML page  base on HTML Tags, respective Tagattributes and Tagboundary.
          - Return: IndexedHTMLContent
       - UpdateHTMLContent(): This method is used for indexing HTML page  base on HTML Tags, respective Tagattributes and Tagboundary.
          - Arguments:
              - (Dict)Params:
                  - keys: 
                    - (string)Tags
                    - (string)attributename
                    - (string)attributevalue
                    - (string)tagcontent
                    - (string)tagcontentoffset
                    - (string)"javascript"
                    - (string)"javascriptoffset"
          - Retrun: HTMLContent["Updated"]

Application 3: Password management Application build to run on user's laptop/desktop or over private LAN network. Files include:
  -  Simple_Web_Server.py : Runs native python web-server and handles majority of application logic. 
  -  databasev2.py: Database wrapper to manage and execute CRUD queries to sqlitedatabases.
  -  processwebpage: Generates dynamic webpages
  -  2 database files: 
      -  authenticate
      -  login
        
Application 4: Secure web development framework which also uses processWebpage module
  Work in progress.

