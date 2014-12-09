from a10sdk.common.A10BaseClass import A10BaseClass


class IpMask(A10BaseClass):
    
    """Class Description::
    Specify a ip address mask network to announce via BGP.

    Class ip-mask supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param description: {"optional": true, "type": "string", "description": "Network specific description (Up to 80 characters describing this network)", "format": "string-rlx"}
    :param route_map: {"description": "Route-map to modify the attributes (Name of the route map)", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}
    :param mask: {"optional": false, "type": "string", "description": "Specify network mask (Network mask, e.g., 255.255.0.0)", "format": "ipv4-netmask"}
    :param comm_value: {"optional": true, "type": "string", "description": "community value in the format 1-4294967295|AA:NN|internet|local-AS|no-advertise|no-export", "format": "string-rlx"}
    :param backdoor: {"default": 0, "optional": true, "type": "number", "description": "Specify a BGP backdoor route", "format": "flag"}
    :param network_ipv4: {"optional": false, "type": "string", "description": "IP prefix", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/router/bgp/{as_number}/network/ip-mask/{network_ipv4}+{mask}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "network_ipv4","mask"]

        self.b_key = "ip-mask"
        self.a10_url="/axapi/v3/router/bgp/{as_number}/network/ip-mask/{network_ipv4}+{mask}"
        self.DeviceProxy = ""
        self.description = ""
        self.route_map = ""
        self.mask = ""
        self.comm_value = ""
        self.backdoor = ""
        self.network_ipv4 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


