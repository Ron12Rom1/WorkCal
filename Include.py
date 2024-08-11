import tkinter as tk
import calendar
from datetime import datetime as _dt
from datetime import timedelta

date_now = _dt.today()
date = date_now

def process_input(input):
    """
    if OK retrun [0] = False [1] = The time inputed
    elif empty day return [0] = False [1] = None
    else return [0] = True [1] = Error message
    """
    if ":" in input:
        hour = input[:-3]
        min = input[-2:]
        if int(hour) >= 0 and int(hour) < 25:
            if int(min) >= 0 and int(min) < 60:
                return (False, input)
            else:
                """whay to do if minutes enters are invalid"""
                return (True, "Invalid minute are entered\nPlease enter a number between 00 and 59")
        else:
            """whay to do if hours enters are invalid"""
            return (True, "Invalid hours are entered\nPlease enter an hour between 0 and 25")
    elif len(input) == 3 or len(input) == 4:
        hour = input[:-2]
        min = input[-2:]
        print(hour, min)
        if int(hour) >= 0 and int(hour) <= 25:
            if int(min) >= 0 and int(min) < 60:
                return (False, input)
            else:
                """whay to do if minutes enters are invalid"""
                return (True, "Invalid minute are entered\nPlease enter a number between 00 and 59")
        else:
            """whay to do if hours enters are invalid"""
            return (True, "Invalid hours are entered\nPlease enter an hour between 0 and 25")
    elif len(input) == 0:
        return (False, None)
    elif len(input) != 3 and len(input) != 4: 
        return (True, "Invalid time entered.\nPlease enter between 3 and 4 numbers in total")
    else:
        return (True, "Invalid time entered. Please enter only numbers and ':' in this format: HH:MM")

def add_to_database(date, in1, in2, entrys):
    mid_label["text"] = ""
    global enter1, enter2
    if ":" not in in1:
        enter1 = str(in1[:-2]) + ":" + str(in1[-2:])
    else: enter1 = in1
    if ":" not in in2:
        enter2 = str(in2[:-2]) + ":" + str(in2[-2:])
    else: enter2 = in2

    if enter1[0] == "0": enter1 = enter1[1:]
    if enter2[0] == "0": enter2 = enter2[1:]

    entrys.append((date, enter1, enter2))
    mid_label["text"] = ("Added a working day from " + str(enter1) + " to " + str(enter2))
    print("Added a working day from ")

def on_press_submit():
    global entrys
    global date
    entrys = []

    mid_label["text"] = ""
    startTime_entry = start_entry.get()
    startTime_entry = process_input(startTime_entry)
    endTime_entry = end_entry.get()
    endTime_entry = process_input(endTime_entry)

    print(startTime_entry, endTime_entry)

    if startTime_entry[0] == False and endTime_entry[0] == False:
        start_entry.delete(0, tk.END)
        end_entry.delete(0, tk.END)
        if startTime_entry[1] == None and endTime_entry[1] == None:
            mid_label["text"] = "Added an empty day"
        elif not(startTime_entry[0]) and not(endTime_entry[0]):
            add_to_database(date.strftime("%Y-%m-%d"), startTime_entry[1], endTime_entry[1], entrys)
        # elif startTime_entry[1] == "" and endTime_entry[1] == "":
        #     mid_label["text"] = "Added an empty day"
        date += timedelta(days=1)
        time_label_2["text"] = str(date.strftime("%a") + " - "+ str(date.strftime("%d/") + str(date.month)))
        print(entrys)
        error_label["text"] = ""
    else:
        error_message = ""
        if startTime_entry[1][0] == 'I':
            print("Herer 2")
            error_message = "Start time: " + str(startTime_entry[1])
        elif endTime_entry[1][0] == 'I':
            error_message = "End time: " + str(endTime_entry[1])
        error_label["text"] = error_message
        mid_label["text"] = ""



def on_press_prev():
    global date
    date -= timedelta(days=1)
    time_label_2["text"] = str(date.strftime("%a") + " - " + str(date.strftime("%d/") + str(date.month)))
    mid_label["text"] = "Went a day back"


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Time Input v1.0")
    winX, winY = 550, 200
    winW, winH = 450, 300
    root.geometry(f"{winW}x{winH}+{winX}+{winY}")  # Create a window 300x200 pixels, starting at (300, 200)
    # root.geometry(str(winW, "x", winH))  # Create a window 300x200 pixels, starting at (300, 200)


    time_label_1 = tk.Label(root, text="Enter work hours for:", font=("Arial", 18))
    time_label_1.grid(row=0, column=0, columnspan=2, sticky="n")

    time_label_2 = tk.Label(root, text=str(date.strftime("%a") + " - " + str(date.strftime("%d/") + str(date.month))), font=("Arial", 18))
    time_label_2.grid(row=1, column=0, columnspan=2, sticky="n")

    strt_text = tk.Label(root, text="From:", font=(14))
    strt_text.grid(row=5, column=0, columnspan=1, sticky="e")
    start_entry = tk.Entry(root, font=(10))
    start_entry.grid(row=5, column=1, sticky="w")

    end_text = tk.Label(root, text="To:", font=(14))
    end_text.grid(row=6, column=0, columnspan=1, sticky="e")
    end_entry = tk.Entry(root, font=(10))
    end_entry.grid(row=6, column=1, sticky="w")

    mid_label = tk.Label(root, text="", font=("arial",11))
    mid_label.grid(row=7, columnspan=2, sticky="n")

    submit_button = tk.Button(root, text="Submit", command=lambda: [on_press_submit()], font=("Arial", 10))
    submit_button.grid(row=8,column=1, columnspan=2, sticky="w")
    previous_day = tk.Button(root, text="Previous day", command=lambda: [on_press_prev()], font=("Arial", 10))
    previous_day.grid(row=8,column=1, columnspan=2, sticky="s")

    mid_label2 = tk.Label(root, text="", font=("Arial", 6))
    mid_label2.grid(row=9)

    error_label = tk.Label(root, text="", fg="red", font=("Arial", 14))
    error_label.grid(row=10, columnspan=2)

    # button

    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)

    root.mainloop()