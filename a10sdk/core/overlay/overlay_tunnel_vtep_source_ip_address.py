from a10sdk.common.A10BaseClass import A10BaseClass


class SourceIpAddress(A10BaseClass):
    
    """Class Description::
    IP Address of the local tunnel end point.

    Class source-ip-address supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param vni_list: {"minItems": 1, "items": {"type": "vni"}, "uniqueItems": true, "array": [{"required": ["segment"], "properties": {"lif": {"description": "Logical interface binding the Provider Partition to the User Partition (logical interface number)", "format": "number", "type": "number", "maximum": 128, "minimum": 1, "optional": true}, "partition": {"description": "Name of the Partition with the L2 segment being extended (Name of the User Partition with the L2 segment being extended)", "format": "string", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}, "segment": {"description": "Id of the segment that is being extended", "format": "number", "type": "number", "maximum": 16777215, "minimum": 1, "optional": false}, "gateway": {"default": 0, "optional": true, "type": "number", "description": "This is a Gateway segment id", "format": "flag"}}}], "type": "array", "$ref": "/axapi/v3/overlay-tunnel/vtep/{id}/source-ip-address/vni/{segment}"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param ip_address: {"optional": false, "type": "string", "description": "Source Tunnel End Point IPv4 address", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/overlay-tunnel/vtep/{id}/source-ip-address`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "source-ip-address"
        self.a10_url="/axapi/v3/overlay-tunnel/vtep/{id}/source-ip-address"
        self.DeviceProxy = ""
        self.vni_list = []
        self.uuid = ""
        self.ip_address = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


