# -*- coding: utf-8 -*-

import sys
sys.path.append('../')

import logging
import traceback as tb
import suds.metrics as metrics
import httplib
import inspect
import urllib
from suds import WebFault
from suds.client import Client
from suds.plugin import MessagePlugin
from HTMLParser import HTMLParser


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

class MyHTMLParser(HTMLParser):
    def handle_starttag(self,tag,attrs):
        try:
            len(self.imgs)
        except Exception as e:
            self.imgs = []

        if tag == "img":
            for attr, value in attrs:
                if attr == "src":
                    self.imgs.append(value)
                    print value
                    
    def handl_endtag(self,tag):
        pass
    def handle_data(self,data):
        pass


def setup_logging():
    logging.basicConfig(level=loggin.INFO)
    logging.getLogger('suds.client').setLevel(logging.DEBUG)


def getGamePlatform(display_string):
    reverse = display_string[::-1]
    res = reverse[1:reverse.find('(')]
    res = res[::-1]

    return res

class MyPlugin(MessagePlugin):
    def marshalled(self,context):
        print context.envelope

def getGameImages(gamename, gameplatform='', extravalues='', num=3):
    result = []

    try:
        print 'Busca por imagem do jogo.'
        client = Client(MS_URL,plugins=[MyPlugin()])
        print 'Iniciando busca...'
        print client
#        arrayofsourcetype = client.factory.create('ArrayOfSourceType')
#        sourcetype = client.factory.create('SourceType')
#        arrayofsourcetype.SourceType = [sourcetype.Image]

#        imagerequest = client.factory.create('ImageRequest')
#        imagerequest.Offset = 0
#        imagerequest.Count = num

#        searchrequest = client.factory.create('SearchRequest')
#        searchrequest.parameters.AppId = MS_KEY
#        searchrequest.parameters.Query = gamename + ' ' + gameplatform + ' ' + extravalues
#        searchrequest.parameters.Image = imagerequest
#        searchrequest.parameters.Sources = arrayofsourcetype

#        response =  client.service.Search(searchrequest)

#        print 'Resultados da busca...'
#        print response
    except WebFault as f:
        print 'WebFault'
        print f
        print f.fault
    except Exception as e:
        print 'Exception'
        print e
        tb.print_exc()

 
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

        httpServ = httplib.HTTPConnection('www.google.com',80)
        httpServ.connect()
        for r in responses:
            name = r.SelectString
            platform = getGamePlatform(r.DisplayString)
            gameid = r.ItemID

            game = Game(name=name,platform=platform,gameid=gameid)
            print game
            query = name + '-' + platform
            query = urllib.urlencode({'q' : query})
            httpServ.request('GET','/search?sugexp=chrome,mod%3D5&'+query+'&um=1&ie=UTF-8&hl=pt-BR&tbm=isch&source=og&sa=N&tab=wi&authuser=0&ei=J6rmT5O4O42c8gS8r_WiAQ&biw=1215&bih=688&sei=KarmT9nXIq636QGO5IjgDg')
#            getGameImages(gamename=name,gameplatform=platform)
            response = httpServ.getresponse()
            if response.status == httplib.OK:
                parser = MyHTMLParser()
                parser.feed(response.read())
            else:
                print "ERROOOO"

            result.append(game)
        httpServ.close()

    except WebFault as f:
        print 'WebFault'
        print f
        print f.fault
    except Exception as e:
        print 'Exception'
        print e
#        tb.print_exc()

    return result

def main():
    getGamesFromSearch('megaman')
#    for game in getGamesFromSearch('megaman'):
#        print game



if __name__=="__main__":
    main()
