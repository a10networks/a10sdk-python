from a10sdk.common.A10BaseClass import A10BaseClass


class DnssecDs(A10BaseClass):
    
    """Class Description::
    DNSSEC DS file for child zone.

    Class dnssec-ds supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param dnssec_ds: {"description": "DNSSEC DS file for child zone", "format": "string", "minLength": 1, "optional": false, "maxLength": 127, "type": "string"}
    :param remote_file: {"optional": true, "type": "string", "description": "profile name for remote url", "format": "url"}
    :param use_mgmt_port: {"default": 0, "optional": true, "type": "number", "description": "Use management port as source port", "format": "flag"}
    :param period: {"description": "Specify the period in second", "format": "number", "type": "number", "maximum": 31536000, "minimum": 60, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/import-periodic/dnssec-ds/{dnssec_ds}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "dnssec_ds"]

        self.b_key = "dnssec-ds"
        self.a10_url="/axapi/v3/import-periodic/dnssec-ds/{dnssec_ds}"
        self.DeviceProxy = ""
        self.uuid = ""
        self.dnssec_ds = ""
        self.remote_file = ""
        self.use_mgmt_port = ""
        self.period = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


