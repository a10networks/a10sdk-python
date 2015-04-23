from a10sdk.common.A10BaseClass import A10BaseClass


class AclIdListList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param msl: {"description": "Maximum Session Life Value", "format": "number", "type": "number", "maximum": 1800, "minimum": 1, "optional": true}
    :param acl_id: {"description": "Acl id", "format": "number", "optional": false, "maximum": 199, "minimum": 1, "type": "number", "$ref": "/axapi/v3/access-list/standard"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param pool: {"description": "Pool or Pool Group (Pool or Pool Group Name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 128, "type": "string", "$ref": "/axapi/v3/ip/nat/pool"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "acl-id-list-list"
        self.DeviceProxy = ""
        self.msl = ""
        self.acl_id = ""
        self.uuid = ""
        self.pool = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class AclNameListList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param msl: {"description": "Maximum Session Life Value", "format": "number", "type": "number", "maximum": 1800, "minimum": 1, "optional": true}
    :param name: {"description": "Apply an access list", "format": "string", "minLength": 1, "optional": false, "maxLength": 16, "type": "string", "$ref": "/axapi/v3/ip/access-list"}
    :param pool: {"description": "Pool or Pool Group (Pool or Pool Group Nam)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 128, "type": "string", "$ref": "/axapi/v3/ip/nat/pool"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "acl-name-list-list"
        self.DeviceProxy = ""
        self.msl = ""
        self.name = ""
        self.pool = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class List(A10BaseClass):
    
    """Class Description::
    access-list-number.

    Class list supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param acl_id_list_list: {"minItems": 1, "items": {"type": "acl-id-list"}, "uniqueItems": true, "array": [{"required": ["acl-id"], "properties": {"msl": {"description": "Maximum Session Life Value", "format": "number", "type": "number", "maximum": 1800, "minimum": 1, "optional": true}, "acl-id": {"description": "Acl id", "format": "number", "optional": false, "maximum": 199, "minimum": 1, "type": "number", "$ref": "/axapi/v3/access-list/standard"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "pool": {"description": "Pool or Pool Group (Pool or Pool Group Name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 128, "type": "string", "$ref": "/axapi/v3/ip/nat/pool"}}}], "type": "array", "$ref": "/axapi/v3/ip/nat/inside/source/list/acl-id-list/{acl-id}"}
    :param acl_name_list_list: {"minItems": 1, "items": {"type": "acl-name-list"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"msl": {"description": "Maximum Session Life Value", "format": "number", "type": "number", "maximum": 1800, "minimum": 1, "optional": true}, "name": {"description": "Apply an access list", "format": "string", "minLength": 1, "optional": false, "maxLength": 16, "type": "string", "$ref": "/axapi/v3/ip/access-list"}, "pool": {"description": "Pool or Pool Group (Pool or Pool Group Nam)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 128, "type": "string", "$ref": "/axapi/v3/ip/nat/pool"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/ip/nat/inside/source/list/acl-name-list/{name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ip/nat/inside/source/list`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "list"
        self.a10_url="/axapi/v3/ip/nat/inside/source/list"
        self.DeviceProxy = ""
        self.acl_id_list_list = []
        self.acl_name_list_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


