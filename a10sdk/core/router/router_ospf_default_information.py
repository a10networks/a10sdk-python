from a10sdk.common.A10BaseClass import A10BaseClass


class DefaultInformation(A10BaseClass):
    
    """Class Description::
    Control distribution of default information.

    Class default-information supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param route_map: {"description": "Route map reference (Pointer to route-map entries)", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param always: {"default": 0, "optional": true, "type": "number", "description": "Always advertise default route", "format": "flag"}
    :param metric: {"description": "OSPF default metric (OSPF metric)", "format": "number", "type": "number", "maximum": 16777214, "minimum": 0, "optional": true}
    :param originate: {"default": 0, "optional": true, "type": "number", "description": "Distribute a default route", "format": "flag"}
    :param metric_type: {"description": "OSPF metric type for default routes", "format": "number", "default": 2, "optional": true, "maximum": 2, "minimum": 1, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/router/ospf/{process_id}/default-information`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "default-information"
        self.a10_url="/axapi/v3/router/ospf/{process_id}/default-information"
        self.DeviceProxy = ""
        self.route_map = ""
        self.uuid = ""
        self.always = ""
        self.metric = ""
        self.originate = ""
        self.metric_type = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


