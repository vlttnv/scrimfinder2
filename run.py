from scrim2 import server
from tornado.ioloop import IOLoop

if __name__ == "__main__":
    server.listen(8080)
    IOLoop.instance().start()

