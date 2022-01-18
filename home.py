from flask import Flask , url_for, render_template,request

key=4
app = Flask(__name__)


@app.route('/encipher',methods=["POST"])
def encipher():
	message= request.form["encipher"]
	encryptedmessage="";
	for i in message:
		value= (ord(i)-ord(' ')+key)%95+ord(' ')
		ch= chr(value)
		encryptedmessage+=ch
	return render_template("base.html",emessage= encryptedmessage)


@app.route('/decipher',methods=["POST"])
def decihper():
	message= request.form["decipher"]
	decryptedmesage=""
	for i in message:
		value= (ord(i)- ord(' ')-key)%(95)+ord(' ')
		ch= chr(value)
		decryptedmesage+=ch
	return render_template("base.html",dmessage=decryptedmesage)


@app.route("/",methods=["GET"])
def home():
	return render_template("base.html")

if __name__ == "__main__": 
	
	app.run()
