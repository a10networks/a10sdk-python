from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param used_address: {"description": "Used Address", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param total_address: {"description": "Total Address", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param free_address: {"description": "Free Address", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.used_address = ""
        self.total_address = ""
        self.free_address = ""

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
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/one-to-one/pool/{pool_name}/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "pool_name"]

        self.b_key = "pool"
        self.a10_url="/axapi/v3/cgnv6/one-to-one/pool/{pool_name}/stats"
        self.DeviceProxy = ""
        self.stats = {}
        self.pool_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


