import binascii
import base64
import pyDes
import secrets
import codecs

#IV has to be 8bit long
iv = '2132435465768797'
#Key has to be 24bit long
# key = '000000000000000000000000000000000000000000000000'
#here is the data you want to encrypt
key = secrets.token_hex(24)
data = "Andrew is a weird bastard"

def encrypt(iv, key, data):
    iv = binascii.unhexlify(iv)
    key = binascii.unhexlify(key)
    k = pyDes.triple_des(key, pyDes.CBC, iv, pad=None, padmode=pyDes.PAD_PKCS5)
    d = k.encrypt(data)
    d = base64.encodebytes(d)
    return d
    
def decrypt(iv, key, data):
    iv = binascii.unhexlify(iv)
    key = binascii.unhexlify(key)
    k = pyDes.triple_des(key, pyDes.CBC, iv, pad=None, padmode=pyDes.PAD_PKCS5)
    data = base64.decodebytes(data)
    d = k.decrypt(data)
    return d

if __name__ == '__main__':
    print ("Plan Text: %s" % data)
    encryptdata = encrypt(iv, key, data)
    print("Encrypted Text: %s" % encryptdata)
    decryptdata = decrypt(iv, key, encryptdata)
    print ("Plan Text: %s" % decryptdata)
    print(key)
    print("//////////////////////////////////////////////////")
    testkey = input("Enter your key:")
    testinput = input("Enter ciphertext:")
    ciphermessage, _ = codecs.escape_decode(testinput, 'hex')
    print(ciphermessage)
    print(type(ciphermessage))
    
    # finalhard=(bytes(testinput, "utf-8", "base64.urlsafe_b64encode"))
    # data_bytes, _ = codecs.escape_decode(data, 'hex')
    # print(finalhard)
    
    print("IT IS FUCKING CORRECT")
    print(decrypt(iv,testkey,ciphermessage))

    