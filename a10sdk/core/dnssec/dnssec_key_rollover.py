from a10sdk.common.A10BaseClass import A10BaseClass


class KeyRollover(A10BaseClass):
    
    """    :param ds_ready_in_parent_zone: {"default": 0, "optional": true, "type": "number", "description": "DS RR is already ready in the parent zone", "format": "flag"}
    :param zsk_start: {"default": 0, "optional": true, "type": "number", "description": "start ZSK rollover in emergency mode", "format": "flag"}
    :param ksk_start: {"default": 0, "optional": true, "type": "number", "description": "start KSK rollover in emergency mode", "format": "flag"}
    :param dnssec_key_type: {"optional": true, "enum": ["ZSK", "KSK"], "type": "string", "description": "'ZSK': Zone Signing Key; 'KSK': Key Signing Key; ", "format": "enum"}
    :param zone_name: {"description": "Specify the name for the DNS zone", "format": "string", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    DNSSEC Key rollover.

    Class key-rollover supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/dnssec/key-rollover`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "key-rollover"
        self.a10_url="/axapi/v3/dnssec/key-rollover"
        self.DeviceProxy = ""
        self.ds_ready_in_parent_zone = ""
        self.zsk_start = ""
        self.ksk_start = ""
        self.dnssec_key_type = ""
        self.zone_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


