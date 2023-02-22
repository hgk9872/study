
async def application(scope, receive, send):
    name = scope["path"].split("/", 1)[-1] or "world"

    await send({
        "type": "http.response.start",
        "status": 200,
        "headers": [
            [b"Content-Type", b"text/plain"],
        ],
    })

    await send({
        "type": "http.response.body",
        "body": f"Hello, {name}!".encode("utf8"),
        "more_body": False,
    })