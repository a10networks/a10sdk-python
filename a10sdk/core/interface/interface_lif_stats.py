from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param num_tx_pkts: {"optional": true, "size": "8", "type": "number", "oid": "6", "format": "counter"}
    :param dropped_dis_tx_pkts: {"optional": true, "size": "8", "type": "number", "oid": "13", "format": "counter"}
    :param num_total_tx_bytes: {"optional": true, "size": "8", "type": "number", "oid": "7", "format": "counter"}
    :param num_multicast_pkts: {"optional": true, "size": "2", "type": "number", "oid": "5", "format": "counter"}
    :param num_unicast_pkts: {"optional": true, "size": "8", "type": "number", "oid": "3", "format": "counter"}
    :param num_broadcast_tx_pkts: {"optional": true, "size": "8", "type": "number", "oid": "9", "format": "counter"}
    :param num_broadcast_pkts: {"optional": true, "size": "8", "type": "number", "oid": "4", "format": "counter"}
    :param num_multicast_tx_pkts: {"optional": true, "size": "8", "type": "number", "oid": "10", "format": "counter"}
    :param num_unicast_tx_pkts: {"optional": true, "size": "8", "type": "number", "oid": "8", "format": "counter"}
    :param dropped_rx_pkts: {"optional": true, "size": "8", "type": "number", "oid": "12", "format": "counter"}
    :param num_total_bytes: {"optional": true, "size": "8", "type": "number", "oid": "2", "format": "counter"}
    :param num_pkts: {"optional": true, "size": "8", "type": "number", "oid": "1", "format": "counter"}
    :param dropped_dis_rx_pkts: {"optional": true, "size": "8", "type": "number", "oid": "11", "format": "counter"}
    :param dropped_tx_pkts: {"optional": true, "size": "8", "type": "number", "oid": "14", "format": "counter"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.num_tx_pkts = ""
        self.dropped_dis_tx_pkts = ""
        self.num_total_tx_bytes = ""
        self.num_multicast_pkts = ""
        self.num_unicast_pkts = ""
        self.num_broadcast_tx_pkts = ""
        self.num_broadcast_pkts = ""
        self.num_multicast_tx_pkts = ""
        self.num_unicast_tx_pkts = ""
        self.dropped_rx_pkts = ""
        self.num_total_bytes = ""
        self.num_pkts = ""
        self.dropped_dis_rx_pkts = ""
        self.dropped_tx_pkts = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Lif(A10BaseClass):
    
    """Class Description::
    Statistics for the object lif.

    Class lif supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ifnum: {"description": "Lif interface number", "format": "number", "optional": false, "oid": "1001", "maximum": 128, "minimum": 1, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/interface/lif/{ifnum}/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "ifnum"]

        self.b_key = "lif"
        self.a10_url="/axapi/v3/interface/lif/{ifnum}/stats"
        self.DeviceProxy = ""
        self.ip = {}
        self.ifnum = ""
        self.isis = {}
        self.stats = {}
        self.bfd = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


