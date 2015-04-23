from a10sdk.common.A10BaseClass import A10BaseClass


class IpCidr(A10BaseClass):
    
    """Class Description::
    Specify a ip network to announce via BGP.

    Class ip-cidr supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param description: {"description": "Network specific description (Up to 80 characters describing this network)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 80, "type": "string"}
    :param route_map: {"description": "Route-map to modify the attributes (Name of the route map)", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}
    :param comm_value: {"optional": true, "type": "string", "description": "community value in the format 1-4294967295|AA:NN|internet|local-AS|no-advertise|no-export", "format": "string-rlx"}
    :param backdoor: {"default": 0, "optional": true, "type": "number", "description": "Specify a BGP backdoor route", "format": "flag"}
    :param network_ipv4_cidr: {"optional": false, "type": "string", "description": "Specify network mask", "format": "ipv4-cidr"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/router/bgp/{as_number}/network/ip-cidr/{network_ipv4_cidr}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "network_ipv4_cidr"]

        self.b_key = "ip-cidr"
        self.a10_url="/axapi/v3/router/bgp/{as_number}/network/ip-cidr/{network_ipv4_cidr}"
        self.DeviceProxy = ""
        self.description = ""
        self.route_map = ""
        self.comm_value = ""
        self.backdoor = ""
        self.network_ipv4_cidr = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


