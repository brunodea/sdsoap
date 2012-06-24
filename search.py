# -*- coding: utf-8 -*-

import sys
sys.path.append('../')

import logging
import traceback as tb
import suds.metrics as metrics
import httplib
import inspect
from suds import WebFault
from suds.client import Client

MS_URL = 'http://api.bing.net/search.wsdl'
MS_KEY = 'PsC095DMrg/uXAzzXZxJUTUo5Iuov92f2RbW/7fazlc='

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
    logging.basicConfig(level=loggin.INFO)
    logging.getLogger('suds.client').setLevel(logging.DEBUG)


def getGamePlatform(display_string):
    reverse = display_string[::-1]
    res = reverse[1:reverse.find('(')]
    res = res[::-1]

    return res

def getGameImages(gamename, gameplatform='', extravalues='', num=3):
    result = []

    try:
        print 'Busca por imagem do jogo.'
        client = Client(MS_URL)
        print 'Iniciando busca...'
        searchrequest = client.factory.create('SearchRequest')
        print 'SearchRequest'
        searchrequest.parameters.AppId = MS_KEY
        searchrequest.parameters.Query = gamename + ' ' + gameplatform + ' ' + extravalues

        arrayofsourcetype = client.factory.create('ArrayOfSourceType')
        sourcetype = client.factory.create('SourceType')
        arrayofsourcetype.SourceType = sourcetype.Image

        searchrequest.parameters.Sources = arrayofsourcetype
        
        imagerequest = client.factory.create('ImageRequest')
        imagerequest.Offset = 0
        imagerequest.Count = num
 
        strings = client.factory.create('ArrayOfString')
        strings.string = []
        imagerequest.Filters = client

        searchrequest.parameters.Image = imagerequest

        print searchrequest
        response =  client.service.Search(searchrequest)

        print 'Resultados da busca...'
        print response
    except WebFault as f:
        print 'WebFault'
        print f
        print f.fault
    except Exception as e:
        print 'Exception'
        print e
#        tb.print_exc()

 
    return result

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
            name = r.SelectString
            platform = getGamePlatform(r.DisplayString)
            gameid = r.ItemID

            result.append(Game(name=name,platform=platform,gameid=gameid))
            getGameImages(gamename=name,gameplatform=platform)


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
