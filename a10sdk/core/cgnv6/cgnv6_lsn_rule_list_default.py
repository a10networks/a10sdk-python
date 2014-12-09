from a10sdk.common.A10BaseClass import A10BaseClass


class UdpCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param action_type: {"enum": ["dnat", "drop", "pass-through", "snat", "set-dscp"], "type": "string", "description": "'dnat': Apply Dest NAT; 'drop': Drop the Packets; 'pass-through': Pass the Packets Through; 'snat': Redirect the Packets to a Different Source NAT Pool; 'set-dscp': To set dscp value for the packets; ", "format": "enum"}
    :param dscp_value: {"enum": ["default", "af11", "af12", "af13", "af21", "af22", "af23", "af31", "af32", "af33", "af41", "af42", "af43", "cs1", "cs2", "cs3", "cs4", "cs5", "cs6", "cs7", "ef", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63"], "type": "string", "description": "'default': Default dscp (000000); 'af11': AF11 (001010); 'af12': AF12 (001100); 'af13': AF13 (001110); 'af21': AF21 (010010); 'af22': AF22 (010100); 'af23': AF23 (010110); 'af31': AF31 (011010); 'af32': AF32 (011100); 'af33': AF33 (011110); 'af41': AF41 (100010); 'af42': AF42 (100100); 'af43': AF43 (100110); 'cs1': CS1 (001000); 'cs2': CS2 (010000); 'cs3': CS3 (011000); 'cs4': CS4 (100000); 'cs5': CS5 (101000); 'cs6': CS6 (110000); 'cs7': CS7 (111000); 'ef': EF (101110); '0': 000000; '1': 000001; '2': 000010; '3': 000011; '4': 000100; '5': 000101; '6': 000110; '7': 000111; '8': 001000; '9': 001001; '10': 001010; '11': 001011; '12': 001100; '13': 001101; '14': 001110; '15': 001111; '16': 010000; '17': 010001; '18': 010010; '19': 010011; '20': 010100; '21': 010101; '22': 010110; '23': 010111; '24': 011000; '25': 011001; '26': 011010; '27': 011011; '28': 011100; '29': 011101; '30': 011110; '31': 011111; '32': 100000; '33': 100001; '34': 100010; '35': 100011; '36': 100100; '37': 100101; '38': 100110; '39': 100111; '40': 101000; '41': 101001; '42': 101010; '43': 101011; '44': 101100; '45': 101101; '46': 101110; '47': 101111; '48': 110000; '49': 110001; '50': 110010; '51': 110011; '52': 110100; '53': 110101; '54': 110110; '55': 110111; '56': 111000; '57': 111001; '58': 111010; '59': 111011; '60': 111100; '61': 111101; '62': 111110; '63': 111111; ", "format": "enum"}
    :param end_port: {"description": "End of Port Range (inclusive)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param ipv4_list: {"minLength": 1, "maxLength": 63, "type": "string", "description": "IP-List (IP-List Name)", "format": "string-rlx"}
    :param action_cfg: {"enum": ["action", "no-action"], "type": "string", "description": "'action': LSN Rule-List Action; 'no-action': Exclude LSN Rule-List Action; ", "format": "enum"}
    :param dscp_direction: {"enum": ["inbound", "outbound"], "type": "string", "description": "'inbound': To set dscp value for inbound packets; 'outbound': To set dscp value for outbound packets; ", "format": "enum"}
    :param start_port: {"description": "Single Port or Start of Port Range (inclusive), Port 0 is Match Any Port", "minimum": 0, "type": "number", "maximum": 65535, "format": "number"}
    :param shared: {"default": 0, "partition-visibility": "private", "type": "number", "description": "The pool is a shared pool", "format": "flag"}
    :param pool: {"minLength": 1, "maxLength": 63, "type": "string", "description": "NAT Pool (NAT Pool or Pool Group)", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "udp-cfg"
        self.DeviceProxy = ""
        self.action_type = ""
        self.dscp_value = ""
        self.end_port = ""
        self.ipv4_list = ""
        self.action_cfg = ""
        self.dscp_direction = ""
        self.start_port = ""
        self.shared = ""
        self.pool = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class TcpCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param action_type: {"enum": ["dnat", "drop", "pass-through", "snat", "set-dscp", "template"], "type": "string", "description": "'dnat': Apply Dest NAT; 'drop': Drop the Packets; 'pass-through': Pass the Packets Through; 'snat': Redirect the Packets to a Different Source NAT Pool; 'set-dscp': To set dscp value for the packets; 'template': Template; ", "format": "enum"}
    :param dscp_value: {"enum": ["default", "af11", "af12", "af13", "af21", "af22", "af23", "af31", "af32", "af33", "af41", "af42", "af43", "cs1", "cs2", "cs3", "cs4", "cs5", "cs6", "cs7", "ef", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63"], "type": "string", "description": "'default': Default dscp (000000); 'af11': AF11 (001010); 'af12': AF12 (001100); 'af13': AF13 (001110); 'af21': AF21 (010010); 'af22': AF22 (010100); 'af23': AF23 (010110); 'af31': AF31 (011010); 'af32': AF32 (011100); 'af33': AF33 (011110); 'af41': AF41 (100010); 'af42': AF42 (100100); 'af43': AF43 (100110); 'cs1': CS1 (001000); 'cs2': CS2 (010000); 'cs3': CS3 (011000); 'cs4': CS4 (100000); 'cs5': CS5 (101000); 'cs6': CS6 (110000); 'cs7': CS7 (111000); 'ef': EF (101110); '0': 000000; '1': 000001; '2': 000010; '3': 000011; '4': 000100; '5': 000101; '6': 000110; '7': 000111; '8': 001000; '9': 001001; '10': 001010; '11': 001011; '12': 001100; '13': 001101; '14': 001110; '15': 001111; '16': 010000; '17': 010001; '18': 010010; '19': 010011; '20': 010100; '21': 010101; '22': 010110; '23': 010111; '24': 011000; '25': 011001; '26': 011010; '27': 011011; '28': 011100; '29': 011101; '30': 011110; '31': 011111; '32': 100000; '33': 100001; '34': 100010; '35': 100011; '36': 100100; '37': 100101; '38': 100110; '39': 100111; '40': 101000; '41': 101001; '42': 101010; '43': 101011; '44': 101100; '45': 101101; '46': 101110; '47': 101111; '48': 110000; '49': 110001; '50': 110010; '51': 110011; '52': 110100; '53': 110101; '54': 110110; '55': 110111; '56': 111000; '57': 111001; '58': 111010; '59': 111011; '60': 111100; '61': 111101; '62': 111110; '63': 111111; ", "format": "enum"}
    :param end_port: {"description": "End of Port Range (inclusive)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param ipv4_list: {"minLength": 1, "maxLength": 63, "type": "string", "description": "IP-List (IP-List Name)", "format": "string-rlx"}
    :param action_cfg: {"enum": ["action", "no-action"], "type": "string", "description": "'action': LSN Rule-List Action; 'no-action': Exclude LSN Rule-List Action; ", "format": "enum"}
    :param dscp_direction: {"enum": ["inbound", "outbound"], "type": "string", "description": "'inbound': To set dscp value for inbound packets; 'outbound': To set dscp value for outbound packets; ", "format": "enum"}
    :param start_port: {"description": "Single Port or Start of Port Range (inclusive), Port 0 is Match Any Port", "minimum": 0, "type": "number", "maximum": 65535, "format": "number"}
    :param shared: {"default": 0, "partition-visibility": "private", "type": "number", "description": "The pool is a shared pool", "format": "flag"}
    :param pool: {"minLength": 1, "maxLength": 63, "type": "string", "description": "NAT Pool (NAT Pool or Pool Group)", "format": "string-rlx"}
    :param http_alg: {"minLength": 1, "maxLength": 63, "type": "string", "description": "HTTP-ALG Template (Template Name)", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "tcp-cfg"
        self.DeviceProxy = ""
        self.action_type = ""
        self.dscp_value = ""
        self.end_port = ""
        self.ipv4_list = ""
        self.action_cfg = ""
        self.dscp_direction = ""
        self.start_port = ""
        self.shared = ""
        self.pool = ""
        self.http_alg = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class DscpCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param action_type: {"enum": ["set-dscp"], "type": "string", "description": "'set-dscp': To set dscp value for the packets; ", "format": "enum"}
    :param action_cfg: {"enum": ["action"], "type": "string", "description": "'action': LSN Rule-List Action; ", "format": "enum"}
    :param dscp_value: {"enum": ["default", "af11", "af12", "af13", "af21", "af22", "af23", "af31", "af32", "af33", "af41", "af42", "af43", "cs1", "cs2", "cs3", "cs4", "cs5", "cs6", "cs7", "ef", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63"], "type": "string", "description": "'default': Default dscp (000000); 'af11': AF11 (001010); 'af12': AF12 (001100); 'af13': AF13 (001110); 'af21': AF21 (010010); 'af22': AF22 (010100); 'af23': AF23 (010110); 'af31': AF31 (011010); 'af32': AF32 (011100); 'af33': AF33 (011110); 'af41': AF41 (100010); 'af42': AF42 (100100); 'af43': AF43 (100110); 'cs1': CS1 (001000); 'cs2': CS2 (010000); 'cs3': CS3 (011000); 'cs4': CS4 (100000); 'cs5': CS5 (101000); 'cs6': CS6 (110000); 'cs7': CS7 (111000); 'ef': EF (101110); '0': 000000; '1': 000001; '2': 000010; '3': 000011; '4': 000100; '5': 000101; '6': 000110; '7': 000111; '8': 001000; '9': 001001; '10': 001010; '11': 001011; '12': 001100; '13': 001101; '14': 001110; '15': 001111; '16': 010000; '17': 010001; '18': 010010; '19': 010011; '20': 010100; '21': 010101; '22': 010110; '23': 010111; '24': 011000; '25': 011001; '26': 011010; '27': 011011; '28': 011100; '29': 011101; '30': 011110; '31': 011111; '32': 100000; '33': 100001; '34': 100010; '35': 100011; '36': 100100; '37': 100101; '38': 100110; '39': 100111; '40': 101000; '41': 101001; '42': 101010; '43': 101011; '44': 101100; '45': 101101; '46': 101110; '47': 101111; '48': 110000; '49': 110001; '50': 110010; '51': 110011; '52': 110100; '53': 110101; '54': 110110; '55': 110111; '56': 111000; '57': 111001; '58': 111010; '59': 111011; '60': 111100; '61': 111101; '62': 111110; '63': 111111; ", "format": "enum"}
    :param dscp_match: {"enum": ["default", "af11", "af12", "af13", "af21", "af22", "af23", "af31", "af32", "af33", "af41", "af42", "af43", "cs1", "cs2", "cs3", "cs4", "cs5", "cs6", "cs7", "ef", "any", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63"], "type": "string", "description": "'default': Default dscp (000000); 'af11': AF11 (001010); 'af12': AF12 (001100); 'af13': AF13 (001110); 'af21': AF21 (010010); 'af22': AF22 (010100); 'af23': AF23 (010110); 'af31': AF31 (011010); 'af32': AF32 (011100); 'af33': AF33 (011110); 'af41': AF41 (100010); 'af42': AF42 (100100); 'af43': AF43 (100110); 'cs1': CS1 (001000); 'cs2': CS2 (010000); 'cs3': CS3 (011000); 'cs4': CS4 (100000); 'cs5': CS5 (101000); 'cs6': CS6 (110000); 'cs7': CS7 (111000); 'ef': EF (101110); 'any': Match any dscp value; '0': 000000; '1': 000001; '2': 000010; '3': 000011; '4': 000100; '5': 000101; '6': 000110; '7': 000111; '8': 001000; '9': 001001; '10': 001010; '11': 001011; '12': 001100; '13': 001101; '14': 001110; '15': 001111; '16': 010000; '17': 010001; '18': 010010; '19': 010011; '20': 010100; '21': 010101; '22': 010110; '23': 010111; '24': 011000; '25': 011001; '26': 011010; '27': 011011; '28': 011100; '29': 011101; '30': 011110; '31': 011111; '32': 100000; '33': 100001; '34': 100010; '35': 100011; '36': 100100; '37': 100101; '38': 100110; '39': 100111; '40': 101000; '41': 101001; '42': 101010; '43': 101011; '44': 101100; '45': 101101; '46': 101110; '47': 101111; '48': 110000; '49': 110001; '50': 110010; '51': 110011; '52': 110100; '53': 110101; '54': 110110; '55': 110111; '56': 111000; '57': 111001; '58': 111010; '59': 111011; '60': 111100; '61': 111101; '62': 111110; '63': 111111; ", "format": "enum"}
    :param dscp_direction: {"enum": ["inbound", "outbound"], "type": "string", "description": "'inbound': To set dscp value for inbound packets; 'outbound': To set dscp value for outbound packets; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "dscp-cfg"
        self.DeviceProxy = ""
        self.action_type = ""
        self.action_cfg = ""
        self.dscp_value = ""
        self.dscp_match = ""
        self.dscp_direction = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class IcmpOthersCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param action_type: {"enum": ["dnat", "drop", "pass-through", "snat", "set-dscp"], "type": "string", "description": "'dnat': Apply Dest NAT; 'drop': Drop the Packets; 'pass-through': Pass the Packets Through; 'snat': Redirect the Packets to a Different Source NAT Pool; 'set-dscp': To set dscp value for the packets; ", "format": "enum"}
    :param dscp_value: {"enum": ["default", "af11", "af12", "af13", "af21", "af22", "af23", "af31", "af32", "af33", "af41", "af42", "af43", "cs1", "cs2", "cs3", "cs4", "cs5", "cs6", "cs7", "ef", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63"], "type": "string", "description": "'default': Default dscp (000000); 'af11': AF11 (001010); 'af12': AF12 (001100); 'af13': AF13 (001110); 'af21': AF21 (010010); 'af22': AF22 (010100); 'af23': AF23 (010110); 'af31': AF31 (011010); 'af32': AF32 (011100); 'af33': AF33 (011110); 'af41': AF41 (100010); 'af42': AF42 (100100); 'af43': AF43 (100110); 'cs1': CS1 (001000); 'cs2': CS2 (010000); 'cs3': CS3 (011000); 'cs4': CS4 (100000); 'cs5': CS5 (101000); 'cs6': CS6 (110000); 'cs7': CS7 (111000); 'ef': EF (101110); '0': 000000; '1': 000001; '2': 000010; '3': 000011; '4': 000100; '5': 000101; '6': 000110; '7': 000111; '8': 001000; '9': 001001; '10': 001010; '11': 001011; '12': 001100; '13': 001101; '14': 001110; '15': 001111; '16': 010000; '17': 010001; '18': 010010; '19': 010011; '20': 010100; '21': 010101; '22': 010110; '23': 010111; '24': 011000; '25': 011001; '26': 011010; '27': 011011; '28': 011100; '29': 011101; '30': 011110; '31': 011111; '32': 100000; '33': 100001; '34': 100010; '35': 100011; '36': 100100; '37': 100101; '38': 100110; '39': 100111; '40': 101000; '41': 101001; '42': 101010; '43': 101011; '44': 101100; '45': 101101; '46': 101110; '47': 101111; '48': 110000; '49': 110001; '50': 110010; '51': 110011; '52': 110100; '53': 110101; '54': 110110; '55': 110111; '56': 111000; '57': 111001; '58': 111010; '59': 111011; '60': 111100; '61': 111101; '62': 111110; '63': 111111; ", "format": "enum"}
    :param ipv4_list: {"minLength": 1, "maxLength": 63, "type": "string", "description": "IP-List (IP-List Name)", "format": "string-rlx"}
    :param action_cfg: {"enum": ["action", "no-action"], "type": "string", "description": "'action': LSN Rule-List Action; 'no-action': Exclude LSN Rule-List Action; ", "format": "enum"}
    :param dscp_direction: {"enum": ["inbound", "outbound"], "type": "string", "description": "'inbound': To set dscp value for inbound packets; 'outbound': To set dscp value for outbound packets; ", "format": "enum"}
    :param shared: {"default": 0, "partition-visibility": "private", "type": "number", "description": "The pool is a shared pool", "format": "flag"}
    :param pool: {"minLength": 1, "maxLength": 63, "type": "string", "description": "NAT Pool (NAT Pool or Pool Group)", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "icmp-others-cfg"
        self.DeviceProxy = ""
        self.action_type = ""
        self.dscp_value = ""
        self.ipv4_list = ""
        self.action_cfg = ""
        self.dscp_direction = ""
        self.shared = ""
        self.pool = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class RuleCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param proto: {"enum": ["tcp", "udp", "icmp", "others", "dscp"], "type": "string", "description": "'tcp': TCP L4 Protoco; 'udp': UDP L4 Protocol; 'icmp': ICMP L4 Protocol; 'others': Other L4 Protocl; 'dscp': Match dscp value; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "rule-cfg"
        self.DeviceProxy = ""
        self.proto = ""
        self.udp_cfg = {}
        self.tcp_cfg = {}
        self.dscp_cfg = {}
        self.icmp_others_cfg = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Default(A10BaseClass):
    
    """Class Description::
    Configure the Generic Rule-Set.

    Class default supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param rule_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"proto": {"enum": ["tcp", "udp", "icmp", "others", "dscp"], "type": "string", "description": "'tcp': TCP L4 Protoco; 'udp': UDP L4 Protocol; 'icmp': ICMP L4 Protocol; 'others': Other L4 Protocl; 'dscp': Match dscp value; ", "format": "enum"}, "udp-cfg": {"type": "object", "properties": {"action-type": {"enum": ["dnat", "drop", "pass-through", "snat", "set-dscp"], "type": "string", "description": "'dnat': Apply Dest NAT; 'drop': Drop the Packets; 'pass-through': Pass the Packets Through; 'snat': Redirect the Packets to a Different Source NAT Pool; 'set-dscp': To set dscp value for the packets; ", "format": "enum"}, "dscp-value": {"enum": ["default", "af11", "af12", "af13", "af21", "af22", "af23", "af31", "af32", "af33", "af41", "af42", "af43", "cs1", "cs2", "cs3", "cs4", "cs5", "cs6", "cs7", "ef", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63"], "type": "string", "description": "'default': Default dscp (000000); 'af11': AF11 (001010); 'af12': AF12 (001100); 'af13': AF13 (001110); 'af21': AF21 (010010); 'af22': AF22 (010100); 'af23': AF23 (010110); 'af31': AF31 (011010); 'af32': AF32 (011100); 'af33': AF33 (011110); 'af41': AF41 (100010); 'af42': AF42 (100100); 'af43': AF43 (100110); 'cs1': CS1 (001000); 'cs2': CS2 (010000); 'cs3': CS3 (011000); 'cs4': CS4 (100000); 'cs5': CS5 (101000); 'cs6': CS6 (110000); 'cs7': CS7 (111000); 'ef': EF (101110); '0': 000000; '1': 000001; '2': 000010; '3': 000011; '4': 000100; '5': 000101; '6': 000110; '7': 000111; '8': 001000; '9': 001001; '10': 001010; '11': 001011; '12': 001100; '13': 001101; '14': 001110; '15': 001111; '16': 010000; '17': 010001; '18': 010010; '19': 010011; '20': 010100; '21': 010101; '22': 010110; '23': 010111; '24': 011000; '25': 011001; '26': 011010; '27': 011011; '28': 011100; '29': 011101; '30': 011110; '31': 011111; '32': 100000; '33': 100001; '34': 100010; '35': 100011; '36': 100100; '37': 100101; '38': 100110; '39': 100111; '40': 101000; '41': 101001; '42': 101010; '43': 101011; '44': 101100; '45': 101101; '46': 101110; '47': 101111; '48': 110000; '49': 110001; '50': 110010; '51': 110011; '52': 110100; '53': 110101; '54': 110110; '55': 110111; '56': 111000; '57': 111001; '58': 111010; '59': 111011; '60': 111100; '61': 111101; '62': 111110; '63': 111111; ", "format": "enum"}, "end-port": {"description": "End of Port Range (inclusive)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "ipv4-list": {"minLength": 1, "maxLength": 63, "type": "string", "description": "IP-List (IP-List Name)", "format": "string-rlx"}, "action-cfg": {"enum": ["action", "no-action"], "type": "string", "description": "'action': LSN Rule-List Action; 'no-action': Exclude LSN Rule-List Action; ", "format": "enum"}, "dscp-direction": {"enum": ["inbound", "outbound"], "type": "string", "description": "'inbound': To set dscp value for inbound packets; 'outbound': To set dscp value for outbound packets; ", "format": "enum"}, "start-port": {"description": "Single Port or Start of Port Range (inclusive), Port 0 is Match Any Port", "minimum": 0, "type": "number", "maximum": 65535, "format": "number"}, "shared": {"default": 0, "partition-visibility": "private", "type": "number", "description": "The pool is a shared pool", "format": "flag"}, "pool": {"minLength": 1, "maxLength": 63, "type": "string", "description": "NAT Pool (NAT Pool or Pool Group)", "format": "string-rlx"}}}, "tcp-cfg": {"type": "object", "properties": {"action-type": {"enum": ["dnat", "drop", "pass-through", "snat", "set-dscp", "template"], "type": "string", "description": "'dnat': Apply Dest NAT; 'drop': Drop the Packets; 'pass-through': Pass the Packets Through; 'snat': Redirect the Packets to a Different Source NAT Pool; 'set-dscp': To set dscp value for the packets; 'template': Template; ", "format": "enum"}, "dscp-value": {"enum": ["default", "af11", "af12", "af13", "af21", "af22", "af23", "af31", "af32", "af33", "af41", "af42", "af43", "cs1", "cs2", "cs3", "cs4", "cs5", "cs6", "cs7", "ef", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63"], "type": "string", "description": "'default': Default dscp (000000); 'af11': AF11 (001010); 'af12': AF12 (001100); 'af13': AF13 (001110); 'af21': AF21 (010010); 'af22': AF22 (010100); 'af23': AF23 (010110); 'af31': AF31 (011010); 'af32': AF32 (011100); 'af33': AF33 (011110); 'af41': AF41 (100010); 'af42': AF42 (100100); 'af43': AF43 (100110); 'cs1': CS1 (001000); 'cs2': CS2 (010000); 'cs3': CS3 (011000); 'cs4': CS4 (100000); 'cs5': CS5 (101000); 'cs6': CS6 (110000); 'cs7': CS7 (111000); 'ef': EF (101110); '0': 000000; '1': 000001; '2': 000010; '3': 000011; '4': 000100; '5': 000101; '6': 000110; '7': 000111; '8': 001000; '9': 001001; '10': 001010; '11': 001011; '12': 001100; '13': 001101; '14': 001110; '15': 001111; '16': 010000; '17': 010001; '18': 010010; '19': 010011; '20': 010100; '21': 010101; '22': 010110; '23': 010111; '24': 011000; '25': 011001; '26': 011010; '27': 011011; '28': 011100; '29': 011101; '30': 011110; '31': 011111; '32': 100000; '33': 100001; '34': 100010; '35': 100011; '36': 100100; '37': 100101; '38': 100110; '39': 100111; '40': 101000; '41': 101001; '42': 101010; '43': 101011; '44': 101100; '45': 101101; '46': 101110; '47': 101111; '48': 110000; '49': 110001; '50': 110010; '51': 110011; '52': 110100; '53': 110101; '54': 110110; '55': 110111; '56': 111000; '57': 111001; '58': 111010; '59': 111011; '60': 111100; '61': 111101; '62': 111110; '63': 111111; ", "format": "enum"}, "end-port": {"description": "End of Port Range (inclusive)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "ipv4-list": {"minLength": 1, "maxLength": 63, "type": "string", "description": "IP-List (IP-List Name)", "format": "string-rlx"}, "action-cfg": {"enum": ["action", "no-action"], "type": "string", "description": "'action': LSN Rule-List Action; 'no-action': Exclude LSN Rule-List Action; ", "format": "enum"}, "dscp-direction": {"enum": ["inbound", "outbound"], "type": "string", "description": "'inbound': To set dscp value for inbound packets; 'outbound': To set dscp value for outbound packets; ", "format": "enum"}, "start-port": {"description": "Single Port or Start of Port Range (inclusive), Port 0 is Match Any Port", "minimum": 0, "type": "number", "maximum": 65535, "format": "number"}, "shared": {"default": 0, "partition-visibility": "private", "type": "number", "description": "The pool is a shared pool", "format": "flag"}, "pool": {"minLength": 1, "maxLength": 63, "type": "string", "description": "NAT Pool (NAT Pool or Pool Group)", "format": "string-rlx"}, "http-alg": {"minLength": 1, "maxLength": 63, "type": "string", "description": "HTTP-ALG Template (Template Name)", "format": "string-rlx"}}}, "dscp-cfg": {"type": "object", "properties": {"action-type": {"enum": ["set-dscp"], "type": "string", "description": "'set-dscp': To set dscp value for the packets; ", "format": "enum"}, "action-cfg": {"enum": ["action"], "type": "string", "description": "'action': LSN Rule-List Action; ", "format": "enum"}, "dscp-value": {"enum": ["default", "af11", "af12", "af13", "af21", "af22", "af23", "af31", "af32", "af33", "af41", "af42", "af43", "cs1", "cs2", "cs3", "cs4", "cs5", "cs6", "cs7", "ef", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63"], "type": "string", "description": "'default': Default dscp (000000); 'af11': AF11 (001010); 'af12': AF12 (001100); 'af13': AF13 (001110); 'af21': AF21 (010010); 'af22': AF22 (010100); 'af23': AF23 (010110); 'af31': AF31 (011010); 'af32': AF32 (011100); 'af33': AF33 (011110); 'af41': AF41 (100010); 'af42': AF42 (100100); 'af43': AF43 (100110); 'cs1': CS1 (001000); 'cs2': CS2 (010000); 'cs3': CS3 (011000); 'cs4': CS4 (100000); 'cs5': CS5 (101000); 'cs6': CS6 (110000); 'cs7': CS7 (111000); 'ef': EF (101110); '0': 000000; '1': 000001; '2': 000010; '3': 000011; '4': 000100; '5': 000101; '6': 000110; '7': 000111; '8': 001000; '9': 001001; '10': 001010; '11': 001011; '12': 001100; '13': 001101; '14': 001110; '15': 001111; '16': 010000; '17': 010001; '18': 010010; '19': 010011; '20': 010100; '21': 010101; '22': 010110; '23': 010111; '24': 011000; '25': 011001; '26': 011010; '27': 011011; '28': 011100; '29': 011101; '30': 011110; '31': 011111; '32': 100000; '33': 100001; '34': 100010; '35': 100011; '36': 100100; '37': 100101; '38': 100110; '39': 100111; '40': 101000; '41': 101001; '42': 101010; '43': 101011; '44': 101100; '45': 101101; '46': 101110; '47': 101111; '48': 110000; '49': 110001; '50': 110010; '51': 110011; '52': 110100; '53': 110101; '54': 110110; '55': 110111; '56': 111000; '57': 111001; '58': 111010; '59': 111011; '60': 111100; '61': 111101; '62': 111110; '63': 111111; ", "format": "enum"}, "dscp-match": {"enum": ["default", "af11", "af12", "af13", "af21", "af22", "af23", "af31", "af32", "af33", "af41", "af42", "af43", "cs1", "cs2", "cs3", "cs4", "cs5", "cs6", "cs7", "ef", "any", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63"], "type": "string", "description": "'default': Default dscp (000000); 'af11': AF11 (001010); 'af12': AF12 (001100); 'af13': AF13 (001110); 'af21': AF21 (010010); 'af22': AF22 (010100); 'af23': AF23 (010110); 'af31': AF31 (011010); 'af32': AF32 (011100); 'af33': AF33 (011110); 'af41': AF41 (100010); 'af42': AF42 (100100); 'af43': AF43 (100110); 'cs1': CS1 (001000); 'cs2': CS2 (010000); 'cs3': CS3 (011000); 'cs4': CS4 (100000); 'cs5': CS5 (101000); 'cs6': CS6 (110000); 'cs7': CS7 (111000); 'ef': EF (101110); 'any': Match any dscp value; '0': 000000; '1': 000001; '2': 000010; '3': 000011; '4': 000100; '5': 000101; '6': 000110; '7': 000111; '8': 001000; '9': 001001; '10': 001010; '11': 001011; '12': 001100; '13': 001101; '14': 001110; '15': 001111; '16': 010000; '17': 010001; '18': 010010; '19': 010011; '20': 010100; '21': 010101; '22': 010110; '23': 010111; '24': 011000; '25': 011001; '26': 011010; '27': 011011; '28': 011100; '29': 011101; '30': 011110; '31': 011111; '32': 100000; '33': 100001; '34': 100010; '35': 100011; '36': 100100; '37': 100101; '38': 100110; '39': 100111; '40': 101000; '41': 101001; '42': 101010; '43': 101011; '44': 101100; '45': 101101; '46': 101110; '47': 101111; '48': 110000; '49': 110001; '50': 110010; '51': 110011; '52': 110100; '53': 110101; '54': 110110; '55': 110111; '56': 111000; '57': 111001; '58': 111010; '59': 111011; '60': 111100; '61': 111101; '62': 111110; '63': 111111; ", "format": "enum"}, "dscp-direction": {"enum": ["inbound", "outbound"], "type": "string", "description": "'inbound': To set dscp value for inbound packets; 'outbound': To set dscp value for outbound packets; ", "format": "enum"}}}, "optional": true, "icmp-others-cfg": {"type": "object", "properties": {"action-type": {"enum": ["dnat", "drop", "pass-through", "snat", "set-dscp"], "type": "string", "description": "'dnat': Apply Dest NAT; 'drop': Drop the Packets; 'pass-through': Pass the Packets Through; 'snat': Redirect the Packets to a Different Source NAT Pool; 'set-dscp': To set dscp value for the packets; ", "format": "enum"}, "dscp-value": {"enum": ["default", "af11", "af12", "af13", "af21", "af22", "af23", "af31", "af32", "af33", "af41", "af42", "af43", "cs1", "cs2", "cs3", "cs4", "cs5", "cs6", "cs7", "ef", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63"], "type": "string", "description": "'default': Default dscp (000000); 'af11': AF11 (001010); 'af12': AF12 (001100); 'af13': AF13 (001110); 'af21': AF21 (010010); 'af22': AF22 (010100); 'af23': AF23 (010110); 'af31': AF31 (011010); 'af32': AF32 (011100); 'af33': AF33 (011110); 'af41': AF41 (100010); 'af42': AF42 (100100); 'af43': AF43 (100110); 'cs1': CS1 (001000); 'cs2': CS2 (010000); 'cs3': CS3 (011000); 'cs4': CS4 (100000); 'cs5': CS5 (101000); 'cs6': CS6 (110000); 'cs7': CS7 (111000); 'ef': EF (101110); '0': 000000; '1': 000001; '2': 000010; '3': 000011; '4': 000100; '5': 000101; '6': 000110; '7': 000111; '8': 001000; '9': 001001; '10': 001010; '11': 001011; '12': 001100; '13': 001101; '14': 001110; '15': 001111; '16': 010000; '17': 010001; '18': 010010; '19': 010011; '20': 010100; '21': 010101; '22': 010110; '23': 010111; '24': 011000; '25': 011001; '26': 011010; '27': 011011; '28': 011100; '29': 011101; '30': 011110; '31': 011111; '32': 100000; '33': 100001; '34': 100010; '35': 100011; '36': 100100; '37': 100101; '38': 100110; '39': 100111; '40': 101000; '41': 101001; '42': 101010; '43': 101011; '44': 101100; '45': 101101; '46': 101110; '47': 101111; '48': 110000; '49': 110001; '50': 110010; '51': 110011; '52': 110100; '53': 110101; '54': 110110; '55': 110111; '56': 111000; '57': 111001; '58': 111010; '59': 111011; '60': 111100; '61': 111101; '62': 111110; '63': 111111; ", "format": "enum"}, "ipv4-list": {"minLength": 1, "maxLength": 63, "type": "string", "description": "IP-List (IP-List Name)", "format": "string-rlx"}, "action-cfg": {"enum": ["action", "no-action"], "type": "string", "description": "'action': LSN Rule-List Action; 'no-action': Exclude LSN Rule-List Action; ", "format": "enum"}, "dscp-direction": {"enum": ["inbound", "outbound"], "type": "string", "description": "'inbound': To set dscp value for inbound packets; 'outbound': To set dscp value for outbound packets; ", "format": "enum"}, "shared": {"default": 0, "partition-visibility": "private", "type": "number", "description": "The pool is a shared pool", "format": "flag"}, "pool": {"minLength": 1, "maxLength": 63, "type": "string", "description": "NAT Pool (NAT Pool or Pool Group)", "format": "string-rlx"}}}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/lsn-rule-list/{name}/default`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "default"
        self.a10_url="/axapi/v3/cgnv6/lsn-rule-list/{name}/default"
        self.DeviceProxy = ""
        self.rule_cfg = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


