# hello_server.py
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
# whatever. just try to build something different.
    def make_app():
        return tornado.web.Application([ (r".+", MainHandler), ])  # URL Mapping

if __name__ == "__main__":
    app = MainHandler.make_app()
    app.listen(8888)    # Port Number
    tornado.ioloop.IOLoop.current().start()
# -> twisted.
