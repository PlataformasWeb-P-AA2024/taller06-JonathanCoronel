from sqlalchemy import create_engine

engine = create_engine('sqlite:///basepaises.db', echo=True)