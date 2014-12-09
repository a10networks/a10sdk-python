from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param active: {"description": "Active Servers", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param current: {"description": "Current Connections", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.active = ""
        self.current = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Port(A10BaseClass):
    
    """Class Description::
    Statistics for the object port.

    Class port supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param port_proto: {"enum": ["tcp", "udp"], "description": "'tcp': TCP Port; 'udp': UDP Port; ", "format": "enum", "type": "string", "oid": "1002", "optional": false}
    :param port_num: {"description": "Port Number", "format": "number", "optional": false, "oid": "1001", "maximum": 65534, "minimum": 0, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/service-ip/{node_name}/port/{port_num}+{port_proto}/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "port_num","port_proto"]

        self.b_key = "port"
        self.a10_url="/axapi/v3/gslb/service-ip/{node_name}/port/{port_num}+{port_proto}/stats"
        self.DeviceProxy = ""
        self.port_proto = ""
        self.stats = {}
        self.port_num = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


