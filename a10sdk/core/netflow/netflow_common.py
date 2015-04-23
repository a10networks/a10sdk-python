from a10sdk.common.A10BaseClass import A10BaseClass


class Common(A10BaseClass):
    
    """Class Description::
    NetFlow/IPFIX common settings.

    Class common supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param max_packet_queue_time: {"description": "Configure netflow packet queue time (Max packet queue time(*20ms). Default:50( *20ms = 1s)))", "format": "number", "default": 50, "optional": true, "maximum": 50, "minimum": 0, "type": "number"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/netflow/common`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "common"
        self.a10_url="/axapi/v3/netflow/common"
        self.DeviceProxy = ""
        self.max_packet_queue_time = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


