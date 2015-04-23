from a10sdk.common.A10BaseClass import A10BaseClass


class PortList(A10BaseClass):
    
    """Class Description::
    Configure or create port list.

    Class port-list supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param listname: {"description": "Specify port list name", "format": "string", "minLength": 1, "optional": false, "maxLength": 31, "type": "string"}
    :param port_list: {"minItems": 1, "items": {"type": "port"}, "uniqueItems": true, "array": [{"required": ["start-port"], "properties": {"end-port": {"description": "Add a range of ports into the current port list (Specify port number)", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": true}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "start-port": {"description": "Specify port number", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": false}}}], "type": "array", "$ref": "/axapi/v3/classification/port-list/{listname}/port/{start-port}"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/classification/port-list/{listname}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "listname"]

        self.b_key = "port-list"
        self.a10_url="/axapi/v3/classification/port-list/{listname}"
        self.DeviceProxy = ""
        self.listname = ""
        self.port_list = []
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


