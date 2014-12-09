from a10sdk.common.A10BaseClass import A10BaseClass


class Email(A10BaseClass):
    
    """Class Description::
    Set logging level which sent to email address.

    Class email supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param filter_list: {"minItems": 1, "items": {"type": "filter"}, "uniqueItems": true, "array": [{"required": ["filter-id"], "properties": {"filter-id": {"description": "Logging via email filter settings", "format": "number", "type": "number", "maximum": 8, "minimum": 1, "optional": false}, "trigger": {"default": 0, "optional": true, "type": "number", "description": "Trigger email, override buffer settings", "format": "flag"}, "expression": {"description": "Reverse Polish Notation, consists of level 0-7, module AFLEX/HMON/..., pattern log-content-pattern, and or/and/not", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 511, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/logging/email/filter/{filter-id}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/logging/email`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "email"
        self.a10_url="/axapi/v3/logging/email"
        self.DeviceProxy = ""
        self.A10WW_buffer = {}
        self.filter_list = []
        self.level = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


