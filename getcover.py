import urllib
import re

def downloadcover (id_,path):
    #build de url
    url='http://www.gamecompare.com/product.aspx?productid='+id_
    #print url
    #open the link
    f = urllib.urlopen(url)
    #get url of the cover
    urlcover = re.search('<div class="productimage"><img src=\"(.*?)\" alt=', f.read()).group(1)
    #downlaod de cover
    print 'Baixando Capa do Jogo: ' + urlcover
    
    urlsplitted = urlcover.split('.')
    extension = urlsplitted[len(urlsplitted)-1]
    if extension == '.gif':
        return None
    
    path = path + '.' + extension

    urllib.urlretrieve(urlcover, path)
    
    return path
