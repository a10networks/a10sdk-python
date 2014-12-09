from a10sdk.common.A10BaseClass import A10BaseClass


class InterfaceIpv4(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ipv4_eth: {"type": "number", "description": "configure lldp management-address interface ethernet (lldp management-address interface port number)", "format": "interface"}
    :param ipv4_mgmt: {"default": 0, "type": "number", "description": "configure lldp management-address interface management", "format": "flag"}
    :param ipv4_ve: {"description": "configure lldp management-address interface ve (lldp management-address interface port number)", "minimum": 2, "type": "number", "maximum": 4094, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "interface-ipv4"
        self.DeviceProxy = ""
        self.ipv4_eth = ""
        self.ipv4_mgmt = ""
        self.ipv4_ve = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ipv4Addr(A10BaseClass):
    
    """Class Description::
    Configure lldp management-address ipv4 address.

    Class ipv4-addr supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ipv4: {"optional": false, "type": "string", "description": "Configure lldp management-address, subtype is ipv4 (lldp management-address ipv4 address)", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/network/lldp/management-address/ipv4-addr/{ipv4}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "ipv4"]

        self.b_key = "ipv4-addr"
        self.a10_url="/axapi/v3/network/lldp/management-address/ipv4-addr/{ipv4}"
        self.DeviceProxy = ""
        self.ipv4 = ""
        self.interface_ipv4 = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


