from a10sdk.common.A10BaseClass import A10BaseClass


class EthernetList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ethernet_start: {"type": "number", "description": "Ethernet Port (Interface number)", "format": "interface"}
    :param ethernet_end: {"type": "number", "description": "Ethernet Port", "format": "interface"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ethernet-list"
        self.DeviceProxy = ""
        self.ethernet_start = ""
        self.ethernet_end = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class BpduFwdGroup(A10BaseClass):
    
    """Class Description::
    STP BPDU forward Group Settings.

    Class bpdu-fwd-group supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param bpdu_fwd_group_number: {"optional": false, "minimum": 1, "type": "number", "maximum": 8, "format": "number"}
    :param ethernet_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ethernet-start": {"type": "number", "description": "Ethernet Port (Interface number)", "format": "interface"}, "ethernet-end": {"type": "number", "description": "Ethernet Port", "format": "interface"}, "optional": true}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/network/bpdu-fwd-group/{bpdu_fwd_group_number}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "bpdu_fwd_group_number"]

        self.b_key = "bpdu-fwd-group"
        self.a10_url="/axapi/v3/network/bpdu-fwd-group/{bpdu_fwd_group_number}"
        self.DeviceProxy = ""
        self.bpdu_fwd_group_number = ""
        self.ethernet_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


