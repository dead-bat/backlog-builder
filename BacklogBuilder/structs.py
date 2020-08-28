# classes, JSON structure, etc. used by BacklogBuilder

class Project:
    """Class for projects and associated backlog calculations"""
    def __init__(self, nm=None, sd=None, ed=None, wd=0, co=0, **kwargs):
        self.name = nm        # type: string = name of project
        self.startDate = sd   # type: datetime - start of project period
        self.endDate = ed     # type: datetime - end of project period
        self.workDays = wd    # type: int - number of working days in the project period
        self.calcOn = co      # type: bool - whether or not a backlog calculation is performed on the project
    
