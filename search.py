# -*- coding: utf-8 -*-

import sys
sys.path.append('../')

import logging
import traceback as tb
import suds.metrics as metrics
import inspect
import suds
from suds import WebFault
from suds.client import Client

MS_KEY = 'mjKwRazoJLnNhZyPnuBXr7u3lj/BCbj2CB4BFIzY4Rg='
MS_URL = 'https://api.datamarket.azure.com/Bing/Search/Image'

class Game(object):
    def __init__(self,name='',platform='',price=0,gameid=''):
        self.name = name
        self.platform = platform
        self.gameid = gameid
        self.ebay = []

    def __str__(self):
        return 'Jogo: %s\nPlataforma: %s\nID: %s\n%s' % (self.name,self.platform, \
            self.gameid,'\n'.join(map(str,self.ebay)))
    def __eq__(self,game):
        if game == None:
            return False
    
        return self.name == game.name and self.platform == game.platform

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
    return_stmt = []
    try:
        print 'Buscando no GameCompare por jogo %s.' % (search)
        url = "http://www.gamecompare.com/GameCompare.asmx?WSDL"
        client = Client(url)
        print 'Iniciando busca...'
        response = client.service.Search('SourceControl', search)
        print 'Resultados da busca:'

        if response.colResults == "":
            return return_stmt

        responses = response.colResults.SearchResult

        for r in responses:
            try:
                name = r.SelectString
                str(name)
                platform = getGamePlatform(r.DisplayString)
                gameid = r.ItemID

                game = Game(name=name,platform=platform,gameid=gameid)
                
                print game
                print '------------------------'
                if not game in result:
                    result.append(game)
            except Exception as e:
               pass
        return_stmt = result     

    except WebFault as f:
        print 'WebFault'
        print f
        print f.fault
    except Exception as e:
        print 'Exception'
        print e

    print 'Fim da busca no GameCompare.'
    return return_stmt

def main():
    setup_logging()
    getGamesFromSearch('megaman',3)



if __name__=="__main__":
    main()
