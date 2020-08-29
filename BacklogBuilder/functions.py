# global and general function definitions for BacklogBuilder
import datetime as dt
import pandas as pd
import numpy as np

# IMPORT SOURCE FILE
def import_source_data(sourceFile):
    import_file = {".xlsx" : (lambda sf : pd.ExcelFile(sf)), ".csv" : (lambda sf : pd.ExcelFile(sf)) } 
    sourceData = import_file[sourceFile[".":]]
    return sourceData

# DATE CALCULATION FUNCTIONS
# calculate working days between two dates
