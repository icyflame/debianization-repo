##File number 4
##
##This file consists of the two main functions that will help to encrypt
##and decrypt the data at the start and at the end of the program.
##
##This is a part of the program in Python Tkinter
##
##created on 20th May, 2013

from Crypto.Cipher import *

global encryptor
global decryptor

key1 = 'developedbysiddharthkannan'

al = []
als = []

def decryptAll():

    filin = open('viper','r')
    filout = open('temp','w')    

    i = filin.read()

    if not i == '':  ##only if the file is not empty

        import json

        decrypted = ARC4.new(key1).decrypt(i)

        jsonDecoded = json.loads(decrypted)

        for i in jsonDecoded.keys():

            filout.write(jsonDecoded[i])

    filin.close()

    filout.close()

    import os
    os.remove('viper')
    os.rename('temp','viper')

    return True

def encryptAll():
    
    filin = open('viper','r')
    filout = open('temp','w')

    import json

    data = filin.readlines()

    if not data == []:  ##only if the file is not empty

        dicts = {}

        for i in range(len(data)):

            dicts[i] = data[i]

        jsonCoded = json.dumps(dicts)

        encrypted = ARC4.new(key1).encrypt(jsonCoded)

        filout.write(encrypted)

    filin.close()

    filout.close()

    import os
    os.remove('viper')
    os.rename('temp','viper')

    return True
