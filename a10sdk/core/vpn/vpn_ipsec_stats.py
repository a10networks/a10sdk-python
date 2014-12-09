from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param packets_err_icv_check: {"optional": true, "size": "4", "type": "number", "oid": "9", "format": "counter"}
    :param packets_err_lifetime_lifebytes: {"optional": true, "size": "8", "type": "number", "oid": "11", "format": "counter"}
    :param packets_err_badspi: {"optional": true, "size": "4", "type": "number", "oid": "10", "format": "counter"}
    :param cavium_err_enc: {"optional": true, "size": "4", "type": "number", "oid": "18", "format": "counter"}
    :param bytes_encrypted: {"optional": true, "size": "4", "type": "number", "oid": "12", "format": "counter"}
    :param anti_replay_num: {"optional": true, "size": "8", "type": "number", "oid": "3", "format": "counter"}
    :param prefrag_error: {"optional": true, "size": "4", "type": "number", "oid": "15", "format": "counter"}
    :param packets_err_encryption: {"optional": true, "size": "4", "type": "number", "oid": "6", "format": "counter"}
    :param rekey_num: {"optional": true, "size": "8", "type": "number", "oid": "4", "format": "counter"}
    :param frags_created: {"optional": true, "size": "4", "type": "number", "oid": "16", "format": "counter"}
    :param packets_err_inactive: {"optional": true, "size": "4", "type": "number", "oid": "5", "format": "counter"}
    :param prefrag_success: {"optional": true, "size": "4", "type": "number", "oid": "14", "format": "counter"}
    :param packets_err_pad_check: {"optional": true, "size": "4", "type": "number", "oid": "7", "format": "counter"}
    :param packets_err_pkt_sanity: {"optional": true, "size": "4", "type": "number", "oid": "8", "format": "counter"}
    :param packets_decrypted: {"optional": true, "size": "8", "type": "number", "oid": "2", "format": "counter"}
    :param frags_reassembled: {"optional": true, "size": "4", "type": "number", "oid": "17", "format": "counter"}
    :param packets_encrypted: {"optional": true, "size": "8", "type": "number", "oid": "1", "format": "counter"}
    :param cavium_err_dec: {"optional": true, "size": "4", "type": "number", "oid": "19", "format": "counter"}
    :param bytes_decrypted: {"optional": true, "size": "4", "type": "number", "oid": "13", "format": "counter"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.packets_err_icv_check = ""
        self.packets_err_lifetime_lifebytes = ""
        self.packets_err_badspi = ""
        self.cavium_err_enc = ""
        self.bytes_encrypted = ""
        self.anti_replay_num = ""
        self.prefrag_error = ""
        self.packets_err_encryption = ""
        self.rekey_num = ""
        self.frags_created = ""
        self.packets_err_inactive = ""
        self.prefrag_success = ""
        self.packets_err_pad_check = ""
        self.packets_err_pkt_sanity = ""
        self.packets_decrypted = ""
        self.frags_reassembled = ""
        self.packets_encrypted = ""
        self.cavium_err_dec = ""
        self.bytes_decrypted = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ipsec(A10BaseClass):
    
    """Class Description::
    Statistics for the object ipsec.

    Class ipsec supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param name: {"description": "IPsec name", "format": "string", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 31, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/vpn/ipsec/{name}/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "ipsec"
        self.a10_url="/axapi/v3/vpn/ipsec/{name}/stats"
        self.DeviceProxy = ""
        self.stats = {}
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


