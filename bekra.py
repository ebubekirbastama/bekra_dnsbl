# -*- coding: utf-8 -*-
from suds.client import Client
from suds.wsse import *

def ggonder(ipi):
 url = 'http://ebubekirbastama.esy.es/dnsblserver/StockQuote.wsdl'
 client = Client(url)
 ip = client.service.gonder(ipi)
 dosya = open("deneme.xml", "w")
 dosya.write(ip)
 dosya.close()
 print "Xml dosyası oluşturuldu."
 return ip
ggonder('ipi')


