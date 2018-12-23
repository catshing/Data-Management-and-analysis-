from sqlalchemy import create_engine
import config

conf = config.get_config('config.ini')
dsn = config.create_dsn(conf['db'])
engine = create_engine(dsn, echo=False)
