from pymongo import MongoClient


def get_database():
    CONNECTION_STRING = "mongodb://admin:mypass@15.222.3.199:27017/?authMechanism=DEFAULT"
    client = MongoClient(CONNECTION_STRING)
    return client['emojibd']


doc = {
    'name': {
        'Ingles': [],
        'Français': [],
        'Dansk': [],
        'Русский': [],
        'Deutsch': [],
        'Chines_simplificado': [],
        'Japones': [],
        'Español': [],
        'Português': [],
    },
    'codes': {
        'Codepoint': '',
        'Shortcode_Discord': '',
        'Shortcode_GitHub': {
            'Ingles': '',
            'Français': '',
            'Dansk': '',
            'Русский': '',
            'Deutsch': '',
            'Chines_simplificado': '',
            'Japones': '',
            'Español': '',
            'Português': '',
        },
        'HTML_Dec': '',
        'HTML_Hex': '',
        'CSS': '',
        'C,C++ e Python': '',
        'Java, JavaScript & JSON': '',
        'Perl': '',
        'PHP & Ruby': '',
        'Punycode': '',
        'URL_Escape_Code': ''

    },
    'categoria': '',
    'sub_categoria': '',
    'palavras_chaves': {
        'Ingles': [],
        'Français': [],
        'Dansk': [],
        'Русский': [],
        'Deutsch': [],
        'Chines_simplificado': [],
        'Japones': [],
        'Español': [],
        'Português': [],
    },
    'link_browse': {
        'instagram': '',
        'YouTube': '',
        'Twitter': '',
        'Yelp': '',
        'Google_Trends': '',
        'instagram': '',
        'Nomad_List': ''
    },
    'version': {
        'Unicode': '',
        'emoji': ''
    },
    'por_fabricante': {
        'Apple': '',
        'Google_Noto_Color_Emoji': '',
        'Samsung': '',
        'Microsoft': '',
        'WhatsApp': '',
        'Twitter': '',
        'Facebook': '',
        'Microsoft_Teams': '',
        'Skype': '',
        'Noto_Color_Emoji_Animated': '',
        'JoyPixels': '',
        'Toss_Face': '',
        'OpenMoji': '',
        'Noto_Emoj_Font': '',
        'Sony_Playstation': '',
        'emojidex': '',
        'Messenger': '',
        'LG': '',
        'HTC': '',
        'Mozilla': ''

    }
}

dbname = get_database()
collection_name = dbname["emojicollection"]
collection_name.insert_one(doc)
