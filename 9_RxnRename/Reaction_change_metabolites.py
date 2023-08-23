#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 10:32:43 2023

@author: hugo
"""

import pandas as pd
import numpy as np

#%% Prepare data
rxns = pd.read_csv("PmegMOA_reacsRevised.csv", header = 0)
mets = pd.read_csv("PmegMOA_metsRevised.csv", header = 0)
old_mets = pd.read_csv("PmegMOA_met.csv", header = 0)
#mets_ana = pd.read_csv("PmegMOA_mets.csv", header = 0)

#mets = mets.drop(["Comments", "Unnamed: 8", "Unnamed: 9"], axis = 1)
mets = mets.drop(['ModelSEED', 'New_ID', 'Comments', 'Unnamed: 9',
                  'Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12'], axis = 1)
mets = mets.fillna("None")
#mets_ana = mets_ana.drop(["Comments", "Unnamed: 7", "Unnamed: 8"], axis = 1)
mets["final_name"] = mets["bigg_name"] + "_" + mets["Compartment"]
#mets_ana["final_name"] = mets_ana["bigg_name"] + "_" + mets_ana["Compartment"]

mets['abbreviation'] = old_mets['Old_name']

#mod_mets = mets[["Old_name", "final_name"]].to_numpy()
mod_mets = mets[["abbreviation", "final_name"]].to_numpy()
mod_reacts = rxns[["Reaction"]].to_numpy()
final_reacs = [None] * len(mod_reacts)
nan_reacs = final_reacs.copy()

#%% Replace names
for r in np.arange(0, len(mod_reacts)):
    
    curr_reac = mod_reacts[r][0].split(" ")
    
    for element_index in np.arange(0, len(curr_reac)):
        try:
            curr_element = curr_reac[element_index]
            met_index = np.where(mod_mets[:, 0] == curr_element)[0][0]
            curr_reac[element_index] = mod_mets[met_index, 1]
            print(curr_reac)
            
        except:
            pass
        
    curr_reac = " ".join(curr_reac)
    final_reacs[r] = curr_reac
    
    if "None" in curr_reac:
        nan_reacs[r] = 1
    else:
        nan_reacs[r] = 0
        
        
    print("done iter number", r)

#%% Add new info to table and export as csv
rxns['Weird_Molecules_present'] = nan_reacs
rxns['translated_reacs'] = final_reacs
rxns.to_csv('reactions_analized.csv', index = False)




