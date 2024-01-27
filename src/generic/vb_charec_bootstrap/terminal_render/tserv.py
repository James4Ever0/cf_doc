from twisted.internet import protocol, reactor
import time
import tornado.ioloop
import tornado.web
#from process_tool import getSingleSession as gss
# import sys
# import multiprocessing
# password is a must here. not kidding.
# called the connection to a process.
content = open("demo.cast","r").read()
altered = open("demo_altered.cast","r").read()
if __name__ == "__main__":
    # not working here.
    # do we need a callback here?
    class RHandler(tornado.web.RequestHandler):
        def get(self):
            global content, altered
            content = altered
            self.write("content changed!\n")
    class MainHandler(tornado.web.RequestHandler):
        def get(self):
            global content
            self.write(content)
        def make_app():
            return tornado.web.Application([(r"/demo.cast",MainHandler),(r"/refresh",RHandler)])
    app = MainHandler.make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
    # sys.exit()
    exit()
    # it works.
    # how to terminate? pid?
    # p.terminate()
    # must be thread?
