from a10sdk.common.A10BaseClass import A10BaseClass


class MultipleFields(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param field: {"description": "Field index number (Index of Field)", "minimum": 1, "type": "number", "maximum": 64, "format": "number"}
    :param csv_type: {"enum": ["ip-from", "ip-to-mask", "continent", "country", "state", "city"], "type": "string", "description": "'ip-from': Beginning address of IP range or subnet; 'ip-to-mask': Ending address of IP range or Mask; 'continent': Continent; 'country': Country; 'state': State or province; 'city': City; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "multiple-fields"
        self.DeviceProxy = ""
        self.field = ""
        self.csv_type = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Csv(A10BaseClass):
    
    """Class Description::
    Specify csv template.

    Class csv supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param delim_char: {"description": "enter a delimiter character, default \",\"", "format": "string-rlx", "default": ",", "minLength": 1, "optional": true, "maxLength": 1, "not": "delim-num", "type": "string"}
    :param multiple_fields: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"field": {"description": "Field index number (Index of Field)", "minimum": 1, "type": "number", "maximum": 64, "format": "number"}, "optional": true, "csv-type": {"enum": ["ip-from", "ip-to-mask", "continent", "country", "state", "city"], "type": "string", "description": "'ip-from': Beginning address of IP range or subnet; 'ip-to-mask': Ending address of IP range or Mask; 'continent': Continent; 'country': Country; 'state': State or province; 'city': City; ", "format": "enum"}}}]}
    :param ipv6_enable: {"default": 0, "optional": true, "type": "number", "description": "Support IPv6 IP ranges", "format": "flag"}
    :param csv_name: {"description": "Specify name of csv template", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param delim_num: {"description": "enter a delimiter number, default 44 (\",\")", "format": "number", "default": 44, "optional": true, "maximum": 255, "minimum": 0, "not": "delim-char", "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/template/csv/{csv_name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "csv_name"]

        self.b_key = "csv"
        self.a10_url="/axapi/v3/gslb/template/csv/{csv_name}"
        self.DeviceProxy = ""
        self.delim_char = ""
        self.multiple_fields = []
        self.ipv6_enable = ""
        self.csv_name = ""
        self.delim_num = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


