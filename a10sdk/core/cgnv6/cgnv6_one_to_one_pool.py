from a10sdk.common.A10BaseClass import A10BaseClass


class Pool(A10BaseClass):
    
    """Class Description::
    Configure CGNv6 one-to-one pool.

    Class pool supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param partition: {"description": "Share with a single partition (Partition Name)", "partition-visibility": "shared", "minLength": 1, "format": "string", "modify-not-allowed": 1, "optional": true, "maxLength": 14, "type": "string"}
    :param group: {"description": "Share with a partition group (Partition Group Name)", "partition-visibility": "shared", "minLength": 1, "format": "string", "modify-not-allowed": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param start_address: {"optional": true, "modify-not-allowed": 1, "type": "string", "description": "Configure start IP address of NAT pool", "format": "ipv4-address"}
    :param vrid: {"description": "Configure VRRP-A vrid (Specify ha VRRP-A vrid)", "format": "number", "optional": true, "maximum": 31, "minimum": 1, "modify-not-allowed": 1, "type": "number"}
    :param netmask: {"optional": true, "modify-not-allowed": 1, "type": "string", "description": "Configure mask for pool", "format": "ipv4-netmask-brief"}
    :param end_address: {"optional": true, "modify-not-allowed": 1, "type": "string", "description": "Configure end IP address of NAT pool", "format": "ipv4-address"}
    :param shared: {"description": "Share this pool with other partitions (default: not shared)", "partition-visibility": "shared", "default": 0, "optional": true, "format": "flag", "modify-not-allowed": 1, "type": "number"}
    :param pool_name: {"description": "Specify pool name or pool group", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/one-to-one/pool/{pool_name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "pool_name"]

        self.b_key = "pool"
        self.a10_url="/axapi/v3/cgnv6/one-to-one/pool/{pool_name}"
        self.DeviceProxy = ""
        self.partition = ""
        self.group = ""
        self.uuid = ""
        self.start_address = ""
        self.vrid = ""
        self.netmask = ""
        self.end_address = ""
        self.shared = ""
        self.pool_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


