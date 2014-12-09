from a10sdk.common.A10BaseClass import A10BaseClass


class EthernetCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param flap_ethernet_end: {"type": "number", "description": "Ethernet Port", "format": "interface"}
    :param flap_ethernet_start: {"type": "number", "description": "Ethernet Port", "format": "interface"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ethernet-cfg"
        self.DeviceProxy = ""
        self.flap_ethernet_end = ""
        self.flap_ethernet_start = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class RestartPortList(A10BaseClass):
    
    """Class Description::
    Ports to be restarted on standby system after transition.

    Class restart-port-list supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ethernet_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "flap-ethernet-end": {"type": "number", "description": "Ethernet Port", "format": "interface"}, "flap-ethernet-start": {"type": "number", "description": "Ethernet Port", "format": "interface"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/vrrp-a/restart-port-list`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "restart-port-list"
        self.a10_url="/axapi/v3/vrrp-a/restart-port-list"
        self.DeviceProxy = ""
        self.ethernet_cfg = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


