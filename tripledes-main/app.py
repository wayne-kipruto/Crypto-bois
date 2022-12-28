
from urllib import request
from tripledes import *

from flask import *
from sendmail import *
from sendsms import *
import secrets
#5429f62ca494b8724c910e26c4498688245e4f6db4d3f75c

app = Flask(__name__)

iv = '2132435465768797'
key = secrets.token_hex(24)

@app.route('/', methods=['POST', 'GET'])
def home():
    return "<h1>Hello, you are at the home page!</h1>"

@app.route('/encrypt', methods=['POST', 'GET'])
def do_encrypt():
    if request.method == 'POST':

        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        phoneNo = request.form.get('phoneNo')
        cipher_text=encrypt(iv,key,message)
        print(cipher_text)
        print(key)
        cipher_string = cipher_text.decode("utf-8")
        # raw_cipher_string = fr'{cipher_string}\n'
        
        mail_send(email,cipher_string)
        send_sms(key,phoneNo) 
        
    return render_template("encrypt.html")
@app.route('/decrypt', methods=['POST','GET'])
def do_decrypt():
    
    keygain = request.form.get('key')
    ciphermessage = request.form.get('ciphermessage')
    final_plain_text = 'No text to display yet'
    if ciphermessage != None:
         finalciphermessage, _ = codecs.escape_decode(ciphermessage, 'hex')
         plaintext = decrypt(iv,keygain,finalciphermessage)
        
         final_plain_text = plaintext.decode("utf-8")

    return render_template("decrypt.html", final_plain_text=final_plain_text)


   



if __name__ == '__main__':
 app.run(debug=True)


