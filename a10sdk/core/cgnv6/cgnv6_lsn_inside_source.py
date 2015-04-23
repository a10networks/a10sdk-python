from a10sdk.common.A10BaseClass import A10BaseClass


class Source(A10BaseClass):
    
    """Class Description::
    Source.

    Class source supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param class_list: {"description": "Class List (Class List Name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/lsn/inside/source`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "source"
        self.a10_url="/axapi/v3/cgnv6/lsn/inside/source"
        self.DeviceProxy = ""
        self.uuid = ""
        self.class_list = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


