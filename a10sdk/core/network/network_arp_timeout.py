from a10sdk.common.A10BaseClass import A10BaseClass


class ArpTimeout(A10BaseClass):
    
    """Class Description::
    ARP entry timeout.

    Class arp-timeout supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param timeout: {"description": "ARP entry timeout", "format": "number", "default": 300, "optional": true, "maximum": 86400, "minimum": 60, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/network/arp-timeout`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "arp-timeout"
        self.a10_url="/axapi/v3/network/arp-timeout"
        self.DeviceProxy = ""
        self.timeout = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


