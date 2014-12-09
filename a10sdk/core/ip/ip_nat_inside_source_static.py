from a10sdk.common.A10BaseClass import A10BaseClass


class Static(A10BaseClass):
    
    """Class Description::
    Static Address Translations.

    Class static supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param nat_address: {"optional": false, "type": "string", "description": "NAT Address", "format": "ipv4-address"}
    :param vrid: {"description": "VRRP-A vrid (Specify ha VRRP-A vrid)", "format": "number", "type": "number", "maximum": 31, "minimum": 1, "optional": true}
    :param src_address: {"optional": false, "type": "string", "description": "Original Source Address", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ip/nat/inside/source/static/{src_address}+{nat_address}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "src_address","nat_address"]

        self.b_key = "static"
        self.a10_url="/axapi/v3/ip/nat/inside/source/static/{src_address}+{nat_address}"
        self.DeviceProxy = ""
        self.nat_address = ""
        self.vrid = ""
        self.src_address = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


