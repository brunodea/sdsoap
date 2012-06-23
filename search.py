# -*- coding: utf-8 -*-

import sys
sys.path.append('../')

import logging
import traceback as tb
import suds.metrics as metrics
from suds import WebFault
from suds.client import Client


class Game(object):
    def __init__(self,name='',platform='',price=0):
        self.name = name
        self.platform = platform
        self.price = price

    def __str__(self):
        return 'Jogo: %s\nPlataforma: %s\nPreco: %d\n' % (self.name,self.platform,self.price)



def setup_logging():
    logging.basicConfig(level=loggin.INFO)
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
        print 'Criando cliente...'
        client = Client(url)
        print 'Iniciando busca...'
        response = client.service.Search('SourceControl', search)
        print 'Resultados da busca:'
        responses = response.colResults.SearchResult
        for r in responses:
            name = r.SelectString
            platform = getGamePlatform(r.DisplayString)

            result.append(Game(name=name,platform=platform))

    except WebFault as f:
        print f
        print f.fault
    except Exception as e:
        print e
        tb.print_exc()

    return result

def main():
    for game in getGamesFromSearch('megaman'):
        print game



if __name__=="__main__":
    main()
