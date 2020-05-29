# -- coding: utf-8 --

import codecs
import os
import sys
import time
import traceback
import win32con
import win32evtlog
import win32evtlogutil
import winerror
import datetime

class creboot:
    def __init__(self,computer_ID = -1):
        self.computer_ID = computer_ID
        self.list_event = list()
        cur = datetime.datetime.now()
        self.time = datetime.date(cur.year,cur.month,cur.day)

    #----------------------------------------------------------------------
    def getAllEvents(self,server, logtypes, basePath):
        """
        """
        if not server:
            serverName = "localhost"
        else:
            serverName = server
        for logtype in logtypes:
            path = os.path.join(basePath, "%s_%s_log.log" % (serverName, logtype))
            self.getEventLogs(server, logtype, path)
    
    #----------------------------------------------------------------------
    def getEventLogs(self,server, logtype, logPath):
        """
        Get the event logs from the specified machine according to the
        logtype (Example: Application) and save it to the appropriately
        named log file
        """
        print ("Logging %s events" % logtype)

        log = codecs.open(logPath, encoding='utf-8', mode='w')
        line_break = '-' * 80
    
        log.write("\n%s Log of %s Events\n" % (server, logtype))
        log.write("Created: %s\n\n" % time.ctime())
        log.write("\n" + line_break + "\n")
        hand = win32evtlog.OpenEventLog(server,logtype)
        total = win32evtlog.GetNumberOfEventLogRecords(hand)
        print ("Total events in %s = %s" % (logtype, total))
        flags = win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ
        events = win32evtlog.ReadEventLog(hand,flags,0)
        evt_dict={win32con.EVENTLOG_AUDIT_FAILURE:'EVENTLOG_AUDIT_FAILURE',
                win32con.EVENTLOG_AUDIT_SUCCESS:'EVENTLOG_AUDIT_SUCCESS',
                win32con.EVENTLOG_INFORMATION_TYPE:'EVENTLOG_INFORMATION_TYPE',
                win32con.EVENTLOG_WARNING_TYPE:'EVENTLOG_WARNING_TYPE',
                win32con.EVENTLOG_ERROR_TYPE:'EVENTLOG_ERROR_TYPE'}
    
        first_day = datetime.date(self.time.year, self.time.month, 1)
        last_day_pre_month = first_day - datetime.timedelta(days = 1)
        first_day_of_pre_month = datetime.date(last_day_pre_month.year, last_day_pre_month.month, 1)

        try:
            events=1
            while events:
                events=win32evtlog.ReadEventLog(hand,flags,0)
                for ev_obj in events:
                    the_date = datetime.date(ev_obj.TimeGenerated.year,ev_obj.TimeGenerated.month,ev_obj.TimeGenerated.day)#.Format("%Y-%m-%d")
                    the_time = ev_obj.TimeGenerated.Format("%Y-%m-%d %H:%M:%S") #'12/23/99 15:54:09'
                    evt_id = str(winerror.HRESULT_CODE(ev_obj.EventID)) # 6005,6006,6009
                    if evt_id == '6005' or evt_id == '6006' :
                        if the_date >= first_day_of_pre_month and the_date <= last_day_pre_month:
                            # should be filter by the_date
                            computer = str(ev_obj.ComputerName)
                            cat = ev_obj.EventCategory
                            ##seconds=date2sec(the_time)
                            record = ev_obj.RecordNumber
                            msg = win32evtlogutil.SafeFormatMessage(ev_obj, logtype)
            
                            source = str(ev_obj.SourceName)
                            if not ev_obj.EventType in evt_dict.keys():
                                evt_type = "unknown"
                            else:
                                evt_type = str(evt_dict[ev_obj.EventType])
                            log.write("Event Date/Time: %s\n" % the_time)
                            log.write("Event ID / Type: %s / %s\n" % (evt_id, evt_type))
                            log.write("Record #%s\n" % record)
                            log.write("Source: %s\n\n" % source)
                            log.write(msg)
                            log.write("\n\n")
                            log.write(line_break)
                            log.write("\n\n")

                            print ("Event ID / Type: %s / %s\n" % (evt_id, evt_type))
                            self.list_event.append({"computer_ID":self.computer_ID,"eventID":int(evt_id),"reboot_date":the_time,"event_log":msg})
        except:
            print (traceback.print_exc(sys.exc_info()))
    
        print ("Log creation finished. Location of log is %s" % logPath)


if __name__ == "__main__":
    server = None  # None = local machine
    logTypes = ["System"]#, "Application", "Security"]
    creboot().getAllEvents(server, logTypes, "C:\download")
