from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "outbound-tcp-packets-received", "outbound-udp-packets-received", "outbound-icmp-packets-received", "outbound-other-packets-received", "outbound-packets-drop", "outbound-ipv6-dest-unreachable", "outbound-fragment-ipv6", "inbound-tcp-packets-received", "inbound-udp-packets-received", "inbound-icmp-packets-received", "inbound-other-packets-received", "inbound-packets-drop", "inbound-ipv4-dest-unreachable", "inbound-fragment-ipv4", "inbound-tunnel-fragment-ipv6", "vport-matched", "unknown-delegated-prefix", "packet-too-big", "not-local-ip", "fragment-error", "other-error"], "type": "string", "description": "'all': all; 'outbound-tcp-packets-received': Outbound TCP packets received; 'outbound-udp-packets-received': Outbound UDP packets received; 'outbound-icmp-packets-received': Outbound ICMP packets received; 'outbound-other-packets-received': Outbound other packets received; 'outbound-packets-drop': Outbound packets dropped; 'outbound-ipv6-dest-unreachable': Outbound IPv6 destination unreachable; 'outbound-fragment-ipv6': Outbound Fragmented IPv6; 'inbound-tcp-packets-received': Inbound TCP packets received; 'inbound-udp-packets-received': Inbound UDP packets received; 'inbound-icmp-packets-received': Inbound ICMP packets received; 'inbound-other-packets-received': Inbound other packets received; 'inbound-packets-drop': Inbound packets dropped; 'inbound-ipv4-dest-unreachable': Inbound IPv4 destination unreachable; 'inbound-fragment-ipv4': Inbound Fragmented IPv4; 'inbound-tunnel-fragment-ipv6': Inbound Fragmented IPv6 in tunnel; 'vport-matched': Traffic match SLB virtual port; 'unknown-delegated-prefix': Unknown 6rd delegated prefix; 'packet-too-big': Packet too big; 'not-local-ip': Not local IP; 'fragment-error': Fragment processing errors; 'other-error': Other errors; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Domain(A10BaseClass):
    
    """Class Description::
    sixrd Domain.

    Class domain supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ipv6_prefix: {"optional": true, "type": "string", "description": "IPv6 prefix", "format": "ipv6-address-plen"}
    :param name: {"description": "6rd Domain name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "outbound-tcp-packets-received", "outbound-udp-packets-received", "outbound-icmp-packets-received", "outbound-other-packets-received", "outbound-packets-drop", "outbound-ipv6-dest-unreachable", "outbound-fragment-ipv6", "inbound-tcp-packets-received", "inbound-udp-packets-received", "inbound-icmp-packets-received", "inbound-other-packets-received", "inbound-packets-drop", "inbound-ipv4-dest-unreachable", "inbound-fragment-ipv4", "inbound-tunnel-fragment-ipv6", "vport-matched", "unknown-delegated-prefix", "packet-too-big", "not-local-ip", "fragment-error", "other-error"], "type": "string", "description": "'all': all; 'outbound-tcp-packets-received': Outbound TCP packets received; 'outbound-udp-packets-received': Outbound UDP packets received; 'outbound-icmp-packets-received': Outbound ICMP packets received; 'outbound-other-packets-received': Outbound other packets received; 'outbound-packets-drop': Outbound packets dropped; 'outbound-ipv6-dest-unreachable': Outbound IPv6 destination unreachable; 'outbound-fragment-ipv6': Outbound Fragmented IPv6; 'inbound-tcp-packets-received': Inbound TCP packets received; 'inbound-udp-packets-received': Inbound UDP packets received; 'inbound-icmp-packets-received': Inbound ICMP packets received; 'inbound-other-packets-received': Inbound other packets received; 'inbound-packets-drop': Inbound packets dropped; 'inbound-ipv4-dest-unreachable': Inbound IPv4 destination unreachable; 'inbound-fragment-ipv4': Inbound Fragmented IPv4; 'inbound-tunnel-fragment-ipv6': Inbound Fragmented IPv6 in tunnel; 'vport-matched': Traffic match SLB virtual port; 'unknown-delegated-prefix': Unknown 6rd delegated prefix; 'packet-too-big': Packet too big; 'not-local-ip': Not local IP; 'fragment-error': Fragment processing errors; 'other-error': Other errors; ", "format": "enum"}}}]}
    :param mtu: {"description": "Tunnel MTU", "format": "number", "type": "number", "maximum": 1480, "minimum": 1280, "optional": true}
    :param ce_ipv4_netmask: {"optional": true, "type": "string", "description": "Mask length", "format": "ipv4-netmask-brief"}
    :param ce_ipv4_network: {"optional": true, "type": "string", "description": "Customer Edge IPv4 network", "format": "ipv4-address"}
    :param br_ipv4_address: {"optional": true, "type": "string", "description": "6rd BR IPv4 address", "format": "ipv4-address"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/sixrd/domain/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "domain"
        self.a10_url="/axapi/v3/cgnv6/sixrd/domain/{name}"
        self.DeviceProxy = ""
        self.ipv6_prefix = ""
        self.name = ""
        self.sampling_enable = []
        self.mtu = ""
        self.ce_ipv4_netmask = ""
        self.ce_ipv4_network = ""
        self.br_ipv4_address = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


