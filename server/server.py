from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application, url
from tornado.websocket import WebSocketHandler

class HelloHandler(RequestHandler):
    def get(self):
        self.write("Hello, world")

class TestSockeet(WebSocketHandler):
    def open(self):
        print("OPEN")

    def on_message(self, message):
        self.write_message("Received: " + message)
        print message

    def on_close(self):
        print "CLOSED"

    def check_origin(self, origin):
        """Check that the request comes from my site

        """
        return True

def make_app():
    return Application([
        url(r"/websocket/", TestSockeet),
        ], debug=True)

if __name__=="__main__":
    app = make_app()
    app.listen(8080)
    IOLoop.current().start()

