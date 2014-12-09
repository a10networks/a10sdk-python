from a10sdk.common.A10BaseClass import A10BaseClass


class Contact(A10BaseClass):
    
    """Class Description::
    Text for mib object sysContact.

    Class contact supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param contact_name: {"description": "Identification of the contact person for this managed node", "format": "string", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/snmp-server/contact`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "contact"
        self.a10_url="/axapi/v3/snmp-server/contact"
        self.DeviceProxy = ""
        self.contact_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


