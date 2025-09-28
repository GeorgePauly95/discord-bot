from src.glask import Glask

App = Glask()


@App.register_route("/books", methods=["GET", "POST"])
def home(request):
    response = """HTTP/1.1 200 OK\r

    GLASK"""
    return response


App.start()
