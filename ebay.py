# -*- encoding: utf-8 -*-

import sys
sys.path.append('../')

import logging
import traceback as tb
import suds.metrics as metrics
import urllib
from suds import WebFault
from suds.client import Client
from suds.sax.element import Element

EBAY_WSDL = 'http://developer.ebay.com/webservices/finding/latest/FindingService.wsdl'
EBAY_KEY  = 'Noneb7d1f-cc0c-4255-9e25-af37007c130'

def setup_logging():
    logging.basicConfig(level=logging.INFO)
    logging.getLogger('suds.client').setLevel(logging.DEBUG)

def getItem(itemname):
    try:
        headers={'X-EBAY-SOA-OPERATION-NAME':'findItemsByKeywords', \
                'X-EBAY-SOA-SECURITY-APPNAME': EBAY_KEY}
        client = Client(EBAY_WSDL,headers=headers)
        keywords = urllib.urlencode({'nothing':itemname}).split('=')
        keywords = keywords[1]
        
        #infos para fazer uma pesquisa melhor
        #no momento a pesquisa retorna trilhões de respostas.
        paginationinput = client.factory.create('PaginationInput')
        postalcode = '22313'
        affiliate = client.factory.create('Affiliate') #para comissões
        sortordertype = client.factory.create('SortOrderType')
        sortordertype = sortordertype.BestMatch
        itemfilters = []
        aspectfilters = []
        outputselectortype = client.factory.create('OutputSelectorType')
        
        osts = [outputselectortype.GalleryInfo]
        
        response = client.service.findItemsByKeywords(paginationinput,postalcode, \
            affiliate,sortordertype,keywords,itemfilters,aspectfilters,osts)
        for res in response:
            if res[0] == 'searchResult':
                if res[1]._count > 0:
                    for r in res[1].item: 
                        title = r.title.encode('utf-8')
                        currentPrice = r.sellingStatus.currentPrice
                        print title
                        print currentPrice._currencyId + ' ' + currentPrice.value
                    break
    
    except WebFault, f:
        print f
        print f.fault
    except Exception, e:
        print e
        tb.print_exc()

def main():
    setup_logging()
    getItem('megaman x')

if __name__=='__main__':
    main()


