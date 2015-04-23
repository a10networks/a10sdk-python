from a10sdk.common.A10BaseClass import A10BaseClass


class StaticDestMapping(A10BaseClass):
    
    """Class Description::
    Stateless NAT46 mapping (IPv4 <-> IPv6).

    Class static-dest-mapping supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param count: {"platform-specific-range": 1, "platform-specific-default": 1, "description": "Set number of consecutive mappings (Number of mappings)", "format": "number", "optional": true, "modify-not-allowed": 1, "type": "number"}
    :param v6_address: {"optional": false, "type": "string", "description": "IPv6 address", "format": "ipv6-address"}
    :param v4_address: {"optional": false, "type": "string", "description": "IPv4 address", "format": "ipv4-address"}
    :param vrid: {"description": "VRRP-A vrid (Specify ha VRRP-A vrid)", "format": "number", "optional": true, "maximum": 31, "minimum": 1, "modify-not-allowed": 1, "type": "number"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/nat46-stateless/static-dest-mapping/{v4_address}+{v6_address}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "v4_address","v6_address"]

        self.b_key = "static-dest-mapping"
        self.a10_url="/axapi/v3/cgnv6/nat46-stateless/static-dest-mapping/{v4_address}+{v6_address}"
        self.DeviceProxy = ""
        self.count = ""
        self.v6_address = ""
        self.v4_address = ""
        self.vrid = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


