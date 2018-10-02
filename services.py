import urllib.request, urllib.parse, urllib.error
import json
import requests 

url = 'https://young-inlet-20837.herokuapp.com/api/notes'


def getAll():
	uh = urllib.request.urlopen(url)
	data = uh.read().decode()
	try:
		js = json.loads(data)
	except:
		js = None

	return js

  
def saveNote(data):
	req = urllib.request.Request(url)
	req.add_header('Content-Type', 'application/json; charset=utf-8')
	jsondata = json.dumps(data)
	jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
	req.add_header('Content-Length', len(jsondataasbytes))
	response = urllib.request.urlopen(req, jsondataasbytes)
	return response.read()

def deleteNote(id):
	url_ = url+ "/" + id;
	r = requests.delete(url_)
	return r.text