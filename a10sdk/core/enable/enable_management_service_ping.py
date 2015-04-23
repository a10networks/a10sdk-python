from a10sdk.common.A10BaseClass import A10BaseClass


class Ping(A10BaseClass):
    
    """    :param acl_v6_list: {"minItems": 1, "items": {"type": "acl-v6"}, "uniqueItems": true, "array": [{"required": ["acl-name"], "properties": {"acl-name": {"description": "ACL name", "format": "string", "minLength": 1, "optional": false, "maxLength": 16, "type": "string"}, "ve-cfg": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ve-end": {"type": "number", "description": "VE port", "format": "number"}, "ve-start": {"type": "number", "description": "VE port (VE Interface number)", "format": "number"}, "optional": true}}]}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "eth-cfg": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ethernet-start": {"type": "number", "description": "Ethernet port (Ethernet Interface number)", "format": "interface"}, "ethernet-end": {"type": "number", "description": "Ethernet port", "format": "interface"}, "optional": true}}]}}}], "type": "array", "$ref": "/axapi/v3/enable-management/service/ping/acl-v6/{acl-name}"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param acl_v4_list: {"minItems": 1, "items": {"type": "acl-v4"}, "uniqueItems": true, "array": [{"required": ["acl-id"], "properties": {"ve-cfg": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ve-end": {"type": "number", "description": "VE port", "format": "number"}, "ve-start": {"type": "number", "description": "VE port (VE Interface number)", "format": "number"}, "optional": true}}]}, "acl-id": {"description": "ACL id", "format": "number", "type": "number", "maximum": 199, "minimum": 1, "optional": false}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "eth-cfg": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ethernet-start": {"type": "number", "description": "Ethernet port (Ethernet Interface number)", "format": "interface"}, "ethernet-end": {"type": "number", "description": "Ethernet port", "format": "interface"}, "optional": true}}]}}}], "type": "array", "$ref": "/axapi/v3/enable-management/service/ping/acl-v4/{acl-id}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Ping service.

    Class ping supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/enable-management/service/ping`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ping"
        self.a10_url="/axapi/v3/enable-management/service/ping"
        self.DeviceProxy = ""
        self.acl_v6_list = []
        self.uuid = ""
        self.acl_v4_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


