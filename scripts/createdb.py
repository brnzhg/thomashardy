import db.testdb as tdb
import configparser
from pathlib import Path
import sqlalchemy as sa

config_filepath = Path(__file__).parent.parent.joinpath('config.ini').absolute()

config = configparser.ConfigParser()
config.read(config_filepath)
db_path = config['DEFAULT']['db_path']

engine = sa.create_engine(db_path, echo=True)
tdb.Base.metadata.create_all(engine)