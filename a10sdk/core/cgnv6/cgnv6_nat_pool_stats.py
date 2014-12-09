from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param icmp_freed: {"optional": true, "size": "8", "type": "number", "oid": "3", "format": "counter"}
    :param tcp_freed: {"optional": true, "size": "8", "type": "number", "oid": "10", "format": "counter"}
    :param udp: {"optional": true, "size": "8", "type": "number", "oid": "5", "format": "counter"}
    :param icmp_total: {"optional": true, "size": "8", "type": "number", "oid": "4", "format": "counter"}
    :param users: {"optional": true, "size": "8", "type": "number", "oid": "1", "format": "counter"}
    :param tcp: {"optional": true, "size": "8", "type": "number", "oid": "9", "format": "counter"}
    :param tcp_rsvd: {"optional": true, "size": "8", "type": "number", "oid": "12", "format": "counter"}
    :param tcp_total: {"optional": true, "size": "8", "type": "number", "oid": "11", "format": "counter"}
    :param udp_rsvd: {"optional": true, "size": "8", "type": "number", "oid": "8", "format": "counter"}
    :param icmp: {"optional": true, "size": "8", "type": "number", "oid": "2", "format": "counter"}
    :param udp_freed: {"optional": true, "size": "8", "type": "number", "oid": "6", "format": "counter"}
    :param udp_total: {"optional": true, "size": "8", "type": "number", "oid": "7", "format": "counter"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.icmp_freed = ""
        self.tcp_freed = ""
        self.udp = ""
        self.icmp_total = ""
        self.users = ""
        self.tcp = ""
        self.tcp_rsvd = ""
        self.tcp_total = ""
        self.udp_rsvd = ""
        self.icmp = ""
        self.udp_freed = ""
        self.udp_total = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Pool(A10BaseClass):
    
    """Class Description::
    Statistics for the object pool.

    Class pool supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param pool_name: {"description": "Specify pool name or pool group", "format": "string-rlx", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/nat/pool/{pool_name}/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "pool_name"]

        self.b_key = "pool"
        self.a10_url="/axapi/v3/cgnv6/nat/pool/{pool_name}/stats"
        self.DeviceProxy = ""
        self.stats = {}
        self.pool_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


