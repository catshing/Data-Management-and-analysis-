import configparser

def get_config(fn):
    conf = configparser.ConfigParser()
    conf.read(fn)
    return conf

def create_dsn(d):
    return f'postgres://{d["username"]}{"" if "password" not in d else ":" + d["password"]}@{d["host"]}/{d["database"]}'
