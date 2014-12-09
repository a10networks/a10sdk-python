from a10sdk.common.A10BaseClass import A10BaseClass


class System(A10BaseClass):
    
    """Class Description::
    Enable system group traps.

    Class system supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param all: {"default": 0, "optional": true, "type": "number", "description": "Enable all system group traps", "format": "flag"}
    :param data_cpu_high: {"default": 0, "optional": true, "type": "number", "description": "Enable data CPU usage high trap", "format": "flag"}
    :param power: {"default": 0, "optional": true, "type": "number", "description": "Enable system power supply trap", "format": "flag"}
    :param start: {"default": 0, "optional": true, "type": "number", "description": "Enable system start trap", "format": "flag"}
    :param high_memory_use: {"default": 0, "optional": true, "type": "number", "description": "Enable system high memory usage trap", "format": "flag"}
    :param pri_disk: {"default": 0, "optional": true, "type": "number", "description": "Enable system primary hard disk trap", "format": "flag"}
    :param file_sys_read_only: {"default": 0, "optional": true, "type": "number", "description": "Enable file system read-only trap", "format": "flag"}
    :param high_temp: {"default": 0, "optional": true, "type": "number", "description": "Enable system high temperature trap", "format": "flag"}
    :param sec_disk: {"default": 0, "optional": true, "type": "number", "description": "Enable system secondary hard disk trap", "format": "flag"}
    :param high_disk_use: {"default": 0, "optional": true, "type": "number", "description": "Enable system high disk usage trap", "format": "flag"}
    :param fan: {"default": 0, "optional": true, "type": "number", "description": "Enable system fan trap", "format": "flag"}
    :param shutdown: {"default": 0, "optional": true, "type": "number", "description": "Enable system shutdown trap", "format": "flag"}
    :param control_cpu_high: {"default": 0, "optional": true, "type": "number", "description": "Enable control CPU usage high trap", "format": "flag"}
    :param license_management: {"default": 0, "optional": true, "type": "number", "description": "Enable license management traps", "format": "flag"}
    :param packet_drop: {"default": 0, "optional": true, "type": "number", "description": "Enable system packet dropped trap", "format": "flag"}
    :param restart: {"default": 0, "optional": true, "type": "number", "description": "Enable system restart trap", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/snmp-server/enable/traps/system`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "system"
        self.a10_url="/axapi/v3/snmp-server/enable/traps/system"
        self.DeviceProxy = ""
        self.A10WW_all = ""
        self.data_cpu_high = ""
        self.power = ""
        self.start = ""
        self.high_memory_use = ""
        self.pri_disk = ""
        self.file_sys_read_only = ""
        self.high_temp = ""
        self.sec_disk = ""
        self.high_disk_use = ""
        self.fan = ""
        self.shutdown = ""
        self.control_cpu_high = ""
        self.license_management = ""
        self.packet_drop = ""
        self.restart = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


