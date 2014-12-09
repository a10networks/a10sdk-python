from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param Req: {"description": "Request", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param Req_Auth: {"description": "Request Matching Authentication Template", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param Req_Allow: {"description": "Request Allowed", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param Req_Skip: {"description": "Request Skipped", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param Error: {"description": "Error", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param Req_Reject: {"description": "Request Rejected", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.Req = ""
        self.Req_Auth = ""
        self.Req_Allow = ""
        self.Req_Skip = ""
        self.Error = ""
        self.Req_Reject = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class AaaPolicy(A10BaseClass):
    
    """Class Description::
    Statistics for the object aaa-policy.

    Class aaa-policy supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param aaa_rule_list: {"minItems": 1, "items": {"type": "aaa-rule"}, "uniqueItems": true, "array": [{"required": ["index"], "properties": {}}], "type": "array", "$ref": "/axapi/v3/aam/aaa-policy/{name}/aaa-rule/{index}"}
    :param name: {"description": "Specify AAA policy name", "format": "string", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/aaa-policy/{name}/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "aaa-policy"
        self.a10_url="/axapi/v3/aam/aaa-policy/{name}/stats"
        self.DeviceProxy = ""
        self.aaa_rule_list = []
        self.stats = {}
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


