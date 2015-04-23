from a10sdk.common.A10BaseClass import A10BaseClass


class Account(A10BaseClass):
    
    """Class Description::
    Authentication account configuration.

    Class account supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param kerberos_spn_list: {"minItems": 1, "items": {"type": "kerberos-spn"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"account": {"description": "Specify domain account for SPN", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}, "realm": {"description": "Specify Kerberos realm", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}, "name": {"description": "Specify AD account name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "encrypted": {"optional": true, "type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.)", "format": "encrypted"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "password": {"default": 0, "optional": true, "type": "number", "description": "Specify password of domain account", "format": "flag"}, "service-principal-name": {"description": "Specify service principal name", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}, "secret-string": {"description": "Password of AD account", "format": "password", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/aam/authentication/account/kerberos-spn/{name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/account`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "account"
        self.a10_url="/axapi/v3/aam/authentication/account"
        self.DeviceProxy = ""
        self.kerberos_spn_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


