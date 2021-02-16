def mainPage():
    with open('templates/main_page.html') as template:
        return template.read()


def secondPage():
    with open('templates/second_page.html') as template:
        return template.read()
