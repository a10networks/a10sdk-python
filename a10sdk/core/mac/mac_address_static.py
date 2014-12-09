from a10sdk.common.A10BaseClass import A10BaseClass


class Static(A10BaseClass):
    
    """Class Description::
    Static MAC commands.

    Class static supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param dest: {"default": 0, "optional": true, "type": "number", "description": "Trap MAC with this DA to CPU", "format": "flag"}
    :param mac: {"optional": false, "type": "string", "description": "Configure a Static MAC address", "format": "mac-address"}
    :param vlan: {"description": "VLAN Id. help-val VLAN Id", "format": "number", "optional": false, "maximum": 4094, "minimum": 1, "type": "number", "$ref": "https://axapi.a10networks.com/axapi/v3/vlan"}
    :param port: {"optional": true, "type": "number", "description": "Ethernet Port on which the Address is applicable. help-val Port Value", "format": "interface"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/mac-address/static/{mac}+{vlan}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "mac","vlan"]

        self.b_key = "static"
        self.a10_url="/axapi/v3/mac-address/static/{mac}+{vlan}"
        self.DeviceProxy = ""
        self.dest = ""
        self.mac = ""
        self.vlan = ""
        self.port = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


