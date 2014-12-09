from a10sdk.common.A10BaseClass import A10BaseClass


class View(A10BaseClass):
    
    """Class Description::
    Defines named "view" - a subset of the overall OID tree.

    Class view supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param mask: {"description": "Hex octets, separated by '.', mask of oid", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "not": "type", "type": "string"}
    :param oid: {"description": "MIB view family name or oid", "format": "string", "minLength": 1, "optional": false, "maxLength": 31, "type": "string"}
    :param type: {"description": "'included': MIB family is included in the view; 'excluded': MIB family is excluded from the view; ", "format": "enum", "type": "string", "enum": ["included", "excluded"], "not": "mask", "optional": true}
    :param viewname: {"description": "Name of the view", "format": "string", "minLength": 1, "optional": false, "maxLength": 31, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/snmp-server/view/{viewname}+{oid}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "viewname","oid"]

        self.b_key = "view"
        self.a10_url="/axapi/v3/snmp-server/view/{viewname}+{oid}"
        self.DeviceProxy = ""
        self.mask = ""
        self.oid = ""
        self.A10WW_type = ""
        self.viewname = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


