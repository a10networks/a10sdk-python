from a10sdk.common.A10BaseClass import A10BaseClass


class Lw4O6(A10BaseClass):
    
    """    :param health_check_gateway_list: {"minItems": 1, "items": {"type": "health-check-gateway"}, "uniqueItems": true, "array": [{"required": ["ipv4-addr", "ipv6-addr"], "properties": {"ipv4-addr": {"optional": false, "type": "string", "description": "LW-4over6 IPv4 Gateway", "format": "ipv4-address"}, "ipv6-addr": {"optional": false, "type": "string", "description": "LW-4over6 IPv6 Gateway", "format": "ipv6-address"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/cgnv6/lw-4o6/health-check-gateway/{ipv4-addr}+{ipv6-addr}"}
    :param binding_table_list: {"minItems": 1, "items": {"type": "binding-table"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"tunnel-address-list": {"minItems": 1, "items": {"type": "tunnel-address"}, "uniqueItems": true, "array": [{"required": ["ipv6-tunnel-addr"], "properties": {"ipv6-tunnel-addr": {"optional": false, "type": "string", "description": "Tunnel IPv6 Endpoint Address", "format": "ipv6-address"}, "nat-address-list": {"minItems": 1, "items": {"type": "nat-address"}, "uniqueItems": true, "array": [{"required": ["ipv4-nat-addr"], "properties": {"ipv4-nat-addr": {"optional": false, "type": "string", "description": "NAT IPv4 Address", "format": "ipv4-address"}, "port-range-list": {"minItems": 1, "items": {"type": "port-range"}, "uniqueItems": true, "array": [{"required": ["port-start", "port-end"], "properties": {"port-start": {"optional": false, "type": "number", "description": "Single Port or Port Range Start", "format": "number"}, "port-end": {"optional": false, "type": "number", "description": "Port Range End", "format": "number"}}}], "type": "array", "$ref": "/axapi/v3/cgnv6/lw-4o6/binding-table/{name}/tunnel-address/{ipv6-tunnel-addr}/nat-address/{ipv4-nat-addr}/port-range/{port-start}+{port-end}"}}}], "type": "array", "$ref": "/axapi/v3/cgnv6/lw-4o6/binding-table/{name}/tunnel-address/{ipv6-tunnel-addr}/nat-address/{ipv4-nat-addr}"}}}], "type": "array", "$ref": "/axapi/v3/cgnv6/lw-4o6/binding-table/{name}/tunnel-address/{ipv6-tunnel-addr}"}, "name": {"description": "LW-4over6 Binding Table Name", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 128, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/cgnv6/lw-4o6/binding-table/{name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Configure LW-4over6.

    Class lw-4o6 supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/lw-4o6`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "lw-4o6"
        self.a10_url="/axapi/v3/cgnv6/lw-4o6"
        self.DeviceProxy = ""
        self.health_check_gateway_list = []
        self.A10WW_global = {}
        self.binding_table_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


