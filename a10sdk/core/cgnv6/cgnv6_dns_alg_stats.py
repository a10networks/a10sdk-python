from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param session_created: {"description": "Session Created", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param response_checked: {"description": "Response Checked", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param rrs_replaced: {"description": "Resource Records Replaced", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param session_freed: {"description": "Session Freed", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.session_created = ""
        self.response_checked = ""
        self.rrs_replaced = ""
        self.session_freed = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class DnsAlg(A10BaseClass):
    
    """Class Description::
    Statistics for the object dns-alg.

    Class dns-alg supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/dns-alg/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "dns-alg"
        self.a10_url="/axapi/v3/cgnv6/dns-alg/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


