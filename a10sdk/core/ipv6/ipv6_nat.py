from a10sdk.common.A10BaseClass import A10BaseClass


class Nat(A10BaseClass):
    
    """Class Description::
    Configure IPv6 NAT.

    Class nat supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param pool_group_list: {"minItems": 1, "items": {"type": "pool-group"}, "uniqueItems": true, "array": [{"required": ["pool-group-name"], "properties": {"member-list": {"minItems": 1, "items": {"type": "member"}, "uniqueItems": true, "array": [{"required": ["pool-name"], "properties": {"uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "pool-name": {"description": "Specify NAT pool name", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/ipv6/nat/pool-group/{pool-group-name}/member/{pool-name}"}, "pool-group-name": {"description": "Specify pool group name", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "vrid": {"description": "Specify VRRP-A vrid (Specify ha VRRP-A vrid)", "format": "number", "optional": true, "maximum": 31, "minimum": 1, "modify-not-allowed": 1, "type": "number"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/ipv6/nat/pool-group/{pool-group-name}"}
    :param pool_list: {"minItems": 1, "items": {"type": "pool"}, "uniqueItems": true, "array": [{"required": ["pool-name"], "properties": {"uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "start-address": {"optional": true, "modify-not-allowed": 1, "type": "string", "description": "Configure start IP address of NAT pool", "format": "ipv6-address"}, "vrid": {"description": "Specify VRRP-A vrid (Specify ha VRRP-A vrid)", "format": "number", "optional": true, "maximum": 31, "minimum": 1, "modify-not-allowed": 1, "type": "number"}, "netmask": {"description": "Configure mask for pool", "format": "number", "optional": true, "maximum": 128, "minimum": 64, "modify-not-allowed": 1, "type": "number"}, "end-address": {"optional": true, "modify-not-allowed": 1, "type": "string", "description": "Configure end IP address of NAT pool", "format": "ipv6-address"}, "ip-rr": {"description": "Use IP address round-robin behavior", "format": "flag", "default": 0, "type": "number", "modify-not-allowed": 1, "optional": true}, "scaleout-device-id": {"description": "Configure Scaleout device id to which this NAT pool is to be bound (Specify Scaleout device id)", "format": "number", "optional": true, "maximum": 64, "minimum": 1, "modify-not-allowed": 1, "type": "number"}, "gateway": {"optional": true, "modify-not-allowed": 1, "type": "string", "description": "Configure gateway IP", "format": "ipv6-address"}, "pool-name": {"description": "Specify pool name", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/ipv6/nat/pool/{pool-name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ipv6/nat`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "nat"
        self.a10_url="/axapi/v3/ipv6/nat"
        self.DeviceProxy = ""
        self.icmpv6 = {}
        self.pool_group_list = []
        self.inside = {}
        self.pool_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


