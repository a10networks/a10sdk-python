from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param Invalid_cred: {"description": "Invalid Credential", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param Bad_req: {"description": "Bad Request", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param Other_error: {"description": "Other Error", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param Request: {"description": "Request", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param Invalid_srv_rsp: {"description": "Invalid Server Response", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param Post_fail: {"description": "POST Failed", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param Error: {"description": "Internal Server Error", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param Not_fnd: {"description": "Not Found", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.Invalid_cred = ""
        self.Bad_req = ""
        self.Other_error = ""
        self.Request = ""
        self.Invalid_srv_rsp = ""
        self.Post_fail = ""
        self.Error = ""
        self.Not_fnd = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Instance(A10BaseClass):
    
    """Class Description::
    Statistics for the object instance.

    Class instance supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param name: {"description": "Specify form-based authentication relay name", "format": "string", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/relay/form-based/instance/{name}/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "instance"
        self.a10_url="/axapi/v3/aam/authentication/relay/form-based/instance/{name}/stats"
        self.DeviceProxy = ""
        self.stats = {}
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


