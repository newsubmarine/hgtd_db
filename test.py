import config

cfg = config.ReadConfig("config.yaml")
print(cfg)

server = cfg['Server']
database = cfg['Database']
print(server['host'])
print("xxx")
