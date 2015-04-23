from a10sdk.common.A10BaseClass import A10BaseClass


class Port(A10BaseClass):
    
    """Class Description::
    Add port to the current port list.

    Class port supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param end_port: {"description": "Add a range of ports into the current port list (Specify port number)", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": true}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param start_port: {"description": "Specify port number", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": false}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/classification/port-list/{listname}/port/{start_port}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "start_port"]

        self.b_key = "port"
        self.a10_url="/axapi/v3/classification/port-list/{listname}/port/{start_port}"
        self.DeviceProxy = ""
        self.end_port = ""
        self.uuid = ""
        self.start_port = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


