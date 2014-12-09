from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param svrsel_fail: {"description": "Server selection failure", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param default_switching: {"description": "Default switching", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}
    :param total_proxy: {"description": "Total proxy conns", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param curr_proxy: {"description": "Current proxy conns", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param target_switching: {"description": "Target ID switching", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "8"}
    :param noroute: {"description": "No route failure", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param client_err: {"description": "Client fail", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param sender_switching: {"description": "Sender ID switching", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "8"}
    :param server_err: {"description": "Server fail", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param snat_fail: {"description": "Source NAT failure", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param insert_clientip: {"description": "Insert client IP", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.svrsel_fail = ""
        self.default_switching = ""
        self.total_proxy = ""
        self.curr_proxy = ""
        self.target_switching = ""
        self.noroute = ""
        self.client_err = ""
        self.sender_switching = ""
        self.server_err = ""
        self.snat_fail = ""
        self.insert_clientip = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Fix(A10BaseClass):
    
    """Class Description::
    Statistics for the object fix.

    Class fix supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/fix/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "fix"
        self.a10_url="/axapi/v3/slb/fix/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


