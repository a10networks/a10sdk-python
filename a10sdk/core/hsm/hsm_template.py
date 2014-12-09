from a10sdk.common.A10BaseClass import A10BaseClass


class Template(A10BaseClass):
    
    """Class Description::
    HSM Template.

    Class template supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param password_string: {"description": "Password (minimum 4 characters)", "format": "password", "minLength": 4, "optional": true, "maxLength": 31, "type": "string"}
    :param encrypted: {"optional": true, "type": "encrypted", "description": "Do NOT use this option manually (This is an A10 reserved keyword) (The ENCRYPTED password string)", "format": "encrypted"}
    :param softhsm_enum: {"optional": true, "enum": ["softHSM"], "type": "string", "description": "'softHSM': software implementation of a cryptographic store; ", "format": "enum"}
    :param password: {"default": 0, "optional": true, "type": "number", "description": "Specify HSM Passphrase", "format": "flag"}
    :param template_name: {"description": "Specify Template name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/hsm/template/{template_name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "template_name"]

        self.b_key = "template"
        self.a10_url="/axapi/v3/hsm/template/{template_name}"
        self.DeviceProxy = ""
        self.password_string = ""
        self.encrypted = ""
        self.softhsm_enum = ""
        self.password = ""
        self.template_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


