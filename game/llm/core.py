import json
import urllib.request
import urllib.error

import ssl, certifi
ctx = ssl.create_default_context(cafile=certifi.where())

BASE = "https://vns-generate.andreyfernandes1361.workers.dev"
URL = f"{BASE}/v1/generate"

def post(payload: dict):
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        URL,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15, context=ctx) as resp:
            body = resp.read().decode("utf-8")
            return resp.status, json.loads(body)
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="ignore")
        try:
            return e.code, json.loads(body)
        except Exception:
            return e.code, {"raw": body}
    except Exception as e:
        return None, {"error": str(e)}
