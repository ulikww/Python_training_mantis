from model.project import Project_designer


def test_login(app):
    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")

def test_add_project(app):
    app.project.add_project(Project_designer(name="ПРОЕКТ №1"))

