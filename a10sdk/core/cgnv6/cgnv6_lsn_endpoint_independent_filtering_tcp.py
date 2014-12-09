from a10sdk.common.A10BaseClass import A10BaseClass


class PortList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param port: {"type": "number", "description": "Single Destination Port or Port Range Start", "format": "number"}
    :param port_end: {"type": "number", "description": "Port Range End", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "port-list"
        self.DeviceProxy = ""
        self.port = ""
        self.port_end = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Tcp(A10BaseClass):
    
    """Class Description::
    Set behavior for TCP.

    Class tcp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param port_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "port": {"type": "number", "description": "Single Destination Port or Port Range Start", "format": "number"}, "port-end": {"type": "number", "description": "Port Range End", "format": "number"}}}]}
    :param session_limit: {"description": "Limit number of EIF sessions that can be created per port", "format": "number", "default": 65535, "optional": true, "maximum": 65535, "minimum": 1, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/lsn/endpoint-independent-filtering/tcp`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "tcp"
        self.a10_url="/axapi/v3/cgnv6/lsn/endpoint-independent-filtering/tcp"
        self.DeviceProxy = ""
        self.port_list = []
        self.session_limit = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


