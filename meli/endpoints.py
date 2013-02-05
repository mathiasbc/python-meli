# -*- coding: utf-8 -*-

# Users and Apps  ==============================================================

# /users/

# /users/:id
#USER_DETAIL = "/users/%(user_id)s"     # Append user_id

# /users/{user_id}/addresses?access_token={...}
#USER_ADDRESSES = \
#    "/users/%(user_id)s/addresses?access_token=%(access_token)s"

# /users/{user_id}/accepted_payment_methods
#USER_ACCEPTED_PAY_METHOD = "/users/%(user_id)s/accepted_payment_methods"

# /applications/{app_id}
# /scopes


# Categories and Listings ======================================================

# /sites  Sites where MELI runs
SITES = "/sites"

# /sites/{site_id}
SITE_DETAIL = "/sites/%(site_id)s"

# /site_domains/{site_domain_url}   Retrieves info about the domain
SITE_DOMAINS = "/site_domains/%(site_domain_url)s"

# /sites/{site_id}/listing_types    
#   Retrieves information about the listing types.
SITE_LISTING_TYPES = "/sites/%(site_id)s/listing_types"

# /sites/{site_id}/listing_exposures
SITE_LISTING_EXPOSURES = "/sites/%(site_id)s/listing_exposures/"

# /sites/{site_id}/listing_prices?price=1
SITE_LISTING_PRICES = "/sites/%(site_id)s/listing_prices"

# /sites/{site_id}/categories
SITE_CATEGORIES = "/sites/%(site_id)s/categories"

# /categories/{category_id}     Information about specific category
CATEGORY_DETAIL = "/categories/%(category_id)s"

# /categories/{category_id}/attributes      I could not make it work
CATEGORY_ATTRIBUTES = ""


# Locations and Currencies =====================================================

# /countries    List the countries
COUNTRIES = "/countries"

# /countries/{country_id}  Info for the country
COUNTRY_DETAIL = "/countries/%(country_id)s"

# /states/{state_id}  Info for a given State
STATE_DETAIL = "/states/%(state_id)s"

# /cities/{city_id}  Info for the given state
CITY_DETAIL = "/cities/%(city_id)s"

# /currencies  Info of the MercadoLibre currencies
CURRENCIES = "/currencies"

# /currencies/{currency_id}
CURRENCY_DETAIL = "/currencies/%(currency_id)s"

# /currency_conversions/search?from={currency_id}&to={currency_id}
CURRENCY_CONVERSION = "/currency_conversions/search"