from a10sdk.common.A10BaseClass import A10BaseClass


class SecurityAttack(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param layer_3: {"default": 0, "type": "number", "description": "drop packets with layer 3 anomaly", "format": "flag"}
    :param layer_4: {"default": 0, "type": "number", "description": "drop packets with layer 4 anomaly", "format": "flag"}
    :param security_attack: {"default": 0, "type": "number", "description": "drop packets causing security attack", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "security-attack"
        self.DeviceProxy = ""
        self.layer_3 = ""
        self.layer_4 = ""
        self.security_attack = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class PacketDeformity(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param layer_4: {"default": 0, "type": "number", "description": "drop packets with layer 4 anomaly", "format": "flag"}
    :param layer_3: {"default": 0, "type": "number", "description": "drop packets with layer 3 anomaly", "format": "flag"}
    :param packet_deformity: {"default": 0, "type": "number", "description": "drop packets with deformity", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "packet-deformity"
        self.DeviceProxy = ""
        self.layer_4 = ""
        self.layer_3 = ""
        self.packet_deformity = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class AnomalyDrop(A10BaseClass):
    
    """Class Description::
    Set IP anomaly drop policy.

    Class anomaly-drop supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param frag: {"default": 0, "optional": true, "type": "number", "description": "drop all fragmented packets", "format": "flag"}
    :param out_of_sequence: {"description": "out of sequence packet threshold (threshold value)", "format": "number", "type": "number", "maximum": 127, "minimum": 1, "optional": true}
    :param tcp_syn_fin: {"default": 0, "optional": true, "type": "number", "description": "drop TCP packets with both syn and fin flags set", "format": "flag"}
    :param drop_all: {"default": 0, "optional": true, "type": "number", "description": "drop all IP anomaly packets", "format": "flag"}
    :param ping_of_death: {"default": 0, "optional": true, "type": "number", "description": "drop oversize ICMP packets", "format": "flag"}
    :param tcp_no_flag: {"default": 0, "optional": true, "type": "number", "description": "drop TCP packets with no flag", "format": "flag"}
    :param zero_window: {"description": "zero window size threshold (threshold value)", "format": "number", "type": "number", "maximum": 127, "minimum": 1, "optional": true}
    :param ip_option: {"default": 0, "optional": true, "type": "number", "description": "drop packets with IP options", "format": "flag"}
    :param land_attack: {"default": 0, "optional": true, "type": "number", "description": "drop IP packets with the same source and destination addresses", "format": "flag"}
    :param tcp_syn_frag: {"default": 0, "optional": true, "type": "number", "description": "drop fragmented TCP packets with syn flag set", "format": "flag"}
    :param bad_content: {"description": "bad content threshold (threshold value)", "format": "number", "type": "number", "maximum": 127, "minimum": 1, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ip/anomaly-drop`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "anomaly-drop"
        self.a10_url="/axapi/v3/ip/anomaly-drop"
        self.DeviceProxy = ""
        self.frag = ""
        self.out_of_sequence = ""
        self.tcp_syn_fin = ""
        self.drop_all = ""
        self.ping_of_death = ""
        self.security_attack = {}
        self.tcp_no_flag = ""
        self.packet_deformity = {}
        self.zero_window = ""
        self.ip_option = ""
        self.land_attack = ""
        self.tcp_syn_frag = ""
        self.bad_content = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


