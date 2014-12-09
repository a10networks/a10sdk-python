from a10sdk.common.A10BaseClass import A10BaseClass


class IfStatsList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counter_sample_records: {"type": "number", "format": "number"}
    :param packet_sample_records: {"type": "number", "format": "number"}
    :param if_num: {"type": "number", "format": "number"}
    :param if_type: {"enum": ["Ethernet", "VE"], "type": "string", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "if-stats-list"
        self.DeviceProxy = ""
        self.counter_sample_records = ""
        self.packet_sample_records = ""
        self.if_num = ""
        self.if_type = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param if_stats_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"counter-sample-records": {"type": "number", "format": "number"}, "packet-sample-records": {"type": "number", "format": "number"}, "if-num": {"type": "number", "format": "number"}, "if-type": {"enum": ["Ethernet", "VE"], "type": "string", "format": "enum"}, "optional": true}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.if_stats_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Global(A10BaseClass):
    
    """Class Description::
    Operational Status for the object global.

    Class global supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/sflow/global/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "global"
        self.a10_url="/axapi/v3/sflow/global/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


