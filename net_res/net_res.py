# import  modules
try:
    from ftplib import FTP
    import configparser
    from pymsgbox import *
    import time
    import matplotlib.pyplot as plt
    from pythonping import ping
    import os
    from win10toast import ToastNotifier
except:
    n=1

def dev():
    print("Stub for developing applications")
    input()

def graph_ping():
    target_link=str(input("Enter URL, or IP-adress to ping: "))
    time_sec=int(input("How long we must ping this URL? (sec): "))
    time_msec=time_sec*1000
    if time_sec%2!=0:
        time_sec+=1
    counter=int(time_sec/2)
    grid_ans=str(input("Do you want to get grid on your graph? [True/False]: "))
    print("If server did not response in 2000 msec, in graph you will see '-1'.")

    # set graph settings
    graph_title="Ping graph of "+target_link
    plt.title(graph_title)
    xlabel_name="Time, sec"
    ylabel_name="Server response time, msec"
    plt.xlabel(xlabel_name)
    plt.ylabel(ylabel_name)
    plt.grid(grid_ans)

    # pinging
    resp_time=[]
    while counter!=0:
        response=ping(target=target_link, count=1, timeout=2)
        rsptime=int(round(response.rtt_avg_ms, 0))
        if rsptime<2000:
            resp_time.append(rsptime)
        if rsptime==2000:
            resp_time.append('-1')
        counter-=1
        time.sleep(1)
    print(resp_time)

    # get time list
    time_list=[ ]
    cntr=0
    while time_sec!=0:
        time_list.append(cntr)
        cntr+=2
        time_sec-=2
    print(time_list)
    plt.plot(time_list, resp_time)
    plt.show()

def ftpmonitor():
    # config reader
    # the input is a file with settings, in which the internal folders are spelled out with commas
    # we split this line into a list, which we will follow and enter into the desired internal directory
    config=configparser.ConfigParser(comment_prefixes=';', inline_comment_prefixes=';') # config file param
    config.read("ftp_settings.ini") # open config file
    hosturl=config.get('ftp_param', 'host')
    folder_list=config.get('ftp_param', 'folder')
    ftplogin=config.get('ftp_param', 'login')
    ftppassword=config.get('ftp_param', 'password')
    tmemon=int(config.get('main', 'tmemon'))
    folder_list=folder_list.split(",")
    folders_number=len(folder_list)

    #ftp set-up
    ftp=FTP(hosturl)
    try:
        ftp.login()
    except:
        ftp.login(ftplogin, ftppassword)
    try:
        for folder_name in folder_list:
            ftp.cwd(folder_name)
    except:
        print("FTP error")
        input()
        exit(0)
    data_launch = ftp.nlst()

    # notification set-up
    def show_alert():
        alert(text='Feature is not ready for use', title='Warning', button='OK') #не обязательно
    toaster = ToastNotifier()

    # output text
    print("Welcome to FTP Manager!")
    print("Before you start using the program, have you checked the settings.ini file? If yes, then enter 'y', if not, then 'n'")
    checker=str(input())
    if checker=='n' :
        print("Check your settings.ini file. Back to main menu.")
        time.sleep(3)
        raise SystemExit('Check your settings.ini file')
    if checker=='y':
            # file monitoring
        print("Press CTRL+C for stop monitoring")
        n=5
        while n>0:
            try:
                data = ftp.nlst()
                if data != data_launch:
                    toaster.show_toast("FTP Manager", #title
                            "Some files has been updated. Click to view.", #description
                            duration=1,
                            callback_on_click=show_alert)
                    data_launch=data
                    time.sleep(tmemon)
            except KeyboardInterrupt:
                break
    else:
        print("Invalid input. Back to main menu.")
        time.sleep(3)
        raise SystemExit('Invalid input.')
    input()