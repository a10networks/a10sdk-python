from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param passthrough: {"optional": true, "size": "8", "type": "number", "oid": "1", "format": "counter"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.passthrough = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Vpn(A10BaseClass):
    
    """Class Description::
    Statistics for the object vpn.

    Class vpn supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ike_gateway_list: {"minItems": 1, "items": {"type": "ike-gateway"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {}}], "type": "array", "$ref": "/axapi/v3/vpn/ike-gateway/{name}"}
    :param revocation_list: {"minItems": 1, "items": {"type": "revocation"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {}}], "type": "array", "$ref": "/axapi/v3/vpn/ike-gateway/{name}/ipsec/{name}/revocation/{name}"}
    :param ipsec_list: {"minItems": 1, "items": {"type": "ipsec"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"stats": {"type": "object", "properties": {"packets-err-icv-check": {"optional": true, "size": "4", "type": "number", "oid": "9", "format": "counter"}, "packets-err-lifetime-lifebytes": {"optional": true, "size": "8", "type": "number", "oid": "11", "format": "counter"}, "packets-err-badspi": {"optional": true, "size": "4", "type": "number", "oid": "10", "format": "counter"}, "cavium-err-enc": {"optional": true, "size": "4", "type": "number", "oid": "18", "format": "counter"}, "bytes-encrypted": {"optional": true, "size": "4", "type": "number", "oid": "12", "format": "counter"}, "anti-replay-num": {"optional": true, "size": "8", "type": "number", "oid": "3", "format": "counter"}, "prefrag-error": {"optional": true, "size": "4", "type": "number", "oid": "15", "format": "counter"}, "packets-err-encryption": {"optional": true, "size": "4", "type": "number", "oid": "6", "format": "counter"}, "rekey-num": {"optional": true, "size": "8", "type": "number", "oid": "4", "format": "counter"}, "frags-created": {"optional": true, "size": "4", "type": "number", "oid": "16", "format": "counter"}, "packets-err-inactive": {"optional": true, "size": "4", "type": "number", "oid": "5", "format": "counter"}, "prefrag-success": {"optional": true, "size": "4", "type": "number", "oid": "14", "format": "counter"}, "packets-err-pad-check": {"optional": true, "size": "4", "type": "number", "oid": "7", "format": "counter"}, "packets-err-pkt-sanity": {"optional": true, "size": "4", "type": "number", "oid": "8", "format": "counter"}, "packets-decrypted": {"optional": true, "size": "8", "type": "number", "oid": "2", "format": "counter"}, "frags-reassembled": {"optional": true, "size": "4", "type": "number", "oid": "17", "format": "counter"}, "packets-encrypted": {"optional": true, "size": "8", "type": "number", "oid": "1", "format": "counter"}, "cavium-err-dec": {"optional": true, "size": "4", "type": "number", "oid": "19", "format": "counter"}, "bytes-decrypted": {"optional": true, "size": "4", "type": "number", "oid": "13", "format": "counter"}}}, "name": {"description": "IPsec name", "format": "string", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 31, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/vpn/ike-gateway/{name}/ipsec/{name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/vpn/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "vpn"
        self.a10_url="/axapi/v3/vpn/stats"
        self.DeviceProxy = ""
        self.stats = {}
        self.ike_gateway_list = []
        self.revocation_list = []
        self.ipsec_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


