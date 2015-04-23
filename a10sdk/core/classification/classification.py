from a10sdk.common.A10BaseClass import A10BaseClass


class PortList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param end_port: {"description": "Add a range of ports into the current port list (Specify port number)", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": true}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param start_port: {"description": "Specify port number", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": false}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "port-list"
        self.DeviceProxy = ""
        self.end_port = ""
        self.uuid = ""
        self.start_port = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class PortListList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param listname: {"description": "Specify port list name", "format": "string", "minLength": 1, "optional": false, "maxLength": 31, "type": "string"}
    :param port_list: {"minItems": 1, "items": {"type": "port"}, "uniqueItems": true, "array": [{"required": ["start-port"], "properties": {"end-port": {"description": "Add a range of ports into the current port list (Specify port number)", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": true}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "start-port": {"description": "Specify port number", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": false}}}], "type": "array", "$ref": "/axapi/v3/classification/port-list/{listname}/port/{start-port}"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "port-list-list"
        self.DeviceProxy = ""
        self.listname = ""
        self.port_list = []
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class IpList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ipv4_start_ip: {"optional": false, "type": "string", "description": "Specify IP address (A.B.C.D)", "format": "ipv4-address"}
    :param mask: {"optional": true, "type": "string", "description": "Specify IP network mask", "format": "ipv4-netmask"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param ipv4_end_ip: {"optional": true, "type": "string", "description": "Add a range of IPs into the current IP list (Specify IP address (A.B.C.D))", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ip-list"
        self.DeviceProxy = ""
        self.ipv4_start_ip = ""
        self.mask = ""
        self.uuid = ""
        self.ipv4_end_ip = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ipv6List(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ipv6_subnet: {"optional": false, "type": "string", "description": "Specify IPv6 subnet range", "format": "ipv6-address-plen"}
    :param ipv6_end_ip: {"optional": true, "type": "string", "description": "Add a range of IPs into the current IP list (Specify IPv6 address)", "format": "ipv6-address"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param ipv6_start_ip: {"optional": false, "type": "string", "description": "Specify IPv6 address", "format": "ipv6-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ipv6-list"
        self.DeviceProxy = ""
        self.ipv6_subnet = ""
        self.ipv6_end_ip = ""
        self.uuid = ""
        self.ipv6_start_ip = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class IpListList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param listname: {"description": "Specify IP list name", "format": "string", "minLength": 1, "optional": false, "maxLength": 31, "type": "string"}
    :param ip_list: {"minItems": 1, "items": {"type": "ip"}, "uniqueItems": true, "array": [{"required": ["ipv4-start-ip"], "properties": {"ipv4-start-ip": {"optional": false, "type": "string", "description": "Specify IP address (A.B.C.D)", "format": "ipv4-address"}, "mask": {"optional": true, "type": "string", "description": "Specify IP network mask", "format": "ipv4-netmask"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "ipv4-end-ip": {"optional": true, "type": "string", "description": "Add a range of IPs into the current IP list (Specify IP address (A.B.C.D))", "format": "ipv4-address"}}}], "type": "array", "$ref": "/axapi/v3/classification/ip-list/{listname}/ip/{ipv4-start-ip}"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param ipv6_list: {"minItems": 1, "items": {"type": "ipv6"}, "uniqueItems": true, "array": [{"required": ["ipv6-subnet", "ipv6-start-ip"], "properties": {"ipv6-subnet": {"optional": false, "type": "string", "description": "Specify IPv6 subnet range", "format": "ipv6-address-plen"}, "ipv6-end-ip": {"optional": true, "type": "string", "description": "Add a range of IPs into the current IP list (Specify IPv6 address)", "format": "ipv6-address"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "ipv6-start-ip": {"optional": false, "type": "string", "description": "Specify IPv6 address", "format": "ipv6-address"}}}], "type": "array", "$ref": "/axapi/v3/classification/ip-list/{listname}/ipv6/{ipv6-subnet}+{ipv6-start-ip}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ip-list-list"
        self.DeviceProxy = ""
        self.listname = ""
        self.ip_list = []
        self.uuid = ""
        self.ipv6_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Classification(A10BaseClass):
    
    """Class Description::
    Traffic Classification configuration commands.

    Class classification supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param port_list_list: {"minItems": 1, "items": {"type": "port-list"}, "uniqueItems": true, "array": [{"required": ["listname"], "properties": {"listname": {"description": "Specify port list name", "format": "string", "minLength": 1, "optional": false, "maxLength": 31, "type": "string"}, "port-list": {"minItems": 1, "items": {"type": "port"}, "uniqueItems": true, "array": [{"required": ["start-port"], "properties": {"end-port": {"description": "Add a range of ports into the current port list (Specify port number)", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": true}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "start-port": {"description": "Specify port number", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": false}}}], "type": "array", "$ref": "/axapi/v3/classification/port-list/{listname}/port/{start-port}"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/classification/port-list/{listname}"}
    :param ip_list_list: {"minItems": 1, "items": {"type": "ip-list"}, "uniqueItems": true, "array": [{"required": ["listname"], "properties": {"listname": {"description": "Specify IP list name", "format": "string", "minLength": 1, "optional": false, "maxLength": 31, "type": "string"}, "ip-list": {"minItems": 1, "items": {"type": "ip"}, "uniqueItems": true, "array": [{"required": ["ipv4-start-ip"], "properties": {"ipv4-start-ip": {"optional": false, "type": "string", "description": "Specify IP address (A.B.C.D)", "format": "ipv4-address"}, "mask": {"optional": true, "type": "string", "description": "Specify IP network mask", "format": "ipv4-netmask"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "ipv4-end-ip": {"optional": true, "type": "string", "description": "Add a range of IPs into the current IP list (Specify IP address (A.B.C.D))", "format": "ipv4-address"}}}], "type": "array", "$ref": "/axapi/v3/classification/ip-list/{listname}/ip/{ipv4-start-ip}"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "ipv6-list": {"minItems": 1, "items": {"type": "ipv6"}, "uniqueItems": true, "array": [{"required": ["ipv6-subnet", "ipv6-start-ip"], "properties": {"ipv6-subnet": {"optional": false, "type": "string", "description": "Specify IPv6 subnet range", "format": "ipv6-address-plen"}, "ipv6-end-ip": {"optional": true, "type": "string", "description": "Add a range of IPs into the current IP list (Specify IPv6 address)", "format": "ipv6-address"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "ipv6-start-ip": {"optional": false, "type": "string", "description": "Specify IPv6 address", "format": "ipv6-address"}}}], "type": "array", "$ref": "/axapi/v3/classification/ip-list/{listname}/ipv6/{ipv6-subnet}+{ipv6-start-ip}"}}}], "type": "array", "$ref": "/axapi/v3/classification/ip-list/{listname}"}
    :param class_list: {"minItems": 1, "items": {"type": "class"}, "uniqueItems": true, "array": [{"required": ["class-name"], "properties": {"disable": {"default": 0, "optional": true, "type": "number", "description": "Disable classification on this class", "format": "flag"}, "match-rule": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"all": {"default": 0, "type": "number", "description": "All traffic", "format": "flag"}, "sip": {"type": "object", "properties": {"sip-except": {"default": 0, "type": "number", "description": "Except source IP", "format": "flag"}, "sip6-value": {"type": "string", "description": "Specify source IPv6 address a:b:c:d:e:f:g:h/nn", "format": "ipv6-address-plen"}, "sip-list": {"description": "Specify source IP list name", "format": "string", "minLength": 1, "maxLength": 31, "type": "string", "$ref": "/axapi/v3/classification/ip-list"}, "sip-value": {"type": "string", "description": "Specify source IPv4 address a.b.c.d(/nn)", "format": "ipv4-cidr"}}}, "optional": true, "prot": {"type": "object", "properties": {"prot-num": {"description": "Specify protocol number", "minimum": 0, "type": "number", "maximum": 255, "format": "number"}, "prot-enum-value": {"enum": ["hopopt", "icmp", "igmp", "ggp", "ipv4", "st", "tcp", "cbt", "egp", "igp", "bbn-rcc", "nvp", "pup", "argus", "emcon", "xnet", "chaos", "udp", "mux", "dcn", "hmp", "prm", "xns-idp", "trunk-1", "trunk-2", "leaf-1", "leaf-2", "rdp", "irtp", "iso-tp4", "netblt", "mfe-nsp", "merit-inp", "dccp", "3pc", "idpr", "xtp", "ddp", "idpr-cmtp", "tp++", "il", "ipv6", "sdrp", "ipv6-route", "ipv6-frag", "idrp", "rsvp", "gre", "dsr", "bna", "esp", "ah", "i-nlsp", "swipe", "narp", "mobile", "tlsp", "skip", "ipv6-icmp", "ipv6-nonxt", "ipv6-opts", "any-host-internal", "cftp", "any-local-network", "sat-expak", "kryptolan", "rvd", "ippc", "any-distributed-fs", "sat-mon", "visa", "ipcv", "cpnx", "cphb", "wsn", "pvp", "br-sat-mon", "sun-nd", "wb-mon", "wb-expak", "iso-ip", "vmtp", "secure-vmtp", "vines", "ttp", "nsfnet-igp", "dgp", "tcf", "eigrp", "ospf", "sprite-rpc", "larp", "mtp", "ax.25", "ipip", "micp", "scc-sp", "etherip", "encap", "any-pri-encrypt-sch", "gmtp", "ifmp", "pnni", "pim", "aris", "scps", "qnx", "active-networks", "ipcomp", "snp", "compaq-peer", "ipx-in-ip", "vrrp", "pgm", "any-0-hop", "l2tp", "ddx", "iatp", "stp", "srp", "uti", "smp", "sm", "ptp", "isis", "fire", "crtp", "crudp", "sscopmce", "iplt", "sps", "pipe", "sctp", "fc", "rsvp-e2e-ignore", "mobility-header", "udplite", "mpls-in-ip", "manet", "hip", "shim6", "wesp", "rohc"], "type": "string", "description": "'hopopt': Hop-by-hop Options for IPv6 (0); 'icmp': Internet Control Message Protocol (1); 'igmp': Internet Group Management Protocol (2); 'ggp': Gateway-gateway Protocol (3); 'ipv4': IPv4 Encapsulation (4); 'st': ST Datagram Mode (5); 'tcp': Transmission Control Protocol (6); 'cbt': CBT (7); 'egp': Exterior Gateway Protocol (8); 'igp': Any Private Interior Gateway (9); 'bbn-rcc': BN RCC Monitoring (10); 'nvp': Network Voice Protocol (11); 'pup': PARC Universal Packet Protocol (12); 'argus': ARGUS (13); 'emcon': EMCON (14); 'xnet': Cross Net Debugger (15); 'chaos': Chaos (16); 'udp': User Datagram Protocol (17); 'mux': Multiplexing Protocol (18); 'dcn': DCN Measurement Subsystems (19); 'hmp': Host Monitoring Protocol (20); 'prm': Packet Radio Measurement Protocol (21); 'xns-idp': Xerox NS IDP (22); 'trunk-1': Trunk-1 (23); 'trunk-2': Trunk-2 (24); 'leaf-1': Leaf-1 (25); 'leaf-2': Leaf-2 (26); 'rdp': Reliable Data Protocol (27); 'irtp': Internet Reliable Transaction Protocol (28); 'iso-tp4': ISO Transport Protocol Class 4 (29); 'netblt': Bulk Data Transfer Protocol (30); 'mfe-nsp': MFE Network Services Protocol (31); 'merit-inp': MERIT Internodal Protocol (32); 'dccp': Datagram Congestion Control Protocol (33); '3pc': Third Party Connect Protocol (34); 'idpr': Inter-Domain Policy Routing Protocol (35); 'xtp': Xpress Tranfer Protocol (36); 'ddp': Datagram Delivery Protocol (37); 'idpr-cmtp': IDPR Control Message Transport Protocol (38); 'tp++': TP++ Transport Protocol (39); 'il': IL Transport Protocol (40); 'ipv6': IPv6 Encapsulation (41); 'sdrp': Source Demand Routing Protocol (42); 'ipv6-route': Routing Header for IPv6 (43); 'ipv6-frag': Fragment Header for IPv6 (44); 'idrp': Inter-Domain Routing Protocol (45); 'rsvp': Resource ReSerVation Protocol (46); 'gre': Generic Routing Encapsulation (47); 'dsr': Dynamic Source Routing Protocol (48); 'bna': BNA (49); 'esp': Encapsulating Security Payload Protocol (50); 'ah': Authentication Header (51); 'i-nlsp': Integrated Net Layer Security TUBA (52); 'swipe': IP with Encryption (53); 'narp': NBMA Address Resolution Protocol (54); 'mobile': IP Mobility (55); 'tlsp': Transport Layer Security Protocol (56); 'skip': SKIP (57); 'ipv6-icmp': ICMP for IPv6 (58); 'ipv6-nonxt': No Next Header for IPv6 (59); 'ipv6-opts': Destination Options for IPv6 (60); 'any-host-internal': ANY-HOST-INTERNAL (61); 'cftp': CFTP (62); 'any-local-network': ANY-LOCAL-NETWORK (63); 'sat-expak': SATNET and Backroom EXPAK (64); 'kryptolan': Kryptolan (65); 'rvd': MIT Remote Virtual Disk Protocol (66); 'ippc': Internet Pluribus Packet Core (67); 'any-distributed-fs': ANY-DISTRIBUTED-FS (68); 'sat-mon': SATNET Monitoring (69); 'visa': VISA Protocol (70); 'ipcv': Internet Packet Core Utility (71); 'cpnx': Computer Protocol Network Executive (72); 'cphb': Computer Protocol Heart Beat (73); 'wsn': Wang Span Network (74); 'pvp': Packet Video Protocol (75); 'br-sat-mon': Backroom SATNET Monitoring (76); 'sun-nd': SUN ND PROTOCOL-Temporary (77); 'wb-mon': WIDEBAND Monitoring (78); 'wb-expak': WIDEBAND EXPAK (79); 'iso-ip': ISO Internet Protocol (80); 'vmtp': Versatile Message Transport (81); 'secure-vmtp': SECURE-VMTP (82); 'vines': VINES (83); 'ttp': TTP (84); 'nsfnet-igp': NSFNET-IGP (85); 'dgp': Dissimilar Gateway Protocol (86); 'tcf': TCF (87); 'eigrp': Enhanced Interior Routing Protocol (88); 'ospf': Open Shortest Path First IGP (89); 'sprite-rpc': Sprite RPC Protocol (90); 'larp': Locus Address Resolution Protocol (91); 'mtp': Multicast Transport Protocol (92); 'ax.25': AX.25 Frames (93); 'ipip': IP-within-IP Encapsulation Protocol (94); 'micp': Mobile Internetworking Control Protocol (95); 'scc-sp': Semaphore Communications Sec. Protocol (96); 'etherip': Ethernet-within-IP Encapsulation (97); 'encap': Encapsulation Header (98); 'any-pri-encrypt-sch': Any Private Encryption Scheme (99); 'gmtp': GMTP (100); 'ifmp': Ipsilon Flow Management Protocol (101); 'pnni': PNNI over IP (102); 'pim': Protocol Independent Multicast (103); 'aris': ARIS (104); 'scps': SCPS (105); 'qnx': QNX (106); 'active-networks': Active Networks (107); 'ipcomp': IP Payload Compression Protocol (108); 'snp': Sitara Networks Protocol (109); 'compaq-peer': Compaq Peer Protocol (110); 'ipx-in-ip': IPX in IP (111); 'vrrp': Virtual Router Redundancy Protocol (112); 'pgm': PGM Reliable Transport Protocol (113); 'any-0-hop': ANY-0-HOP (114); 'l2tp': Layer Two Tunneling Protocol (115); 'ddx': D-II Data Exchange (116); 'iatp': Interactive Agent Transfer Protocol (117); 'stp': Schedule Transfer (118); 'srp': SpectraLink Radio Protocol (119); 'uti': UTI (120); 'smp': Simple Message Protocol (121); 'sm': SM (122); 'ptp': Performance Transparency Protocol (123); 'isis': ISIS over IPv4 (124); 'fire': FIRE (125); 'crtp': Combat Radio Transport Protocol (126); 'crudp': Combat Radio User Datagram (127); 'sscopmce': SSCOPMCE (128); 'iplt': IPLT (129); 'sps': Secure Packet Shield (130); 'pipe': Private IP Encapsulation within IP (131); 'sctp': Stream Control Transmission Protocol (132); 'fc': Fibre Channel (133); 'rsvp-e2e-ignore': Rsvp E2E Ignore (134); 'mobility-header': MOBILITY-HEADER (135); 'udplite': Udp Lite (136); 'mpls-in-ip': Mpls in IP (137); 'manet': MANET (138); 'hip': Host Identity Protocol (139); 'shim6': Shim6 (140); 'wesp': Wrapped Encapsulating Security Payload (141); 'rohc': Robost Header Compression (142); ", "format": "enum"}}}, "dscp": {"type": "object", "properties": {"dscp-value": {"description": "Specify free DSCP value (0-63)", "minimum": 0, "type": "number", "maximum": 63, "format": "number"}, "dscp-enum-value": {"enum": ["af11", "af12", "af13", "af21", "af22", "af23", "af31", "af32", "af33", "af41", "af42", "af43", "cs1", "cs2", "cs3", "cs4", "cs5", "cs6", "cs7", "default", "ef"], "type": "string", "description": "'af11': AF11 DSCP (001010); 'af12': AF12 DSCP (001100; 'af13': AF13 DSCP (001110); 'af21': AF21 DSCP (010010); 'af22': AF22 DSCP (010100); 'af23': AF23 DSCP (010110); 'af31': AF31 DSCP (011010); 'af32': AF32 DSCP (011100); 'af33': AF33 DSCP (011110); 'af41': AF41 DSCP (100010); 'af42': AF42 DSCP (100100); 'af43': AF43 DSCP (100110); 'cs1': CS1(precedence 1) DSCP (001000); 'cs2': S2(precedence 2) DSCP (010000); 'cs3': CS3(precedence 3) DSCP (011000); 'cs4': CS4(precedence 4) DSCP (100000); 'cs5': CS5(precedence 5) DSCP (101000); 'cs6': CS6(precedence 6) DSCP (110000); 'cs7': CS7(precedence 7) DSCP (111000); 'default': Default DSCP (000000); 'ef': EF DSCP (101110); ", "format": "enum"}, "dscp-except": {"default": 0, "type": "number", "description": "Except DSCP value", "format": "flag"}}}, "interface": {"type": "object", "properties": {"ethernet": {"type": "number", "description": "Specify ethernet interface number", "format": "interface"}, "ve": {"type": "number", "description": "Specify virtual ethernet interface number", "format": "interface"}, "trunk": {"type": "number", "description": "Specify trunk interface number", "format": "interface"}}}, "vlan": {"type": "number", "description": "Specify VLAN ID", "format": "number"}, "dport": {"type": "object", "properties": {"dport-list": {"description": "Specify destination port list name", "format": "string", "minLength": 1, "maxLength": 31, "type": "string", "$ref": "/axapi/v3/classification/port-list"}, "dport-except": {"default": 0, "type": "number", "description": "Except destinatino port", "format": "flag"}, "dport-value": {"description": "Specify destination port", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}}}, "sport": {"type": "object", "properties": {"sport-list": {"description": "Specify source port list name", "format": "string", "minLength": 1, "maxLength": 31, "type": "string", "$ref": "/axapi/v3/classification/port-list"}, "sport-except": {"default": 0, "type": "number", "description": "Except source port", "format": "flag"}, "sport-value": {"description": "Specify source port", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}}}, "dip": {"type": "object", "properties": {"dip-list": {"description": "Specify destination IP list name", "format": "string", "minLength": 1, "maxLength": 31, "type": "string", "$ref": "/axapi/v3/classification/ip-list"}, "dip-except": {"default": 0, "type": "number", "description": "Except destination IP", "format": "flag"}, "dip-value": {"type": "string", "description": "Specify destination IPv4 address a.b.c.d(/nn)", "format": "ipv4-cidr"}, "dip6-value": {"type": "string", "description": "Specify destination IPv6 address a:b:c:d:e:f:g:h/nn", "format": "ipv6-address-plen"}}}, "match": {"type": "string", "description": "Configure rule", "format": "string-rlx"}}}]}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "class-name": {"description": "Specify class name", "format": "string", "minLength": 1, "optional": false, "maxLength": 31, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/classification/class/{class-name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/classification`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "classification"
        self.a10_url="/axapi/v3/classification"
        self.DeviceProxy = ""
        self.port_list_list = []
        self.ip_list_list = []
        self.class_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


