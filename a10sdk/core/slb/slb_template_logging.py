from a10sdk.common.A10BaseClass import A10BaseClass


class Logging(A10BaseClass):
    
    """Class Description::
    Logging template.

    Class logging supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param name: {"description": "Logging Template Name", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param format: {"description": "Specfiy a format string for web logging (format string(less than 250 characters) for web logging)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 250, "type": "string"}
    :param local_logging: {"description": "1 to enable local logging (1 to enable local logging, default 0)", "format": "number", "default": 0, "optional": true, "maximum": 1, "minimum": 0, "type": "number"}
    :param keep_end: {"description": "Number of unmasked characters at the end (default: 0)", "format": "number", "default": 0, "optional": true, "maximum": 65535, "minimum": 0, "type": "number"}
    :param mask: {"description": "Character to mask the matched pattern (default: X)", "format": "string", "default": "X", "minLength": 1, "optional": true, "maxLength": 1, "type": "string"}
    :param keep_start: {"description": "Number of unmasked characters at the beginning (default: 0)", "format": "number", "default": 0, "optional": true, "maximum": 65535, "minimum": 0, "type": "number"}
    :param service_group: {"description": "Bind a Service Group to the logging template (Service Group Name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "type": "string", "$ref": "/axapi/v3/slb/service-group"}
    :param pcre_mask: {"description": "Mask matched PCRE pattern in the log", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param tcp_proxy: {"description": "TCP proxy template (TCP Proxy Config name)", "format": "string", "default": "default", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/template/logging/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "logging"
        self.a10_url="/axapi/v3/slb/template/logging/{name}"
        self.DeviceProxy = ""
        self.name = ""
        self.A10WW_format = ""
        self.local_logging = ""
        self.keep_end = ""
        self.mask = ""
        self.keep_start = ""
        self.service_group = ""
        self.pcre_mask = ""
        self.tcp_proxy = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


