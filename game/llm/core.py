import socket
import json
import urllib.request
import urllib.error

import ssl, certifi
ctx = ssl.create_default_context(cafile=certifi.where())

BASE = "https://redhammer.api.br/tsukiyo"
URL = f"{BASE}/v1/generate"

def post(payload: dict):
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        URL,
        data=data,
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "VNClient/1.0",
            "X-VN-KEY": "tsukiyo.T3OYeSq5488vFSMi"
            },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15, context=ctx) as resp:
            body = resp.read().decode("utf-8")
            return resp.status, json.loads(body)
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="ignore")
        hdrs = dict(e.headers.items())
        try:
            return e.code, json.loads(body)
        except Exception:
            return e.code, {"raw": body[:2000], "headers": hdrs}
    except Exception as e:
        return None, {"error": str(e)}

def hasInternet(host="8.8.8.8", port=53, timeout=1):
    """
    Host: 8.8.8.8 (google-public-dns-a.google.com)
    OpenPort: 53/tcp
    Service: domain (DNS/TCP)
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error as ex:
        print(ex)
        return False
