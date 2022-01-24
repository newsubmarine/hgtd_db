<<<<<<< HEAD
Updated on 2022-01-16

- Added authority for SSH processes and database access. 
- Switched from pymysql to Sqlalchemy based framework
- To do : programing Flask app

## To run:
* prepare your config file
* connect SSH: 
    `python3 get_engine.py`
    `export ENGINE_STR=xxx`
    storing the environment variable ENGINE_STR
* Start flask app: python main.py




=======
>>>>>>> 93794ce6c983bb8780729e2513b7193688902252
A preliminary python-based(>=3.6) package for HGTD database development.
2021-8-13

Required packages:
    - pandas, pymysql, sshtunnel, yaml


# Getting started  <a name="getting-started"></a>

## Setup <a name = "setup"></a>
pip install pandas, pymysql, sshtunnel, yaml.

[to do] setup.sh

## Description

* Config.yaml: config your account 
* SQLManager.py: main class connect to database. `python SQLManager.py` will execute a Test sql code.
* WriteHybird.py: write \*.csv file into database. No enough error indication now.
