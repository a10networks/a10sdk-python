from a10sdk.common.A10BaseClass import A10BaseClass


class CmUt(A10BaseClass):
    
    """Class Description::
    CM Unit Test module.

    Class cm-ut supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param post_modify_parent_list: {"minItems": 1, "items": {"type": "post-modify-parent"}, "uniqueItems": true, "array": [{"required": ["k1"], "properties": {"post-modify-child": {"type": "object", "properties": {"f1": {"minimum": 1, "type": "number", "maximum": 32, "format": "number"}}}, "k1": {"minLength": 1, "maxLength": 32, "type": "string", "optional": false, "format": "string"}}}], "type": "array", "$ref": "https://axapi.a10networks.com/axapi/v3/cm-ut/post-modify-parent/{k1}"}
    :param obj_key_2_list: {"minItems": 1, "items": {"type": "obj-key-2"}, "uniqueItems": true, "array": [{"required": ["k1", "k2"], "properties": {"k2": {"minLength": 1, "maxLength": 32, "type": "string", "optional": false, "format": "string"}, "k1": {"optional": false, "minimum": 1, "type": "number", "maximum": 32, "format": "number"}, "d1": {"optional": true, "type": "string", "description": "some data", "format": "ipv4-address"}}}], "type": "array", "$ref": "https://axapi.a10networks.com/axapi/v3/cm-ut/obj-key-2/{k1}+{k2}"}
    :param obj_key_1_list: {"minItems": 1, "items": {"type": "obj-key-1"}, "uniqueItems": true, "array": [{"required": ["k1", "k2"], "properties": {"k2": {"optional": false, "minimum": 1, "type": "number", "maximum": 32, "format": "number"}, "k1": {"minLength": 1, "maxLength": 32, "type": "string", "optional": false, "format": "string"}, "d1": {"description": "some data", "format": "string", "minLength": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "https://axapi.a10networks.com/axapi/v3/cm-ut/obj-key-1/{k1}+{k2}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cm-ut`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "cm-ut"
        self.a10_url="/axapi/v3/cm-ut"
        self.DeviceProxy = ""
        self.list_entry_1 = {}
        self.list_entry_2 = {}
        self.post_modify_parent_list = []
        self.list_enum_1 = {}
        self.obj_key_2_list = []
        self.obj_key_1_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


