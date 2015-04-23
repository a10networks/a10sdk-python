from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "ip_checksum_error", "udp_checksum_error", "session_not_found", "multihop_mismatch", "version_mismatch", "length_too_small", "data_is_short", "invalid_detect_mult", "invalid_multipoint", "invalid_my_disc", "invalid_ttl", "auth_length_invalid", "auth_mismatch", "auth_type_mismatch", "auth_key_id_mismatch", "auth_key_mismatch", "auth_seqnum_invalid", "auth_failed", "local_state_admin_down", "dest_unreachable", "other_error"], "type": "string", "description": "'all': all; 'ip_checksum_error': ip_checksum_error; 'udp_checksum_error': udp_checksum_error; 'session_not_found': session_not_found; 'multihop_mismatch': multihop_mismatch; 'version_mismatch': version_mismatch; 'length_too_small': length_too_small; 'data_is_short': data_is_short; 'invalid_detect_mult': invalid_detect_mult; 'invalid_multipoint': invalid_multipoint; 'invalid_my_disc': invalid_my_disc; 'invalid_ttl': invalid_ttl; 'auth_length_invalid': auth_length_invalid; 'auth_mismatch': auth_mismatch; 'auth_type_mismatch': auth_type_mismatch; 'auth_key_id_mismatch': auth_key_id_mismatch; 'auth_key_mismatch': auth_key_mismatch; 'auth_seqnum_invalid': auth_seqnum_invalid; 'auth_failed': auth_failed; 'local_state_admin_down': local_state_admin_down; 'dest_unreachable': dest_unreachable; 'other_error': other_error; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Bfd(A10BaseClass):
    
    """    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "ip_checksum_error", "udp_checksum_error", "session_not_found", "multihop_mismatch", "version_mismatch", "length_too_small", "data_is_short", "invalid_detect_mult", "invalid_multipoint", "invalid_my_disc", "invalid_ttl", "auth_length_invalid", "auth_mismatch", "auth_type_mismatch", "auth_key_id_mismatch", "auth_key_mismatch", "auth_seqnum_invalid", "auth_failed", "local_state_admin_down", "dest_unreachable", "other_error"], "type": "string", "description": "'all': all; 'ip_checksum_error': ip_checksum_error; 'udp_checksum_error': udp_checksum_error; 'session_not_found': session_not_found; 'multihop_mismatch': multihop_mismatch; 'version_mismatch': version_mismatch; 'length_too_small': length_too_small; 'data_is_short': data_is_short; 'invalid_detect_mult': invalid_detect_mult; 'invalid_multipoint': invalid_multipoint; 'invalid_my_disc': invalid_my_disc; 'invalid_ttl': invalid_ttl; 'auth_length_invalid': auth_length_invalid; 'auth_mismatch': auth_mismatch; 'auth_type_mismatch': auth_type_mismatch; 'auth_key_id_mismatch': auth_key_id_mismatch; 'auth_key_mismatch': auth_key_mismatch; 'auth_seqnum_invalid': auth_seqnum_invalid; 'auth_failed': auth_failed; 'local_state_admin_down': local_state_admin_down; 'dest_unreachable': dest_unreachable; 'other_error': other_error; ", "format": "enum"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    BFD Statistics.

    Class bfd supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/system/bfd`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "bfd"
        self.a10_url="/axapi/v3/system/bfd"
        self.DeviceProxy = ""
        self.sampling_enable = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


