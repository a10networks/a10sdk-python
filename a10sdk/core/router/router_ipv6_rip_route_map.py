from a10sdk.common.A10BaseClass import A10BaseClass


class MapCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param map: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Route map name", "format": "string"}
    :param ve: {"type": "number", "description": "Virtual ethernet interface (Virtual ethernet interface number)", "format": "interface"}
    :param loopback: {"type": "number", "description": "Loopback interface (Port number)", "format": "interface"}
    :param route_map_direction: {"enum": ["in", "out"], "type": "string", "description": "'in': Route map set for input filtering; 'out': Route map set for output filtering; ", "format": "enum"}
    :param trunk: {"type": "number", "description": "Trunk interface (Trunk interface number)", "format": "interface"}
    :param ethernet: {"type": "number", "description": "Ethernet interface (Port number)", "format": "interface"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "map-cfg"
        self.DeviceProxy = ""
        self.A10WW_map = ""
        self.ve = ""
        self.loopback = ""
        self.route_map_direction = ""
        self.trunk = ""
        self.ethernet = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class RouteMap(A10BaseClass):
    
    """Class Description::
    Route map set.

    Class route-map supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param map_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"map": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Route map name", "format": "string"}, "ve": {"type": "number", "description": "Virtual ethernet interface (Virtual ethernet interface number)", "format": "interface"}, "loopback": {"type": "number", "description": "Loopback interface (Port number)", "format": "interface"}, "route-map-direction": {"enum": ["in", "out"], "type": "string", "description": "'in': Route map set for input filtering; 'out': Route map set for output filtering; ", "format": "enum"}, "trunk": {"type": "number", "description": "Trunk interface (Trunk interface number)", "format": "interface"}, "ethernet": {"type": "number", "description": "Ethernet interface (Port number)", "format": "interface"}, "optional": true}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/router/ipv6/rip/route-map`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "route-map"
        self.a10_url="/axapi/v3/router/ipv6/rip/route-map"
        self.DeviceProxy = ""
        self.map_cfg = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


