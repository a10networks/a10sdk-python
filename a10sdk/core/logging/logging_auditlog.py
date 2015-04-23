from a10sdk.common.A10BaseClass import A10BaseClass


class Auditlog(A10BaseClass):
    
    """Class Description::
    Set send auditlog to syslog host.

    Class auditlog supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param host6: {"not": "host4", "optional": true, "type": "string", "description": "Configure the auditlog host", "format": "ipv6-address"}
    :param host4: {"description": "Configure the auditlog host", "format": "host", "minLength": 1, "optional": true, "maxLength": 31, "not": "host6", "type": "string"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param audit_facility: {"optional": true, "enum": ["local0", "local1", "local2", "local3", "local4", "local5", "local6", "local7"], "type": "string", "description": "'local0': Local use; 'local1': Local use; 'local2': Local use; 'local3': Local use; 'local4': Local use; 'local5': Local use; 'local6': Local use; 'local7': Local use;  (Configure the facility of auditlog)", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/logging/auditlog`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "auditlog"
        self.a10_url="/axapi/v3/logging/auditlog"
        self.DeviceProxy = ""
        self.host6 = ""
        self.host4 = ""
        self.uuid = ""
        self.audit_facility = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


