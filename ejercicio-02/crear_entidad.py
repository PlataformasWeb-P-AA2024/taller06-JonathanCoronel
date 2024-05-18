
from configuracion import engine

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


from sqlalchemy import Column, Integer, String

class Pais(Base):
    __tablename__ = 'lospaises'

    id = Column(Integer, primary_key=True)
    nombre_de_pais = Column(String)
    capital = Column(String)
    continente = Column(String)
    dial = Column(String)
    geoname_id = Column(Integer)
    itu = Column(String)
    lenguajes = Column(String)
    es_independiente = Column(String)

    def __repr__(self):
        return "Pais: Nombre=%s Capital=%s Continente:%s Dial=%s, Geoname ID=%d, ITU=%s, Lenguajes=%s, Es independiente=%s" % (
                          self.nombre_de_pais,
                          self.capital,
                          self.continente,
                          self.dial,
                          self.geoname_id,
                          self.itu,
                          self.lenguajes,
                          self.es_independiente)

Base.metadata.create_all(engine)
