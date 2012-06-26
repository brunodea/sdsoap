# -*- encoding: utf-8 -*-

import sys
sys.path.append('../')

import logging
import traceback as tb
import suds.metrics as metrics
from suds import WebFault
from suds.client import Client
from suds.sax.element import Element

EBAY_WSDL = 'http://developer.ebay.com/webservices/finding/latest/FindingService.wsdl'

def setup_logging():
    logging.basicConfig(level=logging.INFO)
    logging.getLogger('suds.client').setLevel(logging.DEBUG)

def getItem(itemname):
    try:
        opdic={'X-EBAY-SOA-OPERATION-NAME':'findItemsByKeywords','X-EBAY-SOA-SECURITY-APPNAME':'Noneb7d1f-cc0c-4255-9e25-af37007c130'}
        client = Client(EBAY_WSDL,headers=opdic)
        keywords = itemname.replace(' ','%20')  #não pode ter espaços, no lugar tem que ter %20.      
        
        #infos para fazer uma pesquisa melhor
        #no momento a pesquisa retorna trilhões de respostas.
        paginationinput = client.factory.create('PaginationInput')
        postalcode = ''
        affiliate = client.factory.create('Affiliate') #para comissões
        sortordertype = client.factory.create('SortOrderType')
        sortordertype = sortordertype.BestMatch
        itemfilters = []
        aspectfilters = []
        outputselectortype = client.factory.create('OutputSelectorType')
        
        osts = [outputselectortype.GalleryInfo]
        
        response = client.service.findItemsByKeywords(keywords=keywords)
        #response = client.service.findItemsByKeywords(paginationinput,postalcode, \
        #    affiliate,sortordertype,keywords,itemfilters,aspectfilters,osts)
        print response
    
    except WebFault, f:
        print f
        print f.fault
    except Exception, e:
        print e
        tb.print_exc()

def main():
    setup_logging()
    getItem('megaman')

if __name__=='__main__':
    main()


