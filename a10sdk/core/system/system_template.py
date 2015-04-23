from a10sdk.common.A10BaseClass import A10BaseClass


class Template(A10BaseClass):
    
    """Class Description::
    Apply template to the whole system.

    Class template supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param template_policy: {"description": "Apply policy template to the whole system (Policy template name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/slb/template/policy"}
    :param template_monitor: {"description": "Apply monitor template to the whole system (Monitor template ID Number)", "format": "number", "optional": true, "maximum": 16, "minimum": 1, "type": "number", "$ref": "/axapi/v3/slb/template/monitor"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/system/template`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "template"
        self.a10_url="/axapi/v3/system/template"
        self.DeviceProxy = ""
        self.template_policy = ""
        self.template_monitor = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


