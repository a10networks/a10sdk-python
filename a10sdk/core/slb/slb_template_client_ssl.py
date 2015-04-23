from a10sdk.common.A10BaseClass import A10BaseClass


class ClientAuthEqualsList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param client_auth_equals: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Forward proxy bypass if SNI string equals another string", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "client-auth-equals-list"
        self.DeviceProxy = ""
        self.client_auth_equals = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "real-estate", "computer-and-internet-security", "financial-services", "business-and-economy", "computer-and-internet-info", "auctions", "shopping", "cult-and-occult", "travel", "drugs", "adult-and-pornography", "home-and-garden", "military", "social-network", "dead-sites", "stock-advice-and-tools", "training-and-tools", "dating", "sex-education", "religion", "entertainment-and-arts", "personal-sites-and-blogs", "legal", "local-information", "streaming-media", "job-search", "gambling", "translation", "reference-and-research", "shareware-and-freeware", "peer-to-peer", "marijuana", "hacking", "games", "philosophy-and-politics", "weapons", "pay-to-surf", "hunting-and-fishing", "society", "educational-institutions", "online-greeting-cards", "sports", "swimsuits-and-intimate-apparel", "questionable", "kids", "hate-and-racism", "personal-storage", "violence", "keyloggers-and-monitoring", "search-engines", "internet-portals", "web-adertisements", "cheating", "gross", "web-based-email", "malware-sites", "phishing-and-other-fraud", "proxy-avoid-and-anonymizers", "spyware-and-adware", "music", "government", "nudity", "news-and-media", "illegal", "CDNs", "internet-communications", "bot-nets", "abortion", "health-and-medicine", "confirmed-SPAM-sources", "SPAM-URLs", "unconfirmed-SPAM-sources", "open-HTTP-proxies", "dynamic-comment", "parked-domains", "alochol-and-tobacco", "private-IP-addresses", "image-and-video-search", "fashion-and-beauty", "recreation-and-hobbies", "motor-vehicles", "web-hosting-sites", "food-and-dining", "uncategorised", "other-category"], "type": "string", "description": "'all': all; 'real-estate': real-estate; 'computer-and-internet-security': computer-and-internet-security; 'financial-services': financial-services; 'business-and-economy': business-and-economy; 'computer-and-internet-info': computer-and-internet-info; 'auctions': auctions; 'shopping': shopping; 'cult-and-occult': cult-and-occult; 'travel': travel; 'drugs': drugs; 'adult-and-pornography': adult-and-pornography; 'home-and-garden': home-and-garden; 'military': military; 'social-network': social-network; 'dead-sites': dead-sites; 'stock-advice-and-tools': stock-advice-and-tools; 'training-and-tools': training-and-tools; 'dating': dating; 'sex-education': sex-education; 'religion': religion; 'entertainment-and-arts': entertainment-and-arts; 'personal-sites-and-blogs': personal-sites-and-blogs; 'legal': legal; 'local-information': local-information; 'streaming-media': streaming-media; 'job-search': job-search; 'gambling': gambling; 'translation': translation; 'reference-and-research': reference-and-research; 'shareware-and-freeware': shareware-and-freeware; 'peer-to-peer': peer-to-peer; 'marijuana': marijuana; 'hacking': hacking; 'games': games; 'philosophy-and-politics': philosophy-and-politics; 'weapons': weapons; 'pay-to-surf': pay-to-surf; 'hunting-and-fishing': hunting-and-fishing; 'society': society; 'educational-institutions': educational-institutions; 'online-greeting-cards': online-greeting-cards; 'sports': sports; 'swimsuits-and-intimate-apparel': swimsuits-and-intimate-apparel; 'questionable': questionable; 'kids': kids; 'hate-and-racism': hate-and-racism; 'personal-storage': personal-storage; 'violence': violence; 'keyloggers-and-monitoring': keyloggers-and-monitoring; 'search-engines': search-engines; 'internet-portals': internet-portals; 'web-adertisements': web-adertisements; 'cheating': cheating; 'gross': gross; 'web-based-email': web-based-email; 'malware-sites': malware-sites; 'phishing-and-other-fraud': phishing-and-other-fraud; 'proxy-avoid-and-anonymizers': proxy-avoid-and-anonymizers; 'spyware-and-adware': spyware-and-adware; 'music': music; 'government': government; 'nudity': nudity; 'news-and-media': news-and-media; 'illegal': illegal; 'CDNs': CDNs; 'internet-communications': internet-communications; 'bot-nets': bot-nets; 'abortion': abortion; 'health-and-medicine': health-and-medicine; 'confirmed-SPAM-sources': confirmed-SPAM-sources; 'SPAM-URLs': SPAM-URLs; 'unconfirmed-SPAM-sources': unconfirmed-SPAM-sources; 'open-HTTP-proxies': open-HTTP-proxies; 'dynamic-comment': dynamic-comment; 'parked-domains': parked-domains; 'alochol-and-tobacco': alochol-and-tobacco; 'private-IP-addresses': private-IP-addresses; 'image-and-video-search': image-and-video-search; 'fashion-and-beauty': fashion-and-beauty; 'recreation-and-hobbies': recreation-and-hobbies; 'motor-vehicles': motor-vehicles; 'web-hosting-sites': web-hosting-sites; 'food-and-dining': food-and-dining; 'uncategorised': uncategorised; 'other-category': other-category; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class EcList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ec: {"enum": ["secp256r1", "secp384r1"], "type": "string", "description": "'secp256r1': X9_62_prime256v1; 'secp384r1': secp384r1; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ec-list"
        self.DeviceProxy = ""
        self.ec = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class EqualsList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param equals: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Forward proxy bypass if SNI string equals another string", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "equals-list"
        self.DeviceProxy = ""
        self.equals = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ClientAuthStartsWithList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param client_auth_starts_with: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Forward proxy bypass if SNI string starts with another string", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "client-auth-starts-with-list"
        self.DeviceProxy = ""
        self.client_auth_starts_with = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ContainsList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param contains: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Forward proxy bypass if SNI string contains another string", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "contains-list"
        self.DeviceProxy = ""
        self.contains = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class EndsWithList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ends_with: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Forward proxy bypass if SNI string ends with another string", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ends-with-list"
        self.DeviceProxy = ""
        self.ends_with = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ServerNameList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param server_name: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Server name indication in Client hello extension (Server name String)", "format": "string"}
    :param server_key: {"minLength": 1, "maxLength": 255, "type": "string", "description": "Server Private Key associated to SNI (Server Private Key Name)", "format": "string"}
    :param server_passphrase: {"minLength": 1, "maxLength": 63, "type": "string", "description": "help Password Phrase", "format": "password"}
    :param server_encrypted: {"type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)", "format": "encrypted"}
    :param server_cert: {"minLength": 1, "maxLength": 255, "type": "string", "description": "Server Certificate associated to SNI (Server Certificate Name)", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "server-name-list"
        self.DeviceProxy = ""
        self.server_name = ""
        self.server_key = ""
        self.server_passphrase = ""
        self.server_encrypted = ""
        self.server_cert = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class CaCerts(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ca_cert: {"minLength": 1, "maxLength": 255, "type": "string", "description": "CA Certificate (CA Certificate Name)", "format": "string"}
    :param client_ocsp: {"default": 0, "type": "number", "description": "Specify ocsp authentication server(s) for client certificate verification", "format": "flag"}
    :param client_ocsp_sg: {"description": "Specify service-group (Service group name)", "format": "string-rlx", "minLength": 1, "maxLength": 127, "type": "string", "$ref": "/axapi/v3/aam/authentication/service-group"}
    :param client_ocsp_srvr: {"description": "Specify authentication server", "format": "string-rlx", "minLength": 1, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/aam/authentication/server/ocsp"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ca-certs"
        self.DeviceProxy = ""
        self.ca_cert = ""
        self.client_ocsp = ""
        self.client_ocsp_sg = ""
        self.client_ocsp_srvr = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ClientAuthContainsList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param client_auth_contains: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Forward proxy bypass if SNI string contains another string", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "client-auth-contains-list"
        self.DeviceProxy = ""
        self.client_auth_contains = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class WebCategory(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param stock_advice_and_tools: {"default": 0, "type": "number", "description": "Category Stock Advice and Tools", "format": "flag"}
    :param news_and_media: {"default": 0, "type": "number", "description": "Category News and Media", "format": "flag"}
    :param business_and_economy: {"default": 0, "type": "number", "description": "Category Business and Economy", "format": "flag"}
    :param phishing_and_other_fraud: {"default": 0, "type": "number", "description": "Category Phishing and Other Frauds", "format": "flag"}
    :param nudity: {"default": 0, "type": "number", "description": "Category Nudity", "format": "flag"}
    :param health_and_medicine: {"default": 0, "type": "number", "description": "Category Health and Medicine", "format": "flag"}
    :param marijuana: {"default": 0, "type": "number", "description": "Category Marijuana", "format": "flag"}
    :param home_and_garden: {"default": 0, "type": "number", "description": "Category Home and Garden", "format": "flag"}
    :param cult_and_occult: {"default": 0, "type": "number", "description": "Category Cult and Occult", "format": "flag"}
    :param society: {"default": 0, "type": "number", "description": "Category Society", "format": "flag"}
    :param fashion_and_beauty: {"default": 0, "type": "number", "description": "Category Fashion and Beauty", "format": "flag"}
    :param personal_storage: {"default": 0, "type": "number", "description": "Category Personal Storage", "format": "flag"}
    :param dynamic_comment: {"default": 0, "type": "number", "description": "Category Dynamic Comment", "format": "flag"}
    :param web_based_email: {"default": 0, "type": "number", "description": "Category Web based email", "format": "flag"}
    :param motor_vehicles: {"default": 0, "type": "number", "description": "Category Motor Vehicles", "format": "flag"}
    :param cdns: {"default": 0, "type": "number", "description": "Category CDNs", "format": "flag"}
    :param shopping: {"default": 0, "type": "number", "description": "Category Shopping", "format": "flag"}
    :param swimsuits_and_intimate_apparel: {"default": 0, "type": "number", "description": "Category Swimsuits and Intimate Apparel", "format": "flag"}
    :param dead_sites: {"default": 0, "type": "number", "description": "Category Dead Sites (db Ops only)", "format": "flag"}
    :param image_and_video_search: {"default": 0, "type": "number", "description": "Category Image and Video Search", "format": "flag"}
    :param proxy_avoid_and_anonymizers: {"default": 0, "type": "number", "description": "Category Proxy Avoid and Anonymizers", "format": "flag"}
    :param streaming_media: {"default": 0, "type": "number", "description": "Category Streaming Media", "format": "flag"}
    :param gross: {"default": 0, "type": "number", "description": "Category Gross", "format": "flag"}
    :param cheating: {"default": 0, "type": "number", "description": "Category Cheating", "format": "flag"}
    :param entertainment_and_arts: {"default": 0, "type": "number", "description": "Category Entertainment and Arts", "format": "flag"}
    :param illegal: {"default": 0, "type": "number", "description": "Category Illegal", "format": "flag"}
    :param travel: {"default": 0, "type": "number", "description": "Category Travel", "format": "flag"}
    :param bot_nets: {"default": 0, "type": "number", "description": "Category Bot Nets", "format": "flag"}
    :param music: {"default": 0, "type": "number", "description": "Category Music", "format": "flag"}
    :param local_information: {"default": 0, "type": "number", "description": "Category Local Information", "format": "flag"}
    :param legal: {"default": 0, "type": "number", "description": "Category Legal", "format": "flag"}
    :param sports: {"default": 0, "type": "number", "description": "Category Sports", "format": "flag"}
    :param weapons: {"default": 0, "type": "number", "description": "Category Weapons", "format": "flag"}
    :param religion: {"default": 0, "type": "number", "description": "Category Religion", "format": "flag"}
    :param private_ip_addresses: {"default": 0, "type": "number", "description": "Category Private IP Addresses", "format": "flag"}
    :param shareware_and_freeware: {"default": 0, "type": "number", "description": "Category Shareware and Freeware", "format": "flag"}
    :param hate_and_racism: {"default": 0, "type": "number", "description": "Category Hate and Racism", "format": "flag"}
    :param open_http_proxies: {"default": 0, "type": "number", "description": "Category Open HTTP Proxies", "format": "flag"}
    :param internet_communications: {"default": 0, "type": "number", "description": "Category Internet Communications", "format": "flag"}
    :param gambling: {"default": 0, "type": "number", "description": "Category Gambling", "format": "flag"}
    :param dating: {"default": 0, "type": "number", "description": "Category Dating", "format": "flag"}
    :param spyware_and_adware: {"default": 0, "type": "number", "description": "Category Spyware and Adware", "format": "flag"}
    :param uncategorized: {"default": 0, "type": "number", "description": "Uncategorized URLs", "format": "flag"}
    :param questionable: {"default": 0, "type": "number", "description": "Category Questionable", "format": "flag"}
    :param alochol_and_tobacco: {"default": 0, "type": "number", "description": "Category Alcohol and Tobacco", "format": "flag"}
    :param malware_sites: {"default": 0, "type": "number", "description": "Category Malware Sites", "format": "flag"}
    :param financial_services: {"default": 0, "type": "number", "description": "Category Financial Services", "format": "flag"}
    :param kids: {"default": 0, "type": "number", "description": "Category Kids", "format": "flag"}
    :param social_network: {"default": 0, "type": "number", "description": "Category Social Network", "format": "flag"}
    :param government: {"default": 0, "type": "number", "description": "Category Government", "format": "flag"}
    :param drugs: {"default": 0, "type": "number", "description": "Category Abused Drugs", "format": "flag"}
    :param web_hosting_sites: {"default": 0, "type": "number", "description": "Category Web Hosting Sites", "format": "flag"}
    :param abortion: {"default": 0, "type": "number", "description": "Category Abortion", "format": "flag"}
    :param personal_sites_and_blogs: {"default": 0, "type": "number", "description": "Category Personal sites and Blogs", "format": "flag"}
    :param pay_to_surf: {"default": 0, "type": "number", "description": "Category Pay to Surf", "format": "flag"}
    :param spam_urls: {"default": 0, "type": "number", "description": "Category SPAM URLs", "format": "flag"}
    :param confirmed_spam_sources: {"default": 0, "type": "number", "description": "Category Confirmed SPAM Sources", "format": "flag"}
    :param educational_institutions: {"default": 0, "type": "number", "description": "Category Educational Institutions", "format": "flag"}
    :param web_adertisements: {"default": 0, "type": "number", "description": "Category Web Advertisements", "format": "flag"}
    :param recreation_and_hobbies: {"default": 0, "type": "number", "description": "Category Recreation and Hobbies", "format": "flag"}
    :param online_greeting_cards: {"default": 0, "type": "number", "description": "Category Online Greeting cards", "format": "flag"}
    :param translation: {"default": 0, "type": "number", "description": "Category Translation", "format": "flag"}
    :param job_search: {"default": 0, "type": "number", "description": "Category Job Search", "format": "flag"}
    :param reference_and_research: {"default": 0, "type": "number", "description": "Category Reference and Research", "format": "flag"}
    :param keyloggers_and_monitoring: {"default": 0, "type": "number", "description": "Category Keyloggers and Monitoring", "format": "flag"}
    :param hunting_and_fishing: {"default": 0, "type": "number", "description": "Category Hunting and Fishing", "format": "flag"}
    :param search_engines: {"default": 0, "type": "number", "description": "Category Search Engines", "format": "flag"}
    :param peer_to_peer: {"default": 0, "type": "number", "description": "Category Peer to Peer", "format": "flag"}
    :param computer_and_internet_security: {"default": 0, "type": "number", "description": "Category Computer and Internet Security", "format": "flag"}
    :param real_estate: {"default": 0, "type": "number", "description": "Category Real Estate", "format": "flag"}
    :param computer_and_internet_info: {"default": 0, "type": "number", "description": "Category Computer and Internet Info", "format": "flag"}
    :param internet_portals: {"default": 0, "type": "number", "description": "Category Internet Portals", "format": "flag"}
    :param violence: {"default": 0, "type": "number", "description": "Category Violence", "format": "flag"}
    :param philosophy_and_politics: {"default": 0, "type": "number", "description": "Category Philosophy and Political Advocacy", "format": "flag"}
    :param training_and_tools: {"default": 0, "type": "number", "description": "Category Training and Tools", "format": "flag"}
    :param sex_education: {"default": 0, "type": "number", "description": "Category Sex Education", "format": "flag"}
    :param unconfirmed_spam_sources: {"default": 0, "type": "number", "description": "Category Unconfirmed SPAM Sources", "format": "flag"}
    :param games: {"default": 0, "type": "number", "description": "Category Games", "format": "flag"}
    :param parked_domains: {"default": 0, "type": "number", "description": "Category Parked Domains", "format": "flag"}
    :param auctions: {"default": 0, "type": "number", "description": "Category Auctions", "format": "flag"}
    :param military: {"default": 0, "type": "number", "description": "Category Military", "format": "flag"}
    :param hacking: {"default": 0, "type": "number", "description": "Category Hacking", "format": "flag"}
    :param adult_and_pornography: {"default": 0, "type": "number", "description": "Category Adult and Pornography", "format": "flag"}
    :param food_and_dining: {"default": 0, "type": "number", "description": "Category Food and Dining", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "web-category"
        self.DeviceProxy = ""
        self.stock_advice_and_tools = ""
        self.news_and_media = ""
        self.business_and_economy = ""
        self.phishing_and_other_fraud = ""
        self.nudity = ""
        self.health_and_medicine = ""
        self.marijuana = ""
        self.home_and_garden = ""
        self.cult_and_occult = ""
        self.society = ""
        self.fashion_and_beauty = ""
        self.personal_storage = ""
        self.dynamic_comment = ""
        self.web_based_email = ""
        self.motor_vehicles = ""
        self.cdns = ""
        self.shopping = ""
        self.swimsuits_and_intimate_apparel = ""
        self.dead_sites = ""
        self.image_and_video_search = ""
        self.proxy_avoid_and_anonymizers = ""
        self.streaming_media = ""
        self.gross = ""
        self.cheating = ""
        self.entertainment_and_arts = ""
        self.illegal = ""
        self.travel = ""
        self.bot_nets = ""
        self.music = ""
        self.local_information = ""
        self.legal = ""
        self.sports = ""
        self.weapons = ""
        self.religion = ""
        self.private_ip_addresses = ""
        self.shareware_and_freeware = ""
        self.hate_and_racism = ""
        self.open_http_proxies = ""
        self.internet_communications = ""
        self.gambling = ""
        self.dating = ""
        self.spyware_and_adware = ""
        self.uncategorized = ""
        self.questionable = ""
        self.alochol_and_tobacco = ""
        self.malware_sites = ""
        self.financial_services = ""
        self.kids = ""
        self.social_network = ""
        self.government = ""
        self.drugs = ""
        self.web_hosting_sites = ""
        self.abortion = ""
        self.personal_sites_and_blogs = ""
        self.pay_to_surf = ""
        self.spam_urls = ""
        self.confirmed_spam_sources = ""
        self.educational_institutions = ""
        self.web_adertisements = ""
        self.recreation_and_hobbies = ""
        self.online_greeting_cards = ""
        self.translation = ""
        self.job_search = ""
        self.reference_and_research = ""
        self.keyloggers_and_monitoring = ""
        self.hunting_and_fishing = ""
        self.search_engines = ""
        self.peer_to_peer = ""
        self.computer_and_internet_security = ""
        self.real_estate = ""
        self.computer_and_internet_info = ""
        self.internet_portals = ""
        self.violence = ""
        self.philosophy_and_politics = ""
        self.training_and_tools = ""
        self.sex_education = ""
        self.unconfirmed_spam_sources = ""
        self.games = ""
        self.parked_domains = ""
        self.auctions = ""
        self.military = ""
        self.hacking = ""
        self.adult_and_pornography = ""
        self.food_and_dining = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class CipherWithoutPrioList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param cipher_wo_prio: {"not": "template-cipher", "enum": ["SSL3_RSA_DES_192_CBC3_SHA", "SSL3_RSA_DES_40_CBC_SHA", "SSL3_RSA_DES_64_CBC_SHA", "SSL3_RSA_RC4_128_MD5", "SSL3_RSA_RC4_128_SHA", "SSL3_RSA_RC4_40_MD5", "TLS1_RSA_AES_128_SHA", "TLS1_RSA_AES_256_SHA", "TLS1_RSA_EXPORT1024_RC4_56_MD5", "TLS1_RSA_EXPORT1024_RC4_56_SHA", "TLS1_RSA_AES_128_SHA256", "TLS1_RSA_AES_256_SHA256", "TLS1_DHE_RSA_AES_128_GCM_SHA256", "TLS1_DHE_RSA_AES_128_SHA", "TLS1_DHE_RSA_AES_128_SHA256", "TLS1_DHE_RSA_AES_256_GCM_SHA384", "TLS1_DHE_RSA_AES_256_SHA", "TLS1_DHE_RSA_AES_256_SHA256", "TLS1_ECDHE_ECDSA_AES_128_GCM_SHA256", "TLS1_ECDHE_ECDSA_AES_128_SHA", "TLS1_ECDHE_ECDSA_AES_128_SHA256", "TLS1_ECDHE_ECDSA_AES_256_GCM_SHA384", "TLS1_ECDHE_ECDSA_AES_256_SHA", "TLS1_ECDHE_RSA_AES_128_GCM_SHA256", "TLS1_ECDHE_RSA_AES_128_SHA", "TLS1_ECDHE_RSA_AES_128_SHA256", "TLS1_ECDHE_RSA_AES_256_GCM_SHA384", "TLS1_ECDHE_RSA_AES_256_SHA", "TLS1_RSA_AES_128_GCM_SHA256", "TLS1_RSA_AES_256_GCM_SHA384"], "type": "string", "description": "'SSL3_RSA_DES_192_CBC3_SHA': SSL3_RSA_DES_192_CBC3_SHA; 'SSL3_RSA_DES_40_CBC_SHA': SSL3_RSA_DES_40_CBC_SHA; 'SSL3_RSA_DES_64_CBC_SHA': SSL3_RSA_DES_64_CBC_SHA; 'SSL3_RSA_RC4_128_MD5': SSL3_RSA_RC4_128_MD5; 'SSL3_RSA_RC4_128_SHA': SSL3_RSA_RC4_128_SHA; 'SSL3_RSA_RC4_40_MD5': SSL3_RSA_RC4_40_MD5; 'TLS1_RSA_AES_128_SHA': TLS1_RSA_AES_128_SHA; 'TLS1_RSA_AES_256_SHA': TLS1_RSA_AES_256_SHA; 'TLS1_RSA_EXPORT1024_RC4_56_MD5': TLS1_RSA_EXPORT1024_RC4_56_MD5; 'TLS1_RSA_EXPORT1024_RC4_56_SHA': TLS1_RSA_EXPORT1024_RC4_56_SHA; 'TLS1_RSA_AES_128_SHA256': TLS1_RSA_AES_128_SHA256; 'TLS1_RSA_AES_256_SHA256': TLS1_RSA_AES_256_SHA256; 'TLS1_DHE_RSA_AES_128_GCM_SHA256': TLS1_DHE_RSA_AES_128_GCM_SHA256; 'TLS1_DHE_RSA_AES_128_SHA': TLS1_DHE_RSA_AES_128_SHA; 'TLS1_DHE_RSA_AES_128_SHA256': TLS1_DHE_RSA_AES_128_SHA256; 'TLS1_DHE_RSA_AES_256_GCM_SHA384': TLS1_DHE_RSA_AES_256_GCM_SHA384; 'TLS1_DHE_RSA_AES_256_SHA': TLS1_DHE_RSA_AES_256_SHA; 'TLS1_DHE_RSA_AES_256_SHA256': TLS1_DHE_RSA_AES_256_SHA256; 'TLS1_ECDHE_ECDSA_AES_128_GCM_SHA256': TLS1_ECDHE_ECDSA_AES_128_GCM_SHA256; 'TLS1_ECDHE_ECDSA_AES_128_SHA': TLS1_ECDHE_ECDSA_AES_128_SHA; 'TLS1_ECDHE_ECDSA_AES_128_SHA256': TLS1_ECDHE_ECDSA_AES_128_SHA256; 'TLS1_ECDHE_ECDSA_AES_256_GCM_SHA384': TLS1_ECDHE_ECDSA_AES_256_GCM_SHA384; 'TLS1_ECDHE_ECDSA_AES_256_SHA': TLS1_ECDHE_ECDSA_AES_256_SHA; 'TLS1_ECDHE_RSA_AES_128_GCM_SHA256': TLS1_ECDHE_RSA_AES_128_GCM_SHA256; 'TLS1_ECDHE_RSA_AES_128_SHA': TLS1_ECDHE_RSA_AES_128_SHA; 'TLS1_ECDHE_RSA_AES_128_SHA256': TLS1_ECDHE_RSA_AES_128_SHA256; 'TLS1_ECDHE_RSA_AES_256_GCM_SHA384': TLS1_ECDHE_RSA_AES_256_GCM_SHA384; 'TLS1_ECDHE_RSA_AES_256_SHA': TLS1_ECDHE_RSA_AES_256_SHA; 'TLS1_RSA_AES_128_GCM_SHA256': TLS1_RSA_AES_128_GCM_SHA256; 'TLS1_RSA_AES_256_GCM_SHA384': TLS1_RSA_AES_256_GCM_SHA384; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "cipher-without-prio-list"
        self.DeviceProxy = ""
        self.cipher_wo_prio = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ClientAuthEndsWithList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param client_auth_ends_with: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Forward proxy bypass if SNI string ends with another string", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "client-auth-ends-with-list"
        self.DeviceProxy = ""
        self.client_auth_ends_with = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class StartsWithList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param starts_with: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Forward proxy bypass if SNI string starts with another string", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "starts-with-list"
        self.DeviceProxy = ""
        self.starts_with = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ClientSsl(A10BaseClass):
    
    """Class Description::
    Client SSL Template.

    Class client-ssl supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param chain_cert: {"description": "Chain Certificate (Chain Certificate Name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param session_cache_timeout: {"description": "Session Cache Timeout (Timeout value, in seconds)", "format": "number", "type": "number", "maximum": 604800, "minimum": 0, "optional": true}
    :param ocspst_sg: {"description": "Specify authentication service group", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "not": "ocspst-srvr", "type": "string", "$ref": "/axapi/v3/aam/authentication/service-group"}
    :param auth_username: {"description": "Specify the Username Field in the Client Certificate(If multi-fields are specificed, prior one has higher priority)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param authorization: {"default": 0, "optional": true, "type": "number", "description": "Specify LDAP server for client SSL authorizaiton", "format": "flag"}
    :param client_auth_equals_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"client-auth-equals": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Forward proxy bypass if SNI string equals another string", "format": "string-rlx"}, "optional": true}}]}
    :param session_ticket_lifetime: {"description": "Session ticket lieftime in seconds from stateless session resumption (Lifetime value in seconds)", "format": "number", "type": "number", "maximum": 2147483647, "minimum": 0, "optional": true}
    :param ocspst_sg_hours: {"description": "Specify update period, in hours", "format": "number", "default": 1, "optional": true, "not-list": ["ocspst-sg-days", "ocspst-sg-minutes"], "maximum": 23, "minimum": 1, "type": "number"}
    :param ocspst_sg_days: {"description": "Specify update period, in days", "format": "number", "optional": true, "not-list": ["ocspst-sg-hours", "ocspst-sg-minutes"], "maximum": 31, "minimum": 1, "type": "number"}
    :param ldap_search_filter: {"description": "Specify LDAP search filter", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param authen_name: {"description": "Specify authorization LDAP server name", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "not": "auth-sg", "type": "string", "$ref": "/axapi/v3/aam/authentication/server/ldap"}
    :param client_auth_case_insensitive: {"default": 0, "optional": true, "type": "number", "description": "Case insensitive forward proxy client auth bypass", "format": "flag"}
    :param ocsp_stapling: {"default": 0, "optional": true, "type": "number", "description": "Config OCSP stapling support", "format": "flag"}
    :param forward_encrypted: {"optional": true, "type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)", "format": "encrypted"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param ocspst_srvr: {"description": "Specify OCSP authentication server", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "not": "ocspst-sg", "type": "string", "$ref": "/axapi/v3/aam/authentication/server/ocsp"}
    :param class_list_name: {"description": "Class List Name", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param forward_proxy_ca_cert: {"description": "CA Certificate for forward proxy (SSL forward proxy CA Certificate Name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param ocspst_sg_timeout: {"description": "Specify retry timeout (Default is 30 mins)", "format": "number", "default": 30, "optional": true, "maximum": 44640, "minimum": 1, "type": "number"}
    :param ssl_false_start_disable: {"default": 0, "optional": true, "type": "number", "description": "disable SSL False Start", "format": "flag"}
    :param key_passphrase: {"description": "Password Phrase", "format": "password", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param template_cipher: {"description": "Cipher Template (Cipher Config Name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "not": "cipher-wo-prio", "type": "string", "$ref": "/axapi/v3/slb/template/cipher"}
    :param ocspst_srvr_minutes: {"description": "Specify update period, in minutes", "format": "number", "optional": true, "not-list": ["ocspst-srvr-days", "ocspst-srvr-hours"], "maximum": 59, "minimum": 1, "type": "number"}
    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "real-estate", "computer-and-internet-security", "financial-services", "business-and-economy", "computer-and-internet-info", "auctions", "shopping", "cult-and-occult", "travel", "drugs", "adult-and-pornography", "home-and-garden", "military", "social-network", "dead-sites", "stock-advice-and-tools", "training-and-tools", "dating", "sex-education", "religion", "entertainment-and-arts", "personal-sites-and-blogs", "legal", "local-information", "streaming-media", "job-search", "gambling", "translation", "reference-and-research", "shareware-and-freeware", "peer-to-peer", "marijuana", "hacking", "games", "philosophy-and-politics", "weapons", "pay-to-surf", "hunting-and-fishing", "society", "educational-institutions", "online-greeting-cards", "sports", "swimsuits-and-intimate-apparel", "questionable", "kids", "hate-and-racism", "personal-storage", "violence", "keyloggers-and-monitoring", "search-engines", "internet-portals", "web-adertisements", "cheating", "gross", "web-based-email", "malware-sites", "phishing-and-other-fraud", "proxy-avoid-and-anonymizers", "spyware-and-adware", "music", "government", "nudity", "news-and-media", "illegal", "CDNs", "internet-communications", "bot-nets", "abortion", "health-and-medicine", "confirmed-SPAM-sources", "SPAM-URLs", "unconfirmed-SPAM-sources", "open-HTTP-proxies", "dynamic-comment", "parked-domains", "alochol-and-tobacco", "private-IP-addresses", "image-and-video-search", "fashion-and-beauty", "recreation-and-hobbies", "motor-vehicles", "web-hosting-sites", "food-and-dining", "uncategorised", "other-category"], "type": "string", "description": "'all': all; 'real-estate': real-estate; 'computer-and-internet-security': computer-and-internet-security; 'financial-services': financial-services; 'business-and-economy': business-and-economy; 'computer-and-internet-info': computer-and-internet-info; 'auctions': auctions; 'shopping': shopping; 'cult-and-occult': cult-and-occult; 'travel': travel; 'drugs': drugs; 'adult-and-pornography': adult-and-pornography; 'home-and-garden': home-and-garden; 'military': military; 'social-network': social-network; 'dead-sites': dead-sites; 'stock-advice-and-tools': stock-advice-and-tools; 'training-and-tools': training-and-tools; 'dating': dating; 'sex-education': sex-education; 'religion': religion; 'entertainment-and-arts': entertainment-and-arts; 'personal-sites-and-blogs': personal-sites-and-blogs; 'legal': legal; 'local-information': local-information; 'streaming-media': streaming-media; 'job-search': job-search; 'gambling': gambling; 'translation': translation; 'reference-and-research': reference-and-research; 'shareware-and-freeware': shareware-and-freeware; 'peer-to-peer': peer-to-peer; 'marijuana': marijuana; 'hacking': hacking; 'games': games; 'philosophy-and-politics': philosophy-and-politics; 'weapons': weapons; 'pay-to-surf': pay-to-surf; 'hunting-and-fishing': hunting-and-fishing; 'society': society; 'educational-institutions': educational-institutions; 'online-greeting-cards': online-greeting-cards; 'sports': sports; 'swimsuits-and-intimate-apparel': swimsuits-and-intimate-apparel; 'questionable': questionable; 'kids': kids; 'hate-and-racism': hate-and-racism; 'personal-storage': personal-storage; 'violence': violence; 'keyloggers-and-monitoring': keyloggers-and-monitoring; 'search-engines': search-engines; 'internet-portals': internet-portals; 'web-adertisements': web-adertisements; 'cheating': cheating; 'gross': gross; 'web-based-email': web-based-email; 'malware-sites': malware-sites; 'phishing-and-other-fraud': phishing-and-other-fraud; 'proxy-avoid-and-anonymizers': proxy-avoid-and-anonymizers; 'spyware-and-adware': spyware-and-adware; 'music': music; 'government': government; 'nudity': nudity; 'news-and-media': news-and-media; 'illegal': illegal; 'CDNs': CDNs; 'internet-communications': internet-communications; 'bot-nets': bot-nets; 'abortion': abortion; 'health-and-medicine': health-and-medicine; 'confirmed-SPAM-sources': confirmed-SPAM-sources; 'SPAM-URLs': SPAM-URLs; 'unconfirmed-SPAM-sources': unconfirmed-SPAM-sources; 'open-HTTP-proxies': open-HTTP-proxies; 'dynamic-comment': dynamic-comment; 'parked-domains': parked-domains; 'alochol-and-tobacco': alochol-and-tobacco; 'private-IP-addresses': private-IP-addresses; 'image-and-video-search': image-and-video-search; 'fashion-and-beauty': fashion-and-beauty; 'recreation-and-hobbies': recreation-and-hobbies; 'motor-vehicles': motor-vehicles; 'web-hosting-sites': web-hosting-sites; 'food-and-dining': food-and-dining; 'uncategorised': uncategorised; 'other-category': other-category; ", "format": "enum"}}}]}
    :param auth_sg: {"description": "Specify authorization LDAP service group", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "not": "authen-name", "type": "string", "$ref": "/axapi/v3/aam/authentication/service-group"}
    :param ec_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "ec": {"enum": ["secp256r1", "secp384r1"], "type": "string", "description": "'secp256r1': X9_62_prime256v1; 'secp384r1': secp384r1; ", "format": "enum"}}}]}
    :param key_encrypted: {"optional": true, "type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)", "format": "encrypted"}
    :param equals_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "equals": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Forward proxy bypass if SNI string equals another string", "format": "string-rlx"}}}]}
    :param client_auth_starts_with_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"client-auth-starts-with": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Forward proxy bypass if SNI string starts with another string", "format": "string-rlx"}, "optional": true}}]}
    :param template_hsm: {"description": "HSM Template (HSM Template Name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param forward_passphrase: {"description": "Password Phrase", "format": "password", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param ldap_base_dn_from_cert: {"default": 0, "optional": true, "type": "number", "description": "Use Subject DN as LDAP search base DN", "format": "flag"}
    :param contains_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"contains": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Forward proxy bypass if SNI string contains another string", "format": "string-rlx"}, "optional": true}}]}
    :param forward_proxy_ca_key: {"description": "CA Private Key for forward proxy (SSL forward proxy CA Key Name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param ocspst_srvr_days: {"description": "Specify update period, in days", "format": "number", "optional": true, "not-list": ["ocspst-srvr-hours", "ocspst-srvr-minutes"], "maximum": 31, "minimum": 1, "type": "number"}
    :param client_auth_class_list: {"description": "Forward proxy client auth bypass if SNI string matches class-list (Class List Name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param session_cache_size: {"description": "Session Cache Size (Specify 0 to disable Session ID reuse.)", "format": "number", "type": "number", "maximum": 8000000, "minimum": 0, "optional": true}
    :param client_certificate: {"description": "'Ignore': Don't request client certificate; 'Require': Require client certificate; 'Request': Request client certificate; ", "format": "enum", "default": "Ignore", "type": "string", "enum": ["Ignore", "Require", "Request"], "optional": true}
    :param ends_with_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ends-with": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Forward proxy bypass if SNI string ends with another string", "format": "string-rlx"}, "optional": true}}]}
    :param ocspst_ca_cert: {"description": "CA certificate", "format": "string", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param ocspst_ocsp: {"default": 0, "optional": true, "type": "number", "description": "Specify OCSP Authentication", "format": "flag"}
    :param forward_proxy_enable: {"default": 0, "optional": true, "type": "number", "description": "Enable SSL forward proxy", "format": "flag"}
    :param key: {"description": "Server Private Key (Key Name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param sslv2_bypass_service_group: {"description": "Service Group for Bypass SSLV2 (Service Group Name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "type": "string", "$ref": "/axapi/v3/slb/service-group"}
    :param server_name_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"server-name": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Server name indication in Client hello extension (Server name String)", "format": "string"}, "server-key": {"minLength": 1, "maxLength": 255, "type": "string", "description": "Server Private Key associated to SNI (Server Private Key Name)", "format": "string"}, "server-passphrase": {"minLength": 1, "maxLength": 63, "type": "string", "description": "help Password Phrase", "format": "password"}, "optional": true, "server-encrypted": {"type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)", "format": "encrypted"}, "server-cert": {"minLength": 1, "maxLength": 255, "type": "string", "description": "Server Certificate associated to SNI (Server Certificate Name)", "format": "string"}}}]}
    :param auth_sg_filter: {"description": "Specify LDAP search filter", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param ca_certs: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ca-cert": {"minLength": 1, "maxLength": 255, "type": "string", "description": "CA Certificate (CA Certificate Name)", "format": "string"}, "client-ocsp": {"default": 0, "type": "number", "description": "Specify ocsp authentication server(s) for client certificate verification", "format": "flag"}, "client-ocsp-sg": {"description": "Specify service-group (Service group name)", "format": "string-rlx", "minLength": 1, "maxLength": 127, "type": "string", "$ref": "/axapi/v3/aam/authentication/service-group"}, "optional": true, "client-ocsp-srvr": {"description": "Specify authentication server", "format": "string-rlx", "minLength": 1, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/aam/authentication/server/ocsp"}}}]}
    :param disable_sslv3: {"default": 0, "optional": true, "type": "number", "description": "Reject Client requests for SSL version 3", "format": "flag"}
    :param ocspst_srvr_timeout: {"description": "Specify retry timeout (Default is 30 mins)", "format": "number", "default": 30, "optional": true, "maximum": 44640, "minimum": 1, "type": "number"}
    :param client_auth_contains_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"client-auth-contains": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Forward proxy bypass if SNI string contains another string", "format": "string-rlx"}, "optional": true}}]}
    :param name: {"description": "Client SSL Template Name", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param auth_sg_dn: {"default": 0, "optional": true, "type": "number", "description": "Use Subject DN as LDAP search base DN", "format": "flag"}
    :param hsm_type: {"optional": true, "enum": ["thales-embed", "thales-hwcrhk"], "type": "string", "description": "'thales-embed': Thales embed key; 'thales-hwcrhk': Thales hwcrhk Key; ", "format": "enum"}
    :param ocspst_srvr_hours: {"description": "Specify update period, in hours", "format": "number", "default": 1, "optional": true, "not-list": ["ocspst-srvr-days", "ocspst-srvr-minutes"], "maximum": 23, "minimum": 1, "type": "number"}
    :param dh_type: {"optional": true, "enum": ["1024", "1024-dsa", "2048", "512"], "type": "string", "description": "'1024': 1024; '1024-dsa': 1024-dsa; '2048': 2048; '512': 512; ", "format": "enum"}
    :param auth_username_attribute: {"description": "Specify attribute name of username for client SSL authorization", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param cert: {"description": "Server Certificate (Certificate Name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param crl: {"description": "Certificate Revocation Lists (Certificate Revocation Lists file name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param case_insensitive: {"default": 0, "optional": true, "type": "number", "description": "Case insensitive forward proxy bypass", "format": "flag"}
    :param cipher_without_prio_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"cipher-wo-prio": {"not": "template-cipher", "enum": ["SSL3_RSA_DES_192_CBC3_SHA", "SSL3_RSA_DES_40_CBC_SHA", "SSL3_RSA_DES_64_CBC_SHA", "SSL3_RSA_RC4_128_MD5", "SSL3_RSA_RC4_128_SHA", "SSL3_RSA_RC4_40_MD5", "TLS1_RSA_AES_128_SHA", "TLS1_RSA_AES_256_SHA", "TLS1_RSA_EXPORT1024_RC4_56_MD5", "TLS1_RSA_EXPORT1024_RC4_56_SHA", "TLS1_RSA_AES_128_SHA256", "TLS1_RSA_AES_256_SHA256", "TLS1_DHE_RSA_AES_128_GCM_SHA256", "TLS1_DHE_RSA_AES_128_SHA", "TLS1_DHE_RSA_AES_128_SHA256", "TLS1_DHE_RSA_AES_256_GCM_SHA384", "TLS1_DHE_RSA_AES_256_SHA", "TLS1_DHE_RSA_AES_256_SHA256", "TLS1_ECDHE_ECDSA_AES_128_GCM_SHA256", "TLS1_ECDHE_ECDSA_AES_128_SHA", "TLS1_ECDHE_ECDSA_AES_128_SHA256", "TLS1_ECDHE_ECDSA_AES_256_GCM_SHA384", "TLS1_ECDHE_ECDSA_AES_256_SHA", "TLS1_ECDHE_RSA_AES_128_GCM_SHA256", "TLS1_ECDHE_RSA_AES_128_SHA", "TLS1_ECDHE_RSA_AES_128_SHA256", "TLS1_ECDHE_RSA_AES_256_GCM_SHA384", "TLS1_ECDHE_RSA_AES_256_SHA", "TLS1_RSA_AES_128_GCM_SHA256", "TLS1_RSA_AES_256_GCM_SHA384"], "type": "string", "description": "'SSL3_RSA_DES_192_CBC3_SHA': SSL3_RSA_DES_192_CBC3_SHA; 'SSL3_RSA_DES_40_CBC_SHA': SSL3_RSA_DES_40_CBC_SHA; 'SSL3_RSA_DES_64_CBC_SHA': SSL3_RSA_DES_64_CBC_SHA; 'SSL3_RSA_RC4_128_MD5': SSL3_RSA_RC4_128_MD5; 'SSL3_RSA_RC4_128_SHA': SSL3_RSA_RC4_128_SHA; 'SSL3_RSA_RC4_40_MD5': SSL3_RSA_RC4_40_MD5; 'TLS1_RSA_AES_128_SHA': TLS1_RSA_AES_128_SHA; 'TLS1_RSA_AES_256_SHA': TLS1_RSA_AES_256_SHA; 'TLS1_RSA_EXPORT1024_RC4_56_MD5': TLS1_RSA_EXPORT1024_RC4_56_MD5; 'TLS1_RSA_EXPORT1024_RC4_56_SHA': TLS1_RSA_EXPORT1024_RC4_56_SHA; 'TLS1_RSA_AES_128_SHA256': TLS1_RSA_AES_128_SHA256; 'TLS1_RSA_AES_256_SHA256': TLS1_RSA_AES_256_SHA256; 'TLS1_DHE_RSA_AES_128_GCM_SHA256': TLS1_DHE_RSA_AES_128_GCM_SHA256; 'TLS1_DHE_RSA_AES_128_SHA': TLS1_DHE_RSA_AES_128_SHA; 'TLS1_DHE_RSA_AES_128_SHA256': TLS1_DHE_RSA_AES_128_SHA256; 'TLS1_DHE_RSA_AES_256_GCM_SHA384': TLS1_DHE_RSA_AES_256_GCM_SHA384; 'TLS1_DHE_RSA_AES_256_SHA': TLS1_DHE_RSA_AES_256_SHA; 'TLS1_DHE_RSA_AES_256_SHA256': TLS1_DHE_RSA_AES_256_SHA256; 'TLS1_ECDHE_ECDSA_AES_128_GCM_SHA256': TLS1_ECDHE_ECDSA_AES_128_GCM_SHA256; 'TLS1_ECDHE_ECDSA_AES_128_SHA': TLS1_ECDHE_ECDSA_AES_128_SHA; 'TLS1_ECDHE_ECDSA_AES_128_SHA256': TLS1_ECDHE_ECDSA_AES_128_SHA256; 'TLS1_ECDHE_ECDSA_AES_256_GCM_SHA384': TLS1_ECDHE_ECDSA_AES_256_GCM_SHA384; 'TLS1_ECDHE_ECDSA_AES_256_SHA': TLS1_ECDHE_ECDSA_AES_256_SHA; 'TLS1_ECDHE_RSA_AES_128_GCM_SHA256': TLS1_ECDHE_RSA_AES_128_GCM_SHA256; 'TLS1_ECDHE_RSA_AES_128_SHA': TLS1_ECDHE_RSA_AES_128_SHA; 'TLS1_ECDHE_RSA_AES_128_SHA256': TLS1_ECDHE_RSA_AES_128_SHA256; 'TLS1_ECDHE_RSA_AES_256_GCM_SHA384': TLS1_ECDHE_RSA_AES_256_GCM_SHA384; 'TLS1_ECDHE_RSA_AES_256_SHA': TLS1_ECDHE_RSA_AES_256_SHA; 'TLS1_RSA_AES_128_GCM_SHA256': TLS1_RSA_AES_128_GCM_SHA256; 'TLS1_RSA_AES_256_GCM_SHA384': TLS1_RSA_AES_256_GCM_SHA384; ", "format": "enum"}, "optional": true}}]}
    :param client_auth_ends_with_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"client-auth-ends-with": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Forward proxy bypass if SNI string ends with another string", "format": "string-rlx"}, "optional": true}}]}
    :param ocspst_sg_minutes: {"description": "Specify update period, in minutes", "format": "number", "optional": true, "not-list": ["ocspst-sg-days", "ocspst-sg-hours"], "maximum": 59, "minimum": 1, "type": "number"}
    :param starts_with_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"starts-with": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Forward proxy bypass if SNI string starts with another string", "format": "string-rlx"}, "optional": true}}]}
    :param close_notify: {"default": 0, "optional": true, "type": "number", "description": "Send close notification when terminate connection", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/template/client-ssl/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "client-ssl"
        self.a10_url="/axapi/v3/slb/template/client-ssl/{name}"
        self.DeviceProxy = ""
        self.chain_cert = ""
        self.session_cache_timeout = ""
        self.ocspst_sg = ""
        self.auth_username = ""
        self.authorization = ""
        self.client_auth_equals_list = []
        self.session_ticket_lifetime = ""
        self.ocspst_sg_hours = ""
        self.ocspst_sg_days = ""
        self.ldap_search_filter = ""
        self.authen_name = ""
        self.client_auth_case_insensitive = ""
        self.ocsp_stapling = ""
        self.forward_encrypted = ""
        self.uuid = ""
        self.ocspst_srvr = ""
        self.class_list_name = ""
        self.forward_proxy_ca_cert = ""
        self.ocspst_sg_timeout = ""
        self.ssl_false_start_disable = ""
        self.key_passphrase = ""
        self.template_cipher = ""
        self.ocspst_srvr_minutes = ""
        self.sampling_enable = []
        self.auth_sg = ""
        self.ec_list = []
        self.key_encrypted = ""
        self.equals_list = []
        self.client_auth_starts_with_list = []
        self.template_hsm = ""
        self.forward_passphrase = ""
        self.ldap_base_dn_from_cert = ""
        self.contains_list = []
        self.forward_proxy_ca_key = ""
        self.ocspst_srvr_days = ""
        self.client_auth_class_list = ""
        self.session_cache_size = ""
        self.client_certificate = ""
        self.ends_with_list = []
        self.ocspst_ca_cert = ""
        self.ocspst_ocsp = ""
        self.forward_proxy_enable = ""
        self.key = ""
        self.sslv2_bypass_service_group = ""
        self.server_name_list = []
        self.auth_sg_filter = ""
        self.ca_certs = []
        self.disable_sslv3 = ""
        self.ocspst_srvr_timeout = ""
        self.client_auth_contains_list = []
        self.name = ""
        self.auth_sg_dn = ""
        self.hsm_type = ""
        self.ocspst_srvr_hours = ""
        self.dh_type = ""
        self.auth_username_attribute = ""
        self.cert = ""
        self.web_category = {}
        self.crl = ""
        self.case_insensitive = ""
        self.cipher_without_prio_list = []
        self.client_auth_ends_with_list = []
        self.ocspst_sg_minutes = ""
        self.starts_with_list = []
        self.close_notify = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


