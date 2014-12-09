from a10sdk.common.A10BaseClass import A10BaseClass


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param alloc_failed: {"type": "number", "format": "number"}
    :param vrid: {"enum": ["default"], "type": "string", "format": "enum"}
    :param ha_group_id: {"enum": ["default"], "type": "string", "format": "enum"}
    :param ip: {"type": "string", "format": "ipv4-address"}
    :param ports_consumed: {"type": "number", "format": "number"}
    :param state: {"enum": ["UP", "DOWN", "DELETE", "DISABLED", "MAINTENANCE"], "type": "string", "format": "enum"}
    :param ipv6: {"type": "string", "format": "ipv6-address"}
    :param ports_freed_total: {"type": "number", "format": "number"}
    :param ports_consumed_total: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.alloc_failed = ""
        self.vrid = ""
        self.ha_group_id = ""
        self.ip = ""
        self.ports_consumed = ""
        self.state = ""
        self.ipv6 = ""
        self.ports_freed_total = ""
        self.ports_consumed_total = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Port(A10BaseClass):
    
    """Class Description::
    Operational Status for the object port.

    Class port supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param protocol: {"enum": ["tcp", "udp"], "description": "'tcp': TCP Port; 'udp': UDP Port; ", "format": "enum", "type": "string", "oid": "1002", "optional": false}
    :param port_number: {"description": "Port Number", "format": "number", "optional": false, "oid": "1001", "maximum": 65534, "minimum": 0, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/server/{name}/port/{port_number}+{protocol}/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "port"
        self.a10_url="/axapi/v3/slb/server/{name}/port/{port_number}+{protocol}/oper"
        self.DeviceProxy = ""
        self.oper = {}
        self.protocol = ""
        self.port_number = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


