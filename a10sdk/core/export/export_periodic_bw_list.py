from a10sdk.common.A10BaseClass import A10BaseClass


class BwList(A10BaseClass):
    
    """Class Description::
    Black white list files.

    Class bw-list supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param remote_file: {"optional": true, "type": "string", "description": "profile name for remote url", "format": "url"}
    :param bw_list: {"description": "Black white List File", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param use_mgmt_port: {"default": 0, "optional": true, "type": "number", "description": "Use management port as source port", "format": "flag"}
    :param period: {"description": "Specify the period in second", "format": "number", "type": "number", "maximum": 31536000, "minimum": 60, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/export-periodic/bw-list/{bw_list}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "bw_list"]

        self.b_key = "bw-list"
        self.a10_url="/axapi/v3/export-periodic/bw-list/{bw_list}"
        self.DeviceProxy = ""
        self.remote_file = ""
        self.bw_list = ""
        self.use_mgmt_port = ""
        self.period = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


