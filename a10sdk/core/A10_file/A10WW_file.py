from a10sdk.common.A10BaseClass import A10BaseClass


class BwList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param action: {"enum": ["create", "import", "export", "copy", "rename", "check", "replace", "delete"], "type": "string", "description": "'create': create; 'import': import; 'export': export; 'copy': copy; 'rename': rename; 'check': check; 'replace': replace; 'delete': delete; ", "format": "enum"}
    :param dst_file: {"minLength": 1, "maxLength": 32, "type": "string", "description": "destination file name for copy and rename action", "format": "string"}
    :param file_handle: {"minLength": 1, "maxLength": 255, "type": "string", "description": "full path of the uploaded file", "format": "string-rlx"}
    :param file: {"minLength": 1, "maxLength": 63, "type": "string", "description": "bw-list file name", "format": "string"}
    :param size: {"description": "bw-list file size in byte", "minimum": 0, "type": "number", "maximum": 2147483647, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "bw-list"
        self.DeviceProxy = ""
        self.action = ""
        self.dst_file = ""
        self.file_handle = ""
        self.A10WW_file = ""
        self.size = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class IpMapList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param action: {"enum": ["create", "import", "export", "copy", "rename", "check", "replace", "delete"], "type": "string", "description": "'create': create; 'import': import; 'export': export; 'copy': copy; 'rename': rename; 'check': check; 'replace': replace; 'delete': delete; ", "format": "enum"}
    :param dst_file: {"minLength": 1, "maxLength": 32, "type": "string", "description": "destination file name for copy and rename action", "format": "string"}
    :param file_handle: {"minLength": 1, "maxLength": 255, "type": "string", "description": "full path of the uploaded file", "format": "string-rlx"}
    :param file: {"minLength": 1, "maxLength": 63, "type": "string", "description": "ip map list file name", "format": "string"}
    :param size: {"description": "ip map list file size in byte", "minimum": 0, "type": "number", "maximum": 2147483647, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ip-map-list"
        self.DeviceProxy = ""
        self.action = ""
        self.dst_file = ""
        self.file_handle = ""
        self.A10WW_file = ""
        self.size = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ClassList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param action: {"enum": ["create", "import", "export", "copy", "rename", "check", "replace", "delete"], "type": "string", "description": "'create': create; 'import': import; 'export': export; 'copy': copy; 'rename': rename; 'check': check; 'replace': replace; 'delete': delete; ", "format": "enum"}
    :param dst_file: {"minLength": 1, "maxLength": 32, "type": "string", "description": "destination file name for copy and rename action", "format": "string"}
    :param file_handle: {"minLength": 1, "maxLength": 255, "type": "string", "description": "full path of the uploaded file", "format": "string-rlx"}
    :param file: {"minLength": 1, "maxLength": 63, "type": "string", "description": "class list local file name", "format": "string"}
    :param size: {"description": "class list file size in byte", "minimum": 0, "type": "number", "maximum": 2147483647, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "class-list"
        self.DeviceProxy = ""
        self.action = ""
        self.dst_file = ""
        self.file_handle = ""
        self.A10WW_file = ""
        self.size = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class File(A10BaseClass):
    
    """    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Local file Mangement.

    Class file supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/file`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "file"
        self.a10_url="/axapi/v3/file"
        self.DeviceProxy = ""
        self.ssl_cert_key = {}
        self.bw_list = {}
        self.ip_map_list = {}
        self.syslog = {}
        self.health_external = {}
        self.auth_portal = {}
        self.aflex = {}
        self.health_postfile = {}
        self.web_category_license = {}
        self.log_backup = {}
        self.ssl_crl = {}
        self.debug_monitor = {}
        self.system_backup = {}
        self.policy = {}
        self.auth_portal_image = {}
        self.class_list = {}
        self.dnssec_ds = {}
        self.local_uri_file = {}
        self.wsdl = {}
        self.ssl_key = {}
        self.A10WW_license = {}
        self.ca_cert = {}
        self.axdebug = {}
        self.xml_schema = {}
        self.startup_config = {}
        self.auth_saml_idp = {}
        self.ssl_cert = {}
        self.dnssec_dnskey = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


