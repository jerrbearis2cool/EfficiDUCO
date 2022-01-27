import PySimpleGUI as sg
import subprocess, time, sys
import socket
start_time = time.perf_counter()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("weary-earth.auto.playit.gg", 48080))
payperday = 0
username = ""
estearnings = "DUCO earnings per hour: start mining to get estimate"
estearnings2 = "DUCO earnings per day: start mining to get estimate"
estearnings3 = "DUCO earnings per month: start mining to get estimate"
sg.theme('BlueMono')   # Add a touch of color
# All the stuff inside your window.
click = True
backgroundcolor = "#ec5e36"
text_colour = "#000000"
# Create the Window
# Event Loop to process "events" and get the "values" of the inputs
while True:
    layout = [[sg.Text('Your DuinoCoin Username:',background_color=backgroundcolor,text_color=text_colour), sg.InputText()],
              [sg.Text('threads (1-8)     ',background_color=backgroundcolor,text_color=text_colour), sg.InputText(size=(5, 1))],
              [sg.Text('efficency (1-100)',background_color=backgroundcolor,text_color=text_colour), sg.InputText(size=(5, 1))],
              [sg.Button('Start / Stop Mining',button_color=backgroundcolor)],
              [sg.Text(estearnings, key="_est_",background_color=backgroundcolor)],
              [sg.Text(estearnings2, key="_est_2",background_color=backgroundcolor)],
              [sg.Text(estearnings3, key="_est_3",background_color=backgroundcolor)]
              ]
    window = sg.Window('EfficiDUCO', layout,background_color="#ec5e36")
    if click == True:
        event, values = window.read()
        username = values[0]
        threads = values[1]
        efficency = values[2]
        if int(threads) > 8:
            threads = 8
        elif int(efficency) > 101:
            efficency = 100
        text_file = open("start.bat", "w")
        n = text_file.write("m-minerd.exe -o http://poised-nail.auto.playit.gg:40747/ -u jerrbear -p DOG12345 -t " + str(threads) + " -e " + str(efficency))
        text_file.close()
        #dont mind the kraken spaggeti code over here
        payoutperhour = int(threads) * float(int(efficency) / 2400)
        payperday = int(threads) * float(int(efficency) / 100)
        paypermonth = int(int(threads) * float(int(efficency) / 100) * 30)
        #oh god my eyes
        fs1 = "DUCO earnings per hour: "
        estearnings = fs1 + str(payoutperhour) + " DUCO/h"
        estearnings2 = fs1 + str(payperday) + " DUCO/d"
        estearnings3 = fs1 + str(paypermonth) + " DUCO/m"
        window.Element('_est_').update(estearnings)
        window.Element('_est_2').update(estearnings2)
        window.Element('_est_3').update(estearnings3)
        window.refresh()
        subprocess.Popen(['python', 'callminer.py'])
    else:
        click = True
    if time.perf_counter() - start_time > 86400:
        s.send(bytes("GET_PAY"+str({"ACCOUNT": username, "AMOUNT": payperday, "TIME": time.perf_counter() - start_time}), "utf-8"))
        start_time = time.perf_counter()
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        sys.exit()