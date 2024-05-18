from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ 

from crear_entidad import Pais

from configuracion import engine

Session = sessionmaker(bind=engine)
session = Session()

#Presentar todos los países del continente americano
print("Presentar todos los países del continente americano")
paises1 = session.query(Pais).filter(Pais.continente.in_(['SA', 'NA'])).all()
for s in paises1:
    print("%s" % (s))
    print("---------")
print("--------------------------------")

#Presentar los países de Asía, ordenados por el atributo Dial.
print("Presentar los países de Asía, ordenados por el atributo Dial")
paises2 = session.query(Pais).filter(Pais.continente=='AS').order_by(Pais.dial).all()
for s in paises2:
    print("%s" % (s))
    print("---------")
print("--------------------------------")

#Presentar los lenguajes de cada país.
print("Presentar los lenguajes de cada país.")
paises3 = session.query(Pais).all()
for s in paises3:
    print("Nombre del Pais: %s - Lenguajes: %s" % (s.nombre_de_pais,s.lenguajes))
    print("---------")
print("--------------------------------")

#Presentar los países ordenados por la capital, siempre que el país pertenezca a Europa
print("Presentar los países ordenados por la capital, siempre que el país pertenezca a Europa")
paises4 = session.query(Pais).filter(Pais.continente=='EU').order_by(Pais.capital).all()
for s in paises4:
    print("%s" % (s))
    print("---------")
print("--------------------------------")

#Presentar todos los países que tengan en su cadena de nombre de país "uador" o en su cadena de capital "ito".
print("Presentar todos los países que tengan en su cadena de nombre de país 'uador' o en su cadena de capital 'ito'")
paises5 = session.query(Pais).filter(or_(Pais.nombre_de_pais.like("%uador%"), Pais.capital.like("%ito%"))).all()
for s in paises5:
    print("%s" % (s))
    print("---------")
print("--------------------------------")