from a10sdk.common.A10BaseClass import A10BaseClass


class CostCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param cost: {"description": "Interface cost", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param instance_id: {"description": "Specify the interface instance ID", "format": "number", "default": 0, "maximum": 255, "minimum": 0, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "cost-cfg"
        self.DeviceProxy = ""
        self.cost = ""
        self.instance_id = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class HelloIntervalCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param hello_interval: {"description": "Time between HELLO packets (Seconds)", "format": "number", "default": 10, "maximum": 65535, "minimum": 1, "type": "number"}
    :param instance_id: {"description": "Specify the interface instance ID", "format": "number", "default": 0, "maximum": 255, "minimum": 0, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "hello-interval-cfg"
        self.DeviceProxy = ""
        self.hello_interval = ""
        self.instance_id = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class PriorityCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param priority: {"description": "Router priority", "format": "number", "default": 1, "maximum": 255, "minimum": 0, "type": "number"}
    :param instance_id: {"description": "Specify the interface instance ID", "format": "number", "default": 0, "maximum": 255, "minimum": 0, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "priority-cfg"
        self.DeviceProxy = ""
        self.priority = ""
        self.instance_id = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class MtuIgnoreCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param mtu_ignore: {"default": 0, "type": "number", "description": "Ignores the MTU in DBD packets", "format": "flag"}
    :param instance_id: {"description": "Specify the interface instance ID", "format": "number", "default": 0, "maximum": 255, "minimum": 0, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "mtu-ignore-cfg"
        self.DeviceProxy = ""
        self.mtu_ignore = ""
        self.instance_id = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class RetransmitIntervalCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param retransmit_interval: {"description": "Time between retransmitting lost link state advertisements (Seconds)", "format": "number", "default": 5, "maximum": 65535, "minimum": 1, "type": "number"}
    :param instance_id: {"description": "Specify the interface instance ID", "format": "number", "default": 0, "maximum": 255, "minimum": 0, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "retransmit-interval-cfg"
        self.DeviceProxy = ""
        self.retransmit_interval = ""
        self.instance_id = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class NetworkList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param broadcast_type: {"enum": ["broadcast", "non-broadcast", "point-to-point", "point-to-multipoint"], "type": "string", "description": "'broadcast': Specify OSPF broadcast multi-access network; 'non-broadcast': Specify OSPF NBMA network; 'point-to-point': Specify OSPF point-to-point network; 'point-to-multipoint': Specify OSPF point-to-multipoint network; ", "format": "enum"}
    :param p2mp_nbma: {"default": 0, "type": "number", "description": "Specify non-broadcast point-to-multipoint network", "format": "flag"}
    :param network_instance_id: {"description": "Specify the interface instance ID", "format": "number", "default": 0, "maximum": 255, "minimum": 0, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "network-list"
        self.DeviceProxy = ""
        self.broadcast_type = ""
        self.p2mp_nbma = ""
        self.network_instance_id = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class TransmitDelayCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param transmit_delay: {"description": "Link state transmit delay (Seconds)", "format": "number", "default": 1, "maximum": 65535, "minimum": 1, "type": "number"}
    :param instance_id: {"description": "Specify the interface instance ID", "format": "number", "default": 0, "maximum": 255, "minimum": 0, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "transmit-delay-cfg"
        self.DeviceProxy = ""
        self.transmit_delay = ""
        self.instance_id = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class NeighborCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param neighbor_priority: {"description": "OSPF priority of non-broadcast neighbor", "minimum": 0, "type": "number", "maximum": 255, "format": "number"}
    :param neig_inst: {"description": "Specify the interface instance ID", "format": "number", "default": 0, "maximum": 255, "minimum": 0, "type": "number"}
    :param neighbor_poll_interval: {"description": "OSPF dead-router polling interval (Seconds)", "minimum": 0, "type": "number", "maximum": 4294967295, "format": "number"}
    :param neighbor_cost: {"description": "OSPF cost for point-to-multipoint neighbor (metric)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param neighbor: {"default": "::", "type": "string", "description": "OSPFv3 neighbor (Neighbor IPv6 address)", "format": "ipv6-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "neighbor-cfg"
        self.DeviceProxy = ""
        self.neighbor_priority = ""
        self.neig_inst = ""
        self.neighbor_poll_interval = ""
        self.neighbor_cost = ""
        self.neighbor = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class DeadIntervalCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param dead_interval: {"description": "Interval after which a neighbor is declared dead (Seconds)", "format": "number", "default": 40, "maximum": 65535, "minimum": 1, "type": "number"}
    :param instance_id: {"description": "Specify the interface instance ID", "format": "number", "default": 0, "maximum": 255, "minimum": 0, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "dead-interval-cfg"
        self.DeviceProxy = ""
        self.dead_interval = ""
        self.instance_id = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ospf(A10BaseClass):
    
    """Class Description::
    Open Shortest Path First for IPv6 (OSPFv3).

    Class ospf supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param bfd: {"default": 0, "optional": true, "type": "number", "description": "Bidirectional Forwarding Detection (BFD)", "format": "flag"}
    :param cost_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"cost": {"description": "Interface cost", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "optional": true, "instance-id": {"description": "Specify the interface instance ID", "format": "number", "default": 0, "maximum": 255, "minimum": 0, "type": "number"}}}]}
    :param hello_interval_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "hello-interval": {"description": "Time between HELLO packets (Seconds)", "format": "number", "default": 10, "maximum": 65535, "minimum": 1, "type": "number"}, "instance-id": {"description": "Specify the interface instance ID", "format": "number", "default": 0, "maximum": 255, "minimum": 0, "type": "number"}}}]}
    :param disable: {"default": 0, "optional": true, "type": "number", "description": "Disable BFD", "format": "flag"}
    :param priority_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"priority": {"description": "Router priority", "format": "number", "default": 1, "maximum": 255, "minimum": 0, "type": "number"}, "optional": true, "instance-id": {"description": "Specify the interface instance ID", "format": "number", "default": 0, "maximum": 255, "minimum": 0, "type": "number"}}}]}
    :param mtu_ignore_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"mtu-ignore": {"default": 0, "type": "number", "description": "Ignores the MTU in DBD packets", "format": "flag"}, "optional": true, "instance-id": {"description": "Specify the interface instance ID", "format": "number", "default": 0, "maximum": 255, "minimum": 0, "type": "number"}}}]}
    :param retransmit_interval_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"retransmit-interval": {"description": "Time between retransmitting lost link state advertisements (Seconds)", "format": "number", "default": 5, "maximum": 65535, "minimum": 1, "type": "number"}, "optional": true, "instance-id": {"description": "Specify the interface instance ID", "format": "number", "default": 0, "maximum": 255, "minimum": 0, "type": "number"}}}]}
    :param network_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"broadcast-type": {"enum": ["broadcast", "non-broadcast", "point-to-point", "point-to-multipoint"], "type": "string", "description": "'broadcast': Specify OSPF broadcast multi-access network; 'non-broadcast': Specify OSPF NBMA network; 'point-to-point': Specify OSPF point-to-point network; 'point-to-multipoint': Specify OSPF point-to-multipoint network; ", "format": "enum"}, "optional": true, "p2mp-nbma": {"default": 0, "type": "number", "description": "Specify non-broadcast point-to-multipoint network", "format": "flag"}, "network-instance-id": {"description": "Specify the interface instance ID", "format": "number", "default": 0, "maximum": 255, "minimum": 0, "type": "number"}}}]}
    :param transmit_delay_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "transmit-delay": {"description": "Link state transmit delay (Seconds)", "format": "number", "default": 1, "maximum": 65535, "minimum": 1, "type": "number"}, "instance-id": {"description": "Specify the interface instance ID", "format": "number", "default": 0, "maximum": 255, "minimum": 0, "type": "number"}}}]}
    :param neighbor_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"neighbor-priority": {"description": "OSPF priority of non-broadcast neighbor", "minimum": 0, "type": "number", "maximum": 255, "format": "number"}, "neig-inst": {"description": "Specify the interface instance ID", "format": "number", "default": 0, "maximum": 255, "minimum": 0, "type": "number"}, "neighbor-poll-interval": {"description": "OSPF dead-router polling interval (Seconds)", "minimum": 0, "type": "number", "maximum": 4294967295, "format": "number"}, "neighbor-cost": {"description": "OSPF cost for point-to-multipoint neighbor (metric)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "neighbor": {"default": "::", "type": "string", "description": "OSPFv3 neighbor (Neighbor IPv6 address)", "format": "ipv6-address"}, "optional": true}}]}
    :param dead_interval_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"dead-interval": {"description": "Interval after which a neighbor is declared dead (Seconds)", "format": "number", "default": 40, "maximum": 65535, "minimum": 1, "type": "number"}, "optional": true, "instance-id": {"description": "Specify the interface instance ID", "format": "number", "default": 0, "maximum": 255, "minimum": 0, "type": "number"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/interface/ethernet/{ifnum}/ipv6/ospf`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ospf"
        self.a10_url="/axapi/v3/interface/ethernet/{ifnum}/ipv6/ospf"
        self.DeviceProxy = ""
        self.bfd = ""
        self.cost_cfg = []
        self.hello_interval_cfg = []
        self.disable = ""
        self.priority_cfg = []
        self.mtu_ignore_cfg = []
        self.retransmit_interval_cfg = []
        self.network_list = []
        self.transmit_delay_cfg = []
        self.neighbor_cfg = []
        self.dead_interval_cfg = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


