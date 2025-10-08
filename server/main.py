from src.glask import Glask

App = Glask()


@App.register_route("/books", methods=["POST", "GET", "PUT"])
def home(request):
    return "George's FLASK", 200, {"Server": "Glask"}

@App.register_route("/journals", methods=["GET"])
def home(request):
    return "FLASK", 200, {"Server": "Jlask"}
App.start()
