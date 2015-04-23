from a10sdk.common.A10BaseClass import A10BaseClass


class Network(A10BaseClass):
    
    """Class Description::
    Specify a network to announce via BGP.

    Class network supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ip_mask_list: {"minItems": 1, "items": {"type": "ip-mask"}, "uniqueItems": true, "array": [{"required": ["network-ipv4", "mask"], "properties": {"description": {"description": "Network specific description (Up to 80 characters describing this network)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 80, "type": "string"}, "route-map": {"description": "Route-map to modify the attributes (Name of the route map)", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}, "mask": {"optional": false, "type": "string", "description": "Specify network mask (Network mask, e.g., 255.255.0.0)", "format": "ipv4-netmask"}, "comm-value": {"optional": true, "type": "string", "description": "community value in the format 1-4294967295|AA:NN|internet|local-AS|no-advertise|no-export", "format": "string-rlx"}, "backdoor": {"default": 0, "optional": true, "type": "number", "description": "Specify a BGP backdoor route", "format": "flag"}, "network-ipv4": {"optional": false, "type": "string", "description": "IP prefix", "format": "ipv4-address"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/router/bgp/{as-number}/network/ip-mask/{network-ipv4}+{mask}"}
    :param ip_cidr_list: {"minItems": 1, "items": {"type": "ip-cidr"}, "uniqueItems": true, "array": [{"required": ["network-ipv4-cidr"], "properties": {"description": {"description": "Network specific description (Up to 80 characters describing this network)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 80, "type": "string"}, "route-map": {"description": "Route-map to modify the attributes (Name of the route map)", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}, "comm-value": {"optional": true, "type": "string", "description": "community value in the format 1-4294967295|AA:NN|internet|local-AS|no-advertise|no-export", "format": "string-rlx"}, "backdoor": {"default": 0, "optional": true, "type": "number", "description": "Specify a BGP backdoor route", "format": "flag"}, "network-ipv4-cidr": {"optional": false, "type": "string", "description": "Specify network mask", "format": "ipv4-cidr"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/router/bgp/{as-number}/network/ip-cidr/{network-ipv4-cidr}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/router/bgp/{as_number}/network`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "network"
        self.a10_url="/axapi/v3/router/bgp/{as_number}/network"
        self.DeviceProxy = ""
        self.synchronization = {}
        self.ip_mask_list = []
        self.ip_cidr_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


