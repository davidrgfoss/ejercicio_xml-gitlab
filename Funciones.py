from datetime import datetime

def ListarInformacion(doc):
    return zip(doc.xpath('//title/text()'), doc.xpath('//description/text()'))

def ContarInformacion(doc,cad):
    return len(doc.xpath('//genre[text() = "%s"]/text()' %(cad)))

def FiltrarInformacion(doc,cad,cad1):
    if float(cad) > float(cad1):
        cad3=cad
        cad=cad1
        cad1=cad3
    return doc.xpath('//book[price/text() >= "%s" and price/text() <= "%s"]/title/text()' %(cad,cad1))

def BuscarInformacion(doc,cad):
    return doc.xpath('//book[subgenre/name/text() = "%s"]/title/text()' %(cad))

def Calcularfecha(doc,fecha1,fecha2):
    if datetime(fecha1[0],fecha1[1],fecha1[2]) > datetime(fecha2[0],fecha2[1],fecha2[2]):
        fecha3=fecha2
        fecha2=fecha1
        fecha1=fecha3
    lista=[]
    for x in doc.xpath('//publish_date/text()'):
        lista.append(x.split("-"))
    lista2=[]
    for x in lista:
        x=[int(f) for f in x]
        lista2.append(x)
    lista=[]
    for x in lista2:
        if datetime(x[0],x[1],x[2]) > datetime(fecha1[0],fecha1[1],fecha1[2]) and datetime(x[0],x[1],x[2]) < datetime(fecha2[0],fecha2[1],fecha2[2]):
            lista.append(str("%02d-%02d-%02d" %(x[0],x[1],x[2])))
    return lista

def Ejerciciolibre(doc,cad):
    return zip(doc.xpath('//book[publish_date/text() = "%s"]/title/text()' %(cad)), doc.xpath('//book[publish_date/text() = "%s"]/genre/text()' %(cad)))

