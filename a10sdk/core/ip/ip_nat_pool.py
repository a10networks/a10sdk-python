from a10sdk.common.A10BaseClass import A10BaseClass


class Pool(A10BaseClass):
    
    """Class Description::
    Configure IP pool name.

    Class pool supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param use_if_ip: {"description": "Use Interface IP", "format": "flag", "default": 0, "optional": true, "plat-pos-list": ["soft-ax"], "not": "start-address", "type": "number"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param start_address: {"description": "Configure start IP address of NAT pool", "format": "ipv4-address", "type": "string", "modify-not-allowed": 1, "not": "use-if-ip", "optional": true}
    :param vrid: {"description": "Configure VRRP-A vrid (Specify ha VRRP-A vrid)", "format": "number", "optional": true, "maximum": 31, "minimum": 1, "modify-not-allowed": 1, "type": "number"}
    :param netmask: {"optional": true, "modify-not-allowed": 1, "type": "string", "description": "Configure mask for pool", "format": "ipv4-netmask-brief"}
    :param end_address: {"optional": true, "modify-not-allowed": 1, "type": "string", "description": "Configure end IP address of NAT pool", "format": "ipv4-address"}
    :param ip_rr: {"description": "Use IP address round-robin behavior", "format": "flag", "default": 0, "type": "number", "modify-not-allowed": 1, "optional": true}
    :param ethernet: {"optional": true, "plat-pos-list": ["soft-ax"], "type": "number", "description": "Ethernet interface", "format": "interface"}
    :param scaleout_device_id: {"description": "Configure Scaleout device id to which this NAT pool is to be bound (Specify Scaleout device id)", "format": "number", "optional": true, "maximum": 64, "minimum": 1, "modify-not-allowed": 1, "type": "number"}
    :param gateway: {"optional": true, "modify-not-allowed": 1, "type": "string", "description": "Configure gateway IP", "format": "ipv4-address"}
    :param pool_name: {"description": "Specify pool name or pool group", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ip/nat/pool/{pool_name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "pool_name"]

        self.b_key = "pool"
        self.a10_url="/axapi/v3/ip/nat/pool/{pool_name}"
        self.DeviceProxy = ""
        self.use_if_ip = ""
        self.uuid = ""
        self.start_address = ""
        self.vrid = ""
        self.netmask = ""
        self.end_address = ""
        self.ip_rr = ""
        self.ethernet = ""
        self.scaleout_device_id = ""
        self.gateway = ""
        self.pool_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


