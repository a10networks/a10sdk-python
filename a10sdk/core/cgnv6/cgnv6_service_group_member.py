from a10sdk.common.A10BaseClass import A10BaseClass


class Member(A10BaseClass):
    
    """Class Description::
    Service Group Member.

    Class member supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param name: {"description": "Member name", "format": "comp-string", "minLength": 1, "optional": false, "maxLength": 127, "type": "string", "$ref": "/axapi/v3/cgnv6/server"}
    :param port: {"description": "Port number", "format": "number", "default": 65534, "optional": false, "maximum": 65534, "minimum": 0, "type": "number", "$ref": "/axapi/v3/cgnv6/server/port"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/service-group/{name}/member/{name}+{port}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name","port"]

        self.b_key = "member"
        self.a10_url="/axapi/v3/cgnv6/service-group/{name}/member/{name}+{port}"
        self.DeviceProxy = ""
        self.name = ""
        self.port = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


