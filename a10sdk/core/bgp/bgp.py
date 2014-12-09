from a10sdk.common.A10BaseClass import A10BaseClass


class NexthopTrigger(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param delay: {"description": "Configure nexthop trigger delay time interval (Nexthop Trigger Delay time interval between 1 and 100)", "minimum": 1, "type": "number", "maximum": 100, "format": "number"}
    :param enable: {"default": 0, "type": "number", "description": "Enable the nexthop tracking functionality", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "nexthop-trigger"
        self.DeviceProxy = ""
        self.delay = ""
        self.enable = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Bgp(A10BaseClass):
    
    """Class Description::
    Border Gateway Protocol (BGP).

    Class bgp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param extended_asn_cap: {"default": 0, "optional": true, "type": "number", "description": "Enable the router to send 4-octet ASN capabilities", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/bgp`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "bgp"
        self.a10_url="/axapi/v3/bgp"
        self.DeviceProxy = ""
        self.nexthop_trigger = {}
        self.extended_asn_cap = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


