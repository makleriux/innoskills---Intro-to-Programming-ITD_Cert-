# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 10:07:51 2021

@author: La l
"""
em_dict = {}

em_dict.update(first_name= 'John')
em_dict.update(last_name = 'Murray')
em_dict.update(age = 37)
em_dict.update(address = {'street': 'james street', 'city': 'Dublin', 'country':'Ireland', 'eircode':'D13GD25'})
em_dict.update(sex ='male')

print("Number of elements in Dictionary " + str(len(em_dict)))

if em_dict['address'].get("city") == "Dublin":
    print("Eircode if person lives in Dublin " + str(em_dict['address'].get('eircode')))
