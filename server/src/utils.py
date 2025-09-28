def splitter(word, delimiter):
    return word.split(delimiter)


def not_found(request):
    return """HTTP/1.1 404 Unauthorized\r

    not_found"""
