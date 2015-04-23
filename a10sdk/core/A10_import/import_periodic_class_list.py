from a10sdk.common.A10BaseClass import A10BaseClass


class ClassList(A10BaseClass):
    
    """Class Description::
    Class list files.

    Class class-list supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param period: {"description": "Specify the period in second", "format": "number", "type": "number", "maximum": 31536000, "minimum": 60, "optional": true}
    :param remote_file: {"optional": true, "type": "string", "description": "profile name for remote url", "format": "url"}
    :param use_mgmt_port: {"default": 0, "optional": true, "type": "number", "description": "Use management port as source port", "format": "flag"}
    :param class_list: {"description": "Class List File", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/import-periodic/class-list/{class_list}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "class_list"]

        self.b_key = "class-list"
        self.a10_url="/axapi/v3/import-periodic/class-list/{class_list}"
        self.DeviceProxy = ""
        self.uuid = ""
        self.period = ""
        self.remote_file = ""
        self.use_mgmt_port = ""
        self.class_list = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


