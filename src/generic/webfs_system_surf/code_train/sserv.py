# hello_server.py
import tornado.ioloop
import tornado.web
# glue it up? use stdin.
# or worse?
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
    def post(self):
        sp=self.request.body
#        sp=self.get_argument("data","no data received")
        print("posted data",sp)
        self.write('normal post received.')
# whatever. just try to build something different.
    def make_app():
        return tornado.web.Application([ (r".+", MainHandler), ])  # URL Mapping

if __name__ == "__main__":
    app = MainHandler.make_app()
    app.listen(8888)    # Port Number
    tornado.ioloop.IOLoop.current().start()
# -> twisted.
