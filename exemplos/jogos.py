# This program is free software; you can redistribute it and/or modify
# it under the terms of the (LGPL) GNU Lesser General Public License as
# published by the Free Software Foundation; either version 3 of the 
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library Lesser General Public License for more details at
# ( http://www.gnu.org/licenses/lgpl.html ).
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
# written by: Jeff Ortel ( jortel@redhat.com )

import sys
sys.path.append('../')

import logging
import traceback as tb
import suds.metrics as metrics
from suds import WebFault
from suds.client import Client

errors = 0

logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.client').setLevel(logging.DEBUG)

#logging.getLogger('suds.client').setLevel(logging.DEBUG)
#logging.getLogger('suds.metrics').setLevel(logging.DEBUG)
#logging.getLogger('suds').setLevel(logging.DEBUG)


def start(url):
    global errors
    print '\n________________________________________________________________\n' 
    print 'Teste @ ( %s ) %d' % (url, errors)


def getGamePlatform(display_string):
    reverse = display_string[::-1]
    res = reverse[1:reverse.find('(')]
    res = res[::-1]

    return res

def main():
    errors = 0
    try:
        url = "http://www.gamecompare.com/GameCompare.asmx?WSDL"
        start(url)
        client = Client(url)
#        print 'CLIENTE:'
#        print client
        result = client.service.Search('SourceControl', 'megaman')
#        print '--------------------------------------------------'
#        print 'RESULTADO:'
        for title, res in result.colResults:
            for r in res:
                print 'Jogo: %s\nPlataforma: %s' % (r.SelectString,getGamePlatform(r.DisplayString))
                print '-------------------------------------------------------'

    except WebFault, f:
        errors += 1
        print f
        print f.fault
    except Exception, e:
        errors += 1
        print e
        tb.print_exc()

    print '\nFinished: errors = %d' % errors

if __name__=="__main__":
    main()
