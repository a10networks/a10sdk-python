from a10sdk.common.A10BaseClass import A10BaseClass


class SlbServerStatistics(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param out_bytes: {"type": "number", "format": "number"}
    :param in_bytes: {"type": "number", "format": "number"}
    :param p_conn: {"type": "number", "format": "number"}
    :param out_pkts: {"type": "number", "format": "number"}
    :param cur_conn: {"type": "number", "format": "number"}
    :param time: {"type": "number", "format": "number"}
    :param in_pkts: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "slb-server-statistics"
        self.DeviceProxy = ""
        self.out_bytes = ""
        self.in_bytes = ""
        self.p_conn = ""
        self.out_pkts = ""
        self.cur_conn = ""
        self.time = ""
        self.in_pkts = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param slb_server_statistics: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"out_bytes": {"type": "number", "format": "number"}, "in_bytes": {"type": "number", "format": "number"}, "p_conn": {"type": "number", "format": "number"}, "out_pkts": {"type": "number", "format": "number"}, "cur_conn": {"type": "number", "format": "number"}, "time": {"type": "number", "format": "number"}, "in_pkts": {"type": "number", "format": "number"}, "optional": true}}]}
    :param end_time: {"type": "number", "format": "number"}
    :param start_time: {"type": "number", "format": "number"}
    :param slb_service_group_name: {"type": "string", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.slb_server_statistics = []
        self.end_time = ""
        self.start_time = ""
        self.slb_service_group_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class SlbServiceGroup(A10BaseClass):
    
    """Class Description::
    Operational Status for the object slb-service-group.

    Class slb-service-group supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/rrd/slb-service-group/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "slb-service-group"
        self.a10_url="/axapi/v3/rrd/slb-service-group/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


