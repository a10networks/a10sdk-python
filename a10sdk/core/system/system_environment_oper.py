from a10sdk.common.A10BaseClass import A10BaseClass


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param fan3a_report: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param power_unit1: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param power_unit3: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param power_unit2: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param fan8a_report: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param voltage_label_17: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param voltage_label_16: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param voltage_label_15: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param voltage_label_14: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param voltage_label_13: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param voltage_label_12: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param voltage_label_11: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param voltage_label_10: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param fan6b_report: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param voltage_label_3: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param physical_temperature: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param fan5a_report: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param fan8b_report: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param fan2a_report: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param fan5b_report: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param fan10b_report: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param fan7b_report: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param voltage_label_4: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param fan9b_report: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param power_unit4: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param fan1b_report: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param voltage_label_9: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param fan10a_report: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param fan2b_report: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param fan4b_report: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param fan9a_report: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param voltage_label_2: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param voltage_label_1: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param voltage_label_7: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param voltage_label_6: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param voltage_label_5: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param fan6a_report: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param fan1a_report: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param fan4a_report: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param fan7a_report: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param voltage_label_8: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param fan3b_report: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.fan3a_report = ""
        self.power_unit1 = ""
        self.power_unit3 = ""
        self.power_unit2 = ""
        self.fan8a_report = ""
        self.voltage_label_17 = ""
        self.voltage_label_16 = ""
        self.voltage_label_15 = ""
        self.voltage_label_14 = ""
        self.voltage_label_13 = ""
        self.voltage_label_12 = ""
        self.voltage_label_11 = ""
        self.voltage_label_10 = ""
        self.fan6b_report = ""
        self.voltage_label_3 = ""
        self.physical_temperature = ""
        self.fan5a_report = ""
        self.fan8b_report = ""
        self.fan2a_report = ""
        self.fan5b_report = ""
        self.fan10b_report = ""
        self.fan7b_report = ""
        self.voltage_label_4 = ""
        self.fan9b_report = ""
        self.power_unit4 = ""
        self.fan1b_report = ""
        self.voltage_label_9 = ""
        self.fan10a_report = ""
        self.fan2b_report = ""
        self.fan4b_report = ""
        self.fan9a_report = ""
        self.voltage_label_2 = ""
        self.voltage_label_1 = ""
        self.voltage_label_7 = ""
        self.voltage_label_6 = ""
        self.voltage_label_5 = ""
        self.fan6a_report = ""
        self.fan1a_report = ""
        self.fan4a_report = ""
        self.fan7a_report = ""
        self.voltage_label_8 = ""
        self.fan3b_report = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Environment(A10BaseClass):
    
    """Class Description::
    Operational Status for the object environment.

    Class environment supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/system/environment/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "environment"
        self.a10_url="/axapi/v3/system/environment/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


