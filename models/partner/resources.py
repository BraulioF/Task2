""" Module of res.partner odoo model """

import xmlrpc.client

url = 'http://52.142.63.20:1269'
db = 'fraccion_test'
username = 'WSadnet@adnetworks.cl'
password = 'WSadnet@adnetworks.cl'

class OdooClient():

   
    def __init__(self):
        self.url = url
        self.db = db
        self.username = username
        self.password = password
  


    def logging(self):
        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
        common.version()
        uid = common.authenticate(db, username, password, {})
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
        return uid, models


class ResPartnerList():
    """Odoo model: res.partner list for customer and company"""
    
    def res_partner():
        """ list partner get """
        odoo_client = OdooClient()
        uid, models = odoo_client.logging()
        #models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
        s_read = models.execute_kw(db, uid, password,
            'res.partner', 'search_read',
            [[['is_company', '=', True], ['customer', '=', True]]],
            {'fields': ['name', 'country_id', 'comment'], 'limit': 5})
        return s_read

