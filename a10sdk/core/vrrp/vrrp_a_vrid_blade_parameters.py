from a10sdk.common.A10BaseClass import A10BaseClass


class BladeParameters(A10BaseClass):
    
    """Class Description::
    blade parameters of VRRP-A vrid.

    Class blade-parameters supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param priority: {"description": "VRRP-A priorty (Priority, default is 150)", "format": "number", "default": 150, "optional": true, "maximum": 255, "minimum": 1, "type": "number"}
    :param fail_over_policy_template: {"description": "Apply a fail over policy template (VRRP-A fail over policy template name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/vrrp-a/fail-over-policy-template"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/vrrp-a/vrid/{vrid_val}/blade-parameters`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "blade-parameters"
        self.a10_url="/axapi/v3/vrrp-a/vrid/{vrid_val}/blade-parameters"
        self.DeviceProxy = ""
        self.priority = ""
        self.fail_over_policy_template = ""
        self.uuid = ""
        self.tracking_options = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


