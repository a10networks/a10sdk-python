from a10sdk.common.A10BaseClass import A10BaseClass


class Sixrd(A10BaseClass):
    
    """Class Description::
    Configure IPv6 Rapid Deployment (sixrd).

    Class sixrd supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param domain_list: {"minItems": 1, "items": {"type": "domain"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"ipv6-prefix": {"optional": true, "type": "string", "description": "IPv6 prefix", "format": "ipv6-address-plen"}, "name": {"description": "6rd Domain name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "sampling-enable": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "outbound-tcp-packets-received", "outbound-udp-packets-received", "outbound-icmp-packets-received", "outbound-other-packets-received", "outbound-packets-drop", "outbound-ipv6-dest-unreachable", "outbound-fragment-ipv6", "inbound-tcp-packets-received", "inbound-udp-packets-received", "inbound-icmp-packets-received", "inbound-other-packets-received", "inbound-packets-drop", "inbound-ipv4-dest-unreachable", "inbound-fragment-ipv4", "inbound-tunnel-fragment-ipv6", "vport-matched", "unknown-delegated-prefix", "packet-too-big", "not-local-ip", "fragment-error", "other-error"], "type": "string", "description": "'all': all; 'outbound-tcp-packets-received': Outbound TCP packets received; 'outbound-udp-packets-received': Outbound UDP packets received; 'outbound-icmp-packets-received': Outbound ICMP packets received; 'outbound-other-packets-received': Outbound other packets received; 'outbound-packets-drop': Outbound packets dropped; 'outbound-ipv6-dest-unreachable': Outbound IPv6 destination unreachable; 'outbound-fragment-ipv6': Outbound Fragmented IPv6; 'inbound-tcp-packets-received': Inbound TCP packets received; 'inbound-udp-packets-received': Inbound UDP packets received; 'inbound-icmp-packets-received': Inbound ICMP packets received; 'inbound-other-packets-received': Inbound other packets received; 'inbound-packets-drop': Inbound packets dropped; 'inbound-ipv4-dest-unreachable': Inbound IPv4 destination unreachable; 'inbound-fragment-ipv4': Inbound Fragmented IPv4; 'inbound-tunnel-fragment-ipv6': Inbound Fragmented IPv6 in tunnel; 'vport-matched': Traffic match SLB virtual port; 'unknown-delegated-prefix': Unknown 6rd delegated prefix; 'packet-too-big': Packet too big; 'not-local-ip': Not local IP; 'fragment-error': Fragment processing errors; 'other-error': Other errors; ", "format": "enum"}}}]}, "mtu": {"description": "Tunnel MTU", "format": "number", "type": "number", "maximum": 1480, "minimum": 1280, "optional": true}, "ce-ipv4-netmask": {"optional": true, "type": "string", "description": "Mask length", "format": "ipv4-netmask-brief"}, "ce-ipv4-network": {"optional": true, "type": "string", "description": "Customer Edge IPv4 network", "format": "ipv4-address"}, "br-ipv4-address": {"optional": true, "type": "string", "description": "6rd BR IPv4 address", "format": "ipv4-address"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/cgnv6/sixrd/domain/{name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/sixrd`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "sixrd"
        self.a10_url="/axapi/v3/cgnv6/sixrd"
        self.DeviceProxy = ""
        self.domain_list = []
        self.fragmentation = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


