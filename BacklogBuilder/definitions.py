# classes, JSON structure, etc. used by BacklogBuilder
"""
Definitions for program-global classes
"""
import datetime as dt
import pandas as pd

# IMPORT FUNCTIONS
def import_from_excel(sourceFile):
    wb = pd.ExcelFile(sourceFile)
    sheet = input("What sheet in the workbook contains your source data? (Default is Sheet1)\n") or "Sheet1"
    return pd.read_excel(wb, sheet_name=sheet)

def import_from_csv(sourceFile):
    return pd.read_csv(sourceFile)

def import_source_data(sourceFile):
    #import_file = { ".xlsx" : lambda sf : import_from_excel(sf), ".csv" : lambda sf : pd.ExcelFile(sf) }
    #sourceData = import_file[sourceFile[(sourceFile.index(".")):]]
    sfext = sourceFile[sourceFile.index("."):]
    if sfext in ['.xlsx', '.xls']:
        sourceData = import_from_excel(sourceFile)
    elif sfext == '.csv':
        sourceData = import_from_csv(sourceFile)
    else:
        return "Import failed: file type not recognized"
    return sourceData

# DATE CALCULATION FUNCTIONS
# calculate working days between two dates

# PROJECT CLASS
class Project:
    """Class for projects and associated backlog calculations"""
    def __init__(self, nm=None, sd=None, ed=None, co=0, tr=0.0, **kwargs):    # The name, start and end dates, and calculation switch fields are required at init; everything else is optional or computed
        self.name = nm        # type: string = name of project
        self.startDate = sd   # type: datetime - start of project period
        self.endDate = ed     # type: datetime - end of project period
        self.calcOn = co      # type: bool - whether or not a backlog calculation is performed on the project
        self.etc = tr         # type: float - estimated working time left on the project
        