from a10sdk.common.A10BaseClass import A10BaseClass


class Axdebug(A10BaseClass):
    
    """Class Description::
    AX Debug Packet File.

    Class axdebug supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param remote_file: {"optional": true, "type": "string", "description": "profile name for remote url", "format": "url"}
    :param merged_pcap: {"default": 0, "optional": true, "type": "number", "description": "Export the merged pcap file when there are multiple Export sessions", "format": "flag"}
    :param period: {"description": "Specify the period in second", "format": "number", "type": "number", "maximum": 31536000, "minimum": 60, "optional": true}
    :param axdebug: {"description": "AX Debug Packet File", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param use_mgmt_port: {"default": 0, "optional": true, "type": "number", "description": "Use management port as source port", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/export-periodic/axdebug/{axdebug}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "axdebug"]

        self.b_key = "axdebug"
        self.a10_url="/axapi/v3/export-periodic/axdebug/{axdebug}"
        self.DeviceProxy = ""
        self.uuid = ""
        self.remote_file = ""
        self.merged_pcap = ""
        self.period = ""
        self.axdebug = ""
        self.use_mgmt_port = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


