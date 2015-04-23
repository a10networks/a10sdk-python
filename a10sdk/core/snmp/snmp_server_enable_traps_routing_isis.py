from a10sdk.common.A10BaseClass import A10BaseClass


class Isis(A10BaseClass):
    
    """Class Description::
    Enable isis traps.

    Class isis supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param isisOwnLSPPurge: {"default": 0, "optional": true, "type": "number", "description": "Enable isisOwnLSPPurge traps", "format": "flag"}
    :param isisOriginatingLSPBufferSizeMis: {"default": 0, "optional": true, "type": "number", "description": "Enable isisOriginatingLSPBufferSizeMismatch traps", "format": "flag"}
    :param isisAuthenticationFailure: {"default": 0, "optional": true, "type": "number", "description": "Enable isisAuthenticationFailure traps", "format": "flag"}
    :param isisAdjacencyChange: {"default": 0, "optional": true, "type": "number", "description": "Enable isisAdjacencyChange traps", "format": "flag"}
    :param isisMaxAreaAddressesMismatch: {"default": 0, "optional": true, "type": "number", "description": "Enable isisMaxAreaAddressesMismatch traps", "format": "flag"}
    :param isisProtocolsSupportedMismatch: {"default": 0, "optional": true, "type": "number", "description": "Enable isisProtocolsSupportedMismatch traps", "format": "flag"}
    :param isisSequenceNumberSkip: {"default": 0, "optional": true, "type": "number", "description": "Enable isisSequenceNumberSkip traps", "format": "flag"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param isisAreaMismatch: {"default": 0, "optional": true, "type": "number", "description": "Enable isisAreaMismatch traps", "format": "flag"}
    :param isisLSPTooLargeToPropagate: {"default": 0, "optional": true, "type": "number", "description": "Enable isisLSPTooLargeToPropagate traps", "format": "flag"}
    :param isisDatabaseOverload: {"default": 0, "optional": true, "type": "number", "description": "Enable isisDatabaseOverload traps", "format": "flag"}
    :param isisRejectedAdjacency: {"default": 0, "optional": true, "type": "number", "description": "Enable isisRejectedAdjacency traps", "format": "flag"}
    :param isisAttemptToExceedMaxSequence: {"default": 0, "optional": true, "type": "number", "description": "Enable isisAttemptToExceedMaxSequence traps", "format": "flag"}
    :param isisIDLenMismatch: {"default": 0, "optional": true, "type": "number", "description": "Enable isisIDLenMismatch traps", "format": "flag"}
    :param isisAuthenticationTypeFailure: {"default": 0, "optional": true, "type": "number", "description": "Enable isisAuthenticationTypeFailure traps", "format": "flag"}
    :param isisVersionSkew: {"default": 0, "optional": true, "type": "number", "description": "Enable isisVersionSkew traps", "format": "flag"}
    :param isisManualAddressDrops: {"default": 0, "optional": true, "type": "number", "description": "Enable isisManualAddressDrops traps", "format": "flag"}
    :param isisCorruptedLSPDetected: {"default": 0, "optional": true, "type": "number", "description": "Enable isisCorruptedLSPDetected traps", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/snmp-server/enable/traps/routing/isis`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "isis"
        self.a10_url="/axapi/v3/snmp-server/enable/traps/routing/isis"
        self.DeviceProxy = ""
        self.isisOwnLSPPurge = ""
        self.isisOriginatingLSPBufferSizeMis = ""
        self.isisAuthenticationFailure = ""
        self.isisAdjacencyChange = ""
        self.isisMaxAreaAddressesMismatch = ""
        self.isisProtocolsSupportedMismatch = ""
        self.isisSequenceNumberSkip = ""
        self.uuid = ""
        self.isisAreaMismatch = ""
        self.isisLSPTooLargeToPropagate = ""
        self.isisDatabaseOverload = ""
        self.isisRejectedAdjacency = ""
        self.isisAttemptToExceedMaxSequence = ""
        self.isisIDLenMismatch = ""
        self.isisAuthenticationTypeFailure = ""
        self.isisVersionSkew = ""
        self.isisManualAddressDrops = ""
        self.isisCorruptedLSPDetected = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


