from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param hits: {"description": "Number of times the site was selected", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.hits = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Site(A10BaseClass):
    
    """Class Description::
    Statistics for the object site.

    Class site supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ip_server_list: {"minItems": 1, "items": {"type": "ip-server"}, "uniqueItems": true, "array": [{"required": ["ip-server-name"], "properties": {"ip-server-name": {"description": "Specify the real server name", "format": "string", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 63, "type": "string"}, "stats": {"type": "object", "properties": {"hits": {"description": "Number of times the IP was selected", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}}}}}], "type": "array", "$ref": "/axapi/v3/gslb/site/{site-name}/ip-server/{ip-server-name}"}
    :param site_name: {"description": "Specify GSLB site name", "format": "string", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 63, "type": "string"}
    :param slb_dev_list: {"minItems": 1, "items": {"type": "slb-dev"}, "uniqueItems": true, "array": [{"required": ["device-name"], "properties": {}}], "type": "array", "$ref": "/axapi/v3/gslb/site/{site-name}/ip-server/{ip-server-name}/active-rdt/easy-rdt/slb-dev/{device-name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/site/{site_name}/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "site_name"]

        self.b_key = "site"
        self.a10_url="/axapi/v3/gslb/site/{site_name}/stats"
        self.DeviceProxy = ""
        self.ip_server_list = []
        self.stats = {}
        self.site_name = ""
        self.slb_dev_list = []
        self.easy_rdt = {}
        self.active_rdt = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


