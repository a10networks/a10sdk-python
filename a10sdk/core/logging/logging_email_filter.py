from a10sdk.common.A10BaseClass import A10BaseClass


class Filter(A10BaseClass):
    
    """Class Description::
    Logging via email filter settings.

    Class filter supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param filter_id: {"description": "Logging via email filter settings", "format": "number", "type": "number", "maximum": 8, "minimum": 1, "optional": false}
    :param trigger: {"default": 0, "optional": true, "type": "number", "description": "Trigger email, override buffer settings", "format": "flag"}
    :param expression: {"description": "Reverse Polish Notation, consists of level 0-7, module AFLEX/HMON/..., pattern log-content-pattern, and or/and/not", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 511, "type": "string"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/logging/email/filter/{filter_id}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "filter_id"]

        self.b_key = "filter"
        self.a10_url="/axapi/v3/logging/email/filter/{filter_id}"
        self.DeviceProxy = ""
        self.filter_id = ""
        self.trigger = ""
        self.expression = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


