from a10sdk.common.A10BaseClass import A10BaseClass


class Radius(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param exact_value_lsn_lid: {"description": "LSN Limit ID (LID index)", "minimum": 1, "type": "number", "maximum": 1023, "format": "number"}
    :param attribute: {"enum": ["custom1", "custom2", "custom3", "imei", "imsi", "msisdn", "default"], "type": "string", "description": "'custom1': Configure RADIUS Attribute Custom 1; 'custom2': Configure RADIUS Attribute Custom 2; 'custom3': Configure RADIUS Attribute Custom 3; 'imei': Configure RADIUS Attribute IMEI; 'imsi': Configure RADIUS Attribute IMSI; 'msisdn': Configure RADIUS Attribute MSISDN; 'default': Configure default; ", "format": "enum"}
    :param starts_with_lsn_lid: {"description": "LSN Limit ID (LID index)", "minimum": 1, "type": "number", "maximum": 1023, "format": "number"}
    :param exact_value: {"minLength": 1, "maxLength": 31, "type": "string", "description": "Value of the attribute", "format": "string-rlx"}
    :param starts_with: {"minLength": 1, "maxLength": 31, "type": "string", "description": "Value of the attribute", "format": "string-rlx"}
    :param default_lsn_lid: {"description": "LSN Limit ID (LID index)", "minimum": 1, "type": "number", "maximum": 1023, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "radius"
        self.DeviceProxy = ""
        self.exact_value_lsn_lid = ""
        self.attribute = ""
        self.starts_with_lsn_lid = ""
        self.exact_value = ""
        self.starts_with = ""
        self.default_lsn_lid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class LsnRadiusProfile(A10BaseClass):
    
    """Class Description::
    Configure LSN RADIUS Profile.

    Class lsn-radius-profile supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param lid_profile_index: {"description": "LSN RADIUS Profile Index", "format": "number", "type": "number", "maximum": 16, "minimum": 1, "optional": false}
    :param radius: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"exact-value-lsn-lid": {"description": "LSN Limit ID (LID index)", "minimum": 1, "type": "number", "maximum": 1023, "format": "number"}, "attribute": {"enum": ["custom1", "custom2", "custom3", "imei", "imsi", "msisdn", "default"], "type": "string", "description": "'custom1': Configure RADIUS Attribute Custom 1; 'custom2': Configure RADIUS Attribute Custom 2; 'custom3': Configure RADIUS Attribute Custom 3; 'imei': Configure RADIUS Attribute IMEI; 'imsi': Configure RADIUS Attribute IMSI; 'msisdn': Configure RADIUS Attribute MSISDN; 'default': Configure default; ", "format": "enum"}, "starts-with-lsn-lid": {"description": "LSN Limit ID (LID index)", "minimum": 1, "type": "number", "maximum": 1023, "format": "number"}, "exact-value": {"minLength": 1, "maxLength": 31, "type": "string", "description": "Value of the attribute", "format": "string-rlx"}, "starts-with": {"minLength": 1, "maxLength": 31, "type": "string", "description": "Value of the attribute", "format": "string-rlx"}, "default-lsn-lid": {"description": "LSN Limit ID (LID index)", "minimum": 1, "type": "number", "maximum": 1023, "format": "number"}, "optional": true}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/lsn-radius-profile/{lid_profile_index}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "lid_profile_index"]

        self.b_key = "lsn-radius-profile"
        self.a10_url="/axapi/v3/cgnv6/lsn-radius-profile/{lid_profile_index}"
        self.DeviceProxy = ""
        self.lid_profile_index = ""
        self.radius = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


