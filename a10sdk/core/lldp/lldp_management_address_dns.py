from a10sdk.common.A10BaseClass import A10BaseClass


class Interface(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ethernet: {"not-list": ["ve", "management"], "type": "number", "description": "configure lldp management-address interface ethernet. help-val lldp management-address interface port number", "format": "interface"}
    :param management: {"default": 0, "not-list": ["ethernet", "ve"], "type": "number", "description": "configure lldp management-address interface management", "format": "flag"}
    :param ve: {"description": "configure lldp management-address interface management. help-val lldp management-address interface port number", "format": "number", "not-list": ["ethernet", "management"], "maximum": 4094, "minimum": 2, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "interface"
        self.DeviceProxy = ""
        self.ethernet = ""
        self.management = ""
        self.ve = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Dns(A10BaseClass):
    
    """Class Description::
    Configure lldp management-address dns address.

    Class dns supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param dns: {"description": "Configure lldp management-address, subtype is dns. help-val lldp management-address dns address", "format": "string", "minLength": 1, "optional": false, "maxLength": 31, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/lldp/management-address/dns/{dns}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "dns"]

        self.b_key = "dns"
        self.a10_url="/axapi/v3/lldp/management-address/dns/{dns}"
        self.DeviceProxy = ""
        self.interface = {}
        self.dns = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


