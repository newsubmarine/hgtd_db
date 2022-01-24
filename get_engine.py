from calendar import c
from ConnHandler import ConnHandler

conn = ConnHandler('.config.yaml')
print('-'*100)
print(f"export ENGINE_STR={conn.get_engine_string()}")