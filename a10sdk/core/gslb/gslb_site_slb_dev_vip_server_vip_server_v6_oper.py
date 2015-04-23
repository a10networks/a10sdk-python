from a10sdk.common.A10BaseClass import A10BaseClass


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


class VipServerV6(A10BaseClass):
    
    """Class Description::
    Operational Status for the object vip-server-v6.

    Class vip-server-v6 supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ipv6: {"optional": false, "oid": "1001", "type": "string", "description": "Specify IP address (IPv6 address)", "format": "ipv6-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/site/{site_name}/slb-dev/{device_name}/vip-server/vip-server-v6/{ipv6}/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "vip-server-v6"
        self.a10_url="/axapi/v3/gslb/site/{site_name}/slb-dev/{device_name}/vip-server/vip-server-v6/{ipv6}/oper"
        self.DeviceProxy = ""
        self.oper = {}
        self.ipv6 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


