from a10sdk.common.A10BaseClass import A10BaseClass


class ServiceGroup(A10BaseClass):
    
    """Class Description::
    Authentication service group.

    Class service-group supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param health_check_disable: {"description": "Disable health check", "format": "flag", "default": 0, "optional": true, "not": "health-check", "type": "number"}
    :param protocol: {"description": "'tcp': TCP AAM service; 'udp': UDP AAM service; ", "format": "enum", "type": "string", "enum": ["tcp", "udp"], "modify-not-allowed": 1, "optional": true}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param lb_method: {"optional": true, "enum": ["round-robin"], "type": "string", "description": "'round-robin': Round robin on server level; ", "format": "enum"}
    :param member_list: {"minItems": 1, "items": {"type": "member"}, "uniqueItems": true, "array": [{"required": ["name", "port"], "properties": {"uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "member-priority": {"description": "Priority of Port in the Group", "format": "number", "type": "number", "maximum": 16, "minimum": 1, "optional": true}, "name": {"description": "Member name", "format": "comp-string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/aam/authentication/server/ldap"}, "member-state": {"description": "'enable': Enable member service port; 'disable': Disable member service port; ", "format": "enum", "default": "enable", "type": "string", "enum": ["enable", "disable"], "optional": true}, "port": {"description": "Port number", "format": "number", "default": 65534, "optional": false, "maximum": 65534, "minimum": 1, "type": "number"}}}], "type": "array", "$ref": "/axapi/v3/aam/authentication/service-group/{name}/member/{name}+{port}"}
    :param health_check: {"description": "Health Check (Monitor Name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "not": "health-check-disable", "type": "string", "$ref": "/axapi/v3/health/monitor"}
    :param name: {"description": "Specify AAM service group name", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 127, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/service-group/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "service-group"
        self.a10_url="/axapi/v3/aam/authentication/service-group/{name}"
        self.DeviceProxy = ""
        self.health_check_disable = ""
        self.protocol = ""
        self.uuid = ""
        self.lb_method = ""
        self.member_list = []
        self.health_check = ""
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


