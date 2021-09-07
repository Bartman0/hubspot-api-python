# coding: utf-8

"""
    CMS Site Search

    Use these endpoints for searching content on your HubSpot hosted CMS website(s).  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.cms.site_search.configuration import Configuration


class ContentSearchResult(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        "id": "int",
        "score": "float",
        "type": "str",
        "domain": "str",
        "url": "str",
        "featured_image_url": "str",
        "language": "str",
        "title": "str",
        "description": "str",
        "category": "str",
        "subcategory": "str",
        "author_full_name": "str",
        "tags": "list[str]",
        "table_id": "int",
        "row_id": "int",
        "published_date": "int",
        "combined_id": "str",
    }

    attribute_map = {
        "id": "id",
        "score": "score",
        "type": "type",
        "domain": "domain",
        "url": "url",
        "featured_image_url": "featuredImageUrl",
        "language": "language",
        "title": "title",
        "description": "description",
        "category": "category",
        "subcategory": "subcategory",
        "author_full_name": "authorFullName",
        "tags": "tags",
        "table_id": "tableId",
        "row_id": "rowId",
        "published_date": "publishedDate",
        "combined_id": "combinedId",
    }

    def __init__(
        self,
        id=None,
        score=None,
        type=None,
        domain=None,
        url=None,
        featured_image_url=None,
        language=None,
        title=None,
        description=None,
        category=None,
        subcategory=None,
        author_full_name=None,
        tags=None,
        table_id=None,
        row_id=None,
        published_date=None,
        combined_id=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """ContentSearchResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._score = None
        self._type = None
        self._domain = None
        self._url = None
        self._featured_image_url = None
        self._language = None
        self._title = None
        self._description = None
        self._category = None
        self._subcategory = None
        self._author_full_name = None
        self._tags = None
        self._table_id = None
        self._row_id = None
        self._published_date = None
        self._combined_id = None
        self.discriminator = None

        self.id = id
        self.score = score
        self.type = type
        self.domain = domain
        self.url = url
        if featured_image_url is not None:
            self.featured_image_url = featured_image_url
        if language is not None:
            self.language = language
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if category is not None:
            self.category = category
        if subcategory is not None:
            self.subcategory = subcategory
        if author_full_name is not None:
            self.author_full_name = author_full_name
        if tags is not None:
            self.tags = tags
        if table_id is not None:
            self.table_id = table_id
        if row_id is not None:
            self.row_id = row_id
        if published_date is not None:
            self.published_date = published_date
        if combined_id is not None:
            self.combined_id = combined_id

    @property
    def id(self):
        """Gets the id of this ContentSearchResult.  # noqa: E501

        The ID of the content.  # noqa: E501

        :return: The id of this ContentSearchResult.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ContentSearchResult.

        The ID of the content.  # noqa: E501

        :param id: The id of this ContentSearchResult.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def score(self):
        """Gets the score of this ContentSearchResult.  # noqa: E501

        The matching score of the document.  # noqa: E501

        :return: The score of this ContentSearchResult.  # noqa: E501
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this ContentSearchResult.

        The matching score of the document.  # noqa: E501

        :param score: The score of this ContentSearchResult.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and score is None:  # noqa: E501
            raise ValueError("Invalid value for `score`, must not be `None`")  # noqa: E501

        self._score = score

    @property
    def type(self):
        """Gets the type of this ContentSearchResult.  # noqa: E501

        The type of document. Can be `SITE_PAGE`, `LANDING_PAGE`, `BLOG_POST`, `LISTING_PAGE`, or `KNOWLEDGE_ARTICLE`.  # noqa: E501

        :return: The type of this ContentSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ContentSearchResult.

        The type of document. Can be `SITE_PAGE`, `LANDING_PAGE`, `BLOG_POST`, `LISTING_PAGE`, or `KNOWLEDGE_ARTICLE`.  # noqa: E501

        :param type: The type of this ContentSearchResult.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["LANDING_PAGE", "BLOG_POST", "SITE_PAGE", "KNOWLEDGE_ARTICLE", "LISTING_PAGE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `type` ({0}), must be one of {1}".format(type, allowed_values))  # noqa: E501

        self._type = type

    @property
    def domain(self):
        """Gets the domain of this ContentSearchResult.  # noqa: E501

        The domain the document is hosted on.  # noqa: E501

        :return: The domain of this ContentSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this ContentSearchResult.

        The domain the document is hosted on.  # noqa: E501

        :param domain: The domain of this ContentSearchResult.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and domain is None:  # noqa: E501
            raise ValueError("Invalid value for `domain`, must not be `None`")  # noqa: E501

        self._domain = domain

    @property
    def url(self):
        """Gets the url of this ContentSearchResult.  # noqa: E501

        The url of the document.  # noqa: E501

        :return: The url of this ContentSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ContentSearchResult.

        The url of the document.  # noqa: E501

        :param url: The url of this ContentSearchResult.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and url is None:  # noqa: E501
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def featured_image_url(self):
        """Gets the featured_image_url of this ContentSearchResult.  # noqa: E501

        URL of the featured image.  # noqa: E501

        :return: The featured_image_url of this ContentSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._featured_image_url

    @featured_image_url.setter
    def featured_image_url(self, featured_image_url):
        """Sets the featured_image_url of this ContentSearchResult.

        URL of the featured image.  # noqa: E501

        :param featured_image_url: The featured_image_url of this ContentSearchResult.  # noqa: E501
        :type: str
        """

        self._featured_image_url = featured_image_url

    @property
    def language(self):
        """Gets the language of this ContentSearchResult.  # noqa: E501

        The document's language.  # noqa: E501

        :return: The language of this ContentSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this ContentSearchResult.

        The document's language.  # noqa: E501

        :param language: The language of this ContentSearchResult.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "af",
            "af-na",
            "af-za",
            "agq",
            "agq-cm",
            "ak",
            "ak-gh",
            "am",
            "am-et",
            "ar",
            "ar-001",
            "ar-ae",
            "ar-bh",
            "ar-dj",
            "ar-dz",
            "ar-eg",
            "ar-eh",
            "ar-er",
            "ar-il",
            "ar-iq",
            "ar-jo",
            "ar-km",
            "ar-kw",
            "ar-lb",
            "ar-ly",
            "ar-ma",
            "ar-mr",
            "ar-om",
            "ar-ps",
            "ar-qa",
            "ar-sa",
            "ar-sd",
            "ar-so",
            "ar-ss",
            "ar-sy",
            "ar-td",
            "ar-tn",
            "ar-ye",
            "as",
            "as-in",
            "asa",
            "asa-tz",
            "ast",
            "ast-es",
            "az",
            "az-az",
            "bas",
            "bas-cm",
            "be",
            "be-by",
            "bem",
            "bem-zm",
            "bez",
            "bez-tz",
            "bg",
            "bg-bg",
            "bm",
            "bm-ml",
            "bn",
            "bn-bd",
            "bn-in",
            "bo",
            "bo-cn",
            "bo-in",
            "br",
            "br-fr",
            "brx",
            "brx-in",
            "bs",
            "bs-ba",
            "ca",
            "ca-ad",
            "ca-es",
            "ca-fr",
            "ca-it",
            "ccp",
            "ccp-bd",
            "ccp-in",
            "ce",
            "ce-ru",
            "cgg",
            "cgg-ug",
            "chr",
            "chr-us",
            "ckb",
            "ckb-iq",
            "ckb-ir",
            "cs",
            "cs-cz",
            "cu",
            "cu-ru",
            "cy",
            "cy-gb",
            "da",
            "da-dk",
            "da-gl",
            "dav",
            "dav-ke",
            "de",
            "de-at",
            "de-be",
            "de-ch",
            "de-de",
            "de-gr",
            "de-it",
            "de-li",
            "de-lu",
            "dje",
            "dje-ne",
            "dsb",
            "dsb-de",
            "dua",
            "dua-cm",
            "dyo",
            "dyo-sn",
            "dz",
            "dz-bt",
            "ebu",
            "ebu-ke",
            "ee",
            "ee-gh",
            "ee-tg",
            "el",
            "el-cy",
            "el-gr",
            "en",
            "en-001",
            "en-150",
            "en-ag",
            "en-ai",
            "en-as",
            "en-at",
            "en-au",
            "en-bb",
            "en-be",
            "en-bi",
            "en-bm",
            "en-bs",
            "en-bw",
            "en-bz",
            "en-ca",
            "en-cc",
            "en-ch",
            "en-ck",
            "en-cm",
            "en-cx",
            "en-cy",
            "en-de",
            "en-dg",
            "en-dk",
            "en-dm",
            "en-er",
            "en-fi",
            "en-fj",
            "en-fk",
            "en-fm",
            "en-gb",
            "en-gd",
            "en-gg",
            "en-gh",
            "en-gi",
            "en-gm",
            "en-gu",
            "en-gy",
            "en-hk",
            "en-ie",
            "en-il",
            "en-im",
            "en-in",
            "en-io",
            "en-je",
            "en-jm",
            "en-ke",
            "en-ki",
            "en-kn",
            "en-ky",
            "en-lc",
            "en-lr",
            "en-ls",
            "en-mg",
            "en-mh",
            "en-mo",
            "en-mp",
            "en-ms",
            "en-mt",
            "en-mu",
            "en-mw",
            "en-my",
            "en-na",
            "en-nf",
            "en-ng",
            "en-nl",
            "en-nr",
            "en-nu",
            "en-nz",
            "en-pg",
            "en-ph",
            "en-pk",
            "en-pn",
            "en-pr",
            "en-pw",
            "en-rw",
            "en-sb",
            "en-sc",
            "en-sd",
            "en-se",
            "en-sg",
            "en-sh",
            "en-si",
            "en-sl",
            "en-ss",
            "en-sx",
            "en-sz",
            "en-tc",
            "en-tk",
            "en-to",
            "en-tt",
            "en-tv",
            "en-tz",
            "en-ug",
            "en-um",
            "en-us",
            "en-vc",
            "en-vg",
            "en-vi",
            "en-vu",
            "en-ws",
            "en-za",
            "en-zm",
            "en-zw",
            "eo",
            "eo-001",
            "es",
            "es-419",
            "es-ar",
            "es-bo",
            "es-br",
            "es-bz",
            "es-cl",
            "es-co",
            "es-cr",
            "es-cu",
            "es-do",
            "es-ea",
            "es-ec",
            "es-es",
            "es-gq",
            "es-gt",
            "es-hn",
            "es-ic",
            "es-mx",
            "es-ni",
            "es-pa",
            "es-pe",
            "es-ph",
            "es-pr",
            "es-py",
            "es-sv",
            "es-us",
            "es-uy",
            "es-ve",
            "et",
            "et-ee",
            "eu",
            "eu-es",
            "ewo",
            "ewo-cm",
            "fa",
            "fa-af",
            "fa-ir",
            "ff",
            "ff-cm",
            "ff-gn",
            "ff-mr",
            "ff-sn",
            "fi",
            "fi-fi",
            "fil",
            "fil-ph",
            "fo",
            "fo-dk",
            "fo-fo",
            "fr",
            "fr-be",
            "fr-bf",
            "fr-bi",
            "fr-bj",
            "fr-bl",
            "fr-ca",
            "fr-cd",
            "fr-cf",
            "fr-cg",
            "fr-ch",
            "fr-ci",
            "fr-cm",
            "fr-dj",
            "fr-dz",
            "fr-fr",
            "fr-ga",
            "fr-gf",
            "fr-gn",
            "fr-gp",
            "fr-gq",
            "fr-ht",
            "fr-km",
            "fr-lu",
            "fr-ma",
            "fr-mc",
            "fr-mf",
            "fr-mg",
            "fr-ml",
            "fr-mq",
            "fr-mr",
            "fr-mu",
            "fr-nc",
            "fr-ne",
            "fr-pf",
            "fr-pm",
            "fr-re",
            "fr-rw",
            "fr-sc",
            "fr-sn",
            "fr-sy",
            "fr-td",
            "fr-tg",
            "fr-tn",
            "fr-vu",
            "fr-wf",
            "fr-yt",
            "fur",
            "fur-it",
            "fy",
            "fy-nl",
            "ga",
            "ga-ie",
            "gd",
            "gd-gb",
            "gl",
            "gl-es",
            "gsw",
            "gsw-ch",
            "gsw-fr",
            "gsw-li",
            "gu",
            "gu-in",
            "guz",
            "guz-ke",
            "gv",
            "gv-im",
            "ha",
            "ha-gh",
            "ha-ne",
            "ha-ng",
            "haw",
            "haw-us",
            "he",
            "hi",
            "hi-in",
            "hr",
            "hr-ba",
            "hr-hr",
            "hsb",
            "hsb-de",
            "hu",
            "hu-hu",
            "hy",
            "hy-am",
            "id",
            "ig",
            "ig-ng",
            "ii",
            "ii-cn",
            "id-id",
            "is",
            "is-is",
            "it",
            "it-ch",
            "it-it",
            "it-sm",
            "it-va",
            "he-il",
            "ja",
            "ja-jp",
            "jgo",
            "jgo-cm",
            "yi",
            "yi-001",
            "jmc",
            "jmc-tz",
            "ka",
            "ka-ge",
            "kab",
            "kab-dz",
            "kam",
            "kam-ke",
            "kde",
            "kde-tz",
            "kea",
            "kea-cv",
            "khq",
            "khq-ml",
            "ki",
            "ki-ke",
            "kk",
            "kk-kz",
            "kkj",
            "kkj-cm",
            "kl",
            "kl-gl",
            "kln",
            "kln-ke",
            "km",
            "km-kh",
            "kn",
            "kn-in",
            "ko",
            "ko-kp",
            "ko-kr",
            "kok",
            "kok-in",
            "ks",
            "ks-in",
            "ksb",
            "ksb-tz",
            "ksf",
            "ksf-cm",
            "ksh",
            "ksh-de",
            "kw",
            "kw-gb",
            "ky",
            "ky-kg",
            "lag",
            "lag-tz",
            "lb",
            "lb-lu",
            "lg",
            "lg-ug",
            "lkt",
            "lkt-us",
            "ln",
            "ln-ao",
            "ln-cd",
            "ln-cf",
            "ln-cg",
            "lo",
            "lo-la",
            "lrc",
            "lrc-iq",
            "lrc-ir",
            "lt",
            "lt-lt",
            "lu",
            "lu-cd",
            "luo",
            "luo-ke",
            "luy",
            "luy-ke",
            "lv",
            "lv-lv",
            "mas",
            "mas-ke",
            "mas-tz",
            "mer",
            "mer-ke",
            "mfe",
            "mfe-mu",
            "mg",
            "mg-mg",
            "mgh",
            "mgh-mz",
            "mgo",
            "mgo-cm",
            "mk",
            "mk-mk",
            "ml",
            "ml-in",
            "mn",
            "mn-mn",
            "mr",
            "mr-in",
            "ms",
            "ms-bn",
            "ms-my",
            "ms-sg",
            "mt",
            "mt-mt",
            "mua",
            "mua-cm",
            "my",
            "my-mm",
            "mzn",
            "mzn-ir",
            "naq",
            "naq-na",
            "nb",
            "nb-no",
            "nb-sj",
            "nd",
            "nd-zw",
            "nds",
            "nds-de",
            "nds-nl",
            "ne",
            "ne-in",
            "ne-np",
            "nl",
            "nl-aw",
            "nl-be",
            "nl-bq",
            "nl-cw",
            "nl-nl",
            "nl-sr",
            "nl-sx",
            "nmg",
            "nmg-cm",
            "nn",
            "nn-no",
            "nnh",
            "nnh-cm",
            "no",
            "no-no",
            "nus",
            "nus-ss",
            "nyn",
            "nyn-ug",
            "om",
            "om-et",
            "om-ke",
            "or",
            "or-in",
            "os",
            "os-ge",
            "os-ru",
            "pa",
            "pa-in",
            "pa-pk",
            "pl",
            "pl-pl",
            "prg",
            "prg-001",
            "ps",
            "ps-af",
            "pt",
            "pt-ao",
            "pt-br",
            "pt-ch",
            "pt-cv",
            "pt-gq",
            "pt-gw",
            "pt-lu",
            "pt-mo",
            "pt-mz",
            "pt-pt",
            "pt-st",
            "pt-tl",
            "qu",
            "qu-bo",
            "qu-ec",
            "qu-pe",
            "rm",
            "rm-ch",
            "rn",
            "rn-bi",
            "ro",
            "ro-md",
            "ro-ro",
            "rof",
            "rof-tz",
            "ru",
            "ru-by",
            "ru-kg",
            "ru-kz",
            "ru-md",
            "ru-ru",
            "ru-ua",
            "rw",
            "rw-rw",
            "rwk",
            "rwk-tz",
            "sa",
            "sah",
            "sah-ru",
            "saq",
            "saq-ke",
            "sbp",
            "sbp-tz",
            "sd",
            "sd-pk",
            "se",
            "se-fi",
            "se-no",
            "se-se",
            "seh",
            "seh-mz",
            "ses",
            "ses-ml",
            "sg",
            "sg-cf",
            "shi",
            "shi-ma",
            "si",
            "si-lk",
            "sk",
            "sk-sk",
            "sl",
            "sl-si",
            "smn",
            "smn-fi",
            "sn",
            "sn-zw",
            "so",
            "so-dj",
            "so-et",
            "so-ke",
            "so-so",
            "sq",
            "sq-al",
            "sq-mk",
            "sq-xk",
            "sr",
            "sr-ba",
            "sr-cs",
            "sr-me",
            "sr-rs",
            "sr-xk",
            "sv",
            "sv-ax",
            "sv-fi",
            "sv-se",
            "sw",
            "sw-cd",
            "sw-ke",
            "sw-tz",
            "sw-ug",
            "sy",
            "ta",
            "ta-in",
            "ta-lk",
            "ta-my",
            "ta-sg",
            "te",
            "te-in",
            "teo",
            "teo-ke",
            "teo-ug",
            "tg",
            "tg-tj",
            "th",
            "th-th",
            "ti",
            "ti-er",
            "ti-et",
            "tk",
            "tk-tm",
            "to",
            "to-to",
            "tr",
            "tr-cy",
            "tr-tr",
            "tt",
            "tt-ru",
            "twq",
            "twq-ne",
            "tzm",
            "tzm-ma",
            "ug",
            "ug-cn",
            "uk",
            "uk-ua",
            "ur",
            "ur-in",
            "ur-pk",
            "uz",
            "uz-af",
            "uz-uz",
            "vai",
            "vai-lr",
            "vi",
            "vi-vn",
            "vo",
            "vo-001",
            "vun",
            "vun-tz",
            "wae",
            "wae-ch",
            "wo",
            "wo-sn",
            "xog",
            "xog-ug",
            "yav",
            "yav-cm",
            "yo",
            "yo-bj",
            "yo-ng",
            "yue",
            "yue-cn",
            "yue-hk",
            "zgh",
            "zgh-ma",
            "zh",
            "zh-cn",
            "zh-hk",
            "zh-mo",
            "zh-sg",
            "zh-tw",
            "zh-hans",
            "zh-hant",
            "zu",
            "zu-za",
        ]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and language not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `language` ({0}), must be one of {1}".format(language, allowed_values))  # noqa: E501

        self._language = language

    @property
    def title(self):
        """Gets the title of this ContentSearchResult.  # noqa: E501

        The title of the returned document.  # noqa: E501

        :return: The title of this ContentSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ContentSearchResult.

        The title of the returned document.  # noqa: E501

        :param title: The title of this ContentSearchResult.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def description(self):
        """Gets the description of this ContentSearchResult.  # noqa: E501

        The result's description. The content will be determined by the value of `length` in the request.  # noqa: E501

        :return: The description of this ContentSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ContentSearchResult.

        The result's description. The content will be determined by the value of `length` in the request.  # noqa: E501

        :param description: The description of this ContentSearchResult.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def category(self):
        """Gets the category of this ContentSearchResult.  # noqa: E501

        For knowledge articles, the category of the article.  # noqa: E501

        :return: The category of this ContentSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ContentSearchResult.

        For knowledge articles, the category of the article.  # noqa: E501

        :param category: The category of this ContentSearchResult.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def subcategory(self):
        """Gets the subcategory of this ContentSearchResult.  # noqa: E501

        For knowledge articles, the subcategory of the article.  # noqa: E501

        :return: The subcategory of this ContentSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._subcategory

    @subcategory.setter
    def subcategory(self, subcategory):
        """Sets the subcategory of this ContentSearchResult.

        For knowledge articles, the subcategory of the article.  # noqa: E501

        :param subcategory: The subcategory of this ContentSearchResult.  # noqa: E501
        :type: str
        """

        self._subcategory = subcategory

    @property
    def author_full_name(self):
        """Gets the author_full_name of this ContentSearchResult.  # noqa: E501

        Name of the author.  # noqa: E501

        :return: The author_full_name of this ContentSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._author_full_name

    @author_full_name.setter
    def author_full_name(self, author_full_name):
        """Sets the author_full_name of this ContentSearchResult.

        Name of the author.  # noqa: E501

        :param author_full_name: The author_full_name of this ContentSearchResult.  # noqa: E501
        :type: str
        """

        self._author_full_name = author_full_name

    @property
    def tags(self):
        """Gets the tags of this ContentSearchResult.  # noqa: E501

        If a blog post, the tags associated with it.  # noqa: E501

        :return: The tags of this ContentSearchResult.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ContentSearchResult.

        If a blog post, the tags associated with it.  # noqa: E501

        :param tags: The tags of this ContentSearchResult.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def table_id(self):
        """Gets the table_id of this ContentSearchResult.  # noqa: E501

        If a dynamic page, the ID of the HubDB table.  # noqa: E501

        :return: The table_id of this ContentSearchResult.  # noqa: E501
        :rtype: int
        """
        return self._table_id

    @table_id.setter
    def table_id(self, table_id):
        """Sets the table_id of this ContentSearchResult.

        If a dynamic page, the ID of the HubDB table.  # noqa: E501

        :param table_id: The table_id of this ContentSearchResult.  # noqa: E501
        :type: int
        """

        self._table_id = table_id

    @property
    def row_id(self):
        """Gets the row_id of this ContentSearchResult.  # noqa: E501

        If a dynamic page, the row ID in the HubDB table.  # noqa: E501

        :return: The row_id of this ContentSearchResult.  # noqa: E501
        :rtype: int
        """
        return self._row_id

    @row_id.setter
    def row_id(self, row_id):
        """Sets the row_id of this ContentSearchResult.

        If a dynamic page, the row ID in the HubDB table.  # noqa: E501

        :param row_id: The row_id of this ContentSearchResult.  # noqa: E501
        :type: int
        """

        self._row_id = row_id

    @property
    def published_date(self):
        """Gets the published_date of this ContentSearchResult.  # noqa: E501

        The date the content was published.  # noqa: E501

        :return: The published_date of this ContentSearchResult.  # noqa: E501
        :rtype: int
        """
        return self._published_date

    @published_date.setter
    def published_date(self, published_date):
        """Sets the published_date of this ContentSearchResult.

        The date the content was published.  # noqa: E501

        :param published_date: The published_date of this ContentSearchResult.  # noqa: E501
        :type: int
        """

        self._published_date = published_date

    @property
    def combined_id(self):
        """Gets the combined_id of this ContentSearchResult.  # noqa: E501

        The ID of the document in HubSpot.  # noqa: E501

        :return: The combined_id of this ContentSearchResult.  # noqa: E501
        :rtype: str
        """
        return self._combined_id

    @combined_id.setter
    def combined_id(self, combined_id):
        """Sets the combined_id of this ContentSearchResult.

        The ID of the document in HubSpot.  # noqa: E501

        :param combined_id: The combined_id of this ContentSearchResult.  # noqa: E501
        :type: str
        """

        self._combined_id = combined_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(lambda item: (item[0], item[1].to_dict()) if hasattr(item[1], "to_dict") else item, value.items()))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ContentSearchResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ContentSearchResult):
            return True

        return self.to_dict() != other.to_dict()
