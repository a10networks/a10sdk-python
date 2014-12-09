from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param Authorize_failure: {"description": "Authorization Failure", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param Other_error: {"description": "Other Error", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param Request: {"description": "Request", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param Authen_success: {"description": "Authentication Success", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param Access_challenge: {"description": "Access-Challenge Message Receive", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param Authen_failure: {"description": "Authentication Failure", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param Timeout_error: {"description": "Timeout", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param Authorize_success: {"description": "Authorization Success", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.Authorize_failure = ""
        self.Other_error = ""
        self.Request = ""
        self.Authen_success = ""
        self.Access_challenge = ""
        self.Authen_failure = ""
        self.Timeout_error = ""
        self.Authorize_success = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Instance(A10BaseClass):
    
    """Class Description::
    Statistics for the object instance.

    Class instance supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param name: {"description": "Specify RADIUS authentication server name", "format": "string-rlx", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/server/radius/instance/{name}/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "instance"
        self.a10_url="/axapi/v3/aam/authentication/server/radius/instance/{name}/stats"
        self.DeviceProxy = ""
        self.stats = {}
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


