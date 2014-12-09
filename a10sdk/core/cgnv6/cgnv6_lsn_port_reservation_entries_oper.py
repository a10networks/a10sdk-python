from a10sdk.common.A10BaseClass import A10BaseClass


class EntryList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param nat_end_port: {"type": "number", "format": "number"}
    :param inside_start_port: {"type": "number", "format": "number"}
    :param nat_address: {"type": "string", "format": "ipv4-address"}
    :param inside_end_port: {"type": "number", "format": "number"}
    :param nat_start_port: {"type": "number", "format": "number"}
    :param inside_address: {"type": "string", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "entry-list"
        self.DeviceProxy = ""
        self.nat_end_port = ""
        self.inside_start_port = ""
        self.nat_address = ""
        self.inside_end_port = ""
        self.nat_start_port = ""
        self.inside_address = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param entry_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"nat-end-port": {"type": "number", "format": "number"}, "inside-start-port": {"type": "number", "format": "number"}, "nat-address": {"type": "string", "format": "ipv4-address"}, "inside-end-port": {"type": "number", "format": "number"}, "nat-start-port": {"type": "number", "format": "number"}, "optional": true, "inside-address": {"type": "string", "format": "ipv4-address"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.entry_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class PortReservationEntries(A10BaseClass):
    
    """Class Description::
    Operational Status for the object port-reservation-entries.

    Class port-reservation-entries supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/lsn/port-reservation-entries/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "port-reservation-entries"
        self.a10_url="/axapi/v3/cgnv6/lsn/port-reservation-entries/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


