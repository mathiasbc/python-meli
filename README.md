python-meli
=======

```python-meli``` is a wrapper for MercadoLibre API, current version of the API is 
V1, this wrapper does not yet totally supports the entire API, see below for 
supported endpoints.

Features
--------

* Categories and Listings:
    - Fully supported, see [the docs](http://developers.mercadolibre.com/API-directory/)
* Locations and Currencies
    - Fully supported, see [the docs](http://developers.mercadolibre.com/API-directory/)

Installation
------------

    git clone https://github.com/mathiasbc/python-meli.git
    cd python-meli
    sudo python setup.py install

Usage
-----

Every method below returns a JSON of the the endpoint response, the following example is just to show the basic usage of this wrapper, however I recommend you to read the meli.py module to see what does every method exactle does and what parameters can be passed to them.


###### Mercado Libre endpoints

```python
from meli.meli import MercadoLibre 

MELI = MercadoLibre()

# Locations and Currencies =================================================
print MELI.countries()
print MELI.country_detail(country_id='PE')
print MELI.state_detail(state_id='PE-ARE')
print MELI.city_detail(city_id='TVBFQ0FSRTE0YjA5')
print MELI.currencies()
print MELI.currency_detail(currency_id='PEN')
print MELI.currency_conversion(currency_id_from='PEN', currency_id_to='USD')


# Categories and Listings ==================================================
print MELI.sites()
print MELI.site_detail(site_id='MPE')
print MELI.site_domains(site_domain_url='www.mercadolibre.com.pe')
print MELI.site_listing_types(site_id='MPE')
print MELI.site_listing_exposures(site_id='MPE', listing_exposure_id='low')
print MELI.site_listing_prices(site_id='MPE', price=10000, quantity=10)
print MELI.site_categories(site_id='MPE')
print MELI.category_detail(category_id='MPE1182')
```


Notes
-----
For the moment oauth is not supported, I'm currently working on it.



Want to help?
-------------
Python-MELI is a usefull wrapper but I would greatly appreciate any help, you could contribute writing the Wiki or forking and then making pull request with new features. Feel free to contact me.


(c) 2012 - Mathias Bustamante mathias@worldrat.com - Distributed under the BSD license - Made in Peru.