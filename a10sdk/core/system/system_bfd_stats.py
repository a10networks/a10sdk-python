from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param udp_checksum_error: {"optional": true, "size": "2", "type": "number", "oid": "2", "format": "counter"}
    :param invalid_detect_mult: {"optional": true, "size": "2", "type": "number", "oid": "8", "format": "counter"}
    :param auth_length_invalid: {"optional": true, "size": "2", "type": "number", "oid": "12", "format": "counter"}
    :param auth_key_mismatch: {"optional": true, "size": "2", "type": "number", "oid": "16", "format": "counter"}
    :param invalid_my_disc: {"optional": true, "size": "2", "type": "number", "oid": "10", "format": "counter"}
    :param multihop_mismatch: {"optional": true, "size": "2", "type": "number", "oid": "4", "format": "counter"}
    :param dest_unreachable: {"optional": true, "size": "2", "type": "number", "oid": "20", "format": "counter"}
    :param length_too_small: {"optional": true, "size": "2", "type": "number", "oid": "6", "format": "counter"}
    :param auth_mismatch: {"optional": true, "size": "2", "type": "number", "oid": "13", "format": "counter"}
    :param auth_failed: {"optional": true, "size": "2", "type": "number", "oid": "18", "format": "counter"}
    :param auth_type_mismatch: {"optional": true, "size": "2", "type": "number", "oid": "14", "format": "counter"}
    :param invalid_ttl: {"optional": true, "size": "2", "type": "number", "oid": "11", "format": "counter"}
    :param data_is_short: {"optional": true, "size": "2", "type": "number", "oid": "7", "format": "counter"}
    :param session_not_found: {"optional": true, "size": "2", "type": "number", "oid": "3", "format": "counter"}
    :param auth_seqnum_invalid: {"optional": true, "size": "2", "type": "number", "oid": "17", "format": "counter"}
    :param local_state_admin_down: {"optional": true, "size": "2", "type": "number", "oid": "19", "format": "counter"}
    :param ip_checksum_error: {"optional": true, "size": "2", "type": "number", "oid": "1", "format": "counter"}
    :param version_mismatch: {"optional": true, "size": "2", "type": "number", "oid": "5", "format": "counter"}
    :param auth_key_id_mismatch: {"optional": true, "size": "2", "type": "number", "oid": "15", "format": "counter"}
    :param other_error: {"optional": true, "size": "2", "type": "number", "oid": "21", "format": "counter"}
    :param invalid_multipoint: {"optional": true, "size": "2", "type": "number", "oid": "9", "format": "counter"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.udp_checksum_error = ""
        self.invalid_detect_mult = ""
        self.auth_length_invalid = ""
        self.auth_key_mismatch = ""
        self.invalid_my_disc = ""
        self.multihop_mismatch = ""
        self.dest_unreachable = ""
        self.length_too_small = ""
        self.auth_mismatch = ""
        self.auth_failed = ""
        self.auth_type_mismatch = ""
        self.invalid_ttl = ""
        self.data_is_short = ""
        self.session_not_found = ""
        self.auth_seqnum_invalid = ""
        self.local_state_admin_down = ""
        self.ip_checksum_error = ""
        self.version_mismatch = ""
        self.auth_key_id_mismatch = ""
        self.other_error = ""
        self.invalid_multipoint = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Bfd(A10BaseClass):
    
    """Class Description::
    Statistics for the object bfd.

    Class bfd supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/system/bfd/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "bfd"
        self.a10_url="/axapi/v3/system/bfd/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


