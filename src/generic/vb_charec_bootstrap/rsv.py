# hello_server.py
import tornado.ioloop
import tornado.web
# use a separate thread to check redis content.
import threading, time
from or_func import trusty
# what is that trusty?
min_d = 0.5
glob_buf = []
lastcall = None
glob_lock = False
# find same things?
def recipe():
#    lock[0] = True
    global glob_buf
#    global glob_lock
#    glob_buf.append("random")
#    if not glob_lock:
#        print("not locking!")
#        glob_lock = True
    a,b = trusty((25,80))
#    print(a,b)
    if a is not None:
        if b is not None:
            glob_buf.append((a,b))
#        glob_lock = False
    else:
        print("locking!")
#    lock[0] = False

def lg():
    while True:
        time.sleep(1)
        print(len(glob_buf),[type(x) for x in glob_buf])

class RecipeHandler(tornado.web.RequestHandler):      
    def get(self):
        self.write("recipe here!")

class R(tornado.web.RequestHandler):      
    def get(self):
        global lastcall
        global glob_lock
        self.write("calculation!")
        diff = None
        # how do you start another thread?
        tx = time.time()
        if lastcall is None:
            diff = 0.6
#            lastcall = time.time()
        else:
            diff = tx - lastcall
        lastcall = tx
        if diff > min_d:
            print("not blocking!",diff)
            if not glob_lock:
                print("not locking!")
                glob_lock = True
                recipe()
            # must be this prooblem. only one thread here?
#                t = threading.Thread(target=recipe , args=())
#                t.setDaemon(True)
#                t.start()
                glob_lock = False
            else:
                print("locking!")
        else:
            print("blocking!",diff)
            # error will not block this thing, or will it block?
        # you can blow things up?
        # some calculation here.

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
    def make_app():
        return tornado.web.Application([(r"/r",R),(r"/recipe", RecipeHandler), (r".+", MainHandler), ])  # URL Mapping
if __name__ == "__main__":
    tx = threading.Thread(target=lg , args=())
    tx.setDaemon(True)
    tx.start()
    app = MainHandler.make_app()
    app.listen(8888)    # Port Number
    tornado.ioloop.IOLoop.current().start()
