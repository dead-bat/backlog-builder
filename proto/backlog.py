#                   
# BACKLOG BUILDER alpha
# This is the prototype built for TractManager
# All identifying and proprietary information has been
# removed to make this a generic solution
#
# IMPORTS
import pandas as pd
import io
import datetime
import numpy as np
import math
#
# the configuration also needs to be imported:
import bl_config
#
# GLOBAL DECLARATIONS
backlog_sheets = bl_config.SRC_SHEETS
blxl = pd.ExcelFile('./backlog.xlsx')
logfile = open("./log.csv", "w")
todays_date = datetime.date.today()
holidays_list = bl_config.H_DAYS
months_start = pd.date_range(start=(todays_date.replace(day=1)), periods=12, freq='MS')
months_end = pd.date_range(start=todays_date, periods=12, freq='M')
weekmask = 'Mon Tue Wed Thu Fri'
holidayCalendar = pd.offsets.CustomBusinessDay(holidays=holidays_list, weekmask=weekmask)
writer = pd.ExcelWriter('./calculations.xlsx', engine='xlsxwriter', date_format='MM/DD/YYYY', datetime_format='MM/DD/YYYY')
zer0ut = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#
#
# FUNCTIONS
def auditProjectDates(sd, ed):              
    if sd is pd.NaT or sd < todays_date:    
        sd = todays_date                    
    else:                                   
        sd = sd                             
    if ed is pd.NaT or ed < todays_date:    
        ed = todays_date                    
    else:                                                               
        ed = ed                                                         
    wdays = pd.bdate_range(start=sd, end=ed, freq=holidayCalendar)      
    wdaysCount = wdays.size                                             
    return sd, ed, wdays, wdaysCount        
#                                           
def calcWorkDaysPerMonth(projCal):          
    wdpm = []                               
    a = 0                                   
    while a < months_start.size:            
        wdc = 0                             
        wdim = pd.bdate_range(start=months_start[a], end=months_end[a], freq=holidayCalendar)   
        for date in projCal:                
            if date in wdim:
                wdc = wdc + 1
        wdpm.append(wdc)
        wdc = 0
        a = a + 1
    return wdpm
#
def calculateMonthlyRolloff(mwd, hpd):
    mro = []
    for eachMonth in mwd:
        mro.append(eachMonth * hpd)
    return mro
#
def calculateSysAdmin(sah, psd, ped):
    mro = []                                
    if math.isnan(sah) != True:             
        monthlyHours = sah
    else:
        monthlyHours = 0
    first_month = psd.replace(day=1)
    last_month = ped + pd.offsets.MonthEnd(0)
    for eachMonth in months_start:
        if eachMonth >= first_month and eachMonth <= last_month:
            mro.append(monthlyHours)
        else:
            mro.append(0)
    return mro
#
#
#
#
# MAIN PROGRAM
for each_sheet in backlog_sheets:
    output = []
    bldf = pd.read_excel(blxl, sheet_name=each_sheet)
    for p in bldf.index:
        projectName = bldf["Project Name"][p]
        try:              #   
            startDate = bldf["Client Intro Call/Start Date"][p]
        except:
            startDate = bldf["Scheduled Start"][p]
        endDate = bldf["Project Scheduled Finish"][p]
        projectState = bldf["State"][p]
        projectPhase = bldf["Phase"][p]
        projectEtc = bldf["Task ETC"][p]
        sysAdminHrs = bldf["Sys Admin Hrs per Month"][p]
        startDate, endDate, wdCal, wdCount = auditProjectDates(startDate, endDate)
        hrsPerDay = projectEtc / wdCount
        monthlyWorkDays = calcWorkDaysPerMonth(wdCal)
        if startDate is None:
            output.append(zer0ut)
        else:
            if projectState == "Not Started" or projectState == "In Progress":
                if projectPhase != "READINESS" and projectPhase != "System Administration":
                    rolloff = calculateMonthlyRolloff(monthlyWorkDays, hrsPerDay)
                    output.append(rolloff)
                elif projectPhase == "System Administration":
                    sysAdminRolloff = calculateSysAdmin(sysAdminHrs, startDate, endDate)
                    output.append(sysAdminRolloff)
                elif projectPhase == "READINESS":
                    output.append(zer0ut)
            else:
                output.append(zer0ut)
    logfile.writelines(each_sheet + "," + str(p) + "\n")
    outdf = pd.DataFrame(data=output, columns=months_start)
    new_backlog = bldf.join(outdf)
    new_backlog.to_excel(writer, each_sheet, index=None, header=True)
    print(new_backlog)
    p = 0
writer.save()
writer.close()
blxl.close()
logfile.close()