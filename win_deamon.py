#!/usr/bin/python
# -*- coding: utf-8 -*-
import win32serviceutil
import win32service
import win32event
import monitor
class SmallestPythonService(win32serviceutil.ServiceFramework):
    _svc_name_ = "WriteCache"
    _svc_display_name_ = "WriteCache Monitor Service"
    def __init__(self, args):
        self.threads = []
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
    def SvcDoRun(self):
        #This is my program !
        monitor.wrong()
        self.threads = []
        self.ReportServiceStatus(win32service.SERVICE_RUNNING)
        win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)
if __name__=='__main__':
    win32serviceutil.HandleCommandLine(SmallestPythonService)