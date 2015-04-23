from a10sdk.common.A10BaseClass import A10BaseClass


class Member(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param member_name: {"platform-specific-default": 1, "type": "string", "description": "Service name", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "member"
        self.DeviceProxy = ""
        self.member_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class DisableSiteList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param disable_site: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Site name", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "disable-site-list"
        self.DeviceProxy = ""
        self.disable_site = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ServiceGroup(A10BaseClass):
    
    """Class Description::
    Specify GSLB Service Group.

    Class service-group supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param member: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"member-name": {"platform-specific-default": 1, "type": "string", "description": "Service name", "format": "string-rlx"}, "optional": true}}]}
    :param service_group_name: {"description": "Specify Service Group name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param disable_site_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "disable-site": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Site name", "format": "string"}}}]}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param disable: {"default": 0, "optional": true, "type": "number", "description": "Disable all members", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/service-group/{service_group_name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "service_group_name"]

        self.b_key = "service-group"
        self.a10_url="/axapi/v3/gslb/service-group/{service_group_name}"
        self.DeviceProxy = ""
        self.member = []
        self.service_group_name = ""
        self.disable_site_list = []
        self.uuid = ""
        self.disable = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


