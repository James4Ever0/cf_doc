# remember or get some code.
import itertools
import tornado.web
import tornado.ioloop

arr=[]
def mix_and_eval(*args):
    for x in itertools.permutations(args):
        try:
            print(eval("".join(x)))
            print("success",x)
        except:
            print("error",x)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        global arr
        arr =[]
        self.write("purging the database.")
    def post(self):
        global arr
        sp = self.request.body
        arr.append(sp.decode())
        mix_and_eval(*arr)
        self.write("data received.")
    def make_app():
        return tornado.web.Application([(r".+",MainHandler),])

if __name__ == "__main__":
    app=MainHandler.make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

