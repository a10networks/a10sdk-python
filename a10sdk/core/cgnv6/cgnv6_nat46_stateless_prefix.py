from a10sdk.common.A10BaseClass import A10BaseClass


class Prefix(A10BaseClass):
    
    """Class Description::
    Enable Stateless NAT46 IPv6 source address.

    Class prefix supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ipv6_prefix: {"optional": true, "type": "string", "description": "IPv6 prefix", "format": "ipv6-address-plen"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/nat46-stateless/prefix`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "prefix"
        self.a10_url="/axapi/v3/cgnv6/nat46-stateless/prefix"
        self.DeviceProxy = ""
        self.ipv6_prefix = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


