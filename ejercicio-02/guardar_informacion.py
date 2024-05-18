from sqlalchemy.orm import sessionmaker

from crear_entidad import Pais
from configuracion import engine
import requests

Session = sessionmaker(bind=engine)
session = Session()

datos = requests.get('https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json')
datos_json = datos.json()

for d in datos_json:
    p = Pais(nombre_de_pais=d['CLDR display name'], capital=d['Capital'], continente=d['Continent'], dial=d['Dial'],
             geoname_id=d['Geoname ID'], itu=d['ITU'], lenguajes=d['Languages'], es_independiente=d['is_independent'])
    session.add(p)

session.commit()