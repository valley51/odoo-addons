'''
Created by auto_sdk on 2015.09.17
'''
from openerp.addons.sale_taobao.top.api.base import RestApi
class ItemsOnsaleGetRequest(RestApi):
    def __init__(self,domain='gw.api.taobao.com',port=80):
        RestApi.__init__(self,domain, port)
        self.fields = None

    def getapiname(self):
        return 'taobao.items.onsale.get'

class ItemSkusGetRequest(RestApi):
    def __init__(self,domain='gw.api.taobao.com',port=80):
        RestApi.__init__(self,domain, port)
        self.fields = None

    def getapiname(self):
        return 'taobao.item.skus.get'
