from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param Failed: {"optional": true, "size": "8", "type": "number", "oid": "4", "format": "counter"}
    :param Total_Used: {"optional": true, "size": "8", "type": "number", "oid": "2", "format": "counter"}
    :param Total_Freed: {"optional": true, "size": "8", "type": "number", "oid": "3", "format": "counter"}
    :param Port_Usage: {"optional": true, "size": "8", "type": "number", "oid": "1", "format": "counter"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.Failed = ""
        self.Total_Used = ""
        self.Total_Freed = ""
        self.Port_Usage = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Pool(A10BaseClass):
    
    """Class Description::
    Statistics for the object pool.

    Class pool supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param pool_name: {"description": "Specify pool name", "format": "string-rlx", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ipv6/nat/pool/{pool_name}/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "pool_name"]

        self.b_key = "pool"
        self.a10_url="/axapi/v3/ipv6/nat/pool/{pool_name}/stats"
        self.DeviceProxy = ""
        self.stats = {}
        self.pool_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


