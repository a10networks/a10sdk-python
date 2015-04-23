from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "so_pkts_conn_in", "so_pkts_conn_redirect", "so_pkts_dropped", "so_pkts_errors", "so_pkts_in", "so_pkts_new_conn_in", "so_pkts_new_conn_redirect", "so_pkts_out", "so_pkts_redirect", "so_pkts_conn_sync_fail", "so_pkts_nat_reserve_fail", "so_pkts_nat_release_fail", "so_pkts_conn_l7_sync", "so_pkts_conn_l4_sync", "so_pkts_redirect_conn_aged_out"], "type": "string", "description": "'all': all; 'so_pkts_conn_in': Total packets processed for an established connection; 'so_pkts_conn_redirect': Total packets redirected for an established connection; 'so_pkts_dropped': Total packets dropped; 'so_pkts_errors': Total packet errors; 'so_pkts_in': Total packets in-coming; 'so_pkts_new_conn_in': Total packets processed for a new connection; 'so_pkts_new_conn_redirect': Total packets redirected for a new connection; 'so_pkts_out': Total packets sent out; 'so_pkts_redirect': Total packets redirected; 'so_pkts_conn_sync_fail': Total connection sync failures; 'so_pkts_nat_reserve_fail': Total NAT reserve failures; 'so_pkts_nat_release_fail': Total NAT release failures; 'so_pkts_conn_l7_sync': Total L7 connection syncs; 'so_pkts_conn_l4_sync': Total L4 connection syncs; 'so_pkts_redirect_conn_aged_out': Total redirect conns aged out; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class SoCounters(A10BaseClass):
    
    """    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "so_pkts_conn_in", "so_pkts_conn_redirect", "so_pkts_dropped", "so_pkts_errors", "so_pkts_in", "so_pkts_new_conn_in", "so_pkts_new_conn_redirect", "so_pkts_out", "so_pkts_redirect", "so_pkts_conn_sync_fail", "so_pkts_nat_reserve_fail", "so_pkts_nat_release_fail", "so_pkts_conn_l7_sync", "so_pkts_conn_l4_sync", "so_pkts_redirect_conn_aged_out"], "type": "string", "description": "'all': all; 'so_pkts_conn_in': Total packets processed for an established connection; 'so_pkts_conn_redirect': Total packets redirected for an established connection; 'so_pkts_dropped': Total packets dropped; 'so_pkts_errors': Total packet errors; 'so_pkts_in': Total packets in-coming; 'so_pkts_new_conn_in': Total packets processed for a new connection; 'so_pkts_new_conn_redirect': Total packets redirected for a new connection; 'so_pkts_out': Total packets sent out; 'so_pkts_redirect': Total packets redirected; 'so_pkts_conn_sync_fail': Total connection sync failures; 'so_pkts_nat_reserve_fail': Total NAT reserve failures; 'so_pkts_nat_release_fail': Total NAT release failures; 'so_pkts_conn_l7_sync': Total L7 connection syncs; 'so_pkts_conn_l4_sync': Total L4 connection syncs; 'so_pkts_redirect_conn_aged_out': Total redirect conns aged out; ", "format": "enum"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Show scaleout statistics.

    Class so-counters supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/so-counters`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "so-counters"
        self.a10_url="/axapi/v3/so-counters"
        self.DeviceProxy = ""
        self.sampling_enable = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


