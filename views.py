def index():
    """ HTML-view to be displayed as a user request to "/" route """
    with open('templates/index.html') as template:
        return template.read()


def post():
    """ HTML-view to be displayed as a user request to "/blog" route """
    with open('templates/post.html') as template:
        return template.read()
