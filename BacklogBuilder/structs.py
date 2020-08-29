# classes, JSON structure, etc. used by BacklogBuilder
"""
Definitions for program-global classes
"""

import BacklogBuilder.functions

class Project:
    """Class for projects and associated backlog calculations"""
    def __init__(self, nm=None, sd=None, ed=None, co=0, **kwargs):    # The name, start and end dates, and calculation switch fields are required at init; everything else is optional or computed
        self.name = nm        # type: string = name of project
        self.startDate = sd   # type: datetime - start of project period
        self.endDate = ed     # type: datetime - end of project period
        self.calcOn = co      # type: bool - whether or not a backlog calculation is performed on the project
        