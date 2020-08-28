#
# BACKLOG BUILDER alpha
#
# Configurations
#
import datetime
# Holiday Dates
H_DAYS = [datetime.datetime(2020, 1, 1),   datetime.datetime(2020, 5, 25),  datetime.datetime(2020, 7, 4),       # LIST OF HOLIDAYS
         datetime.datetime(2020, 9, 7),    datetime.datetime(2020, 11, 26), datetime.datetime(2020, 11, 27),     # *** Needs to be updated every January to the January 2 years out.
         datetime.datetime(2020, 12, 24),  datetime.datetime(2020, 12, 25), datetime.datetime(2021, 1, 1),       # *** i.e. In January 2020, we updated the list to include every holiday
         datetime.datetime(2021, 5, 31),   datetime.datetime(2021, 7, 4),   datetime.datetime(2021, 9, 6),       # *** through New Years Day 2022. Maintaing this dating scheme will ensure
         datetime.datetime(2021, 11, 25),  datetime.datetime(2021, 11, 26), datetime.datetime(2021, 12, 24),     # *** no holidays are forgotten during calculation.
         datetime.datetime(2021, 12, 25),  datetime.datetime(2022, 1, 1)]                                        #
#
# Backlog sheets to calculate
SRC_SHEETS = ["MediTract", "MDB Purchased Services", "MedApproved", "Total Value Management", "EMTS", "Hayes"]