from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param Stapling_Certificate_Unknown: {"description": "Total OCSP Stapling Unknown Certificate Response", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param Stapling_Certificate_Good: {"description": "Total OCSP Stapling Good Certificate Response", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param Stapling_Certificate_Revoked: {"description": "Total OCSP Stapling Revoked Certificate Response", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.Stapling_Certificate_Unknown = ""
        self.Stapling_Certificate_Good = ""
        self.Stapling_Certificate_Revoked = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ocsp(A10BaseClass):
    
    """Class Description::
    Statistics for the object ocsp.

    Class ocsp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param instance_list: {"minItems": 1, "items": {"type": "instance"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"stats": {"type": "object", "properties": {"Stapling-Timeout": {"description": "OCSP Stapling Timeout", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}, "Certificate-Revoked": {"description": "Revoked Certificate Response", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}, "Request": {"description": "Request", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}, "Stapling-Certificate-Revoked": {"description": "OCSP Stapling Revoked Certificate Response", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}, "Certificate-Unknown": {"description": "Unknown Certificate Response", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}, "Stapling-Certificate-Unknown": {"description": "OCSP Stapling Unknown Certificate Response", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}, "Stapling-Certificate-Good": {"description": "OCSP Stapling Good Certificate Response", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}, "Timeout": {"description": "Timeout", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}, "Certificate-Good": {"description": "Good Certificate Response", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}, "Stapling-Request": {"description": "OCSP Stapling Request Send", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}}}, "name": {"description": "Specify OCSP authentication server name", "format": "string-rlx", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 63, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/aam/authentication/server/ocsp/instance/{name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/server/ocsp/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ocsp"
        self.a10_url="/axapi/v3/aam/authentication/server/ocsp/stats"
        self.DeviceProxy = ""
        self.stats = {}
        self.instance_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


