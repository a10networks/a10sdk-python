from a10sdk.common.A10BaseClass import A10BaseClass


class SnmpServer(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param trap_source: {"default": 0, "type": "number", "description": "The trap source", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "snmp-server"
        self.DeviceProxy = ""
        self.trap_source = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Loopback(A10BaseClass):
    
    """Class Description::
    Loopback interface.

    Class loopback supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ifnum: {"description": "Loopback interface number", "format": "number", "type": "number", "maximum": 10, "minimum": 0, "optional": false}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/interface/loopback/{ifnum}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "ifnum"]

        self.b_key = "loopback"
        self.a10_url="/axapi/v3/interface/loopback/{ifnum}"
        self.DeviceProxy = ""
        self.ip = {}
        self.ifnum = ""
        self.ipv6 = {}
        self.isis = {}
        self.snmp_server = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


