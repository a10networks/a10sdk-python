from a10sdk.common.A10BaseClass import A10BaseClass


class ExcludeIp(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param exclude_ip_start: {"type": "string", "description": "Single IP address or IP address range start", "format": "ipv4-address"}
    :param exclude_ip_end: {"type": "string", "description": "Address range end", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "exclude-ip"
        self.DeviceProxy = ""
        self.exclude_ip_start = ""
        self.exclude_ip_end = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Pool(A10BaseClass):
    
    """Class Description::
    Configure CGNv6 NAT pool.

    Class pool supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param max_users_per_ip: {"description": "Number of users that can be assigned to a NAT IP", "format": "number", "optional": true, "maximum": 64512, "minimum": 1, "modify-not-allowed": 1, "type": "number"}
    :param group: {"description": "Share with a partition group (Partition Group Name)", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param start_address: {"optional": true, "modify-not-allowed": 1, "type": "string", "description": "Configure start IP address of NAT pool", "format": "ipv4-address"}
    :param vrid: {"description": "Configure VRRP-A vrid (Specify ha VRRP-A vrid)", "format": "number", "optional": true, "maximum": 31, "minimum": 1, "modify-not-allowed": 1, "type": "number"}
    :param partition: {"description": "Share with a single partition (Partition Name)", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 14, "type": "string"}
    :param netmask: {"optional": true, "modify-not-allowed": 1, "type": "string", "description": "Configure mask for pool", "format": "ipv4-netmask-brief"}
    :param end_address: {"optional": true, "modify-not-allowed": 1, "type": "string", "description": "Configure end IP address of NAT pool", "format": "ipv4-address"}
    :param shared: {"description": "Share this pool with other partitions (default: not shared)", "partition-visibility": "shared", "default": 0, "optional": true, "format": "flag", "modify-not-allowed": 1, "type": "number"}
    :param exclude_ip: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"exclude-ip-start": {"type": "string", "description": "Single IP address or IP address range start", "format": "ipv4-address"}, "optional": true, "exclude-ip-end": {"type": "string", "description": "Address range end", "format": "ipv4-address"}}}]}
    :param pool_name: {"description": "Specify pool name or pool group", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/nat/pool/{pool_name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "pool_name"]

        self.b_key = "pool"
        self.a10_url="/axapi/v3/cgnv6/nat/pool/{pool_name}"
        self.DeviceProxy = ""
        self.max_users_per_ip = ""
        self.group = ""
        self.start_address = ""
        self.vrid = ""
        self.partition = ""
        self.netmask = ""
        self.end_address = ""
        self.shared = ""
        self.exclude_ip = []
        self.pool_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


