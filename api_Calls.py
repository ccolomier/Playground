# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 00:41:16 2021

@author: colomich
"""
import requests
import pandas as pd

parameters = {
    #Limit to how many pokemon will be returned
    'limit': 151
}

pokemon = requests.get("https://pokeapi.co/api/v2/pokemon", params=parameters)

poke_json = pokemon.json()

print(type(poke_json))
poke_df = pd.DataFrame.from_dict(poke_json['results'])

print(poke_df.head(10))
