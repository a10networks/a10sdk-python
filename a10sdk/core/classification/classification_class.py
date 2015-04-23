from a10sdk.common.A10BaseClass import A10BaseClass


class Sip(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param sip_except: {"default": 0, "type": "number", "description": "Except source IP", "format": "flag"}
    :param sip6_value: {"type": "string", "description": "Specify source IPv6 address a:b:c:d:e:f:g:h/nn", "format": "ipv6-address-plen"}
    :param sip_list: {"description": "Specify source IP list name", "format": "string", "minLength": 1, "maxLength": 31, "type": "string", "$ref": "/axapi/v3/classification/ip-list"}
    :param sip_value: {"type": "string", "description": "Specify source IPv4 address a.b.c.d(/nn)", "format": "ipv4-cidr"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sip"
        self.DeviceProxy = ""
        self.sip_except = ""
        self.sip6_value = ""
        self.sip_list = ""
        self.sip_value = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Prot(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param prot_num: {"description": "Specify protocol number", "minimum": 0, "type": "number", "maximum": 255, "format": "number"}
    :param prot_enum_value: {"enum": ["hopopt", "icmp", "igmp", "ggp", "ipv4", "st", "tcp", "cbt", "egp", "igp", "bbn-rcc", "nvp", "pup", "argus", "emcon", "xnet", "chaos", "udp", "mux", "dcn", "hmp", "prm", "xns-idp", "trunk-1", "trunk-2", "leaf-1", "leaf-2", "rdp", "irtp", "iso-tp4", "netblt", "mfe-nsp", "merit-inp", "dccp", "3pc", "idpr", "xtp", "ddp", "idpr-cmtp", "tp++", "il", "ipv6", "sdrp", "ipv6-route", "ipv6-frag", "idrp", "rsvp", "gre", "dsr", "bna", "esp", "ah", "i-nlsp", "swipe", "narp", "mobile", "tlsp", "skip", "ipv6-icmp", "ipv6-nonxt", "ipv6-opts", "any-host-internal", "cftp", "any-local-network", "sat-expak", "kryptolan", "rvd", "ippc", "any-distributed-fs", "sat-mon", "visa", "ipcv", "cpnx", "cphb", "wsn", "pvp", "br-sat-mon", "sun-nd", "wb-mon", "wb-expak", "iso-ip", "vmtp", "secure-vmtp", "vines", "ttp", "nsfnet-igp", "dgp", "tcf", "eigrp", "ospf", "sprite-rpc", "larp", "mtp", "ax.25", "ipip", "micp", "scc-sp", "etherip", "encap", "any-pri-encrypt-sch", "gmtp", "ifmp", "pnni", "pim", "aris", "scps", "qnx", "active-networks", "ipcomp", "snp", "compaq-peer", "ipx-in-ip", "vrrp", "pgm", "any-0-hop", "l2tp", "ddx", "iatp", "stp", "srp", "uti", "smp", "sm", "ptp", "isis", "fire", "crtp", "crudp", "sscopmce", "iplt", "sps", "pipe", "sctp", "fc", "rsvp-e2e-ignore", "mobility-header", "udplite", "mpls-in-ip", "manet", "hip", "shim6", "wesp", "rohc"], "type": "string", "description": "'hopopt': Hop-by-hop Options for IPv6 (0); 'icmp': Internet Control Message Protocol (1); 'igmp': Internet Group Management Protocol (2); 'ggp': Gateway-gateway Protocol (3); 'ipv4': IPv4 Encapsulation (4); 'st': ST Datagram Mode (5); 'tcp': Transmission Control Protocol (6); 'cbt': CBT (7); 'egp': Exterior Gateway Protocol (8); 'igp': Any Private Interior Gateway (9); 'bbn-rcc': BN RCC Monitoring (10); 'nvp': Network Voice Protocol (11); 'pup': PARC Universal Packet Protocol (12); 'argus': ARGUS (13); 'emcon': EMCON (14); 'xnet': Cross Net Debugger (15); 'chaos': Chaos (16); 'udp': User Datagram Protocol (17); 'mux': Multiplexing Protocol (18); 'dcn': DCN Measurement Subsystems (19); 'hmp': Host Monitoring Protocol (20); 'prm': Packet Radio Measurement Protocol (21); 'xns-idp': Xerox NS IDP (22); 'trunk-1': Trunk-1 (23); 'trunk-2': Trunk-2 (24); 'leaf-1': Leaf-1 (25); 'leaf-2': Leaf-2 (26); 'rdp': Reliable Data Protocol (27); 'irtp': Internet Reliable Transaction Protocol (28); 'iso-tp4': ISO Transport Protocol Class 4 (29); 'netblt': Bulk Data Transfer Protocol (30); 'mfe-nsp': MFE Network Services Protocol (31); 'merit-inp': MERIT Internodal Protocol (32); 'dccp': Datagram Congestion Control Protocol (33); '3pc': Third Party Connect Protocol (34); 'idpr': Inter-Domain Policy Routing Protocol (35); 'xtp': Xpress Tranfer Protocol (36); 'ddp': Datagram Delivery Protocol (37); 'idpr-cmtp': IDPR Control Message Transport Protocol (38); 'tp++': TP++ Transport Protocol (39); 'il': IL Transport Protocol (40); 'ipv6': IPv6 Encapsulation (41); 'sdrp': Source Demand Routing Protocol (42); 'ipv6-route': Routing Header for IPv6 (43); 'ipv6-frag': Fragment Header for IPv6 (44); 'idrp': Inter-Domain Routing Protocol (45); 'rsvp': Resource ReSerVation Protocol (46); 'gre': Generic Routing Encapsulation (47); 'dsr': Dynamic Source Routing Protocol (48); 'bna': BNA (49); 'esp': Encapsulating Security Payload Protocol (50); 'ah': Authentication Header (51); 'i-nlsp': Integrated Net Layer Security TUBA (52); 'swipe': IP with Encryption (53); 'narp': NBMA Address Resolution Protocol (54); 'mobile': IP Mobility (55); 'tlsp': Transport Layer Security Protocol (56); 'skip': SKIP (57); 'ipv6-icmp': ICMP for IPv6 (58); 'ipv6-nonxt': No Next Header for IPv6 (59); 'ipv6-opts': Destination Options for IPv6 (60); 'any-host-internal': ANY-HOST-INTERNAL (61); 'cftp': CFTP (62); 'any-local-network': ANY-LOCAL-NETWORK (63); 'sat-expak': SATNET and Backroom EXPAK (64); 'kryptolan': Kryptolan (65); 'rvd': MIT Remote Virtual Disk Protocol (66); 'ippc': Internet Pluribus Packet Core (67); 'any-distributed-fs': ANY-DISTRIBUTED-FS (68); 'sat-mon': SATNET Monitoring (69); 'visa': VISA Protocol (70); 'ipcv': Internet Packet Core Utility (71); 'cpnx': Computer Protocol Network Executive (72); 'cphb': Computer Protocol Heart Beat (73); 'wsn': Wang Span Network (74); 'pvp': Packet Video Protocol (75); 'br-sat-mon': Backroom SATNET Monitoring (76); 'sun-nd': SUN ND PROTOCOL-Temporary (77); 'wb-mon': WIDEBAND Monitoring (78); 'wb-expak': WIDEBAND EXPAK (79); 'iso-ip': ISO Internet Protocol (80); 'vmtp': Versatile Message Transport (81); 'secure-vmtp': SECURE-VMTP (82); 'vines': VINES (83); 'ttp': TTP (84); 'nsfnet-igp': NSFNET-IGP (85); 'dgp': Dissimilar Gateway Protocol (86); 'tcf': TCF (87); 'eigrp': Enhanced Interior Routing Protocol (88); 'ospf': Open Shortest Path First IGP (89); 'sprite-rpc': Sprite RPC Protocol (90); 'larp': Locus Address Resolution Protocol (91); 'mtp': Multicast Transport Protocol (92); 'ax.25': AX.25 Frames (93); 'ipip': IP-within-IP Encapsulation Protocol (94); 'micp': Mobile Internetworking Control Protocol (95); 'scc-sp': Semaphore Communications Sec. Protocol (96); 'etherip': Ethernet-within-IP Encapsulation (97); 'encap': Encapsulation Header (98); 'any-pri-encrypt-sch': Any Private Encryption Scheme (99); 'gmtp': GMTP (100); 'ifmp': Ipsilon Flow Management Protocol (101); 'pnni': PNNI over IP (102); 'pim': Protocol Independent Multicast (103); 'aris': ARIS (104); 'scps': SCPS (105); 'qnx': QNX (106); 'active-networks': Active Networks (107); 'ipcomp': IP Payload Compression Protocol (108); 'snp': Sitara Networks Protocol (109); 'compaq-peer': Compaq Peer Protocol (110); 'ipx-in-ip': IPX in IP (111); 'vrrp': Virtual Router Redundancy Protocol (112); 'pgm': PGM Reliable Transport Protocol (113); 'any-0-hop': ANY-0-HOP (114); 'l2tp': Layer Two Tunneling Protocol (115); 'ddx': D-II Data Exchange (116); 'iatp': Interactive Agent Transfer Protocol (117); 'stp': Schedule Transfer (118); 'srp': SpectraLink Radio Protocol (119); 'uti': UTI (120); 'smp': Simple Message Protocol (121); 'sm': SM (122); 'ptp': Performance Transparency Protocol (123); 'isis': ISIS over IPv4 (124); 'fire': FIRE (125); 'crtp': Combat Radio Transport Protocol (126); 'crudp': Combat Radio User Datagram (127); 'sscopmce': SSCOPMCE (128); 'iplt': IPLT (129); 'sps': Secure Packet Shield (130); 'pipe': Private IP Encapsulation within IP (131); 'sctp': Stream Control Transmission Protocol (132); 'fc': Fibre Channel (133); 'rsvp-e2e-ignore': Rsvp E2E Ignore (134); 'mobility-header': MOBILITY-HEADER (135); 'udplite': Udp Lite (136); 'mpls-in-ip': Mpls in IP (137); 'manet': MANET (138); 'hip': Host Identity Protocol (139); 'shim6': Shim6 (140); 'wesp': Wrapped Encapsulating Security Payload (141); 'rohc': Robost Header Compression (142); ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "prot"
        self.DeviceProxy = ""
        self.prot_num = ""
        self.prot_enum_value = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Dscp(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param dscp_value: {"description": "Specify free DSCP value (0-63)", "minimum": 0, "type": "number", "maximum": 63, "format": "number"}
    :param dscp_enum_value: {"enum": ["af11", "af12", "af13", "af21", "af22", "af23", "af31", "af32", "af33", "af41", "af42", "af43", "cs1", "cs2", "cs3", "cs4", "cs5", "cs6", "cs7", "default", "ef"], "type": "string", "description": "'af11': AF11 DSCP (001010); 'af12': AF12 DSCP (001100; 'af13': AF13 DSCP (001110); 'af21': AF21 DSCP (010010); 'af22': AF22 DSCP (010100); 'af23': AF23 DSCP (010110); 'af31': AF31 DSCP (011010); 'af32': AF32 DSCP (011100); 'af33': AF33 DSCP (011110); 'af41': AF41 DSCP (100010); 'af42': AF42 DSCP (100100); 'af43': AF43 DSCP (100110); 'cs1': CS1(precedence 1) DSCP (001000); 'cs2': S2(precedence 2) DSCP (010000); 'cs3': CS3(precedence 3) DSCP (011000); 'cs4': CS4(precedence 4) DSCP (100000); 'cs5': CS5(precedence 5) DSCP (101000); 'cs6': CS6(precedence 6) DSCP (110000); 'cs7': CS7(precedence 7) DSCP (111000); 'default': Default DSCP (000000); 'ef': EF DSCP (101110); ", "format": "enum"}
    :param dscp_except: {"default": 0, "type": "number", "description": "Except DSCP value", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "dscp"
        self.DeviceProxy = ""
        self.dscp_value = ""
        self.dscp_enum_value = ""
        self.dscp_except = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Interface(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ethernet: {"type": "number", "description": "Specify ethernet interface number", "format": "interface"}
    :param ve: {"type": "number", "description": "Specify virtual ethernet interface number", "format": "interface"}
    :param trunk: {"type": "number", "description": "Specify trunk interface number", "format": "interface"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "interface"
        self.DeviceProxy = ""
        self.ethernet = ""
        self.ve = ""
        self.trunk = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Dport(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param dport_list: {"description": "Specify destination port list name", "format": "string", "minLength": 1, "maxLength": 31, "type": "string", "$ref": "/axapi/v3/classification/port-list"}
    :param dport_except: {"default": 0, "type": "number", "description": "Except destinatino port", "format": "flag"}
    :param dport_value: {"description": "Specify destination port", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "dport"
        self.DeviceProxy = ""
        self.dport_list = ""
        self.dport_except = ""
        self.dport_value = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Sport(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param sport_list: {"description": "Specify source port list name", "format": "string", "minLength": 1, "maxLength": 31, "type": "string", "$ref": "/axapi/v3/classification/port-list"}
    :param sport_except: {"default": 0, "type": "number", "description": "Except source port", "format": "flag"}
    :param sport_value: {"description": "Specify source port", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sport"
        self.DeviceProxy = ""
        self.sport_list = ""
        self.sport_except = ""
        self.sport_value = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Dip(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param dip_list: {"description": "Specify destination IP list name", "format": "string", "minLength": 1, "maxLength": 31, "type": "string", "$ref": "/axapi/v3/classification/ip-list"}
    :param dip_except: {"default": 0, "type": "number", "description": "Except destination IP", "format": "flag"}
    :param dip_value: {"type": "string", "description": "Specify destination IPv4 address a.b.c.d(/nn)", "format": "ipv4-cidr"}
    :param dip6_value: {"type": "string", "description": "Specify destination IPv6 address a:b:c:d:e:f:g:h/nn", "format": "ipv6-address-plen"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "dip"
        self.DeviceProxy = ""
        self.dip_list = ""
        self.dip_except = ""
        self.dip_value = ""
        self.dip6_value = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class MatchRule(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param all: {"default": 0, "type": "number", "description": "All traffic", "format": "flag"}
    :param vlan: {"type": "number", "description": "Specify VLAN ID", "format": "number"}
    :param match: {"type": "string", "description": "Configure rule", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "match-rule"
        self.DeviceProxy = ""
        self.A10WW_all = ""
        self.sip = {}
        self.prot = {}
        self.dscp = {}
        self.interface = {}
        self.vlan = ""
        self.dport = {}
        self.sport = {}
        self.dip = {}
        self.match = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Class(A10BaseClass):
    
    """Class Description::
    Configure or create class.

    Class class supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param disable: {"default": 0, "optional": true, "type": "number", "description": "Disable classification on this class", "format": "flag"}
    :param match_rule: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"all": {"default": 0, "type": "number", "description": "All traffic", "format": "flag"}, "sip": {"type": "object", "properties": {"sip-except": {"default": 0, "type": "number", "description": "Except source IP", "format": "flag"}, "sip6-value": {"type": "string", "description": "Specify source IPv6 address a:b:c:d:e:f:g:h/nn", "format": "ipv6-address-plen"}, "sip-list": {"description": "Specify source IP list name", "format": "string", "minLength": 1, "maxLength": 31, "type": "string", "$ref": "/axapi/v3/classification/ip-list"}, "sip-value": {"type": "string", "description": "Specify source IPv4 address a.b.c.d(/nn)", "format": "ipv4-cidr"}}}, "optional": true, "prot": {"type": "object", "properties": {"prot-num": {"description": "Specify protocol number", "minimum": 0, "type": "number", "maximum": 255, "format": "number"}, "prot-enum-value": {"enum": ["hopopt", "icmp", "igmp", "ggp", "ipv4", "st", "tcp", "cbt", "egp", "igp", "bbn-rcc", "nvp", "pup", "argus", "emcon", "xnet", "chaos", "udp", "mux", "dcn", "hmp", "prm", "xns-idp", "trunk-1", "trunk-2", "leaf-1", "leaf-2", "rdp", "irtp", "iso-tp4", "netblt", "mfe-nsp", "merit-inp", "dccp", "3pc", "idpr", "xtp", "ddp", "idpr-cmtp", "tp++", "il", "ipv6", "sdrp", "ipv6-route", "ipv6-frag", "idrp", "rsvp", "gre", "dsr", "bna", "esp", "ah", "i-nlsp", "swipe", "narp", "mobile", "tlsp", "skip", "ipv6-icmp", "ipv6-nonxt", "ipv6-opts", "any-host-internal", "cftp", "any-local-network", "sat-expak", "kryptolan", "rvd", "ippc", "any-distributed-fs", "sat-mon", "visa", "ipcv", "cpnx", "cphb", "wsn", "pvp", "br-sat-mon", "sun-nd", "wb-mon", "wb-expak", "iso-ip", "vmtp", "secure-vmtp", "vines", "ttp", "nsfnet-igp", "dgp", "tcf", "eigrp", "ospf", "sprite-rpc", "larp", "mtp", "ax.25", "ipip", "micp", "scc-sp", "etherip", "encap", "any-pri-encrypt-sch", "gmtp", "ifmp", "pnni", "pim", "aris", "scps", "qnx", "active-networks", "ipcomp", "snp", "compaq-peer", "ipx-in-ip", "vrrp", "pgm", "any-0-hop", "l2tp", "ddx", "iatp", "stp", "srp", "uti", "smp", "sm", "ptp", "isis", "fire", "crtp", "crudp", "sscopmce", "iplt", "sps", "pipe", "sctp", "fc", "rsvp-e2e-ignore", "mobility-header", "udplite", "mpls-in-ip", "manet", "hip", "shim6", "wesp", "rohc"], "type": "string", "description": "'hopopt': Hop-by-hop Options for IPv6 (0); 'icmp': Internet Control Message Protocol (1); 'igmp': Internet Group Management Protocol (2); 'ggp': Gateway-gateway Protocol (3); 'ipv4': IPv4 Encapsulation (4); 'st': ST Datagram Mode (5); 'tcp': Transmission Control Protocol (6); 'cbt': CBT (7); 'egp': Exterior Gateway Protocol (8); 'igp': Any Private Interior Gateway (9); 'bbn-rcc': BN RCC Monitoring (10); 'nvp': Network Voice Protocol (11); 'pup': PARC Universal Packet Protocol (12); 'argus': ARGUS (13); 'emcon': EMCON (14); 'xnet': Cross Net Debugger (15); 'chaos': Chaos (16); 'udp': User Datagram Protocol (17); 'mux': Multiplexing Protocol (18); 'dcn': DCN Measurement Subsystems (19); 'hmp': Host Monitoring Protocol (20); 'prm': Packet Radio Measurement Protocol (21); 'xns-idp': Xerox NS IDP (22); 'trunk-1': Trunk-1 (23); 'trunk-2': Trunk-2 (24); 'leaf-1': Leaf-1 (25); 'leaf-2': Leaf-2 (26); 'rdp': Reliable Data Protocol (27); 'irtp': Internet Reliable Transaction Protocol (28); 'iso-tp4': ISO Transport Protocol Class 4 (29); 'netblt': Bulk Data Transfer Protocol (30); 'mfe-nsp': MFE Network Services Protocol (31); 'merit-inp': MERIT Internodal Protocol (32); 'dccp': Datagram Congestion Control Protocol (33); '3pc': Third Party Connect Protocol (34); 'idpr': Inter-Domain Policy Routing Protocol (35); 'xtp': Xpress Tranfer Protocol (36); 'ddp': Datagram Delivery Protocol (37); 'idpr-cmtp': IDPR Control Message Transport Protocol (38); 'tp++': TP++ Transport Protocol (39); 'il': IL Transport Protocol (40); 'ipv6': IPv6 Encapsulation (41); 'sdrp': Source Demand Routing Protocol (42); 'ipv6-route': Routing Header for IPv6 (43); 'ipv6-frag': Fragment Header for IPv6 (44); 'idrp': Inter-Domain Routing Protocol (45); 'rsvp': Resource ReSerVation Protocol (46); 'gre': Generic Routing Encapsulation (47); 'dsr': Dynamic Source Routing Protocol (48); 'bna': BNA (49); 'esp': Encapsulating Security Payload Protocol (50); 'ah': Authentication Header (51); 'i-nlsp': Integrated Net Layer Security TUBA (52); 'swipe': IP with Encryption (53); 'narp': NBMA Address Resolution Protocol (54); 'mobile': IP Mobility (55); 'tlsp': Transport Layer Security Protocol (56); 'skip': SKIP (57); 'ipv6-icmp': ICMP for IPv6 (58); 'ipv6-nonxt': No Next Header for IPv6 (59); 'ipv6-opts': Destination Options for IPv6 (60); 'any-host-internal': ANY-HOST-INTERNAL (61); 'cftp': CFTP (62); 'any-local-network': ANY-LOCAL-NETWORK (63); 'sat-expak': SATNET and Backroom EXPAK (64); 'kryptolan': Kryptolan (65); 'rvd': MIT Remote Virtual Disk Protocol (66); 'ippc': Internet Pluribus Packet Core (67); 'any-distributed-fs': ANY-DISTRIBUTED-FS (68); 'sat-mon': SATNET Monitoring (69); 'visa': VISA Protocol (70); 'ipcv': Internet Packet Core Utility (71); 'cpnx': Computer Protocol Network Executive (72); 'cphb': Computer Protocol Heart Beat (73); 'wsn': Wang Span Network (74); 'pvp': Packet Video Protocol (75); 'br-sat-mon': Backroom SATNET Monitoring (76); 'sun-nd': SUN ND PROTOCOL-Temporary (77); 'wb-mon': WIDEBAND Monitoring (78); 'wb-expak': WIDEBAND EXPAK (79); 'iso-ip': ISO Internet Protocol (80); 'vmtp': Versatile Message Transport (81); 'secure-vmtp': SECURE-VMTP (82); 'vines': VINES (83); 'ttp': TTP (84); 'nsfnet-igp': NSFNET-IGP (85); 'dgp': Dissimilar Gateway Protocol (86); 'tcf': TCF (87); 'eigrp': Enhanced Interior Routing Protocol (88); 'ospf': Open Shortest Path First IGP (89); 'sprite-rpc': Sprite RPC Protocol (90); 'larp': Locus Address Resolution Protocol (91); 'mtp': Multicast Transport Protocol (92); 'ax.25': AX.25 Frames (93); 'ipip': IP-within-IP Encapsulation Protocol (94); 'micp': Mobile Internetworking Control Protocol (95); 'scc-sp': Semaphore Communications Sec. Protocol (96); 'etherip': Ethernet-within-IP Encapsulation (97); 'encap': Encapsulation Header (98); 'any-pri-encrypt-sch': Any Private Encryption Scheme (99); 'gmtp': GMTP (100); 'ifmp': Ipsilon Flow Management Protocol (101); 'pnni': PNNI over IP (102); 'pim': Protocol Independent Multicast (103); 'aris': ARIS (104); 'scps': SCPS (105); 'qnx': QNX (106); 'active-networks': Active Networks (107); 'ipcomp': IP Payload Compression Protocol (108); 'snp': Sitara Networks Protocol (109); 'compaq-peer': Compaq Peer Protocol (110); 'ipx-in-ip': IPX in IP (111); 'vrrp': Virtual Router Redundancy Protocol (112); 'pgm': PGM Reliable Transport Protocol (113); 'any-0-hop': ANY-0-HOP (114); 'l2tp': Layer Two Tunneling Protocol (115); 'ddx': D-II Data Exchange (116); 'iatp': Interactive Agent Transfer Protocol (117); 'stp': Schedule Transfer (118); 'srp': SpectraLink Radio Protocol (119); 'uti': UTI (120); 'smp': Simple Message Protocol (121); 'sm': SM (122); 'ptp': Performance Transparency Protocol (123); 'isis': ISIS over IPv4 (124); 'fire': FIRE (125); 'crtp': Combat Radio Transport Protocol (126); 'crudp': Combat Radio User Datagram (127); 'sscopmce': SSCOPMCE (128); 'iplt': IPLT (129); 'sps': Secure Packet Shield (130); 'pipe': Private IP Encapsulation within IP (131); 'sctp': Stream Control Transmission Protocol (132); 'fc': Fibre Channel (133); 'rsvp-e2e-ignore': Rsvp E2E Ignore (134); 'mobility-header': MOBILITY-HEADER (135); 'udplite': Udp Lite (136); 'mpls-in-ip': Mpls in IP (137); 'manet': MANET (138); 'hip': Host Identity Protocol (139); 'shim6': Shim6 (140); 'wesp': Wrapped Encapsulating Security Payload (141); 'rohc': Robost Header Compression (142); ", "format": "enum"}}}, "dscp": {"type": "object", "properties": {"dscp-value": {"description": "Specify free DSCP value (0-63)", "minimum": 0, "type": "number", "maximum": 63, "format": "number"}, "dscp-enum-value": {"enum": ["af11", "af12", "af13", "af21", "af22", "af23", "af31", "af32", "af33", "af41", "af42", "af43", "cs1", "cs2", "cs3", "cs4", "cs5", "cs6", "cs7", "default", "ef"], "type": "string", "description": "'af11': AF11 DSCP (001010); 'af12': AF12 DSCP (001100; 'af13': AF13 DSCP (001110); 'af21': AF21 DSCP (010010); 'af22': AF22 DSCP (010100); 'af23': AF23 DSCP (010110); 'af31': AF31 DSCP (011010); 'af32': AF32 DSCP (011100); 'af33': AF33 DSCP (011110); 'af41': AF41 DSCP (100010); 'af42': AF42 DSCP (100100); 'af43': AF43 DSCP (100110); 'cs1': CS1(precedence 1) DSCP (001000); 'cs2': S2(precedence 2) DSCP (010000); 'cs3': CS3(precedence 3) DSCP (011000); 'cs4': CS4(precedence 4) DSCP (100000); 'cs5': CS5(precedence 5) DSCP (101000); 'cs6': CS6(precedence 6) DSCP (110000); 'cs7': CS7(precedence 7) DSCP (111000); 'default': Default DSCP (000000); 'ef': EF DSCP (101110); ", "format": "enum"}, "dscp-except": {"default": 0, "type": "number", "description": "Except DSCP value", "format": "flag"}}}, "interface": {"type": "object", "properties": {"ethernet": {"type": "number", "description": "Specify ethernet interface number", "format": "interface"}, "ve": {"type": "number", "description": "Specify virtual ethernet interface number", "format": "interface"}, "trunk": {"type": "number", "description": "Specify trunk interface number", "format": "interface"}}}, "vlan": {"type": "number", "description": "Specify VLAN ID", "format": "number"}, "dport": {"type": "object", "properties": {"dport-list": {"description": "Specify destination port list name", "format": "string", "minLength": 1, "maxLength": 31, "type": "string", "$ref": "/axapi/v3/classification/port-list"}, "dport-except": {"default": 0, "type": "number", "description": "Except destinatino port", "format": "flag"}, "dport-value": {"description": "Specify destination port", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}}}, "sport": {"type": "object", "properties": {"sport-list": {"description": "Specify source port list name", "format": "string", "minLength": 1, "maxLength": 31, "type": "string", "$ref": "/axapi/v3/classification/port-list"}, "sport-except": {"default": 0, "type": "number", "description": "Except source port", "format": "flag"}, "sport-value": {"description": "Specify source port", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}}}, "dip": {"type": "object", "properties": {"dip-list": {"description": "Specify destination IP list name", "format": "string", "minLength": 1, "maxLength": 31, "type": "string", "$ref": "/axapi/v3/classification/ip-list"}, "dip-except": {"default": 0, "type": "number", "description": "Except destination IP", "format": "flag"}, "dip-value": {"type": "string", "description": "Specify destination IPv4 address a.b.c.d(/nn)", "format": "ipv4-cidr"}, "dip6-value": {"type": "string", "description": "Specify destination IPv6 address a:b:c:d:e:f:g:h/nn", "format": "ipv6-address-plen"}}}, "match": {"type": "string", "description": "Configure rule", "format": "string-rlx"}}}]}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param class_name: {"description": "Specify class name", "format": "string", "minLength": 1, "optional": false, "maxLength": 31, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/classification/class/{class_name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "class_name"]

        self.b_key = "class"
        self.a10_url="/axapi/v3/classification/class/{class_name}"
        self.DeviceProxy = ""
        self.disable = ""
        self.match_rule = []
        self.uuid = ""
        self.class_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


