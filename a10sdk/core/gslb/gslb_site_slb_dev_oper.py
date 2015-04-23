from a10sdk.common.A10BaseClass import A10BaseClass


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param dev_gw_state: {"type": "string", "format": "string"}
    :param dev_attr: {"type": "string", "format": "string"}
    :param dev_ip_cnt: {"type": "number", "format": "number"}
    :param dev_name: {"type": "string", "format": "string"}
    :param dev_ip: {"type": "string", "format": "string"}
    :param dev_session_num: {"type": "number", "format": "number"}
    :param dev_admin_preference: {"type": "number", "format": "number"}
    :param dev_session_util: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.dev_gw_state = ""
        self.dev_attr = ""
        self.dev_ip_cnt = ""
        self.dev_name = ""
        self.dev_ip = ""
        self.dev_session_num = ""
        self.dev_admin_preference = ""
        self.dev_session_util = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class DevVipPortList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param dev_vip_port_num: {"type": "number", "format": "number"}
    :param dev_vip_port_state: {"type": "string", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "dev-vip-port-list"
        self.DeviceProxy = ""
        self.dev_vip_port_num = ""
        self.dev_vip_port_state = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param dev_vip_addr: {"type": "string", "format": "string"}
    :param dev_vip_state: {"type": "string", "format": "string"}
    :param dev_vip_port_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"dev-vip-port-num": {"type": "number", "format": "number"}, "dev-vip-port-state": {"type": "string", "format": "string"}, "optional": true}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.dev_vip_addr = ""
        self.dev_vip_state = ""
        self.dev_vip_port_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class VipServerV4List(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ipv4: {"optional": false, "oid": "1001", "type": "string", "description": "Specify IP address", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "vip-server-v4-list"
        self.DeviceProxy = ""
        self.oper = {}
        self.ipv4 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class DevVipPortList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param dev_vip_port_num: {"type": "number", "format": "number"}
    :param dev_vip_port_state: {"type": "string", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "dev-vip-port-list"
        self.DeviceProxy = ""
        self.dev_vip_port_num = ""
        self.dev_vip_port_state = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param dev_vip_addr: {"type": "string", "format": "string"}
    :param dev_vip_state: {"type": "string", "format": "string"}
    :param dev_vip_port_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"dev-vip-port-num": {"type": "number", "format": "number"}, "dev-vip-port-state": {"type": "string", "format": "string"}, "optional": true}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.dev_vip_addr = ""
        self.dev_vip_state = ""
        self.dev_vip_port_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class VipServerV6List(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ipv6: {"optional": false, "oid": "1001", "type": "string", "description": "Specify IP address (IPv6 address)", "format": "ipv6-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "vip-server-v6-list"
        self.DeviceProxy = ""
        self.oper = {}
        self.ipv6 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class DevVipPortList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param dev_vip_port_num: {"type": "number", "format": "number"}
    :param dev_vip_port_state: {"type": "string", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "dev-vip-port-list"
        self.DeviceProxy = ""
        self.dev_vip_port_num = ""
        self.dev_vip_port_state = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param dev_vip_addr: {"type": "string", "format": "string"}
    :param dev_vip_state: {"type": "string", "format": "string"}
    :param dev_vip_port_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"dev-vip-port-num": {"type": "number", "format": "number"}, "dev-vip-port-state": {"type": "string", "format": "string"}, "optional": true}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.dev_vip_addr = ""
        self.dev_vip_state = ""
        self.dev_vip_port_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class VipServerNameList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param vip_name: {"description": "Specify a VIP name for the SLB device", "format": "string", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "vip-server-name-list"
        self.DeviceProxy = ""
        self.oper = {}
        self.vip_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class VipServer(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param vip_server_v4_list: {"minItems": 1, "items": {"type": "vip-server-v4"}, "uniqueItems": true, "array": [{"required": ["ipv4"], "properties": {"oper": {"type": "object", "properties": {"dev_vip_addr": {"type": "string", "format": "string"}, "dev_vip_state": {"type": "string", "format": "string"}, "dev-vip-port-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"dev-vip-port-num": {"type": "number", "format": "number"}, "dev-vip-port-state": {"type": "string", "format": "string"}, "optional": true}}]}}}, "ipv4": {"optional": false, "oid": "1001", "type": "string", "description": "Specify IP address", "format": "ipv4-address"}}}], "type": "array", "$ref": "/axapi/v3/gslb/site/{site-name}/slb-dev/{device-name}/vip-server/vip-server-v4/{ipv4}"}
    :param vip_server_v6_list: {"minItems": 1, "items": {"type": "vip-server-v6"}, "uniqueItems": true, "array": [{"required": ["ipv6"], "properties": {"oper": {"type": "object", "properties": {"dev_vip_addr": {"type": "string", "format": "string"}, "dev_vip_state": {"type": "string", "format": "string"}, "dev-vip-port-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"dev-vip-port-num": {"type": "number", "format": "number"}, "dev-vip-port-state": {"type": "string", "format": "string"}, "optional": true}}]}}}, "ipv6": {"optional": false, "oid": "1001", "type": "string", "description": "Specify IP address (IPv6 address)", "format": "ipv6-address"}}}], "type": "array", "$ref": "/axapi/v3/gslb/site/{site-name}/slb-dev/{device-name}/vip-server/vip-server-v4/{ipv4}/vip-server-v6/{ipv6}"}
    :param vip_server_name_list: {"minItems": 1, "items": {"type": "vip-server-name"}, "uniqueItems": true, "array": [{"required": ["vip-name"], "properties": {"oper": {"type": "object", "properties": {"dev_vip_addr": {"type": "string", "format": "string"}, "dev_vip_state": {"type": "string", "format": "string"}, "dev-vip-port-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"dev-vip-port-num": {"type": "number", "format": "number"}, "dev-vip-port-state": {"type": "string", "format": "string"}, "optional": true}}]}}}, "vip-name": {"description": "Specify a VIP name for the SLB device", "format": "string", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 63, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/gslb/site/{site-name}/slb-dev/{device-name}/vip-server/vip-server-v4/{ipv4}/vip-server-v6/{ipv6}/vip-server-name/{vip-name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "vip-server"
        self.DeviceProxy = ""
        self.oper = {}
        self.vip_server_v4_list = []
        self.vip_server_v6_list = []
        self.vip_server_name_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class SlbDev(A10BaseClass):
    
    """Class Description::
    Operational Status for the object slb-dev.

    Class slb-dev supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param device_name: {"description": "Specify SLB device name", "format": "string", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/site/{site_name}/slb-dev/{device_name}/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "slb-dev"
        self.a10_url="/axapi/v3/gslb/site/{site_name}/slb-dev/{device_name}/oper"
        self.DeviceProxy = ""
        self.oper = {}
        self.device_name = ""
        self.vip_server = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


