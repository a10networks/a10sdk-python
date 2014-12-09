from a10sdk.common.A10BaseClass import A10BaseClass


class Group(A10BaseClass):
    
    """Class Description::
    Define a User Security Model group.

    Class group supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param read: {"description": "specify a read view for the group (read view name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param groupname: {"description": "Name of the group", "format": "string", "minLength": 1, "optional": false, "maxLength": 31, "type": "string"}
    :param v3: {"optional": true, "enum": ["auth", "noauth", "priv"], "type": "string", "description": "'auth': group using the authNoPriv Security Level; 'noauth': group using the noAuthNoPriv Security Level; 'priv': group using SNMPv3 authPriv security level; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/snmp-server/group/{groupname}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "groupname"]

        self.b_key = "group"
        self.a10_url="/axapi/v3/snmp-server/group/{groupname}"
        self.DeviceProxy = ""
        self.read = ""
        self.groupname = ""
        self.v3 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


