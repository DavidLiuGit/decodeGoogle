"""
Very simple HTTP server in python.
Usage::
	./dummy-web-server.py [<port>]
Send a GET request::
	curl http://localhost
Send a HEAD request::
	curl -I http://localhost
Send a POST request::
	curl -d "foo=bar&bin=baz" http://localhost
"""
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
from decode_nlp import analyze
from graph import getGraph
from jokeFinder import findJoke

class S(BaseHTTPRequestHandler):
	def _set_headers(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()

	def do_GET(self):
		self._set_headers()
		self.wfile.write("<html><body><h1>hi!</h1></body></html>")

	def do_HEAD(self):
		self._set_headers()

	def do_OPTIONS(self):
		self.send_response(200, "ok")
		self.send_header('Access-Control-Allow-Origin', self.headers.dict['origin'])
		self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
		self.send_header('Access-Control-Allow-Headers', 'Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With')

	def do_POST(self):
		# Doesn't do anything with posted data
		content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
		post_data = self.rfile.read(content_length) # <--- Gets the data itself

		#Analyze sentence to get key words and sentiment
		nlp_output = analyze(post_data) # format: {'text': '', 'sentiment': 0, 'entities':[]}

		#Testing
		print(nlp_output)


		#Analyze keywords with knowledge graph
		graph = getGraph(nlp_output['entities'], 5)

		#print("Graph")
		#print(graph)

		#Search joke database for joke
		#TODO
		joke = findJoke(nlp_output['entities'])
		
		#Write response

		#self._set_headers()
		#self.response.out.write(graph)
		self.send_header('Content-type', 'text/html')
		self.send_response(200,{"graph":graph,"sentiment":nlp_output['sentiment'],"joke":joke})
		#self.wfile.write("<html><body><h1>POST!</h1></body></html>")
		#self.wfile.write("<html><body><h1>POST!"+str(nlp_output)+"</h1></body></html>")
		self.end_headers
		
		
def run(server_class=HTTPServer, handler_class=S, port=80):
	server_address = ('', port)
	httpd = server_class(server_address, handler_class)
	print 'Starting httpd...'
	httpd.serve_forever()

if __name__ == "__main__":
	from sys import argv

	if len(argv) == 2:
		run(port=int(argv[1]))
	else:
		run()
