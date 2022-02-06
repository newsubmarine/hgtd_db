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

- Database CRUD main code:
    - `python Root/opration.py <operation>`, type --help for more help

Query metadatas from the database:
- `python Root/opration.py query --type <tablename> --action <action> --expression `, <action> includes:
    - 'list_all_tables': print out all defind tables in `model/hgtdpdb_model.py` (the __tablename__ of models).
    - 'list_all_columns': specify a table --type <tablename> ( <tablename> can be readed by performing '--list_all_tables') , columns will be listed from this table.
    - 'query_all': qeury all entries.
    - 'query_first': query the first entries.
    - to query with selections, turn on `--expression`, definition is in clause.py

Write metadatas to the database:
- `python Root/opration.py insert --type <tablename> --input <input csv> --update`,
    - input format should be identical with the template. See example share/csv_template/sensor_tempplate.csv
    - turn on `-- update` if the input rows are reduplicated.

Currently logos are at default level.





