from a10sdk.common.A10BaseClass import A10BaseClass


class EthernetStatistics(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param tx_bits: {"type": "number", "format": "number"}
    :param rx_packets: {"type": "number", "format": "number"}
    :param rx_drop: {"type": "number", "format": "number"}
    :param tx_error: {"type": "number", "format": "number"}
    :param rx_error: {"type": "number", "format": "number"}
    :param time: {"type": "number", "format": "number"}
    :param tx_drop: {"type": "number", "format": "number"}
    :param tx_packets: {"type": "number", "format": "number"}
    :param rx_bits: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ethernet-statistics"
        self.DeviceProxy = ""
        self.tx_bits = ""
        self.rx_packets = ""
        self.rx_drop = ""
        self.tx_error = ""
        self.rx_error = ""
        self.time = ""
        self.tx_drop = ""
        self.tx_packets = ""
        self.rx_bits = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ethernet_index: {"type": "number", "format": "number"}
    :param end_time: {"type": "number", "format": "number"}
    :param start_time: {"type": "number", "format": "number"}
    :param ethernet_statistics: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"tx_bits": {"type": "number", "format": "number"}, "rx_packets": {"type": "number", "format": "number"}, "rx_drop": {"type": "number", "format": "number"}, "optional": true, "tx_error": {"type": "number", "format": "number"}, "rx_error": {"type": "number", "format": "number"}, "time": {"type": "number", "format": "number"}, "tx_drop": {"type": "number", "format": "number"}, "tx_packets": {"type": "number", "format": "number"}, "rx_bits": {"type": "number", "format": "number"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.ethernet_index = ""
        self.end_time = ""
        self.start_time = ""
        self.ethernet_statistics = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ethernet(A10BaseClass):
    
    """Class Description::
    Operational Status for the object ethernet.

    Class ethernet supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/rrd/ethernet/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ethernet"
        self.a10_url="/axapi/v3/rrd/ethernet/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


