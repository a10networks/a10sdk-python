from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param Failure: {"description": "Failure", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param Request: {"description": "Request", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param Success: {"description": "Success", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.Failure = ""
        self.Request = ""
        self.Success = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class WsFederation(A10BaseClass):
    
    """Class Description::
    Statistics for the object ws-federation.

    Class ws-federation supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param name: {"description": "Specify WS-Federation authentication relay name", "format": "string", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/relay/ws-federation/{name}/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "ws-federation"
        self.a10_url="/axapi/v3/aam/authentication/relay/ws-federation/{name}/stats"
        self.DeviceProxy = ""
        self.stats = {}
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


