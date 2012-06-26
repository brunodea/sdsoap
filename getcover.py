import urllib
import re

#id is provided by the web service
id='1859458'
#build de url
url='http://www.gamecompare.com/product.aspx?productid='+id
print url
#open the link
f = urllib.urlopen(url)
#get url of the cover
urlcover = re.search('<div class="productimage"><img src=\"(.*?)\" alt=', f.read()).group(1)
#downlaod de cover
print 'Downloading: ' + urlcover
urllib.urlretrieve(urlcover, "00000002.jpg")