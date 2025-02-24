# wandbox_client.py
import requests

def compile_and_run(code, stdin, compiler="gcc-13.2.0-c", options="-march=native -std=c11 -O2", timeout=20):
    """
    Wandbox の API を利用して C言語のソースコードをコンパイル・実行する。
    """
    url = "https://wandbox.org/api/compile.json"
    payload = {
        "code": code,
        "compiler": compiler,
        "options": options,
        "stdin": stdin,
    }
    try:
        response = requests.post(url, json=payload, timeout=timeout)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"HTTP error: {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}