from a10sdk.common.A10BaseClass import A10BaseClass


class ResourceUsage(A10BaseClass):
    
    """    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param class_list_ipv6_addr_count: {"platform-specific-range": 1, "platform-specific-default": 1, "description": "Total IPv6 addresses for class-list", "format": "number", "optional": true, "type": "number"}
    :param max_aflex_file_size: {"description": "Set maximum aFleX file size (Maximum file size in KBytes, default is 32K)", "format": "number", "default": 32, "optional": true, "maximum": 256, "minimum": 16, "type": "number"}
    :param l4_session_count: {"platform-specific-range": 1, "platform-specific-default": 1, "description": "Total Sessions in the System", "format": "number", "optional": true, "type": "number"}
    :param auth_portal_html_file_size: {"description": "Specify maximum html file size for http authentication", "format": "number", "default": 20, "optional": true, "maximum": 120, "minimum": 4, "type": "number"}
    :param auth_portal_image_file_size: {"description": "Specify maximum image file size for default portal", "format": "number", "default": 6, "optional": true, "maximum": 80, "minimum": 1, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Configure System Resource Usage.

    Class resource-usage supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/system/resource-usage`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "resource-usage"
        self.a10_url="/axapi/v3/system/resource-usage"
        self.DeviceProxy = ""
        self.uuid = ""
        self.class_list_ipv6_addr_count = ""
        self.max_aflex_file_size = ""
        self.l4_session_count = ""
        self.auth_portal_html_file_size = ""
        self.auth_portal_image_file_size = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


