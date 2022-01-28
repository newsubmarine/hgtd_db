Updated on 2022-01-25


- Added authority for SSH processes and database access. 
- Switched from pymysql to Sqlalchemy based framework
- To do : user privilege, fullfill write/upload demands, programing Flask app

## Setup:
- conda create --name hgtd_db python=3.6
- conda activate hgtd_db
- pip install -r requirement.txt
- export PYTHONPATH=$PWD:$PYTHONPATH

## To run:
- prepare your config file: .config.yaml, used in `Root/database.py`: If you are at lxplus.cern.ch, you don't need to setup SSH sshtunnel, so "server" can be empty.
    - "db" block: fill in your account to connect database
- Test the framework: python run/hgtdpdb_test.py

Query metadatas from the database:
- `python Root/query.py <action> --type <tablename>`, <action> includs:
    - 'list_all_tables': print out all defind tables in `model/hgtdpdb_model.py` (not tables in database, it will be another way to retrieve the exsit tables in database.)
    - 'list_all_columns': specify a table (can be readed by perform '--list_all_table') --type <tablename> and columns will be listed from this table.
    - 'query_all': qeury all entries.
    - 'query_first': query the first entries.
    - 'query with selections: will be a further step.

Currently logos are on at "INFO" level. Can be closed by changing setLevel(logging.INFO) to setLevel(logging.WARNING)





