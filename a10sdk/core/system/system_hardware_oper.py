from a10sdk.common.A10BaseClass import A10BaseClass


class SslCards(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param unknown_ssl_cards: {"type": "number", "format": "number"}
    :param hsm: {"type": "number", "format": "number"}
    :param ssl_devices: {"type": "number", "format": "number"}
    :param nitroxpx: {"type": "number", "format": "number"}
    :param nitrox3: {"type": "number", "format": "number"}
    :param nitrox2: {"type": "number", "format": "number"}
    :param nitrox1: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ssl-cards"
        self.DeviceProxy = ""
        self.unknown_ssl_cards = ""
        self.hsm = ""
        self.ssl_devices = ""
        self.nitroxpx = ""
        self.nitrox3 = ""
        self.nitrox2 = ""
        self.nitrox1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class CompressionCards(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param aha363: {"type": "number", "format": "number"}
    :param unknown_compression: {"type": "number", "format": "number"}
    :param gzip_devices: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "compression-cards"
        self.DeviceProxy = ""
        self.aha363 = ""
        self.unknown_compression = ""
        self.gzip_devices = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param bios_version: {"type": "string", "format": "string"}
    :param fpga_summary: {"type": "string", "format": "string"}
    :param cpu_cores: {"type": "number", "format": "number"}
    :param l23_asic: {"type": "string", "format": "string"}
    :param bios_release_date: {"type": "string", "format": "string"}
    :param ipmi: {"type": "string", "format": "string"}
    :param storage: {"type": "string", "format": "string"}
    :param cpu_stepping: {"type": "number", "format": "number"}
    :param fpga_date: {"type": "string", "format": "string"}
    :param memory: {"type": "string", "format": "string"}
    :param platform_description: {"type": "string", "format": "string"}
    :param serial: {"type": "string", "format": "string"}
    :param cpu: {"type": "string", "format": "string"}
    :param ports: {"type": "string", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.bios_version = ""
        self.fpga_summary = ""
        self.cpu_cores = ""
        self.l23_asic = ""
        self.bios_release_date = ""
        self.ipmi = ""
        self.storage = ""
        self.cpu_stepping = ""
        self.fpga_date = ""
        self.memory = ""
        self.platform_description = ""
        self.ssl_cards = {}
        self.serial = ""
        self.compression_cards = {}
        self.cpu = ""
        self.ports = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Hardware(A10BaseClass):
    
    """Class Description::
    Operational Status for the object hardware.

    Class hardware supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/system/hardware/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "hardware"
        self.a10_url="/axapi/v3/system/hardware/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


