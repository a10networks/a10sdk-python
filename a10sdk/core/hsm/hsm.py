from a10sdk.common.A10BaseClass import A10BaseClass


class Hsm(A10BaseClass):
    
    """Class Description::
    Hardware Security Module commands.

    Class hsm supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param template_list: {"minItems": 1, "items": {"type": "template"}, "uniqueItems": true, "array": [{"required": ["template-name"], "properties": {"password-string": {"description": "Password (minimum 4 characters)", "format": "password", "minLength": 4, "optional": true, "maxLength": 31, "type": "string"}, "encrypted": {"optional": true, "type": "encrypted", "description": "Do NOT use this option manually (This is an A10 reserved keyword) (The ENCRYPTED password string)", "format": "encrypted"}, "softhsm-enum": {"optional": true, "enum": ["softHSM"], "type": "string", "description": "'softHSM': software implementation of a cryptographic store; ", "format": "enum"}, "password": {"default": 0, "optional": true, "type": "number", "description": "Specify HSM Passphrase", "format": "flag"}, "template-name": {"description": "Specify Template name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/hsm/template/{template-name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/hsm`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "hsm"
        self.a10_url="/axapi/v3/hsm"
        self.DeviceProxy = ""
        self.template_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


