from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param bad_hop_limit: {"description": "R.S. Bad Hop Limit", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "2"}
    :param bad_icmpv6_code: {"description": "R.S. Unknown ICMPv6 Code", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "2"}
    :param bad_icmpv6_csum: {"description": "R.S. Bad ICMPv6 Checksum", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "2"}
    :param truncated: {"description": "R.S. Truncated", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "2"}
    :param no_free_buffers: {"description": "No Free Buffers to send R.A.", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "2"}
    :param rate_limit: {"description": "R.S. Rate Limited", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "2"}
    :param l2_addr_and_unspec: {"description": "R.S. Src Link-Layer Option and Unspecified Address", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "2"}
    :param bad_icmpv6_option: {"description": "R.S. Bad ICMPv6 Option", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "2"}
    :param periodic_sent: {"description": "Periodic Router Advertisements (R.A.) Sent", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "2"}
    :param good_recv: {"description": "Good Router Solicitations (R.S.) Received", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "2"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.bad_hop_limit = ""
        self.bad_icmpv6_code = ""
        self.bad_icmpv6_csum = ""
        self.truncated = ""
        self.no_free_buffers = ""
        self.rate_limit = ""
        self.l2_addr_and_unspec = ""
        self.bad_icmpv6_option = ""
        self.periodic_sent = ""
        self.good_recv = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class NdiscRa(A10BaseClass):
    
    """Class Description::
    Statistics for the object ndisc-ra.

    Class ndisc-ra supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/system/ndisc-ra/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ndisc-ra"
        self.a10_url="/axapi/v3/system/ndisc-ra/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


