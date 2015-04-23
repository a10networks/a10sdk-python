from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param stock_advice_and_tools: {"optional": true, "size": "8", "type": "number", "oid": "16", "format": "counter"}
    :param news_and_media: {"optional": true, "size": "8", "type": "number", "oid": "63", "format": "counter"}
    :param business_and_economy: {"optional": true, "size": "8", "type": "number", "oid": "4", "format": "counter"}
    :param phishing_and_other_fraud: {"optional": true, "size": "8", "type": "number", "oid": "57", "format": "counter"}
    :param nudity: {"optional": true, "size": "8", "type": "number", "oid": "62", "format": "counter"}
    :param CDNs: {"optional": true, "size": "8", "type": "number", "oid": "65", "format": "counter"}
    :param marijuana: {"optional": true, "size": "8", "type": "number", "oid": "32", "format": "counter"}
    :param home_and_garden: {"optional": true, "size": "8", "type": "number", "oid": "12", "format": "counter"}
    :param cult_and_occult: {"optional": true, "size": "8", "type": "number", "oid": "8", "format": "counter"}
    :param society: {"optional": true, "size": "8", "type": "number", "oid": "39", "format": "counter"}
    :param unconfirmed_SPAM_sources: {"optional": true, "size": "8", "type": "number", "oid": "72", "format": "counter"}
    :param personal_storage: {"optional": true, "size": "8", "type": "number", "oid": "47", "format": "counter"}
    :param dynamic_comment: {"optional": true, "size": "8", "type": "number", "oid": "74", "format": "counter"}
    :param web_based_email: {"optional": true, "size": "8", "type": "number", "oid": "55", "format": "counter"}
    :param motor_vehicles: {"optional": true, "size": "8", "type": "number", "oid": "81", "format": "counter"}
    :param shopping: {"optional": true, "size": "8", "type": "number", "oid": "7", "format": "counter"}
    :param swimsuits_and_intimate_apparel: {"optional": true, "size": "8", "type": "number", "oid": "43", "format": "counter"}
    :param dead_sites: {"optional": true, "size": "8", "type": "number", "oid": "15", "format": "counter"}
    :param image_and_video_search: {"optional": true, "size": "8", "type": "number", "oid": "78", "format": "counter"}
    :param other_category: {"optional": true, "size": "8", "type": "number", "oid": "85", "format": "counter"}
    :param web_hosting_sites: {"optional": true, "size": "8", "type": "number", "oid": "82", "format": "counter"}
    :param proxy_avoid_and_anonymizers: {"optional": true, "size": "8", "type": "number", "oid": "58", "format": "counter"}
    :param streaming_media: {"optional": true, "size": "8", "type": "number", "oid": "25", "format": "counter"}
    :param gross: {"optional": true, "size": "8", "type": "number", "oid": "54", "format": "counter"}
    :param uncategorised: {"optional": true, "size": "8", "type": "number", "oid": "84", "format": "counter"}
    :param cheating: {"optional": true, "size": "8", "type": "number", "oid": "53", "format": "counter"}
    :param entertainment_and_arts: {"optional": true, "size": "8", "type": "number", "oid": "21", "format": "counter"}
    :param illegal: {"optional": true, "size": "8", "type": "number", "oid": "64", "format": "counter"}
    :param travel: {"optional": true, "size": "8", "type": "number", "oid": "9", "format": "counter"}
    :param bot_nets: {"optional": true, "size": "8", "type": "number", "oid": "67", "format": "counter"}
    :param music: {"optional": true, "size": "8", "type": "number", "oid": "60", "format": "counter"}
    :param local_information: {"optional": true, "size": "8", "type": "number", "oid": "24", "format": "counter"}
    :param legal: {"optional": true, "size": "8", "type": "number", "oid": "23", "format": "counter"}
    :param sports: {"optional": true, "size": "8", "type": "number", "oid": "42", "format": "counter"}
    :param weapons: {"optional": true, "size": "8", "type": "number", "oid": "36", "format": "counter"}
    :param religion: {"optional": true, "size": "8", "type": "number", "oid": "20", "format": "counter"}
    :param private_IP_addresses: {"optional": true, "size": "8", "type": "number", "oid": "77", "format": "counter"}
    :param shareware_and_freeware: {"optional": true, "size": "8", "type": "number", "oid": "30", "format": "counter"}
    :param hate_and_racism: {"optional": true, "size": "8", "type": "number", "oid": "46", "format": "counter"}
    :param open_HTTP_proxies: {"optional": true, "size": "8", "type": "number", "oid": "73", "format": "counter"}
    :param internet_communications: {"optional": true, "size": "8", "type": "number", "oid": "66", "format": "counter"}
    :param gambling: {"optional": true, "size": "8", "type": "number", "oid": "27", "format": "counter"}
    :param dating: {"optional": true, "size": "8", "type": "number", "oid": "18", "format": "counter"}
    :param spyware_and_adware: {"optional": true, "size": "8", "type": "number", "oid": "59", "format": "counter"}
    :param confirmed_SPAM_sources: {"optional": true, "size": "8", "type": "number", "oid": "70", "format": "counter"}
    :param questionable: {"optional": true, "size": "8", "type": "number", "oid": "44", "format": "counter"}
    :param malware_sites: {"optional": true, "size": "8", "type": "number", "oid": "56", "format": "counter"}
    :param financial_services: {"optional": true, "size": "8", "type": "number", "oid": "3", "format": "counter"}
    :param kids: {"optional": true, "size": "8", "type": "number", "oid": "45", "format": "counter"}
    :param social_network: {"optional": true, "size": "8", "type": "number", "oid": "14", "format": "counter"}
    :param government: {"optional": true, "size": "8", "type": "number", "oid": "61", "format": "counter"}
    :param drugs: {"optional": true, "size": "8", "type": "number", "oid": "10", "format": "counter"}
    :param health_and_medicine: {"optional": true, "size": "8", "type": "number", "oid": "69", "format": "counter"}
    :param abortion: {"optional": true, "size": "8", "type": "number", "oid": "68", "format": "counter"}
    :param personal_sites_and_blogs: {"optional": true, "size": "8", "type": "number", "oid": "22", "format": "counter"}
    :param pay_to_surf: {"optional": true, "size": "8", "type": "number", "oid": "37", "format": "counter"}
    :param alochol_and_tobacco: {"optional": true, "size": "8", "type": "number", "oid": "76", "format": "counter"}
    :param educational_institutions: {"optional": true, "size": "8", "type": "number", "oid": "40", "format": "counter"}
    :param web_adertisements: {"optional": true, "size": "8", "type": "number", "oid": "52", "format": "counter"}
    :param recreation_and_hobbies: {"optional": true, "size": "8", "type": "number", "oid": "80", "format": "counter"}
    :param online_greeting_cards: {"optional": true, "size": "8", "type": "number", "oid": "41", "format": "counter"}
    :param translation: {"optional": true, "size": "8", "type": "number", "oid": "28", "format": "counter"}
    :param SPAM_URLs: {"optional": true, "size": "8", "type": "number", "oid": "71", "format": "counter"}
    :param job_search: {"optional": true, "size": "8", "type": "number", "oid": "26", "format": "counter"}
    :param reference_and_research: {"optional": true, "size": "8", "type": "number", "oid": "29", "format": "counter"}
    :param keyloggers_and_monitoring: {"optional": true, "size": "8", "type": "number", "oid": "49", "format": "counter"}
    :param hunting_and_fishing: {"optional": true, "size": "8", "type": "number", "oid": "38", "format": "counter"}
    :param search_engines: {"optional": true, "size": "8", "type": "number", "oid": "50", "format": "counter"}
    :param peer_to_peer: {"optional": true, "size": "8", "type": "number", "oid": "31", "format": "counter"}
    :param computer_and_internet_security: {"optional": true, "size": "8", "type": "number", "oid": "2", "format": "counter"}
    :param real_estate: {"optional": true, "size": "8", "type": "number", "oid": "1", "format": "counter"}
    :param computer_and_internet_info: {"optional": true, "size": "8", "type": "number", "oid": "5", "format": "counter"}
    :param internet_portals: {"optional": true, "size": "8", "type": "number", "oid": "51", "format": "counter"}
    :param violence: {"optional": true, "size": "8", "type": "number", "oid": "48", "format": "counter"}
    :param philosophy_and_politics: {"optional": true, "size": "8", "type": "number", "oid": "35", "format": "counter"}
    :param training_and_tools: {"optional": true, "size": "8", "type": "number", "oid": "17", "format": "counter"}
    :param sex_education: {"optional": true, "size": "8", "type": "number", "oid": "19", "format": "counter"}
    :param games: {"optional": true, "size": "8", "type": "number", "oid": "34", "format": "counter"}
    :param parked_domains: {"optional": true, "size": "8", "type": "number", "oid": "75", "format": "counter"}
    :param auctions: {"optional": true, "size": "8", "type": "number", "oid": "6", "format": "counter"}
    :param military: {"optional": true, "size": "8", "type": "number", "oid": "13", "format": "counter"}
    :param hacking: {"optional": true, "size": "8", "type": "number", "oid": "33", "format": "counter"}
    :param fashion_and_beauty: {"optional": true, "size": "8", "type": "number", "oid": "79", "format": "counter"}
    :param adult_and_pornography: {"optional": true, "size": "8", "type": "number", "oid": "11", "format": "counter"}
    :param food_and_dining: {"optional": true, "size": "8", "type": "number", "oid": "83", "format": "counter"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.stock_advice_and_tools = ""
        self.news_and_media = ""
        self.business_and_economy = ""
        self.phishing_and_other_fraud = ""
        self.nudity = ""
        self.CDNs = ""
        self.marijuana = ""
        self.home_and_garden = ""
        self.cult_and_occult = ""
        self.society = ""
        self.unconfirmed_SPAM_sources = ""
        self.personal_storage = ""
        self.dynamic_comment = ""
        self.web_based_email = ""
        self.motor_vehicles = ""
        self.shopping = ""
        self.swimsuits_and_intimate_apparel = ""
        self.dead_sites = ""
        self.image_and_video_search = ""
        self.other_category = ""
        self.web_hosting_sites = ""
        self.proxy_avoid_and_anonymizers = ""
        self.streaming_media = ""
        self.gross = ""
        self.uncategorised = ""
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
        self.private_IP_addresses = ""
        self.shareware_and_freeware = ""
        self.hate_and_racism = ""
        self.open_HTTP_proxies = ""
        self.internet_communications = ""
        self.gambling = ""
        self.dating = ""
        self.spyware_and_adware = ""
        self.confirmed_SPAM_sources = ""
        self.questionable = ""
        self.malware_sites = ""
        self.financial_services = ""
        self.kids = ""
        self.social_network = ""
        self.government = ""
        self.drugs = ""
        self.health_and_medicine = ""
        self.abortion = ""
        self.personal_sites_and_blogs = ""
        self.pay_to_surf = ""
        self.alochol_and_tobacco = ""
        self.educational_institutions = ""
        self.web_adertisements = ""
        self.recreation_and_hobbies = ""
        self.online_greeting_cards = ""
        self.translation = ""
        self.SPAM_URLs = ""
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
        self.games = ""
        self.parked_domains = ""
        self.auctions = ""
        self.military = ""
        self.hacking = ""
        self.fashion_and_beauty = ""
        self.adult_and_pornography = ""
        self.food_and_dining = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ClientSsl(A10BaseClass):
    
    """Class Description::
    Statistics for the object client-ssl.

    Class client-ssl supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param name: {"description": "Client SSL Template Name", "format": "string-rlx", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/template/client-ssl/{name}/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "client-ssl"
        self.a10_url="/axapi/v3/slb/template/client-ssl/{name}/stats"
        self.DeviceProxy = ""
        self.stats = {}
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


