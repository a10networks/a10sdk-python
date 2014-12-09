from a10sdk.common.A10BaseClass import A10BaseClass


class Limit(A10BaseClass):
    
    """Class Description::
    Specify limit for GSLB Message Protocol.

    Class limit supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ardt_response: {"description": "Response Messages of Active RDT, default is 1000 (Number)", "format": "number", "default": 1000, "optional": true, "maximum": 1000000, "minimum": 0, "type": "number"}
    :param conn_response: {"description": "Response Messages of Connection Load, default is no limit (Number)", "format": "number", "default": 0, "optional": true, "maximum": 1000000, "minimum": 0, "type": "number"}
    :param ardt_session: {"description": "Sessions of Active RDT, default is 32768 (Number)", "format": "number", "default": 32768, "optional": true, "maximum": 1000000, "minimum": 0, "type": "number"}
    :param ardt_query: {"description": "Query Messages of Active RDT, default is 200 (Number)", "format": "number", "default": 200, "optional": true, "maximum": 1000000, "minimum": 0, "type": "number"}
    :param message: {"description": "Amount of Messages, default is 10000 (Number)", "format": "number", "default": 10000, "optional": true, "maximum": 1000000, "minimum": 0, "type": "number"}
    :param response: {"description": "Amount of Response Messages, default is 3600 (Number)", "format": "number", "default": 3600, "optional": true, "maximum": 1000000, "minimum": 0, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/protocol/limit`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "limit"
        self.a10_url="/axapi/v3/gslb/protocol/limit"
        self.DeviceProxy = ""
        self.ardt_response = ""
        self.conn_response = ""
        self.ardt_session = ""
        self.ardt_query = ""
        self.message = ""
        self.response = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


