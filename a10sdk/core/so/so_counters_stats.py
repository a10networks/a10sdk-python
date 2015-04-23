from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param so_pkts_conn_sync_fail: {"description": "Total connection sync failures", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}
    :param so_pkts_new_conn_redirect: {"description": "Total packets redirected for a new connection", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param so_pkts_conn_l7_sync: {"description": "Total L7 connection syncs", "format": "counter", "type": "number", "oid": "13", "optional": true, "size": "8"}
    :param so_pkts_nat_reserve_fail: {"description": "Total NAT reserve failures", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "8"}
    :param so_pkts_errors: {"description": "Total packet errors", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param so_pkts_conn_redirect: {"description": "Total packets redirected for an established connection", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param so_pkts_redirect: {"description": "Total packets redirected", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}
    :param so_pkts_conn_in: {"description": "Total packets processed for an established connection", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param so_pkts_new_conn_in: {"description": "Total packets processed for a new connection", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param so_pkts_nat_release_fail: {"description": "Total NAT release failures", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "8"}
    :param so_pkts_dropped: {"description": "Total packets dropped", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param so_pkts_out: {"description": "Total packets sent out", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param so_pkts_in: {"description": "Total packets in-coming", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param so_pkts_redirect_conn_aged_out: {"description": "Total redirect conns aged out", "format": "counter", "type": "number", "oid": "15", "optional": true, "size": "8"}
    :param so_pkts_conn_l4_sync: {"description": "Total L4 connection syncs", "format": "counter", "type": "number", "oid": "14", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.so_pkts_conn_sync_fail = ""
        self.so_pkts_new_conn_redirect = ""
        self.so_pkts_conn_l7_sync = ""
        self.so_pkts_nat_reserve_fail = ""
        self.so_pkts_errors = ""
        self.so_pkts_conn_redirect = ""
        self.so_pkts_redirect = ""
        self.so_pkts_conn_in = ""
        self.so_pkts_new_conn_in = ""
        self.so_pkts_nat_release_fail = ""
        self.so_pkts_dropped = ""
        self.so_pkts_out = ""
        self.so_pkts_in = ""
        self.so_pkts_redirect_conn_aged_out = ""
        self.so_pkts_conn_l4_sync = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class SoCounters(A10BaseClass):
    
    """Class Description::
    Statistics for the object so-counters.

    Class so-counters supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/so-counters/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "so-counters"
        self.a10_url="/axapi/v3/so-counters/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


