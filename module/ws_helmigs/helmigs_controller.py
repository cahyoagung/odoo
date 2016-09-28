import openerp.http as http
from openerp.http import request
from openerp.http import Response
import werkzeug

class HelmigsController(http.Controller):

    @http.route('/my_url/some_html', type="http")
    def some_html(self):
        return "<h1>This is a test</h1>"

    @http.route('/my_url/some_json', type="json", auth='none', methods=['GET','POST'], website=True)
    def some_json(self):
        return {"sample_dictionary": "This is a sample JSON dictionary"}


class MyController(http.Controller):
    @http.route('custom/myjson', type='json', auth='none', methods=['GET','POST'], website=True)
    def myjson(self):
        return {"data":"cahyo agung prastio"}