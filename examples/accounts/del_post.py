if __name__ == '__main__':
    import os
    import sys

    sys.path.append(
        os.path.realpath(
            os.path.join(
                os.getcwd(), sys.argv[0], os.pardir, os.pardir, os.pardir
            )
        )
    )

from examples import config

BODY = {
    "nbgtrackid": "string",
    "payload": {
        "code": "string",
        "name": "string",
        "products": [
            "string"
        ],
        "metadata": [
            "string"
        ],
        "balance": 0.0,
        "islocked": True
    }
}

import httplib, urllib, base64, json

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': config.NBG_SECONDARY_KEY,
}

params = urllib.urlencode({
})

try:
    conn = httplib.HTTPSConnection('nbgdemo.azure-api.net')
    conn.request("POST", "/testnodeapi/api/accounts/del?%s" % params, json.dumps(BODY), headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print(e)
