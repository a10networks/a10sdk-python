from a10sdk.common.A10BaseClass import A10BaseClass


class Kerberos(A10BaseClass):
    
    """Class Description::
    Kerberos Authentication Relay.

    Class kerberos supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param instance_list: {"minItems": 1, "items": {"type": "instance"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"kerberos-account": {"description": "Specify the kerberos account name", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}, "name": {"description": "Specify Kerberos authentication relay name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "encrypted": {"optional": true, "type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED secret string)", "format": "encrypted"}, "kerberos-realm": {"description": "Specify the kerberos realm", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}, "kerberos-kdc-service-group": {"description": "Specify an authentication service group as multiple KDCs", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "not": "kerberos-kdc", "type": "string", "$ref": "/axapi/v3/aam/authentication/service-group"}, "timeout": {"description": "Specify timeout for kerberos transport, default is 10 seconds (The timeout, default is 10 seconds)", "format": "number", "default": 10, "optional": true, "maximum": 255, "minimum": 1, "type": "number"}, "password": {"default": 0, "optional": true, "type": "number", "description": "Specify password of Kerberos password", "format": "flag"}, "kerberos-kdc": {"description": "Specify the kerberos kdc ip or host name", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "not": "kerberos-kdc-service-group", "type": "string"}, "port": {"description": "Specify The KDC port, default is 88", "format": "number", "default": 88, "optional": true, "maximum": 65535, "minimum": 1, "type": "number"}, "secret-string": {"description": "The kerberos client password", "format": "password", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/aam/authentication/relay/kerberos/instance/{name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/relay/kerberos`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "kerberos"
        self.a10_url="/axapi/v3/aam/authentication/relay/kerberos"
        self.DeviceProxy = ""
        self.instance_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


