# -*- coding: utf-8 -*-
from meli.meli import MercadoLibre 


if __name__ == "__main__":
    MELI = MercadoLibre()

    # Locations and Currencies =================================================
    print MELI.countries()
    #print MELI.country_detail(country_id='PE')
    #print MELI.state_detail(state_id='PE-ARE')
    #print MELI.city_detail(city_id='TVBFQ0FSRTE0YjA5')
    #print MELI.currencies()
    #print MELI.currency_detail(currency_id='PEN')
    #print MELI.currency_conversion(currency_id_from='PEN', currency_id_to='USD')

    # Users and Apps ===========================================================
    

    # Categories and Listings ==================================================
    #print MELI.sites()
    #print MELI.site_detail(site_id='MPE')
    #print MELI.site_domains(site_domain_url='www.mercadolibre.com.pe')
    #print MELI.site_listing_types(site_id='MPE')
    #print MELI.site_listing_exposures(site_id='MPE', listing_exposure_id='low')
    #print MELI.site_listing_prices(site_id='MPE', price=10000, quantity=10)
    #print MELI.site_categories(site_id='MPE')
    #print MELI.category_detail(category_id='MPE1182')
