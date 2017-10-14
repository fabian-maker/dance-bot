#!/usr/bin/pythonRoot3.4

import cgi, cgitb 
from time import sleep
cgitb.enable 

RESPONSE='''Content-Type: text/html

<html>
<head>
	<title>Dance-Bot</title>
</head>
<body>
    <div style="text-align:center">
    <h1>Dance-Bot</h1>
<form action="http://192.168.178.48/cgi-bin/switch.py" method="Get">
	<input type="hidden" name ="switch" value="on"/>
	<input type="submit" value="Aufnehmen"/>
	</form>
<form action="http://192.168.178.48/cgi-bin/switch.py" method="Get">
	<input type="hidden" name ="switch" value="off"/>
	<input type="submit" value="Ueben"/>
	</form>
</body>
</html>'''

form = cgi.FieldStorage()
switch = form.getvalue('switch','off')
if switch =='on':
import #nehmen
else:
import #richtung
print(RESPONSE)	

