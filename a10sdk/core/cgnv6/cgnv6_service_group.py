from a10sdk.common.A10BaseClass import A10BaseClass


class ServiceGroup(A10BaseClass):
    
    """Class Description::
    Service Group.

    Class service-group supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param shared_partition: {"description": "Share with a single partition (Partition Name)", "partition-visibility": "shared", "minLength": 1, "format": "string", "optional": true, "maxLength": 14, "type": "string"}
    :param protocol: {"description": "'tcp': TCP LB service; 'udp': UDP LB service; ", "format": "enum", "type": "string", "enum": ["tcp", "udp"], "modify-not-allowed": 1, "optional": true}
    :param name: {"description": "CGNV6 Service Name", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 127, "type": "string"}
    :param health_check: {"description": "Health Check (Monitor Name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "type": "string", "$ref": "/axapi/v3/health/monitor"}
    :param member_list: {"minItems": 1, "items": {"type": "member"}, "uniqueItems": true, "array": [{"required": ["name", "port"], "properties": {"name": {"description": "Member name", "format": "comp-string", "minLength": 1, "optional": false, "maxLength": 127, "type": "string", "$ref": "/axapi/v3/cgnv6/server"}, "port": {"description": "Port number", "format": "number", "default": 65534, "optional": false, "maximum": 65534, "minimum": 0, "type": "number", "$ref": "/axapi/v3/cgnv6/server/port"}}}], "type": "array", "$ref": "/axapi/v3/cgnv6/service-group/{name}/member/{name}+{port}"}
    :param shared_group: {"description": "Share with a partition group (Partition Group Name)", "partition-visibility": "shared", "minLength": 1, "format": "string", "optional": true, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/service-group/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "service-group"
        self.a10_url="/axapi/v3/cgnv6/service-group/{name}"
        self.DeviceProxy = ""
        self.shared_partition = ""
        self.protocol = ""
        self.name = ""
        self.health_check = ""
        self.member_list = []
        self.shared_group = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


