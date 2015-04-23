from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param total_count: {"optional": true, "size": "8", "type": "number", "oid": "1", "format": "counter"}
    :param hit_count: {"optional": true, "size": "8", "type": "number", "oid": "1", "format": "counter"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.total_count = ""
        self.hit_count = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class AaaRule(A10BaseClass):
    
    """Class Description::
    Statistics for the object aaa-rule.

    Class aaa-rule supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param index: {"description": "Specify AAA rule index", "format": "number", "optional": false, "oid": "1001", "maximum": 256, "minimum": 1, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/aaa-policy/{name}/aaa-rule/{index}/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "index"]

        self.b_key = "aaa-rule"
        self.a10_url="/axapi/v3/aam/aaa-policy/{name}/aaa-rule/{index}/stats"
        self.DeviceProxy = ""
        self.index = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


