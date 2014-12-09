from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param total_fwd_bytes: {"description": "Forward bytes", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param total_conn: {"description": "Total connections", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param total_fwd_packets: {"description": "Forward packets", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param curr_pconn: {"description": "Persistent connections", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param curr_conn: {"description": "Current connections", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param total_rev_packets: {"description": "Reverse packets", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param total_rev_bytes: {"description": "Reverse bytes", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.total_fwd_bytes = ""
        self.total_conn = ""
        self.total_fwd_packets = ""
        self.curr_pconn = ""
        self.curr_conn = ""
        self.total_rev_packets = ""
        self.total_rev_bytes = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Passthrough(A10BaseClass):
    
    """Class Description::
    Statistics for the object passthrough.

    Class passthrough supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/passthrough/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "passthrough"
        self.a10_url="/axapi/v3/slb/passthrough/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


