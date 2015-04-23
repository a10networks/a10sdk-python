from a10sdk.common.A10BaseClass import A10BaseClass


class AreaList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param area_id_addr: {"type": "string", "description": "OSPF area ID in IP address format", "format": "ipv4-address"}
    :param tag: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Set the OSPFv3 process tag", "format": "string"}
    :param instance_id: {"description": "Set the interface instance ID", "format": "number", "default": 0, "maximum": 255, "minimum": 0, "type": "number"}
    :param area_id_num: {"description": "OSPF area ID as a decimal value", "minimum": 0, "type": "number", "maximum": 4294967295, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "area-list"
        self.DeviceProxy = ""
        self.area_id_addr = ""
        self.tag = ""
        self.instance_id = ""
        self.area_id_num = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ospf(A10BaseClass):
    
    """Class Description::
    Open Shortest Path First for IPv6 (OSPFv3).

    Class ospf supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param area_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"area-id-addr": {"type": "string", "description": "OSPF area ID in IP address format", "format": "ipv4-address"}, "tag": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Set the OSPFv3 process tag", "format": "string"}, "optional": true, "instance-id": {"description": "Set the interface instance ID", "format": "number", "default": 0, "maximum": 255, "minimum": 0, "type": "number"}, "area-id-num": {"description": "OSPF area ID as a decimal value", "minimum": 0, "type": "number", "maximum": 4294967295, "format": "number"}}}]}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/interface/ve/{ifnum}/ipv6/router/ospf`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ospf"
        self.a10_url="/axapi/v3/interface/ve/{ifnum}/ipv6/router/ospf"
        self.DeviceProxy = ""
        self.area_list = []
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


