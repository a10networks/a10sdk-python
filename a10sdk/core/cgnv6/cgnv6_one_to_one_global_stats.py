from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param total_map_freed: {"description": "Total One-to-One Address Mapping Freed", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param map_alloc_failure: {"description": "One-to-One Address Mapping Allocation Failure", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param total_map_allocated: {"description": "Total One-to-One Address Mapping Allocated", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.total_map_freed = ""
        self.map_alloc_failure = ""
        self.total_map_allocated = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Global(A10BaseClass):
    
    """Class Description::
    Statistics for the object global.

    Class global supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/one-to-one/global/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "global"
        self.a10_url="/axapi/v3/cgnv6/one-to-one/global/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


