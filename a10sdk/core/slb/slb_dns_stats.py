from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param nat_resp: {"description": "(NAT) No. of responses", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "2"}
    :param slb_resp_no_match: {"description": "No. of requests with no response", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "2"}
    :param nat_xid_reused: {"description": "(NAT) No. of requests reusing a transaction id", "format": "counter", "type": "number", "oid": "13", "optional": true, "size": "2"}
    :param slb_req: {"description": "No. of requests", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "2"}
    :param slb_no_resp: {"description": "No. of resource failures", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "2"}
    :param nat_req: {"description": "(NAT) No. of requests", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "2"}
    :param slb_req_rexmit: {"description": "No. of request retransmits", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "2"}
    :param nat_no_resource: {"description": "(NAT) No. of resource failures", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "2"}
    :param nat_no_resp: {"description": "(NAT) No. of resource failures", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "2"}
    :param nat_req_rexmit: {"description": "(NAT) No. of request retransmits", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "2"}
    :param nat_resp_no_match: {"description": "(NAT) No. of requests with no response", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "2"}
    :param slb_no_resource: {"description": "No. of resource failures", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "2"}
    :param slb_resp: {"description": "No. of responses", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "2"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.nat_resp = ""
        self.slb_resp_no_match = ""
        self.nat_xid_reused = ""
        self.slb_req = ""
        self.slb_no_resp = ""
        self.nat_req = ""
        self.slb_req_rexmit = ""
        self.nat_no_resource = ""
        self.nat_no_resp = ""
        self.nat_req_rexmit = ""
        self.nat_resp_no_match = ""
        self.slb_no_resource = ""
        self.slb_resp = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Dns(A10BaseClass):
    
    """Class Description::
    Statistics for the object dns.

    Class dns supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/dns/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "dns"
        self.a10_url="/axapi/v3/slb/dns/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


