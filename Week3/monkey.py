#!/usr/bin/python3
#Name:zhangjun
#Email:aceg452161724@qq.com
#Time:2018/5/21 19:30

# !/usr/bin/env python
# -*- coding: utf-8 -*-


import wx
import os
import time
import string


class MyFrame(wx.Frame):
    delayDefault = "2"
    seedDefault = "5000000"
    executionFrequencyDefault = "600000"
    logDir = "./"
    pacegeMode = ["mobi.wifi.toolbox"]

    def __init__(self):

        wx.Frame.__init__(self, None, -1, "Monkey自动化测试工具".decode('utf-8'), size=(500, 800))
        panel = wx.Panel(self, -1)

        xPos = 10
        xPos1 = 180
        yPos = 12
        yDelta = 40

        ignoreFATALStr = "忽略程序崩溃"
        ignoreAnrStr = "忽略程序无响应"
        ignoreSafeStr = "忽略安全异常"
        errorStopStr = "出错中断程序"
        localErrorStr = "本地代码导致的崩溃"
        default = "默认"
        seedStr = "种子数："
        processTimesStr = "执行次数:"
        delayStr = "延时:"
        processTypeStr = "执行方式:"
        pacageNameStr = "包名:"
        logLeverStr = "日志输出等级:"
        loadAppStr = "读取程序包"
        selectAllStr = "全部选择"
        cancelAllStr = "全部取消"
        defaultParamsStr = "默认参数"
        hotMonkeyStr = "一键Monkey"
        hotMonkeyWifiStr = "一键测Wifi"
        stopMonkeyStr = "停止Monkey"
        startMonkeyStr = "开始Monkey"
        execLogStr = "生成Log"
        logLeverSStr = "简单"
        logLeverNStr = "普通"
        logLeverFStr = "详细"

        excuteMode = [ignoreFATALStr.decode('utf-8'),
                      ignoreAnrStr.decode('utf-8'),
                      ignoreSafeStr.decode('utf-8'),
                      errorStopStr.decode('utf-8'),
                      localErrorStr.decode('utf-8'),
                      default.decode('utf-8')
                      ]

        logMode = [logLeverSStr.decode('utf-8'), logLeverNStr.decode('utf-8'), logLeverFStr.decode('utf-8')]
        executionModeDefault = excuteMode[0]

        menuBar = wx.MenuBar()
        menu1 = wx.Menu("")
        menuBar.Append(menu1, "File")
        self.SetMenuBar(menuBar)

        wx.StaticText(panel, -1, seedStr.decode('utf-8'), pos=(xPos, yPos))
        self.seedCtrl = wx.TextCtrl(panel, -1, "", pos=(xPos1, yPos))
        self.seedCtrl.Bind(wx.EVT_KILL_FOCUS, self.OnAction)
        self.seedCtrl.SetFocus()

        wx.StaticText(panel, -1, processTimesStr.decode('utf-8'), pos=(xPos, yPos + yDelta))
        self.excuteNumCtrl = wx.TextCtrl(panel, -1, "", pos=(xPos1, yPos + yDelta))

        wx.StaticText(panel, -1, delayStr.decode('utf-8'), pos=(xPos, yPos + 2 * yDelta))
        self.delayNumCtrl = wx.TextCtrl(panel, -1, "", pos=(xPos1, yPos + 2 * yDelta))

        wx.StaticText(panel, -1, processTypeStr.decode('utf-8'), pos=(xPos, yPos + 3 * yDelta))

        wx.StaticText(panel, -1, pacageNameStr.decode('utf-8'), pos=(xPos, yPos + 4 * yDelta))

        self.excuteModeCtrl = wx.ComboBox(panel, -1, "", (xPos1, yPos + 3 * yDelta), choices=excuteMode,
                                          style=wx.CB_DROPDOWN)

        self.excutePacageCtrl = wx.ComboBox(panel, -1, "", (xPos1, yPos + 4 * yDelta), choices=self.pacegeMode,
                                            style=wx.CB_DROPDOWN)

        self.checkListBox = wx.CheckListBox(panel, -1, (xPos, yPos + 5 * yDelta), (400, 350), [])

        yPoslayout = yPos + 15 * yDelta

        wx.StaticText(panel, -1, logLeverStr.decode('utf-8'), pos=(xPos, yPoslayout - yDelta))
        self.logModeCtrl = wx.ComboBox(panel, -1, "", (xPos1, yPoslayout - yDelta), choices=logMode,
                                       style=wx.CB_DROPDOWN)

        self.readButton = wx.Button(panel, -1, loadAppStr.decode('utf-8'), pos=(xPos, yPoslayout))
        self.Bind(wx.EVT_BUTTON, self.OnReadClick, self.readButton)
        self.readButton.SetDefault()

        self.selectButton = wx.Button(panel, -1, selectAllStr.decode('utf-8'), pos=(xPos + 120, yPoslayout))
        self.Bind(wx.EVT_BUTTON, self.OnSelectAllClick, self.selectButton)
        self.selectButton.SetDefault()

        self.unselectButton = wx.Button(panel, -1, cancelAllStr.decode('utf-8'), pos=(xPos + 120 * 2, yPoslayout))
        self.Bind(wx.EVT_BUTTON, self.OnUnselectClick, self.unselectButton)

        self.defaultButton = wx.Button(panel, -1, defaultParamsStr.decode('utf-8'), pos=(xPos, yPoslayout + yDelta))
        self.Bind(wx.EVT_BUTTON, self.OnResetClick, self.defaultButton)
        self.defaultButton.SetDefault()

        self.quickButton = wx.Button(panel, -1, hotMonkeyStr.decode('utf-8'), pos=(xPos + 120, yPoslayout + yDelta))
        self.Bind(wx.EVT_BUTTON, self.OnQuickStartClick, self.quickButton)
        self.quickButton.SetDefault()

        self.doButton = wx.Button(panel, -1, startMonkeyStr.decode('utf-8'), pos=(xPos + 120 * 2, yPoslayout + yDelta))
        self.Bind(wx.EVT_BUTTON, self.OnStartClick, self.doButton)
        self.doButton.SetDefault()

        self.logButton = wx.Button(panel, -1, execLogStr.decode('utf-8'), pos=(xPos, yPoslayout + 2 * yDelta))
        self.Bind(wx.EVT_BUTTON, self.OnBuildLog, self.logButton)
        self.logButton.SetDefault()

        self.quickWifiButton = wx.Button(panel, -1, hotMonkeyWifiStr.decode('utf-8'),
                                         pos=(xPos + 120, yPoslayout + 2 * yDelta))
        self.Bind(wx.EVT_BUTTON, self.OnQuickWifi, self.quickWifiButton)
        self.quickWifiButton.SetDefault()

        self.stopButton = wx.Button(panel, -1, stopMonkeyStr.decode('utf-8'),
                                    pos=(xPos + 120 * 2, yPoslayout + 2 * yDelta))
        self.Bind(wx.EVT_BUTTON, self.OnStop, self.stopButton)
        self.stopButton.SetDefault()

    def OnQuickWifi(self, event):
        self.Reset()
        self.StartCmd(" -p mobi.wifi.toolbox")

    def OnStop(self, event):
        os.system("adb shell ps | grep monkey > c:/temp.txt")
        f = open("c:/temp.txt", 'r')
        line = f.readline()
        if (line != ""):
            cmd = "adb shell kill " + line.strip().split()[1]
            print("****" + cmd + "****")
            os.system(cmd)
        f.close()

    def OnAction(self, event):
        value = self.seedCtrl.GetValue().strip()
        if all(x in '0123456789' for x in value):
            print
            value
            self.seedCtrl.SetValue(str(self.seedCtrl.GetValue()))

    def OnQuickStartClick(self, event):
        self.Reset()
        self.StartCmd("")

    def OnSelectAllClick(self, event):
        listString = self.checkListBox
        count = listString.GetCount()
        array = []
        for i in range(0, count):
            array.append(i)
        listString.SetChecked(array)

    def OnUnselectClick(self, event):
        self.checkListBox.SetChecked([])

    def OnResetClick(self, event):
        self.Reset()

    def OnReadClick(self, event):
        self.checkListBox.Clear()
        os.system("adb shell pm list packages > D:/log.log")
        home = 'd:'
        f = open(home + "/log.log", 'r')
        line = f.readline()
        while line:
            line = f.readline()
            if (line != ""):
                line = line.split(':')[1]
                print
                "====" + line
                self.checkListBox.Append(line)
        f.close()

    def OnStartClick(self, event):
        self.StartCmd("")

    def Reset(self):
        self.ListFiles("/sdcard/mtklog")
        self.seedCtrl.SetValue(self.seedDefault)
        self.excuteNumCtrl.SetValue(self.executionFrequencyDefault)
        self.delayNumCtrl.SetValue(self.delayDefault)
        self.excuteModeCtrl.SetSelection(5)
        self.logModeCtrl.SetSelection(0)
        self.excutePacageCtrl.SetSelection(0)

    def StartCmd(self, pacageName):

        seed = self.seedCtrl.GetValue()
        excuteNum = self.excuteNumCtrl.GetValue()
        delayNum = self.delayNumCtrl.GetValue()
        excuteMode = self.excuteModeCtrl.GetValue()
        date = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
        listString = self.checkListBox

        package_section = ""
        package_list = listString.GetCheckedStrings()
        print
        "select package count:" + str(len(package_list))
        for i in range(0, len(package_list)):
            print
            package_list
            package = package_list[i]
            pack = package.strip('\r\n')
            package_section += (" -p " + pack)

        print
        package_section.decode('utf-8')

        seed_section = " -s " + self.seedCtrl.GetValue()
        delay_section = " --throttle " + delayNum
        log_section = ""
        mode_section = ""

        log_id = self.logModeCtrl.GetSelection()
        if (log_id == 0):
            log_section += " -v"
        elif (log_id == 1):
            log_section += " -v -v"
        elif (log_id == 2):
            log_section += " -v -v -v"

        mode_id = self.excuteModeCtrl.GetSelection()
        mode = [" --ignore-crashes ",
                " --ignore-timeouts ",
                " --ignore-security-exceptions ",
                " --ignore-native-crashes ",
                " --monitor-native-crashes "]
        if (mode_id == 0):
            mode_section = mode[0]
        elif (mode_id == 1):
            mode_section = mode[1]
        elif (mode_id == 2):
            mode_section = mode[2]
        elif (mode_id == 3):
            mode_section = mode[3]
        elif (mode_id == 4):
            mode_section = mode[4]
        else:
            mode_section = mode[0] + mode[1] + mode[2] + mode[3] + mode[4]
        ##############   create monkey log dir ###############

        # usr_home = os.path.expanduser('~')
        # os.chdir(usr_home)
        logDir = "c:\MonkeyLog_" + date
        # os.system("mkdir "+logDir)
        self.logDir = logDir.decode('utf-8')
        print
        self.logDir
        # os.chdir(logDir)
        ###############  record monkey trace ################


        if (pacageName != ""):
            package_section = pacageName
        elif (self.excutePacageCtrl.GetSelection() != ""):
            package_section = " -p " + self.pacegeMode[self.excutePacageCtrl.GetSelection()]
        print
        "package_section " + package_section

        monkeyCmd = "adb shell monkey "
        monkeyCmd = monkeyCmd + delay_section + seed_section + package_section + log_section + mode_section
        monkeyCmd = monkeyCmd + " " + excuteNum + " > c:/trace.log_" + date
        print
        monkeyCmd
        os.system(monkeyCmd)
        # adb shell monkey  --throttle 2 -s 5000000 -v -v -v --ignore-crashes  --ignore-timeouts  --ignore-security-exceptions  --ignore-native-crashes  --monitor-native-crashes  60000000 > trace.log
        # adb shell monkey  --throttle 2 -s 5000000 mobi.wifi.toolbox -v -v -v --ignore-crashes  --ignore-timeouts  --ignore-security-exceptions  --ignore-native-crashes  --monitor-native-crashes  60000000 > trace.log
        # adb shell monkey  --throttle 2 -s 5000000 mobi.wifi.toolbox -v -v -v --ignore-crashes  --ignore-timeouts  --ignore-security-exceptions  --ignore-native-crashes  --monitor-native-crashes  60000000 > trace.log
        # adb shell monkey  --throttle 2 -s 5000000 -p mobi.wifi.toolbox -v -v -v --ignore-crashes  --ignore-timeouts  --ignore-security-exceptions  --ignore-native-crashes  --monitor-native-crashes  60000000 > trace.log

    def ListFiles(self, path):
        for root, dirs, files in os.walk(path):
            log_f = ""
            for f in files:
                if (f.find("main") == 0):
                    log_f = f.strip()
                    os.chdir(root)
                    if (log_f != ""):
                        grep_cmd = "grep -Eni -B20 -A20 'FATAL|error|exception|system.err|androidruntime' " + log_f + " > " + log_f + "_fatal.log"
                        os.system(grep_cmd)
        print
        "--------------finish build log-----------------"

    # com.xixi.leakcanary
    # adb shell monkey  --throttle 2 -s 5000000 -p com.xixi.leakcanary -v -v -v --ignore-crashes  --ignore-timeouts  --ignore-security-exceptions  --ignore-native-crashes  --monitor-native-crashes  6000 > c:/trace1.log
    def BuildFatalLog(self, path):
        self.ListFiles(path)

    def OnBuildLog(self, event):
        os.chdir(self.logDir)
        print
        self.logDir
        date = time.strftime('%Y-%m-%d-%H-%M', time.localtime(time.time()))
        dir_m = "Monkey_Log_" + date.replace("-", "")
        dir0 = "sdcard0_mtklog"
        dir1 = "sdcard1_mtklog"

        if (os.path.exists(dir_m + "/" + dir0)):
            print
            "already exists"
        else:
            os.system("mkdir -p " + dir_m + "/" + dir0)

        if (os.path.exists(dir_m + "/" + dir1)):
            print
            "already exists"
        else:
            os.system("mkdir -p " + dir_m + "/" + dir1)

        os.chdir(dir_m)
        os.system("adb pull /storage/sdcard0/mtklog/ " + dir0)
        os.system("adb pull /storage/sdcard1/mtklog/ " + dir1)
        self.BuildFatalLog(os.getcwd())


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    frame.Show(True)
    app.MainLoop()