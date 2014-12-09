from a10sdk.common.A10BaseClass import A10BaseClass


class IpServerPort(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param vport: {"type": "number", "format": "number"}
    :param vport_state: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ip-server-port"
        self.DeviceProxy = ""
        self.vport = ""
        self.vport_state = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param state: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param ip_server: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param ip_server_port: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "vport": {"type": "number", "format": "number"}, "vport-state": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}}}]}
    :param ip_address: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.state = ""
        self.ip_server = ""
        self.ip_server_port = []
        self.ip_address = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class IpServer(A10BaseClass):
    
    """Class Description::
    Operational Status for the object ip-server.

    Class ip-server supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ip_server_name: {"description": "Specify the real server name", "format": "string", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/site/{site_name}/ip-server/{ip_server_name}/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ip-server"
        self.a10_url="/axapi/v3/gslb/site/{site_name}/ip-server/{ip_server_name}/oper"
        self.DeviceProxy = ""
        self.oper = {}
        self.ip_server_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


