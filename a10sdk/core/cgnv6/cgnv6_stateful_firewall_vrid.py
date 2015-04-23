from a10sdk.common.A10BaseClass import A10BaseClass


class Vrid(A10BaseClass):
    
    """Class Description::
    Set VRRP-A vrid for stateful firewall.

    Class vrid supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param vrid_value: {"description": "Set VRRP-A vrid for stateful firewall (IPv4 and IPv6)", "format": "number", "type": "number", "maximum": 31, "minimum": 1, "optional": true}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/stateful-firewall/vrid`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "vrid"
        self.a10_url="/axapi/v3/cgnv6/stateful-firewall/vrid"
        self.DeviceProxy = ""
        self.vrid_value = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


