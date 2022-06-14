# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 14:51:38 2022

@author: KD
"""

import glassdoor_scraper as gs
import pandas as pd

path="C:/Users/KD/Documents/ds-salary/chromedriver"
df = gs.get_jobs('data scientist',1000, False, path, 15)

#C:/Users/KD/Desktop/Projects/Salary-estimator-using-Data-Science-main/chromedriver.exe