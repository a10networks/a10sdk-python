from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param num_tx_pkts: {"description": "Transmitted packtes", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param rate_byte_rcvd: {"description": "Byte received rate bits/sec", "format": "counter", "type": "number", "oid": "14", "optional": true, "size": "8"}
    :param num_total_tx_bytes: {"description": "Transmitte bytes", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param rate_pkt_rcvd: {"description": "Packet received rate packets/sec", "format": "counter", "type": "number", "oid": "13", "optional": true, "size": "8"}
    :param num_multicast_pkts: {"description": "Received multicasts", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param num_unicast_pkts: {"description": "Received unicasts", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param num_broadcast_tx_pkts: {"description": "Transmitted broadcasts", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}
    :param num_broadcast_pkts: {"description": "Received braodcasts", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param num_multicast_tx_pkts: {"description": "Transmitted multicasts", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}
    :param rate_byte_sent: {"description": "Byte sent rate bits/sec", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "8"}
    :param num_unicast_tx_pkts: {"description": "Trasnmitted unicasts", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param num_total_bytes: {"description": "Input bytes", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param load_interval: {"description": "Load Interval", "format": "counter", "type": "number", "oid": "15", "optional": true, "size": "8"}
    :param num_pkts: {"description": "Input packets", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param rate_pkt_sent: {"description": "Packet sent rate packets/sec", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.num_tx_pkts = ""
        self.rate_byte_rcvd = ""
        self.num_total_tx_bytes = ""
        self.rate_pkt_rcvd = ""
        self.num_multicast_pkts = ""
        self.num_unicast_pkts = ""
        self.num_broadcast_tx_pkts = ""
        self.num_broadcast_pkts = ""
        self.num_multicast_tx_pkts = ""
        self.rate_byte_sent = ""
        self.num_unicast_tx_pkts = ""
        self.num_total_bytes = ""
        self.load_interval = ""
        self.num_pkts = ""
        self.rate_pkt_sent = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ve(A10BaseClass):
    
    """Class Description::
    Statistics for the object ve.

    Class ve supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ifnum: {"optional": false, "oid": "1001", "type": "number", "description": "Virtual ethernet interface number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/interface/ve/{ifnum}/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "ifnum"]

        self.b_key = "ve"
        self.a10_url="/axapi/v3/interface/ve/{ifnum}/stats"
        self.DeviceProxy = ""
        self.ifnum = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


