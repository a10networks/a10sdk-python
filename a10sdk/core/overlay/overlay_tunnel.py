from a10sdk.common.A10BaseClass import A10BaseClass


class OverlayTunnel(A10BaseClass):
    
    """Class Description::
    Configure a Tunnel end point.

    Class overlay-tunnel supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param vtep_list: {"minItems": 1, "items": {"type": "vtep"}, "uniqueItems": true, "array": [{"required": ["id"], "properties": {"uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "destination-ip-address-list": {"minItems": 1, "items": {"type": "destination-ip-address"}, "uniqueItems": true, "array": [{"required": ["ip-address"], "properties": {"vni-list": {"minItems": 1, "items": {"type": "vni"}, "uniqueItems": true, "array": [{"required": ["segment"], "properties": {"segment": {"description": "VNI configured for the remote VTEP", "format": "number", "type": "number", "maximum": 16777215, "minimum": 1, "optional": false}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/overlay-tunnel/vtep/{id}/destination-ip-address/{ip-address}/vni/{segment}"}, "encap": {"optional": true, "enum": ["nvgre", "vxlan"], "type": "string", "description": "'nvgre': Tunnel Encapsulation Type is NVGRE; 'vxlan': Tunnel Encapsulation Type is NVGRE; ", "format": "enum"}, "ip-address": {"optional": false, "type": "string", "description": "IP Address of the remote VTEP", "format": "ipv4-address"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/overlay-tunnel/vtep/{id}/destination-ip-address/{ip-address}"}, "encap": {"description": "'nvgre': Tunnel Encapsulation Type is NVGRE; 'vxlan': Tunnel Encapsulation Type is NVGRE; ", "format": "enum", "default": "vxlan", "type": "string", "enum": ["nvgre", "vxlan"], "optional": true}, "host-list": {"minItems": 1, "items": {"type": "host"}, "uniqueItems": true, "array": [{"required": ["ip-addr", "overlay-mac-addr", "vni", "destination-vtep"], "properties": {"destination-vtep": {"optional": false, "type": "string", "description": "Configure the VTEP IP address (IPv4 address of the VTEP for the remote host)", "format": "ipv4-address"}, "ip-addr": {"optional": false, "type": "string", "description": "IPv4 address of the overlay host", "format": "ipv4-address"}, "vni": {"description": " Configure the segment id ( VNI of the remote host)", "format": "number", "type": "number", "maximum": 16777215, "minimum": 1, "optional": false}, "overlay-mac-addr": {"optional": false, "type": "string", "description": "MAC Address of the overlay host", "format": "mac-address"}}}], "type": "array", "$ref": "/axapi/v3/overlay-tunnel/vtep/{id}/host/{ip-addr}+{overlay-mac-addr}+{vni}+{destination-vtep}"}, "id": {"description": "VTEP Identifier", "format": "number", "type": "number", "maximum": 64, "minimum": 1, "optional": false}, "source-ip-address": {"type": "object", "properties": {"vni-list": {"minItems": 1, "items": {"type": "vni"}, "uniqueItems": true, "array": [{"required": ["segment"], "properties": {"lif": {"description": "Logical interface binding the Provider Partition to the User Partition (logical interface number)", "format": "number", "type": "number", "maximum": 128, "minimum": 1, "optional": true}, "partition": {"description": "Name of the Partition with the L2 segment being extended (Name of the User Partition with the L2 segment being extended)", "format": "string", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}, "segment": {"description": "Id of the segment that is being extended", "format": "number", "type": "number", "maximum": 16777215, "minimum": 1, "optional": false}, "gateway": {"default": 0, "optional": true, "type": "number", "description": "This is a Gateway segment id", "format": "flag"}}}], "type": "array", "$ref": "/axapi/v3/overlay-tunnel/vtep/{id}/source-ip-address/vni/{segment}"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "maxLength": 64, "type": "string"}, "ip-address": {"type": "string", "description": "Source Tunnel End Point IPv4 address", "format": "ipv4-address"}}, "$ref": "/axapi/v3/overlay-tunnel/vtep/{id}/source-ip-address"}}}], "type": "array", "$ref": "/axapi/v3/overlay-tunnel/vtep/{id}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/overlay-tunnel`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "overlay-tunnel"
        self.a10_url="/axapi/v3/overlay-tunnel"
        self.DeviceProxy = ""
        self.options = {}
        self.vtep_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


