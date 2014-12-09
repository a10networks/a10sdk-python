from a10sdk.common.A10BaseClass import A10BaseClass


class OneToOne(A10BaseClass):
    
    """Class Description::
    Set one-to-one NAT parameters.

    Class one-to-one supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param pool_group_list: {"minItems": 1, "items": {"type": "pool-group"}, "uniqueItems": true, "array": [{"required": ["pool-group-name"], "properties": {"member-list": {"minItems": 1, "items": {"type": "member"}, "uniqueItems": true, "array": [{"required": ["pool-name"], "properties": {"pool-name": {"description": "Specify CGNv6 one-to-one pool name", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/cgnv6/one-to-one/pool-group/{pool-group-name}/member/{pool-name}"}, "pool-group-name": {"description": "Specify pool group name", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "vrid": {"description": "Specify VRRP-A vrid", "format": "number", "optional": true, "maximum": 31, "minimum": 1, "modify-not-allowed": 1, "type": "number"}}}], "type": "array", "$ref": "/axapi/v3/cgnv6/one-to-one/pool-group/{pool-group-name}"}
    :param pool_list: {"minItems": 1, "items": {"type": "pool"}, "uniqueItems": true, "array": [{"required": ["pool-name"], "properties": {"partition": {"description": "Share with a single partition (Partition Name)", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 14, "type": "string"}, "group": {"description": "Share with a partition group (Partition Group Name)", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 63, "type": "string"}, "start-address": {"optional": true, "modify-not-allowed": 1, "type": "string", "description": "Configure start IP address of NAT pool", "format": "ipv4-address"}, "vrid": {"description": "Configure VRRP-A vrid (Specify ha VRRP-A vrid)", "format": "number", "optional": true, "maximum": 31, "minimum": 1, "modify-not-allowed": 1, "type": "number"}, "netmask": {"optional": true, "modify-not-allowed": 1, "type": "string", "description": "Configure mask for pool", "format": "ipv4-netmask-brief"}, "end-address": {"optional": true, "modify-not-allowed": 1, "type": "string", "description": "Configure end IP address of NAT pool", "format": "ipv4-address"}, "shared": {"description": "Share this pool with other partitions (default: not shared)", "partition-visibility": "shared", "default": 0, "optional": true, "format": "flag", "modify-not-allowed": 1, "type": "number"}, "pool-name": {"description": "Specify pool name or pool group", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/cgnv6/one-to-one/pool/{pool-name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/one-to-one`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "one-to-one"
        self.a10_url="/axapi/v3/cgnv6/one-to-one"
        self.DeviceProxy = ""
        self.pool_group_list = []
        self.A10WW_global = {}
        self.pool_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


