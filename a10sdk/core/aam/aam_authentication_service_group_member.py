from a10sdk.common.A10BaseClass import A10BaseClass


class Member(A10BaseClass):
    
    """Class Description::
    Authentication service group member.

    Class member supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param member_priority: {"description": "Priority of Port in the Group", "format": "number", "type": "number", "maximum": 16, "minimum": 1, "optional": true}
    :param name: {"description": "Member name", "format": "comp-string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/aam/authentication/server/ldap"}
    :param member_state: {"description": "'enable': Enable member service port; 'disable': Disable member service port; ", "format": "enum", "default": "enable", "type": "string", "enum": ["enable", "disable"], "optional": true}
    :param port: {"description": "Port number", "format": "number", "default": 65534, "optional": false, "maximum": 65534, "minimum": 0, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/service-group/{name}/member/{name}+{port}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name","port"]

        self.b_key = "member"
        self.a10_url="/axapi/v3/aam/authentication/service-group/{name}/member/{name}+{port}"
        self.DeviceProxy = ""
        self.member_priority = ""
        self.name = ""
        self.member_state = ""
        self.port = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


