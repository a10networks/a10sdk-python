from a10sdk.common.A10BaseClass import A10BaseClass


class Vtep(A10BaseClass):
    
    """Class Description::
    Virtual Tunnel end point Configuration.

    Class vtep supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param destination_ip_address_list: {"minItems": 1, "items": {"type": "destination-ip-address"}, "uniqueItems": true, "array": [{"required": ["ip-address"], "properties": {"vni-list": {"minItems": 1, "items": {"type": "vni"}, "uniqueItems": true, "array": [{"required": ["segment"], "properties": {"segment": {"description": "VNI configured for the remote VTEP", "format": "number", "type": "number", "maximum": 16777215, "minimum": 1, "optional": false}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/overlay-tunnel/vtep/{id}/destination-ip-address/{ip-address}/vni/{segment}"}, "encap": {"optional": true, "enum": ["nvgre", "vxlan"], "type": "string", "description": "'nvgre': Tunnel Encapsulation Type is NVGRE; 'vxlan': Tunnel Encapsulation Type is NVGRE; ", "format": "enum"}, "ip-address": {"optional": false, "type": "string", "description": "IP Address of the remote VTEP", "format": "ipv4-address"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/overlay-tunnel/vtep/{id}/destination-ip-address/{ip-address}"}
    :param encap: {"description": "'nvgre': Tunnel Encapsulation Type is NVGRE; 'vxlan': Tunnel Encapsulation Type is NVGRE; ", "format": "enum", "default": "vxlan", "type": "string", "enum": ["nvgre", "vxlan"], "optional": true}
    :param host_list: {"minItems": 1, "items": {"type": "host"}, "uniqueItems": true, "array": [{"required": ["ip-addr", "overlay-mac-addr", "vni", "destination-vtep"], "properties": {"destination-vtep": {"optional": false, "type": "string", "description": "Configure the VTEP IP address (IPv4 address of the VTEP for the remote host)", "format": "ipv4-address"}, "ip-addr": {"optional": false, "type": "string", "description": "IPv4 address of the overlay host", "format": "ipv4-address"}, "vni": {"description": " Configure the segment id ( VNI of the remote host)", "format": "number", "type": "number", "maximum": 16777215, "minimum": 1, "optional": false}, "overlay-mac-addr": {"optional": false, "type": "string", "description": "MAC Address of the overlay host", "format": "mac-address"}}}], "type": "array", "$ref": "/axapi/v3/overlay-tunnel/vtep/{id}/host/{ip-addr}+{overlay-mac-addr}+{vni}+{destination-vtep}"}
    :param id: {"description": "VTEP Identifier", "format": "number", "type": "number", "maximum": 64, "minimum": 1, "optional": false}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/overlay-tunnel/vtep/{id}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "id"]

        self.b_key = "vtep"
        self.a10_url="/axapi/v3/overlay-tunnel/vtep/{id}"
        self.DeviceProxy = ""
        self.uuid = ""
        self.destination_ip_address_list = []
        self.encap = ""
        self.host_list = []
        self.A10WW_id = ""
        self.source_ip_address = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


