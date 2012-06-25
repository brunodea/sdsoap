# -*- coding: utf-8 -*-

import sys
sys.path.append('../')

import logging
import traceback as tb
import suds.metrics as metrics
import inspect
import urllib
import urllib2
import httplib
import suds
from suds import WebFault
from suds.client import Client
import urllib
import contextlib
from xml.dom.minidom import parseString

MS_KEY = 'mjKwRazoJLnNhZyPnuBXr7u3lj/BCbj2CB4BFIzY4Rg='
MS_URL = 'https://api.datamarket.azure.com/Bing/Search/Image'
NUM_IMGS = 4

class Game(object):
    def __init__(self,name='',platform='',price=0,gameid=''):
        self.name = name
        self.platform = platform
        self.price = price
        self.gameid = gameid
        self.imgs = []

    def __str__(self):
        return 'Jogo: %s\nPlataforma: %s\nPreco: %d\nID: %s\n' % (self.name,self.platform,self.price,self.gameid)

def setup_logging():
    logging.basicConfig(level=logging.INFO)
    logging.getLogger('suds.client').setLevel(logging.DEBUG)


def getGamePlatform(display_string):
    reverse = display_string[::-1]
    res = reverse[1:reverse.find('(')]
    res = res[::-1]

    return res

def getGamesFromSearch(search):
    result = []
    try:
        print 'Busca por jogo %s.' % (search)
        url = "http://www.gamecompare.com/GameCompare.asmx?WSDL"
        client = Client(url)
        print 'Iniciando busca...'
        response = client.service.Search('SourceControl', search)
        print 'Resultados da busca:'
        responses = response.colResults.SearchResult

        for r in responses:
            try:
                name = r.SelectString
                str(name)
                platform = getGamePlatform(r.DisplayString)
                gameid = r.ItemID

                game = Game(name=name,platform=platform,gameid=gameid)
                #print game

                result.append(game)
            except Exception as e:
               pass
        return_stmt = result
#        passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
#        passman.add_password(None, MS_URL,' ',MS_KEY)
        
#        authhandler = urllib2.HTTPBasicAuthHandler(passman)
#        opener = urllib2.build_opener(authhandler)
        
#        urllib2.install_opener(opener)
#        return_stmt = []
#        for r in result:
#            print '-----------------------Get Image Request-------------------------'
            
#            query = '\''+r.name + ' ' + r.platform +'\''
#            query = urllib.urlencode({'Query':query,'$top':NUM_IMGS})
#            url = MS_URL+'?'+query
#            with contextlib.closing(urllib2.urlopen(url)) as x:
#                data = x.read()
#                dom = parseString(data)
#                xmltag = dom.getElementsByTagName('d:MediaUrl')
#                gameimages = []
#                for elem in xmltag:
#                    xml = elem.toxml()
#                    imageurl = xml.replace('<d:MediaUrl m:type="Edm.String">','').replace('</d:MediaUrl>','')
#                    if '.png' in imageurl or '.jpg' in imageurl:
#                        gameimages.append(imageurl)
#                        print imageurl
#                r.imgs = gameimages
#                return_stmt.append(r)               

    except WebFault as f:
        print 'WebFault'
        print f
        print f.fault
    except Exception as e:
        print 'Exception'
        print e

    return return_stmt

def main():
    setup_logging()
    getGamesFromSearch('megaman')



if __name__=="__main__":
    main()
