from a10sdk.common.A10BaseClass import A10BaseClass


class Ospf(A10BaseClass):
    
    """Class Description::
    Enable OSPFv2 traps.

    Class ospf supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ospfLsdbOverflow: {"default": 0, "optional": true, "type": "number", "description": "Enable ospfLsdbOverflow traps", "format": "flag"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param ospfVirtIfRxBadPacket: {"default": 0, "optional": true, "type": "number", "description": "Enable ospfVirtIfRxBadPacket traps", "format": "flag"}
    :param ospfNbrStateChange: {"default": 0, "optional": true, "type": "number", "description": "Enable ospfNbrStateChange traps", "format": "flag"}
    :param ospfIfStateChange: {"default": 0, "optional": true, "type": "number", "description": "Enable ospfIfStateChange traps", "format": "flag"}
    :param ospfVirtNbrStateChange: {"default": 0, "optional": true, "type": "number", "description": "Enable ospfVirtNbrStateChange traps", "format": "flag"}
    :param ospfLsdbApproachingOverflow: {"default": 0, "optional": true, "type": "number", "description": "Enable ospfLsdbApproachingOverflow traps", "format": "flag"}
    :param ospfIfAuthFailure: {"default": 0, "optional": true, "type": "number", "description": "Enable ospfIfAuthFailure traps", "format": "flag"}
    :param ospfVirtIfAuthFailure: {"default": 0, "optional": true, "type": "number", "description": "Enable ospfVirtIfAuthFailure traps", "format": "flag"}
    :param ospfVirtIfConfigError: {"default": 0, "optional": true, "type": "number", "description": "Enable ospfVirtIfConfigError traps", "format": "flag"}
    :param ospfIfConfigError: {"default": 0, "optional": true, "type": "number", "description": "Enable ospfIfConfigError traps", "format": "flag"}
    :param ospfTxRetransmit: {"default": 0, "optional": true, "type": "number", "description": "Enable ospfTxRetransmit traps", "format": "flag"}
    :param ospfVirtIfStateChange: {"default": 0, "optional": true, "type": "number", "description": "Enable ospfVirtIfStateChange traps", "format": "flag"}
    :param ospfVirtIfTxRetransmit: {"default": 0, "optional": true, "type": "number", "description": "Enable ospfVirtIfTxRetransmit traps", "format": "flag"}
    :param ospfMaxAgeLsa: {"default": 0, "optional": true, "type": "number", "description": "Enable ospfMaxAgeLsa traps", "format": "flag"}
    :param ospfIfRxBadPacket: {"default": 0, "optional": true, "type": "number", "description": "Enable ospfIfRxBadPacket traps", "format": "flag"}
    :param ospfOriginateLsa: {"default": 0, "optional": true, "type": "number", "description": "Enable ospfOriginateLsa traps", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/snmp-server/enable/traps/routing/ospf`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ospf"
        self.a10_url="/axapi/v3/snmp-server/enable/traps/routing/ospf"
        self.DeviceProxy = ""
        self.ospfLsdbOverflow = ""
        self.uuid = ""
        self.ospfVirtIfRxBadPacket = ""
        self.ospfNbrStateChange = ""
        self.ospfIfStateChange = ""
        self.ospfVirtNbrStateChange = ""
        self.ospfLsdbApproachingOverflow = ""
        self.ospfIfAuthFailure = ""
        self.ospfVirtIfAuthFailure = ""
        self.ospfVirtIfConfigError = ""
        self.ospfIfConfigError = ""
        self.ospfTxRetransmit = ""
        self.ospfVirtIfStateChange = ""
        self.ospfVirtIfTxRetransmit = ""
        self.ospfMaxAgeLsa = ""
        self.ospfIfRxBadPacket = ""
        self.ospfOriginateLsa = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


