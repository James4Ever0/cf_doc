import tornado.ioloop
import tornado.web
from wdf import termControl
import subprocess, sys, os
import signal
# password is a must here. not kidding.
# called the connection to a process.
pid = None
def getPid():
    return subprocess.Popen([sys.executable,"tserv.py"],close_fds=True).pid
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        global pid
        if pid is None:
            pass
        else:
            os.kill(pid,signal.SIGKILL)
        pid = getPid()
        self.write("resetting server on 8888\n")
    def post(self):
        # you can post things here. relay to 8888.
        sp = self.request.body
        rg = termControl(sp)
        if rg is None:
            self.write("")
        else:
            self.write(rg)
        # pass a function to the place?
    def make_app():
        return tornado.web.Application([(r".+",MainHandler),])
if __name__ == "__main__":
    pid = getPid()
    app = MainHandler.make_app()
    app.listen(9999)
    tornado.ioloop.IOLoop.current().start()
    if pid is not None:
        os.kill(pid,signal.SIGKILL)
    exit()
    # sys.exit()
    # it works.
    # how to terminate? pid?
    # p.terminate()
    # must be thread?
