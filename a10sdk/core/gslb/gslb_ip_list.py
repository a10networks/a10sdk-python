from a10sdk.common.A10BaseClass import A10BaseClass


class GslbIpListAddrList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ip: {"type": "string", "description": "Specify IP address", "format": "ipv4-address"}
    :param ip_mask: {"type": "string", "description": "IP mask", "format": "ipv4-netmask"}
    :param id: {"description": "ID Number", "minimum": 0, "type": "number", "maximum": 31, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "gslb-ip-list-addr-list"
        self.DeviceProxy = ""
        self.ip = ""
        self.ip_mask = ""
        self.A10WW_id = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class IpList(A10BaseClass):
    
    """Class Description::
    Specify a IP List.

    Class ip-list supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param gslb_ip_list_addr_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ip": {"type": "string", "description": "Specify IP address", "format": "ipv4-address"}, "ip-mask": {"type": "string", "description": "IP mask", "format": "ipv4-netmask"}, "optional": true, "id": {"description": "ID Number", "minimum": 0, "type": "number", "maximum": 31, "format": "number"}}}]}
    :param gslb_ip_list_filename: {"description": "Load IP List file (IP List filename)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param gslb_ip_list_obj_name: {"description": "Specify IP List name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/ip-list/{gslb_ip_list_obj_name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "gslb_ip_list_obj_name"]

        self.b_key = "ip-list"
        self.a10_url="/axapi/v3/gslb/ip-list/{gslb_ip_list_obj_name}"
        self.DeviceProxy = ""
        self.gslb_ip_list_addr_list = []
        self.gslb_ip_list_filename = ""
        self.gslb_ip_list_obj_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


