from a10sdk.common.A10BaseClass import A10BaseClass


class Network(A10BaseClass):
    
    """Class Description::
    Specify a network to announce via BGP.

    Class network supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ipv6_network_list: {"minItems": 1, "items": {"type": "ipv6-network"}, "uniqueItems": true, "array": [{"required": ["network-ipv6"], "properties": {"network-ipv6": {"optional": false, "type": "string", "description": "Specify a network to announce via BGP", "format": "ipv6-address-plen"}, "backdoor": {"default": 0, "optional": true, "type": "number", "description": "Specify a BGP backdoor route", "format": "flag"}, "route-map": {"description": "Route-map to modify the attributes (Name of the route map)", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}, "description": {"optional": true, "type": "string", "description": "Network specific description (Up to 80 characters describing this network)", "format": "string-rlx"}, "comm-value": {"optional": true, "type": "string", "description": "community value in the format 1-4294967295|AA:NN|internet|local-AS|no-advertise|no-export", "format": "string-rlx"}}}], "type": "array", "$ref": "/axapi/v3/router/bgp/{as-number}/address-family/ipv6/network/ipv6-network/{network-ipv6}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/router/bgp/{as_number}/address-family/ipv6/network`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "network"
        self.a10_url="/axapi/v3/router/bgp/{as_number}/address-family/ipv6/network"
        self.DeviceProxy = ""
        self.ipv6_network_list = []
        self.synchronization = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


