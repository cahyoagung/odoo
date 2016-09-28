import openerp.http as http
from openerp.http import request

class HelmigsController(http.Controller):

    @http.route('/my_url/some_html', type="http")
    def some_html(self):
        return "<h1>This is a test</h1>"

    @http.route('/my_url/some_json', type="json")
    def some_json(self):
        return {"sample_dictionary": "This is a sample JSON dictionary"}
