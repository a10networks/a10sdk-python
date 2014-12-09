from a10sdk.common.A10BaseClass import A10BaseClass


class VirtualLinkList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param dead_interval: {"description": "Dead router detection time (Seconds)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param hello_interval: {"description": "Hello packet interval (Seconds)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param bfd: {"default": 0, "type": "number", "description": "Bidirectional Forwarding Detection (BFD)", "format": "flag"}
    :param transmit_delay: {"description": "LSA transmission delay (Seconds)", "format": "number", "default": 1, "maximum": 3600, "minimum": 1, "type": "number"}
    :param value: {"type": "string", "description": "ID (IP addr) associated with virtual link neighbor", "format": "ipv4-address"}
    :param retransmit_interval: {"description": "LSA retransmit interval (Seconds)", "minimum": 1, "type": "number", "maximum": 3600, "format": "number"}
    :param instance_id: {"description": "OSPFv3 instance ID", "format": "number", "default": 0, "maximum": 255, "minimum": 0, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "virtual-link-list"
        self.DeviceProxy = ""
        self.dead_interval = ""
        self.hello_interval = ""
        self.bfd = ""
        self.transmit_delay = ""
        self.value = ""
        self.retransmit_interval = ""
        self.instance_id = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class RangeList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param option: {"enum": ["advertise", "not-advertise"], "type": "string", "description": "'advertise': Advertise this range (default); 'not-advertise': DoNotAdvertise this range; ", "format": "enum"}
    :param value: {"type": "string", "description": "Area range for IPv6 prefix", "format": "ipv6-address-plen"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "range-list"
        self.DeviceProxy = ""
        self.option = ""
        self.value = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Area(A10BaseClass):
    
    """Class Description::
    OSPF area parameters.

    Class area supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param area_ipv4: {"optional": false, "type": "string", "description": "OSPFv3 area ID in IP address format", "format": "ipv4-address"}
    :param virtual_link_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"dead-interval": {"description": "Dead router detection time (Seconds)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "hello-interval": {"description": "Hello packet interval (Seconds)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "bfd": {"default": 0, "type": "number", "description": "Bidirectional Forwarding Detection (BFD)", "format": "flag"}, "transmit-delay": {"description": "LSA transmission delay (Seconds)", "format": "number", "default": 1, "maximum": 3600, "minimum": 1, "type": "number"}, "value": {"type": "string", "description": "ID (IP addr) associated with virtual link neighbor", "format": "ipv4-address"}, "retransmit-interval": {"description": "LSA retransmit interval (Seconds)", "minimum": 1, "type": "number", "maximum": 3600, "format": "number"}, "optional": true, "instance-id": {"description": "OSPFv3 instance ID", "format": "number", "default": 0, "maximum": 255, "minimum": 0, "type": "number"}}}]}
    :param no_summary: {"default": 0, "optional": true, "type": "number", "description": "Do not inject inter-area routes into area", "format": "flag"}
    :param stub: {"default": 0, "optional": true, "type": "number", "description": "Configure OSPFv3 area as stub", "format": "flag"}
    :param range_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "option": {"enum": ["advertise", "not-advertise"], "type": "string", "description": "'advertise': Advertise this range (default); 'not-advertise': DoNotAdvertise this range; ", "format": "enum"}, "value": {"type": "string", "description": "Area range for IPv6 prefix", "format": "ipv6-address-plen"}}}]}
    :param default_cost: {"description": "Set the summary-default cost of a NSSA or stub area (Stub's advertised default summary cost)", "format": "number", "default": 1, "optional": true, "maximum": 16777215, "minimum": 0, "type": "number"}
    :param area_num: {"description": "OSPFv3 area ID as a decimal value", "format": "number", "type": "number", "maximum": 4294967295, "minimum": 0, "optional": false}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/router/ipv6/ospf/{process_id}/area/{area_ipv4}+{area_num}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "area_ipv4","area_num"]

        self.b_key = "area"
        self.a10_url="/axapi/v3/router/ipv6/ospf/{process_id}/area/{area_ipv4}+{area_num}"
        self.DeviceProxy = ""
        self.area_ipv4 = ""
        self.virtual_link_list = []
        self.no_summary = ""
        self.stub = ""
        self.range_list = []
        self.default_cost = ""
        self.area_num = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


