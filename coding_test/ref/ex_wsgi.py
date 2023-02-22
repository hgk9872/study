from wsgiref.simple_server import make_server

def application(environ, start_response):
    name = environ["PATH_INFO"].split("/", 1)[-1] or "world"

    status = "200 OK"
    headers = [
        ("Content-Type", "text/plain; charset=utf-8"),
    ]

    start_response(status, headers)

    return [
        f"Hello {name}!".encode("utf-8"),
    ]

with make_server("", 9001, application) as httpd:
    print("Serving on port 9001 ... ")
    httpd.serve_forever()