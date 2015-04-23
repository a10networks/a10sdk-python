from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param bandwidth_red_dropped_bytes: {"optional": true, "size": "8", "type": "number", "oid": "19", "format": "counter"}
    :param bandwidth_bytes: {"optional": true, "size": "8", "type": "number", "oid": "13", "format": "counter"}
    :param bandwidth_dropped_bytes: {"optional": true, "size": "8", "type": "number", "oid": "17", "format": "counter"}
    :param conform_packets: {"optional": true, "size": "8", "type": "number", "oid": "11", "format": "counter"}
    :param dropped_packets: {"optional": true, "size": "8", "type": "number", "oid": "7", "format": "counter"}
    :param packets: {"optional": true, "size": "8", "type": "number", "oid": "5", "format": "counter"}
    :param bytes: {"optional": true, "size": "8", "type": "number", "oid": "4", "format": "counter"}
    :param exceed_packets: {"optional": true, "size": "8", "type": "number", "oid": "12", "format": "counter"}
    :param bandwidth_packets: {"optional": true, "size": "8", "type": "number", "oid": "14", "format": "counter"}
    :param total_session: {"optional": true, "size": "8", "type": "number", "oid": "9", "format": "counter"}
    :param peak_rate: {"optional": true, "size": "8", "type": "number", "oid": "3", "format": "counter"}
    :param current_rate: {"optional": true, "size": "8", "type": "number", "oid": "1", "format": "counter"}
    :param active_session: {"optional": true, "size": "8", "type": "number", "oid": "8", "format": "counter"}
    :param everage_rate: {"optional": true, "size": "8", "type": "number", "oid": "2", "format": "counter"}
    :param dropped_bytes: {"optional": true, "size": "8", "type": "number", "oid": "6", "format": "counter"}
    :param bandwidth_queue_bytes: {"optional": true, "size": "8", "type": "number", "oid": "15", "format": "counter"}
    :param bandwidth_dropped_packets: {"optional": true, "size": "8", "type": "number", "oid": "18", "format": "counter"}
    :param bandwidth_red_dropped_packets: {"optional": true, "size": "8", "type": "number", "oid": "20", "format": "counter"}
    :param bandwidth_queue_packets: {"optional": true, "size": "8", "type": "number", "oid": "16", "format": "counter"}
    :param dropped_session: {"optional": true, "size": "8", "type": "number", "oid": "10", "format": "counter"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.bandwidth_red_dropped_bytes = ""
        self.bandwidth_bytes = ""
        self.bandwidth_dropped_bytes = ""
        self.conform_packets = ""
        self.dropped_packets = ""
        self.packets = ""
        self.A10WW_bytes = ""
        self.exceed_packets = ""
        self.bandwidth_packets = ""
        self.total_session = ""
        self.peak_rate = ""
        self.current_rate = ""
        self.active_session = ""
        self.everage_rate = ""
        self.dropped_bytes = ""
        self.bandwidth_queue_bytes = ""
        self.bandwidth_dropped_packets = ""
        self.bandwidth_red_dropped_packets = ""
        self.bandwidth_queue_packets = ""
        self.dropped_session = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Class(A10BaseClass):
    
    """Class Description::
    Statistics for the object class.

    Class class supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param name: {"description": "class name", "format": "string", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 31, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/qos/policy/{name}/class/{name}/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "class"
        self.a10_url="/axapi/v3/qos/policy/{name}/class/{name}/stats"
        self.DeviceProxy = ""
        self.stats = {}
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


