import os
from flask import Flask,render_template,request,redirect,url_for
import re

app = Flask(__name__) #initialize the app

@app.route("/output")
def give_out(file_path = "code.txt"):
	# function for running the txt file as python and returning output
	command = f'python {file_path}'
	output = os.popen(command)
	output = output.read()
	output = re.sub("\n",r"<br>",output)

	return output

@app.route("/",methods=["POST","GET"])
def add_code():
	#in browser text input
	if request.method == "POST":
		entered = request.form["code"]
		with open('code.txt','w') as f:
			f.write(entered)
		return redirect(url_for("give_out"))
	return render_template("code_input.html")



if __name__ == "__main__":
	app.run(debug=True)