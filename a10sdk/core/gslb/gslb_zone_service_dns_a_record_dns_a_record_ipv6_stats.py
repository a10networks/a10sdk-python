from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param hits: {"description": "Number of times the record has been used", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.hits = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class DnsARecordIpv6(A10BaseClass):
    
    """Class Description::
    Statistics for the object dns-a-record-ipv6.

    Class dns-a-record-ipv6 supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param dns_a_record_ipv6: {"optional": false, "oid": "1001", "type": "string", "description": "IPV6 address", "format": "ipv6-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/zone/{name}/service/{service_port}+{service_name}/dns-a-record/dns-a-record-ipv6/{dns_a_record_ipv6}/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "dns_a_record_ipv6"]

        self.b_key = "dns-a-record-ipv6"
        self.a10_url="/axapi/v3/gslb/zone/{name}/service/{service_port}+{service_name}/dns-a-record/dns-a-record-ipv6/{dns_a_record_ipv6}/stats"
        self.DeviceProxy = ""
        self.dns_a_record_ipv6 = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


