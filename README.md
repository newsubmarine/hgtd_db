A preliminary python-based(>=3.6) package for HGTD database development.

2021-8-13

required packages:
    - pandas, pymysql, sshtunnel, yaml


# Getting started  <a name="getting-started"></a>

## Setup <a name = "setup"</a>
pip install pandas, pymysql, sshtunnel, yaml
[to do] setup.sh

## Description

* Config.yaml: config your account 
* SQLManager.py: main class connect to database. `python SQLManager.py will execute a Test sql code`
* WriteHybird.py: write \*.csv file into database. No enough error indication now.
