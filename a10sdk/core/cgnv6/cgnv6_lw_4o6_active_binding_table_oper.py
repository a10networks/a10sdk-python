from a10sdk.common.A10BaseClass import A10BaseClass


class EntryList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param port_start: {"type": "number", "format": "number"}
    :param fwd_match_count: {"type": "number", "format": "number"}
    :param port_end: {"type": "number", "format": "number"}
    :param tunnel_address: {"type": "string", "format": "ipv6-address"}
    :param nat_address: {"type": "string", "format": "ipv4-address"}
    :param rev_match_count: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "entry-list"
        self.DeviceProxy = ""
        self.port_start = ""
        self.fwd_match_count = ""
        self.port_end = ""
        self.tunnel_address = ""
        self.nat_address = ""
        self.rev_match_count = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param entry_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"port-start": {"type": "number", "format": "number"}, "fwd-match-count": {"type": "number", "format": "number"}, "port-end": {"type": "number", "format": "number"}, "tunnel-address": {"type": "string", "format": "ipv6-address"}, "nat-address": {"type": "string", "format": "ipv4-address"}, "rev-match-count": {"type": "number", "format": "number"}, "optional": true}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.entry_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ActiveBindingTable(A10BaseClass):
    
    """Class Description::
    Operational Status for the object active-binding-table.

    Class active-binding-table supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/lw-4o6/active-binding-table/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "active-binding-table"
        self.a10_url="/axapi/v3/cgnv6/lw-4o6/active-binding-table/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


