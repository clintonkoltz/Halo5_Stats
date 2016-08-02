import httplib, urllib, base64
apikey = "2336650f744d485481c99a91b6d0c7b5"

headers = {
            # Request headers
                'Ocp-Apim-Subscription-Key': apikey ,
                }

params = urllib.urlencode({})

try:
    conn = httplib.HTTPSConnection('www.haloapi.com')
    conn.request("GET", "/metadata/h5/metadata/game-base-variants?%s" %
            params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    data
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

