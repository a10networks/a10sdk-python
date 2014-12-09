from a10sdk.common.A10BaseClass import A10BaseClass


class DestinationIpAddress(A10BaseClass):
    
    """Class Description::
    Configure remote tunnel end point parameters.

    Class destination-ip-address supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param vni_list: {"minItems": 1, "items": {"type": "vni"}, "uniqueItems": true, "array": [{"required": ["segment"], "properties": {"segment": {"description": "VNI configured for the remote VTEP", "format": "number", "type": "number", "maximum": 16777215, "minimum": 1, "optional": false}}}], "type": "array", "$ref": "/axapi/v3/overlay-tunnel/vtep/{id}/destination-ip-address/{ip-address}/vni/{segment}"}
    :param encap: {"optional": true, "enum": ["nvgre", "vxlan"], "type": "string", "description": "'nvgre': Tunnel Encapsulation Type is NVGRE; 'vxlan': Tunnel Encapsulation Type is NVGRE; ", "format": "enum"}
    :param ip_address: {"optional": false, "type": "string", "description": "IP Address of the remote VTEP", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/overlay-tunnel/vtep/{id}/destination-ip-address/{ip_address}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "ip_address"]

        self.b_key = "destination-ip-address"
        self.a10_url="/axapi/v3/overlay-tunnel/vtep/{id}/destination-ip-address/{ip_address}"
        self.DeviceProxy = ""
        self.vni_list = []
        self.encap = ""
        self.ip_address = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


