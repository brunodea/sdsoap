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

class EBayItem(object):
    def __init__(self,title,currency,price,link_ebay):
        self.title = title
        self.currency = currency
        self.price = price
        self.link_ebay = link_ebay
        
    def __str__(self):
        return self.currency + ' ' + self.price + ' ' + self.title + '\n' + self.link_ebay


def setup_logging():
    logging.basicConfig(level=logging.INFO)
    logging.getLogger('suds.client').setLevel(logging.DEBUG)

def getEBayItems(itemname,num_res_items):
    items = []
    try:
        headers={'X-EBAY-SOA-OPERATION-NAME':'findItemsByKeywords', \
                'X-EBAY-SOA-SECURITY-APPNAME': EBAY_KEY}
        client = Client(EBAY_WSDL,headers=headers)
        keywords = itemname
        
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
                    i = 0
                    for r in res[1].item:
                        currentPrice = r.sellingStatus.currentPrice
                        ebayitem = EBayItem(unicode(r.title),currentPrice._currencyId,currentPrice.value,r.viewItemURL)
                        print ebayitem
                        items.append(ebayitem)
                        i = i + 1
                        if i == num_res_items:
                            break
                    break
    
    except WebFault, f:
        print f
        print f.fault
    except Exception, e:
        print e
        tb.print_exc()
    return items

def main():
    setup_logging()
    getEBayItem('\"megaman x\" SNES',5)

if __name__=='__main__':
    main()


