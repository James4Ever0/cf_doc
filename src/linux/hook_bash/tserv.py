from twisted.internet import protocol, reactor
import time
import tornado.ioloop
import tornado.web
import pickle
#from process_tool import getSingleSession as gss
# import sys
# import multiprocessing
import threading
# password is a must here. not kidding.
# called the connection to a process.
class MyPP(protocol.ProcessProtocol):
    def __init__(self):
        self.db=[]

    def gen(self,a,b):
        return {'time':time.time(),'fd':a,'data':b}

    def connectionMade(self):
        print('connection made!')

    def write(self, a):
        self.db.append(self.gen(0,a))
        self.transport.write(a)

    def processExited(self, reason):
        print("processExited, status %s" % (reason.value.exitCode,))

    def outReceived(self, data):
        self.db.append(self.gen(1,data))

    def errReceived(self, data):
        self.db.append(self.gen(2,data))
# you are going to serve at a different port?
if __name__ == "__main__":
    # multiprocessing.freeze_support()
    # while mainthread is alive... -> do the thing.
    pp = MyPP()
    # command = ['screen', '-x']
    command = ['bash']
    # does this work in WINDOWS?
    def theFunc(a):
        a.run()
    reactor.spawnProcess(pp, command[0], command, {'TERM': 'xterm'}, usePTY=True)
    # print("{MIDDLE}")
    p =threading.Thread(target=theFunc,args=(reactor,))
    p.setDaemon(True) # the whole shit.
    # print("{AHEAD}")
    # start after the set.
    # somehow.
    # all dead here. not even better than JS.
    p.start() # not RUN!
    # what the heck?
    # with TIMESTAMP.
    # print("{OF}")
    pp.write(b"parrot\n")
    time.sleep(0.1)
    # not working here.
    class MainHandler(tornado.web.RequestHandler):
        def get(self):
            self.write("hello world\n")
        def post(self):
            sp = self.request.body
            pp.write(sp+b"\n")
            time.sleep(0.1)
            self.write(pickle.dumps(pp.db))
            pp.db=[]
            # pass a function to the place?
        def make_app():
            return tornado.web.Application([(r".+",MainHandler),])
    app = MainHandler.make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
    # sys.exit()
    exit()
    # it works.
    # how to terminate? pid?
    # p.terminate()
    # must be thread?
