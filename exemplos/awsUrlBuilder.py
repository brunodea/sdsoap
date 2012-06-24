0import urllib2

def amazon_test_url():
    import base64, hashlib, hmac, time
    from urllib import urlencode, quote_plus

    AWS_ACCESS_KEY_ID = 'ACCESS_KEY_DO_DAVI'
    AWS_SECRET_ACCESS_KEY = 'SECRET_ACCESS_KEY_DO_DAVI'  
    TEST_ISBN = '9780735619678' #http://stackoverflow.com/questions/1711/what-is-the-single-most-influential-book-every-programmer-should-read

    base_url = "http://webservices.amazon.com/onca/xml"
    url_params = dict(
        Service='AWSECommerceService', 
        Operation='ItemLookup', 
        IdType='ISBN', 
        ItemId=TEST_ISBN,
        SearchIndex='Books',
        AWSAccessKeyId=AWS_ACCESS_KEY_ID,  
        ResponseGroup='Images,ItemAttributes,EditorialReview,SalesRank')

    #Can add Version='2009-01-06'. What is it BTW? API version?


    # Add a ISO 8601 compliant timestamp (in GMT)
    url_params['Timestamp'] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

    # Sort the URL parameters by key
    keys = url_params.keys()
    keys.sort()
    # Get the values in the same order of the sorted keys
    values = map(url_params.get, keys)

    # Reconstruct the URL parameters and encode them
    url_string = urlencode(zip(keys,values))

    #Construct the string to sign
    string_to_sign = "GET\necs.amazonaws.com\n/onca/xml\n%s" % url_string

    # Sign the request
    signature = hmac.new(
        key=AWS_SECRET_ACCESS_KEY,
        msg=string_to_sign,
        digestmod=hashlib.sha256).digest()

    # Base64 encode the signature
    signature = base64.encodestring(signature).strip()

    # Make the signature URL safe
    urlencoded_signature = quote_plus(signature)
    url_string += "&Signature=%s" % urlencoded_signature

    print "%s?%s\n\n%s\n\n%s" % (base_url, url_string, urlencoded_signature, signature)
    #urllib2.urlopen("http://www.google.com")

amazon_test_url()