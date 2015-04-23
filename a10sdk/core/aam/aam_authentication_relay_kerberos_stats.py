from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param Other_error: {"description": "Total Other Error", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param Timeout_error: {"description": "Total Timeout", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param Request_send: {"description": "Total Request Send", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param Response_get: {"description": "Total Response Get", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.Other_error = ""
        self.Timeout_error = ""
        self.Request_send = ""
        self.Response_get = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Kerberos(A10BaseClass):
    
    """Class Description::
    Statistics for the object kerberos.

    Class kerberos supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param instance_list: {"minItems": 1, "items": {"type": "instance"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"stats": {"type": "object", "properties": {"Current-requests-of-user": {"description": "Current Pending Requests of User", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}, "Response-receive": {"description": "Response Receive", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}, "Request-send": {"description": "Request Send", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}, "Tickets": {"description": "Tickets", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}}}, "name": {"description": "Specify Kerberos authentication relay name", "format": "string", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 63, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/aam/authentication/relay/kerberos/instance/{name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/relay/kerberos/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "kerberos"
        self.a10_url="/axapi/v3/aam/authentication/relay/kerberos/stats"
        self.DeviceProxy = ""
        self.stats = {}
        self.instance_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


