# Test Application to be used with gunicorn http server to validate the setup!
# TODO - need to come back and finish off installing gunicorn to be able to test this app
# Ref link - http://gunicorn.org/#quickstart

def app(environ, start_response):
    data = b"Hello, World!\n"
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])
