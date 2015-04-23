from a10sdk.common.A10BaseClass import A10BaseClass


class L3InlineModeFlag(A10BaseClass):
    
    """Class Description::
    Enable OSPF under Layer 3 Inline Hot Standby Mode.

    Class l3-inline-mode-flag supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param l3_inline_mode: {"description": "Enable Layer 3 Inline Hot Standby Mode", "partition-visibility": "shared", "default": 0, "type": "number", "format": "flag", "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/vrrp-a/l3-inline-mode-flag`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "l3-inline-mode-flag"
        self.a10_url="/axapi/v3/vrrp-a/l3-inline-mode-flag"
        self.DeviceProxy = ""
        self.uuid = ""
        self.l3_inline_mode = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


