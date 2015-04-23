from a10sdk.common.A10BaseClass import A10BaseClass


class TypeLast(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param last: {"type": "string", "format": "string"}
    :param type: {"type": "string", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "type-last"
        self.DeviceProxy = ""
        self.last = ""
        self.A10WW_type = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param state: {"type": "string", "format": "string"}
    :param type_last: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"last": {"type": "string", "format": "string"}, "type": {"type": "string", "format": "string"}, "optional": true}}]}
    :param gslb_site: {"type": "string", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.state = ""
        self.type_last = []
        self.gslb_site = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Site(A10BaseClass):
    
    """Class Description::
    Operational Status for the object site.

    Class site supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ip_server_list: {"minItems": 1, "items": {"type": "ip-server"}, "uniqueItems": true, "array": [{"required": ["ip-server-name"], "properties": {"oper": {"type": "object", "properties": {"state": {"type": "string", "format": "string"}, "ip-server": {"type": "string", "format": "string"}, "ip-server-port": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "vport": {"type": "number", "format": "number"}, "vport-state": {"type": "string", "format": "string"}}}]}, "ip-address": {"type": "string", "format": "string"}}}, "ip-server-name": {"description": "Specify the real server name", "format": "string", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 63, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/gslb/site/{site-name}/ip-server/{ip-server-name}"}
    :param site_name: {"description": "Specify GSLB site name", "format": "string", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 63, "type": "string"}
    :param slb_dev_list: {"minItems": 1, "items": {"type": "slb-dev"}, "uniqueItems": true, "array": [{"required": ["device-name"], "properties": {"oper": {"type": "object", "properties": {"dev_gw_state": {"type": "string", "format": "string"}, "dev_attr": {"type": "string", "format": "string"}, "dev_ip_cnt": {"type": "number", "format": "number"}, "dev_name": {"type": "string", "format": "string"}, "dev_ip": {"type": "string", "format": "string"}, "dev_session_num": {"type": "number", "format": "number"}, "dev_admin_preference": {"type": "number", "format": "number"}, "dev_session_util": {"type": "number", "format": "number"}}}, "device-name": {"description": "Specify SLB device name", "format": "string", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 63, "type": "string"}, "vip-server": {"type": "object", "properties": {"oper": {"type": "object", "properties": {}}, "vip-server-v4-list": {"minItems": 1, "items": {"type": "vip-server-v4"}, "uniqueItems": true, "array": [{"required": ["ipv4"], "properties": {"oper": {"type": "object", "properties": {"dev_vip_addr": {"type": "string", "format": "string"}, "dev_vip_state": {"type": "string", "format": "string"}, "dev-vip-port-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"dev-vip-port-num": {"type": "number", "format": "number"}, "dev-vip-port-state": {"type": "string", "format": "string"}, "optional": true}}]}}}, "ipv4": {"optional": false, "oid": "1001", "type": "string", "description": "Specify IP address", "format": "ipv4-address"}}}], "type": "array", "$ref": "/axapi/v3/gslb/site/{site-name}/ip-server/{ip-server-name}/slb-dev/{device-name}/vip-server/vip-server-v4/{ipv4}"}, "vip-server-v6-list": {"minItems": 1, "items": {"type": "vip-server-v6"}, "uniqueItems": true, "array": [{"required": ["ipv6"], "properties": {"oper": {"type": "object", "properties": {"dev_vip_addr": {"type": "string", "format": "string"}, "dev_vip_state": {"type": "string", "format": "string"}, "dev-vip-port-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"dev-vip-port-num": {"type": "number", "format": "number"}, "dev-vip-port-state": {"type": "string", "format": "string"}, "optional": true}}]}}}, "ipv6": {"optional": false, "oid": "1001", "type": "string", "description": "Specify IP address (IPv6 address)", "format": "ipv6-address"}}}], "type": "array", "$ref": "/axapi/v3/gslb/site/{site-name}/ip-server/{ip-server-name}/slb-dev/{device-name}/vip-server/vip-server-v4/{ipv4}/vip-server-v6/{ipv6}"}, "vip-server-name-list": {"minItems": 1, "items": {"type": "vip-server-name"}, "uniqueItems": true, "array": [{"required": ["vip-name"], "properties": {"oper": {"type": "object", "properties": {"dev_vip_addr": {"type": "string", "format": "string"}, "dev_vip_state": {"type": "string", "format": "string"}, "dev-vip-port-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"dev-vip-port-num": {"type": "number", "format": "number"}, "dev-vip-port-state": {"type": "string", "format": "string"}, "optional": true}}]}}}, "vip-name": {"description": "Specify a VIP name for the SLB device", "format": "string", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 63, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/gslb/site/{site-name}/ip-server/{ip-server-name}/slb-dev/{device-name}/vip-server/vip-server-v4/{ipv4}/vip-server-v6/{ipv6}/vip-server-name/{vip-name}"}}, "$ref": "/axapi/v3/gslb/site/{site-name}/ip-server/{ip-server-name}/slb-dev/{device-name}/vip-server"}}}], "type": "array", "$ref": "/axapi/v3/gslb/site/{site-name}/ip-server/{ip-server-name}/slb-dev/{device-name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/site/{site_name}/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "site"
        self.a10_url="/axapi/v3/gslb/site/{site_name}/oper"
        self.DeviceProxy = ""
        self.oper = {}
        self.ip_server_list = []
        self.site_name = ""
        self.slb_dev_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


