# Standard python libraries
import os
import json
import base64
import sqlite3
import shutil

# Need to install ( pypiwin32 )
import win32crypt

# Need to install ( pycryptodomex )
from Cryptodome.Cipher import AES

file_path = os.environ["USERPROFILE"] + r"\AppData\Local\Google\Chrome\User Data\Local State"
with open(file_path, "r", encoding="utf-8") as f:
    js_data = f.read()
    py_data = json.loads(js_data)
print(py_data["os_crypt"]["encrypted_key"])
