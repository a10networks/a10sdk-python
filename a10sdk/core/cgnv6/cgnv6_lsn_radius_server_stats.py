from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param radius_request_dropped: {"description": "RADIUS Request Dropped (Malformed Packet)", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param imsi_received: {"description": "IMSI Received", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param ha_standby_dropped: {"description": "HA Standby Dropped", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param custom_received: {"description": "Custom attribute Received", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param imei_received: {"description": "IMEI Received", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param radius_table_full: {"description": "RADIUS Request Dropped (Table Full)", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param msisdn_received: {"description": "MSISDN Received", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param radius_request_received: {"description": "RADIUS Request Received", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.radius_request_dropped = ""
        self.imsi_received = ""
        self.ha_standby_dropped = ""
        self.custom_received = ""
        self.imei_received = ""
        self.radius_table_full = ""
        self.msisdn_received = ""
        self.radius_request_received = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Server(A10BaseClass):
    
    """Class Description::
    Statistics for the object server.

    Class server supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/lsn/radius/server/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "server"
        self.a10_url="/axapi/v3/cgnv6/lsn/radius/server/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


