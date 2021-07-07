""" Module of res.partner odoo model """
from ..auth import odoo 

url = 'http://52.142.63.20:1269'
db = 'fraccion_test'
username = 'WSadnet@adnetworks.cl'
password = 'WSadnet@adnetworks.cl'

class ResPartnerList():
    """Odoo model: res.partner list for customer and company"""
    
    def res_partner():
        """ list partner get """
        odoo_client = odoo.OdooClient()
        uid, models = odoo_client.logging()
        
        s_read = models.execute_kw(db, uid, password,
            'res.partner', 'search_read',
            [[['is_company', '=', True], ['customer', '=', True]]],
            {'fields': ['name', 'country_id', 'comment'], 'limit': 5})
        return s_read

