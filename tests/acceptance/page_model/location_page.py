from tests.acceptance.page_model.base_page import BasePage


class LocationPage(BasePage):
    @property
    def url(self):
        return super(LocationPage, self).url + '/directory/places/'
