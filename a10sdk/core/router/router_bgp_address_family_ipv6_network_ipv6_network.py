from a10sdk.common.A10BaseClass import A10BaseClass


class Ipv6Network(A10BaseClass):
    
    """Class Description::
    Specify a ip address mask network to announce via BGP.

    Class ipv6-network supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param network_ipv6: {"optional": false, "type": "string", "description": "Specify a network to announce via BGP", "format": "ipv6-address-plen"}
    :param backdoor: {"default": 0, "optional": true, "type": "number", "description": "Specify a BGP backdoor route", "format": "flag"}
    :param route_map: {"description": "Route-map to modify the attributes (Name of the route map)", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}
    :param description: {"optional": true, "type": "string", "description": "Network specific description (Up to 80 characters describing this network)", "format": "string-rlx"}
    :param comm_value: {"optional": true, "type": "string", "description": "community value in the format 1-4294967295|AA:NN|internet|local-AS|no-advertise|no-export", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/router/bgp/{as_number}/address-family/ipv6/network/ipv6-network/{network_ipv6}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "network_ipv6"]

        self.b_key = "ipv6-network"
        self.a10_url="/axapi/v3/router/bgp/{as_number}/address-family/ipv6/network/ipv6-network/{network_ipv6}"
        self.DeviceProxy = ""
        self.network_ipv6 = ""
        self.backdoor = ""
        self.route_map = ""
        self.description = ""
        self.comm_value = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


