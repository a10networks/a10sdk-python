from a10sdk.common.A10BaseClass import A10BaseClass


class HsmDev(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param hsm_ip: {"type": "string", "description": "Specify HSM Device IP Address", "format": "ipv4-address"}
    :param hsm_port: {"description": "Specify Port", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param hsm_priority: {"description": "Specify Priority", "minimum": 1, "type": "number", "maximum": 100, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "hsm-dev"
        self.DeviceProxy = ""
        self.hsm_ip = ""
        self.hsm_port = ""
        self.hsm_priority = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Template(A10BaseClass):
    
    """Class Description::
    HSM Template.

    Class template supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param protection_ocs: {"description": "Operator Card Set", "format": "flag", "default": 0, "optional": true, "not-list": ["protection-module", "softcard"], "type": "number"}
    :param password: {"default": 0, "optional": true, "type": "number", "description": "Specify HSM Passphrase", "format": "flag"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param encrypted: {"optional": true, "type": "encrypted", "description": "Do NOT use this option manually (This is an A10 reserved keyword) (The ENCRYPTED password string)", "format": "encrypted"}
    :param template_name: {"description": "Specify Template name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param password_string: {"description": "Password (minimum 4 characters)", "format": "password", "minLength": 4, "optional": true, "maxLength": 31, "type": "string"}
    :param protection_softcard_hash: {"description": "Hash", "format": "string", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param softhsm_enum: {"optional": true, "enum": ["softHSM", "thalesHSM"], "type": "string", "description": "'softHSM': software implementation of a cryptographic store; 'thalesHSM': Thales HSM; ", "format": "enum"}
    :param protection: {"default": 0, "optional": true, "type": "number", "description": "Specify Protection Method", "format": "flag"}
    :param rfs_port: {"description": "Specify Port", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": true}
    :param hsm_dev: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"hsm-ip": {"type": "string", "description": "Specify HSM Device IP Address", "format": "ipv4-address"}, "optional": true, "hsm-port": {"description": "Specify Port", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "hsm-priority": {"description": "Specify Priority", "minimum": 1, "type": "number", "maximum": 100, "format": "number"}}}]}
    :param rfs_ip: {"optional": true, "type": "string", "description": "Specify Thales Remote File System", "format": "ipv4-address"}
    :param softcard: {"description": "Softcard", "format": "flag", "default": 0, "optional": true, "not-list": ["protection-module", "protection-ocs"], "type": "number"}
    :param protection_module: {"description": "Module", "format": "flag", "default": 0, "optional": true, "not-list": ["protection-ocs", "softcard"], "type": "number"}
    :param sec_world: {"description": "Security World Name", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}
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
        self.protection_ocs = ""
        self.password = ""
        self.uuid = ""
        self.encrypted = ""
        self.template_name = ""
        self.password_string = ""
        self.protection_softcard_hash = ""
        self.softhsm_enum = ""
        self.protection = ""
        self.rfs_port = ""
        self.hsm_dev = []
        self.rfs_ip = ""
        self.softcard = ""
        self.protection_module = ""
        self.sec_world = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


