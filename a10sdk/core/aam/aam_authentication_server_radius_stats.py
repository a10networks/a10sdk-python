from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param Authorize_failure: {"description": "Total Authorization Failure", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param Other_error: {"description": "Total Other Error", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param Request: {"description": "Total Request", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param Authen_success: {"description": "Total Authentication Success", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param Access_challenge: {"description": "Total Access-Challenge Message Receive", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param Authen_failure: {"description": "Total Authentication Failure", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param Timeout_error: {"description": "Total Timeout", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param Authorize_success: {"description": "Total Authorization Success", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
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


class Radius(A10BaseClass):
    
    """Class Description::
    Statistics for the object radius.

    Class radius supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param instance_list: {"minItems": 1, "items": {"type": "instance"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"stats": {"type": "object", "properties": {"Authorize_failure": {"description": "Authorization Failure", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}, "Other_error": {"description": "Other Error", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}, "Request": {"description": "Request", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}, "Authen_success": {"description": "Authentication Success", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}, "Access_challenge": {"description": "Access-Challenge Message Receive", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}, "Authen_failure": {"description": "Authentication Failure", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}, "Timeout_error": {"description": "Timeout", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}, "Authorize_success": {"description": "Authorization Success", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}}}, "name": {"description": "Specify RADIUS authentication server name", "format": "string-rlx", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 63, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/aam/authentication/server/radius/instance/{name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/server/radius/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "radius"
        self.a10_url="/axapi/v3/aam/authentication/server/radius/stats"
        self.DeviceProxy = ""
        self.stats = {}
        self.instance_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


