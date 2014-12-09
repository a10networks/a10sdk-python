from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param limit_total_drop: {"description": "Total rate limit drops", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "2"}
    :param v6_limit_intf_drop: {"description": "Interfaces rate limit drops (v6)", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "2"}
    :param limit_vserver_drop: {"description": "Virtual Server rate limit drops", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "2"}
    :param v6_limit_vserver_drop: {"description": "Virtual Server rate limit drops (v6)", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "2"}
    :param over_limit_drop: {"description": "Over limit drops", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "2"}
    :param v6_lockup_time_left: {"description": "Lockup time left (v6)", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "8"}
    :param v6_limit_total_drop: {"description": "Total rate limit drops (v6)", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "2"}
    :param v6_curr_rate: {"description": "Current rate (v6)", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "8"}
    :param lockup_time_left: {"description": "Lockup time left", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param limit_intf_drop: {"description": "Interfaces rate limit drops", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "2"}
    :param curr_rate: {"description": "Current rate", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param v6_over_limit_drop: {"description": "Over limit drops (v6)", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "2"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.limit_total_drop = ""
        self.v6_limit_intf_drop = ""
        self.limit_vserver_drop = ""
        self.v6_limit_vserver_drop = ""
        self.over_limit_drop = ""
        self.v6_lockup_time_left = ""
        self.v6_limit_total_drop = ""
        self.v6_curr_rate = ""
        self.lockup_time_left = ""
        self.limit_intf_drop = ""
        self.curr_rate = ""
        self.v6_over_limit_drop = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class IcmpRate(A10BaseClass):
    
    """Class Description::
    Statistics for the object icmp-rate.

    Class icmp-rate supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/system/icmp-rate/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "icmp-rate"
        self.a10_url="/axapi/v3/system/icmp-rate/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


