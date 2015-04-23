from a10sdk.common.A10BaseClass import A10BaseClass


class Hsm(A10BaseClass):
    
    """Class Description::
    Hardware Security Module commands.

    Class hsm supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param template_list: {"minItems": 1, "items": {"type": "template"}, "uniqueItems": true, "array": [{"required": ["template-name"], "properties": {"protection-ocs": {"description": "Operator Card Set", "format": "flag", "default": 0, "optional": true, "not-list": ["protection-module", "softcard"], "type": "number"}, "password": {"default": 0, "optional": true, "type": "number", "description": "Specify HSM Passphrase", "format": "flag"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "encrypted": {"optional": true, "type": "encrypted", "description": "Do NOT use this option manually (This is an A10 reserved keyword) (The ENCRYPTED password string)", "format": "encrypted"}, "template-name": {"description": "Specify Template name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "password-string": {"description": "Password (minimum 4 characters)", "format": "password", "minLength": 4, "optional": true, "maxLength": 31, "type": "string"}, "protection-softcard-hash": {"description": "Hash", "format": "string", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}, "softhsm-enum": {"optional": true, "enum": ["softHSM", "thalesHSM"], "type": "string", "description": "'softHSM': software implementation of a cryptographic store; 'thalesHSM': Thales HSM; ", "format": "enum"}, "protection": {"default": 0, "optional": true, "type": "number", "description": "Specify Protection Method", "format": "flag"}, "rfs-port": {"description": "Specify Port", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": true}, "hsm-dev": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"hsm-ip": {"type": "string", "description": "Specify HSM Device IP Address", "format": "ipv4-address"}, "optional": true, "hsm-port": {"description": "Specify Port", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "hsm-priority": {"description": "Specify Priority", "minimum": 1, "type": "number", "maximum": 100, "format": "number"}}}]}, "rfs-ip": {"optional": true, "type": "string", "description": "Specify Thales Remote File System", "format": "ipv4-address"}, "softcard": {"description": "Softcard", "format": "flag", "default": 0, "optional": true, "not-list": ["protection-module", "protection-ocs"], "type": "number"}, "protection-module": {"description": "Module", "format": "flag", "default": 0, "optional": true, "not-list": ["protection-ocs", "softcard"], "type": "number"}, "sec-world": {"description": "Security World Name", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/hsm/template/{template-name}"}
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


