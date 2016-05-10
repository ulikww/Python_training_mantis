

class ProjectHelper:
    def __init__(self,app):
        self.app = app

    def add_project(self, project):
        wd = self.app.wd
        self.transition_contact_page()
        wd.find_element_by_xpath("//table[3]/tbody/tr[1]/td/form/input[2]").click()
        self.change_field_value_project("name", project.name)
        wd.find_element_by_css_selector("input.button").click()

    def del_project(self, project):
        wd = self.app.wd
        wd.transition_contact_page(self)
        wd.find_element_by_xpath("//table[3]/tbody/tr[1]/td/form/input[2]").click()
        self.change_field_value_project("name", project.name)
        wd.find_element_by_css_selector("input.button").click()

    def change_field_value_project(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def transition_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()