import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    def img(name):
        return f"""
    <h2>{name}<h2>
    <img src="/api/Render?name={name}" style="width:80%"> </img>
        """

    output = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="utf-8">
    <title>title</title>
    <link rel="stylesheet" href="style.css">
    <script src="script.js"></script>
    </head>
    <body>
    Code on <a href='https://github.com/idvorkin/render-matplotlib'> github</a>
    """

    for name in "productivity,what-to-work-on,not-valid,career-convo".split(","):
        output += img(name)

    output += """
    </body>
    </html>
    """
    return func.HttpResponse(output, mimetype="text/html")
