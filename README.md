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
- prepare your config file: .config.yaml: If you are at lxplus.cern.ch, you don't need to setup SSH sshtunnel, so "server" can be empty.
- Test the framework: python run/hgtdpdb_test.py



