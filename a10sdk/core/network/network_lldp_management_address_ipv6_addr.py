from a10sdk.common.A10BaseClass import A10BaseClass


class InterfaceIpv6(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ipv6_ve: {"description": "configure lldp management-address interface ve (lldp management-address interface port number)", "minimum": 2, "type": "number", "maximum": 4094, "format": "number"}
    :param ipv6_eth: {"type": "number", "description": "configure lldp management-address interface ethernet (lldp management-address interface port number)", "format": "interface"}
    :param ipv6_mgmt: {"default": 0, "type": "number", "description": "configure lldp management-address interface management", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "interface-ipv6"
        self.DeviceProxy = ""
        self.ipv6_ve = ""
        self.ipv6_eth = ""
        self.ipv6_mgmt = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ipv6Addr(A10BaseClass):
    
    """Class Description::
    Configure lldp management-address ipv6 address.

    Class ipv6-addr supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ipv6: {"optional": false, "type": "string", "description": "Configure lldp management-address, subtype is ipv6 (lldp management-address ipv6 address)", "format": "ipv6-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/network/lldp/management-address/ipv6-addr/{ipv6}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "ipv6"]

        self.b_key = "ipv6-addr"
        self.a10_url="/axapi/v3/network/lldp/management-address/ipv6-addr/{ipv6}"
        self.DeviceProxy = ""
        self.interface_ipv6 = {}
        self.ipv6 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


