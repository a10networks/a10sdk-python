from a10sdk.common.A10BaseClass import A10BaseClass


class DnsDomainExpect(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param dns_domain_response: {"minLength": 1, "maxLength": 31, "type": "string", "description": "Specify response code range (e.g. 0,1-5) (Format is xx,xx-xx (xx between [0,15]))", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "dns-domain-expect"
        self.DeviceProxy = ""
        self.dns_domain_response = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class DnsIpv6Expect(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param dns_ipv6_response: {"minLength": 1, "maxLength": 31, "type": "string", "description": "Specify response code range (e.g. 0,1-5) (Format is xx,xx-xx (xx between [0,15]))", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "dns-ipv6-expect"
        self.DeviceProxy = ""
        self.dns_ipv6_response = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class DnsIpv4Expect(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param dns_ipv4_response: {"minLength": 1, "maxLength": 31, "type": "string", "description": "Specify response code range (e.g. 0,1-5) (Format is xx,xx-xx (xx between [0,15]))", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "dns-ipv4-expect"
        self.DeviceProxy = ""
        self.dns_ipv4_response = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Dns(A10BaseClass):
    
    """Class Description::
    DNS type.

    Class dns supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param dns_domain_type: {"optional": true, "enum": ["A", "CNAME", "SOA", "PTR", "MX", "TXT", "AAAA"], "type": "string", "description": "'A': Used for storing Ipv4 address (default); 'CNAME': Canonical name for a DNS alias; 'SOA': Start of authority; 'PTR': Domain name pointer; 'MX': Mail exchanger; 'TXT': Text string; 'AAAA': Used for storing Ipv6 128-bits address; ", "format": "enum"}
    :param dns_domain: {"description": "Specify fully qualified domain name of the host", "format": "string", "minLength": 1, "optional": true, "maxLength": 255, "not": "dns-ip-key", "type": "string"}
    :param dns_domain_recurse: {"description": "'enabled': Set the recursion bit; 'disabled': Clear the recursion bit; ", "format": "enum", "default": "enabled", "type": "string", "enum": ["enabled", "disabled"], "optional": true}
    :param dns_ipv4_recurse: {"description": "'enabled': Set the recursion bit; 'disabled': Clear the recursion bit; ", "format": "enum", "default": "enabled", "type": "string", "enum": ["enabled", "disabled"], "optional": true}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param dns_ipv6_port: {"description": "Specify DNS port, default is 53 (DNS Port(default 53))", "format": "number", "default": 53, "optional": true, "maximum": 65534, "minimum": 1, "type": "number"}
    :param dns_ipv4_port: {"description": "Specify DNS port, default is 53 (DNS Port(default 53))", "format": "number", "default": 53, "optional": true, "maximum": 65534, "minimum": 1, "type": "number"}
    :param dns_domain_port: {"description": "Specify DNS port, default is 53 (DNS Port(default 53))", "format": "number", "default": 53, "optional": true, "maximum": 65534, "minimum": 1, "type": "number"}
    :param dns_ipv6_recurse: {"description": "'enabled': Set the recursion bit; 'disabled': Clear the recursion bit; ", "format": "enum", "default": "enabled", "type": "string", "enum": ["enabled", "disabled"], "optional": true}
    :param dns_ipv6_tcp: {"default": 0, "optional": true, "type": "number", "description": "Configure DNS transport over TCP, default is UDP", "format": "flag"}
    :param dns_domain_tcp: {"default": 0, "optional": true, "type": "number", "description": "Configure DNS transport over TCP, default is UDP", "format": "flag"}
    :param dns: {"default": 0, "optional": true, "type": "number", "description": "DNS type", "format": "flag"}
    :param dns_ipv4_tcp: {"default": 0, "optional": true, "type": "number", "description": "Configure DNS transport over TCP, default is UDP", "format": "flag"}
    :param dns_ipv4_addr: {"not": "dns-ipv6-addr", "optional": true, "type": "string", "description": "Specify IPv4 address", "format": "ipv4-address"}
    :param dns_ipv6_addr: {"not": "dns-ipv4-addr", "optional": true, "type": "string", "description": "Specify IPv6 address", "format": "ipv6-address"}
    :param dns_ip_key: {"description": "Reverse DNS lookup (Specify IPv4 or IPv6 address)", "format": "flag", "default": 0, "optional": true, "not": "dns-domain", "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/health/monitor/{name}/method/dns`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "dns"
        self.a10_url="/axapi/v3/health/monitor/{name}/method/dns"
        self.DeviceProxy = ""
        self.dns_domain_type = ""
        self.dns_domain = ""
        self.dns_domain_recurse = ""
        self.dns_ipv4_recurse = ""
        self.uuid = ""
        self.dns_ipv6_port = ""
        self.dns_domain_expect = {}
        self.dns_ipv4_port = ""
        self.dns_ipv6_expect = {}
        self.dns_domain_port = ""
        self.dns_ipv6_recurse = ""
        self.dns_ipv6_tcp = ""
        self.dns_ipv4_expect = {}
        self.dns_domain_tcp = ""
        self.dns = ""
        self.dns_ipv4_tcp = ""
        self.dns_ipv4_addr = ""
        self.dns_ipv6_addr = ""
        self.dns_ip_key = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


