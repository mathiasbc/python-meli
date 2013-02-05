# -*- coding: utf-8 -*-

import endpoints
import constants
import utils
from methods import get, post

class MercadoLibre(object):
    """
    Object that contains all the functionallity that MELI API offers
    """

    def __init__(self, api_version=None):
        """
        If api_version is not passed it defaults to the one on contants.py
        """
        if api_version is not None:
            self.API_VERSION = str(api_version)
        else:
            self.API_VERSION = constants.DEFAULT_API_VERSION

        self.API_PREFIX_URL = constants.API_PARTIAL_URL % { 
            'api_version': self.API_VERSION 
        }

    def sites(self):
        """
        Returns information about the sites where MercadoLibre runs as JSON.
        """
        url = self.API_PREFIX_URL + endpoints.SITES
        response = get(url)
        return response

    def site_detail(self, site_id):
        """
        @site_id: id of the request site, MPE (PERU)
        @return: Returns the detailed information of a site as JSON.
        """
        url = self.API_PREFIX_URL + endpoints.SITE_DETAIL % {
            'site_id': site_id
        }
        response = get(url)
        return response

    def site_domains(self, site_domain_url):
        """
        @site_domain_url: www.mercadolibre.com.pe
        @returns: Information about specific domain as JSON
        """
        url = self.API_PREFIX_URL + endpoints.SITE_DOMAINS % {
            'site_domain_url': site_domain_url
        }
        response = get(url)
        return response


    def site_listing_types(self, site_id):
        """
        @site_id: id of the request site, MPE (PERU)
        @return: Returns information about the listing types as JSON
        """
        url = self.API_PREFIX_URL + endpoints.SITE_LISTING_TYPES % {
            'site_id': site_id
        }
        response = get(url)
        return response

    def site_listing_exposures(self, site_id, listing_exposure_id=None):
        """
        Lisits the different exposures types on MercadoLibre

        @site_id: id of the request site, MPE (PERU)
        @listing_exposure_id: id of the exposure, low, mid, high...

        @return: Returns advertising exposures as JSON
        """
        url = self.API_PREFIX_URL + endpoints.SITE_LISTING_EXPOSURES % {
            'site_id': site_id
        }

        # adding exposure_id .../low 
        if listing_exposure_id is not None:
            url += listing_exposure_id

        response = get(url)
        return response

    def site_listing_prices(self, site_id, price, 
            listing_type_id=None, quantity=None, 
            category_id=None, currency_id=None
        ):
        """
        Lists the prices of listing items by different criteria

        @site_id: id of the request site, MPE (PERU)
        @price: price of the object, 500
        @listing_type_id: gold, premium, silver, bronce, free
        @quantity: amount of pulicid items, 5
        @category_id: , MLA1744
        @currency_id: USD(US dollars), PEN(Soles)

        @return: Returns the listing prices as JSON
        """
        url = self.API_PREFIX_URL + endpoints.SITE_LISTING_PRICES % {
            'site_id': site_id
        }

        # create query params
        params = {'price': price, 'listing_type_id': listing_type_id,
            'quantity': quantity, 'category_id': category_id, 
            'currency_id': currency_id
        }

        # erase fields with None
        utils.erase_none_values(params)

        response = get(url, params=params)
        return response

    def site_categories(self, site_id):
        """
        @site_id: id of the request categories, MPE (PERU)
        @return: Returns the site categories as JSON.
        """
        url = self.API_PREFIX_URL + endpoints.SITE_CATEGORIES % {
            'site_id': site_id
        }

        response = get(url)
        return response

    def category_detail(self, category_id):
        """
        @category_id: MPE1182
        @returns Information of the category as JSON
        """
        url = self.API_PREFIX_URL + endpoints.CATEGORY_DETAIL % {
            'category_id': category_id
        }

        response = get(url)
        return response

    def countries(self):
        """
        @return: Countries on MercadoLibre as JSON
        """
        url = self.API_PREFIX_URL + endpoints.COUNTRIES
        response = get(url)
        return response

    def country_detail(self, country_id):
        """
        @country_id: PE(Peru), AR(Agentina)...
        @return: Detailed info of a country as JSON 
        """
        url = self.API_PREFIX_URL + endpoints.COUNTRY_DETAIL % {
            'country_id': country_id
        }

        response = get(url)
        return response

    def state_detail(self, state_id):
        """
        @state_id: PE-ARE(Arequipa-Peru)...
        @return: Detailed info for given state as JSON
        """
        url = self.API_PREFIX_URL + endpoints.STATE_DETAIL % {
            'state_id': state_id
        }

        response = get(url)
        return response

    def city_detail(self, city_id):
        """
        @city_id: TVBFQ0FSRTE0YjA5 (Arequipa-Arequipa-Peru)
        @returns: Detailed info for the given city as JSON
        """
        url = self.API_PREFIX_URL + endpoints.CITY_DETAIL % {
            'city_id': city_id
        }

        response = get(url)
        return response

    def currencies(self):
        """
        @return: Info of the currencies in MercadoLibre as JSON
        """
        url = self.API_PREFIX_URL + endpoints.CURRENCIES
        response = get(url)
        return response

    def currency_detail(self, currency_id):
        """
        @currency_id: PEN (Soles, Peru)...
        @return: Info of the given currency
        """
        url = self.API_PREFIX_URL + endpoints.CURRENCY_DETAIL % {
            'currency_id': currency_id
        }

        response = get(url)
        return response

    def currency_conversion(self, currency_id_from, currency_id_to):
        """
        @currency_id_from: currency to convert, PEN
        @currency_id_to: currency to convert to, USD
        @returns: Information about the conversion as JSON
        """
        url = self.API_PREFIX_URL + endpoints.CURRENCY_CONVERSION

        # create query params
        params = { 'from': currency_id_from, 'to': currency_id_to }

        response = get(url, params=params)
        return response



