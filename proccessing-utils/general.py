import base64
import mimetypes
from pathlib import Path
from typing import Dict
import requests

# local
import encryptor


def to_binary(x: str | Dict) -> bytes:
    """Converts a base64 string or dictionary to a binary string that can be sent in a POST."""
    if isinstance(x, dict):
        if x.get("data"):
            base64str = x["data"]
        else:
            base64str = encode_url_or_file_to_base64(x["name"])
    else:
        base64str = x
    return base64.b64decode(base64str.split(",")[1])



def encode_url_or_file_to_base64(path: str | Path, encryption_key: bytes | None = None):
    if validate_url(str(path)):
        return encode_url_to_base64(str(path), encryption_key=encryption_key)
    else:
        return encode_file_to_base64(str(path), encryption_key=encryption_key)
    


def validate_url(possible_url: str) -> bool:
    headers = {"User-Agent": ""}
    try:
        head_request = requests.head(possible_url, headers=headers)
        if head_request.status_code == 405:
            return requests.get(possible_url, headers=headers).ok
        return head_request.ok
    except Exception:
        return False
    

def encode_url_to_base64(url, encryption_key=None):
    encoded_string = base64.b64encode(requests.get(url).content)
    if encryption_key:
        encoded_string = encryptor.decrypt(encryption_key, encoded_string)
    base64_str = str(encoded_string, "utf-8")
    mimetype = get_mimetype(url)
    return (
        "data:" + (mimetype if mimetype is not None else "") + ";base64," + base64_str
    )


def encode_file_to_base64(f, encryption_key=None):
    with open(f, "rb") as file:
        encoded_string = base64.b64encode(file.read())
        if encryption_key:
            encoded_string = encryptor.decrypt(encryption_key, encoded_string)
        base64_str = str(encoded_string, "utf-8")
        mimetype = get_mimetype(f)
        return (
            "data:"
            + (mimetype if mimetype is not None else "")
            + ";base64,"
            + base64_str
        )
    

def get_mimetype(filename: str) -> str | None:
    mimetype = mimetypes.guess_type(filename)[0]
    if mimetype is not None:
        mimetype = mimetype.replace("x-wav", "wav").replace("x-flac", "flac")
    return mimetype