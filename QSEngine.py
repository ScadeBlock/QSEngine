## QSEngine - A secure engine for making website
## QSEngine 1.0.0 by OWSoft
from flask import Flask,url_for,jsonify,request
from flask_cors import CORS, cross_origin
from threading import Thread
import sys,string,random
## Init value
availble = []
script = {}
## Support Function
def random_id(number = 10):
	ran = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k = number))	
	return ran
if len(sys.argv) == 1:
	print("""QSEngine 1.0.0
-- Using qs [filename] [arg]""")
	sys.exit()
f = open(sys.argv[1],"r")
data = f.read()
f.close()
data = data.split(";")
clear_data = []
for i in data:
	i = i.replace(r"\n","")
	clear_data.append(i)
class QSEngine():
	def __init__(self):
		self.app = Flask(__name__)
		self.app.config['TEMPLATES_AUTO_RELOAD'] = True # Auto reload template
		CORS(self.app)
	def initapp(self):
		@self.app.route("/")
		def main():
			return """<script type="text/javascript">
	original_url = window.location.origin;
	fetch(original_url+"/canvasroute")
	  .then(response => response.json())
	  .then(data => location.href = original_url+"/canvasimg?id="+data["result"]);
	</script>"""
		@self.app.route("/canvasroute")
		def idgre():
			rv = str(random_id())
			availble.append(rv)
			exec("machine"+rv+"=Machine(\""+rv+"\")", globals())
			return jsonify({"result":rv})
		@self.app.route("/click")
		def clickthat():
			index = request.args.get('id')
			x = request.args.get('x')
			y = request.args.get('y')
			exec(f"machine{index}.click({x},{y})", globals())
			return jsonify({"result":"compelete!"})
		@self.app.route("/canvasimg")
		def canvasl():
			index = request.args.get('id')
			if not index in availble:
				return jsonify({"result":"this id not found in server"})
			exec(f"""machine{index}.first_load()""")
			return """<script type="text/javascript">
function updateframe() {
	document.getElementById('src').src = document.getElementById('src').src + "?" + new Date().getTime();
}	
function printMousePos(event) {
	original_url = window.location.origin;
	var x = event.clientX;
	var y = event.clientY;
	var url = new URL(window.location.href);
	var idex = url.searchParams.get("id");
	fetch(original_url+"/click?id="+idex+"&x="+x+"&y="+y)
}

document.addEventListener("click", printMousePos);
setInterval(updateframe, """+self.second+""");
</script>
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title></title>
	<style>
	*{
		margin: 0;
	}
	</style>
</head>
<body>
<img src="./static/"""+index+""".jpg" style="width:100%;height:100%" draggable="false" id="src">
</body>
</html>
"""
	def set_time(self,second):
		self.second = second
	def run(self):
		import logging
		logging.basicConfig(filename='error.log',level=logging.DEBUG)
		self.app.run()

for i in clear_data:
	i = str(i) 
	if len(i) == 0:
		pass
	else:
		if i[0] == "\n":
			i = i[1:]
		if i[0] == "@":
			i = i[1:]
			i = i.split(".")
			i[0] = i[0].lower()
			if i[0] == "qs":
				if ":" in i[1]:
					rcdata = i[1].split(":")
				else:
					rcdata = [i[1]]
				if rcdata[0] == "init":
					gc = QSEngine()
				elif rcdata[0] == "initdata":
					gc.initapp()
				elif rcdata[0] == "run":
					gc.run()
				elif rcdata[0] == "setscreenupt":
					gc.set_time(rcdata[1])
				else:
					print("ERROR: No function found")
			elif i[0] == "machine":
				rcdata = i[1].split(":")
				if rcdata[0] == "load":
					dataval = script[rcdata[1]]
					exec(dataval, globals())
			elif i[0] == "script":
				rcdata = i[1].split(":")
				if rcdata[0] == "add":
					f = open(rcdata[1]+".py","r")
					dataval = f.read()
					f.close()
					script[rcdata[1]] = dataval
				elif rcdata[0] == "load":
					def rn():
						exec(script[rcdata[1]])
					Thread(target=rn).start()

		elif i[0] == "/" and i[1] == "/":
			pass