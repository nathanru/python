import tornado.ioloop
import tornado.web

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(f"Served Successfully from Ubuntu-WSL.")
        self.set_header("Access-Control-Allow-Origin",
        "https://myfreetesting.xyz")
    def options(self):
        self.set_header("Access-Control-Allow-Origin",
        "https://myfreetesting.xyz")
        self.set_header("Access-Control-Allow-Headers",
        "Content-Type")
        self.set_status(204)
        self.finish()

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", basicRequestHandler),
    ])


    port = 8080
    app.listen(port)
    print(f"Application is ready and running on port {port} on the Ubuntu server")
    tornado.ioloop.IOLoop.current().start()
