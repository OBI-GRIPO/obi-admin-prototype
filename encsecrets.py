#!/usr/bin/env python3
import base64
import sys
import configparser

def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode('utf8')).decode('utf8')

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode('utf8')
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

config = configparser.ConfigParser()
config.read('plain.cnf')
try:
  key = sys.argv[1]
except IndexError:
  print("Usage: encrypt.py passphrase")

print(encode(key,config['Secrets']['formio_host']),file=open("secrets/formio_host","w"))
print(encode(key,config['Secrets']['formio_admin_email']),file=open("secrets/formio_admin_email","w"))
print(encode(key,config['Secrets']['formio_admin_password']),file=open("secrets/formio_admin_password","w"))
print(encode(key,config['Secrets']['bd_vnc_password']),file=open("secrets/bd_vnc_password","w"))
print(encode(key,config['Secrets']['bd_user']),file=open("secrets/bd_user","w"))
print(encode(key,config['Secrets']['bd_email']),file=open("secrets/bd_email","w"))
print(encode(key,config['Secrets']['bd_password']),file=open("secrets/bd_password","w"))

#print(decode(key,encode(key,api_dbpassword)))
