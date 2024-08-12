
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from datetime import datetime as _dt
from datetime import timedelta



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\ronro\Documents\Coding\VisualStudio\Python\Prigects\WorkCalender\build\assets\frame0")

date = _dt.today()

def change_mid_text(new_text, is_error=False):
    """Updates the mid label text."""
    canvas.itemconfig((11,), text=new_text, fill="red" if is_error else "black") 
    print(f"Updated mid label text to: {new_text}")

def on_press_next():
    """move to the next day"""
    global date
    date += timedelta(days=1)
    target_text = canvas.find_withtag("target_text")  # Find the text element with the tag
    canvas.itemconfig(target_text, text=date.strftime("%a %d/%m")) 
    change_mid_text("Moved to next day")

def on_press_prev():
    """move a day back"""
    global date
    date -= timedelta(days=1)
    # target_text =  (11,)#canvas.find_withtag("target_text")  # Find the text element with the tag
    canvas.itemconfig((11,), text=date.strftime("%a %d/%m")) 
    change_mid_text("Moved to previous day")

def check_input(time_start, time_end):
    if time_start == "" or time_end == "":
        change_mid_text("Please enter both start and end times", True)
        return 0
    elif not time_start.replace(":", "").isdigit() or not time_end.replace(":", "").isdigit():
        change_mid_text("Please enter only numbers", True)
        return 0
    else: return 1

def procces_time_format(time_start, time_end):
    """Processes the time format and returns the format to be entered in the database.
    in this format: (startTime, endTime).
    if there is a format or numerical value error, returns (None, None)
    and sets mid label to error message"""
    
    times = [time_start, time_end]
    times.reverse()
    to_return = [None, None]
    for i, time in enumerate(times):
        if ":" in time:
            hour = time[:-3]
            min = time[-2:]
            if int(hour) >= 0 and int(hour) <= 25:
                if int(min) >= 0 and int(min) < 60:
                    to_return[i] = time
                else:
                    """whay to do if minutes enters are invalid"""
                    change_mid_text(f"{'Start time Eroor: ' if i == 1 else 'End time eroor: '}Invalid minutes entered\n    Please enter a number between 00 and 59", True)
                    to_return[i] = None
            else:
                """whay to do if hours enters are invalid"""
                change_mid_text(f"{'Start time Eroor: ' if i == 1 else 'End time eroor: '}Invalid hours are entered\n    Please enter an hour between 0 and 25", True)
                to_return[i] = None
        elif len(time) == 3 or len(time) == 4:
            hour = time[:-2]
            min = time[-2:]
            print(hour, min)
            if int(hour) >= 0 and int(hour) <= 25:
                if int(min) >= 0 and int(min) < 60:
                    to_return[i] = f"{hour[1:]}:{min}" if hour[0] == "0" else f"{hour}:{min}"
                else:
                    """whay to do if minutes enters are invalid"""
                    change_mid_text(f"{'Start time Eroor: ' if i == 1 else ' End time eroor: '}Invalid minutes entered\nPlease enter a number between 00 and 59", True)
                    to_return[i] = None
            else:
                """whay to do if hours enters are invalid"""
                change_mid_text(f"{'Start time Eroor: ' if i == 1 else 'End time eroor: '}Invalid hours are entered\n   Please enter an hour between 0 and 25", True)
                to_return[i] = None
        elif len(time) == 0:
            return (False, None)
        elif len(time) != 3 and len(time) != 4: 
            change_mid_text(f"{'Start time Eroor: ' if i == 1 else 'End time eroor: '}Invalid time entered.\nPlease enter between 3 and 4 numbers in total", True)
            to_return[i] = None
        else:
            change_mid_text(f"{'Start time Eroor: ' if i == 1 else 'End time eroor: '}Invalid time entered. Please enter only numbers and ':' in this format: HH:MM", True)
            to_return[i] = None
    
    return to_return

def on_press_submit():
    time_start = entry_1.get()
    time_end = entry_2.get()
    check = check_input(time_start, time_end)
    if check:
        time_start_toEnter, time_end_toEnter = procces_time_format(time_start, time_end)
        if time_start_toEnter != None and time_end_toEnter != None:
            """ if evrything is OK """
            print(f"Time start: {time_start_toEnter}, Time end: {time_end_toEnter}")
            entry_1.delete(0, 999)
            entry_2.delete(0, 999)
            change_mid_text(f"Added a new working day from: {time_start_toEnter} to: {time_end_toEnter}")
        else: 
            """ if there is an error """
            print("There is an error")
    else: 
        """ if there is an error """
        print("There is an error")

def update_text_on_button_click():
    """Updates the text of the target text element to 'No' when clicked."""
    target_text = canvas.find_withtag("target_text")  # Find the text element with the tag
    canvas.itemconfig(target_text, text="No") 

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.title("WorkCal")
window.geometry("800x500")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 500,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)

#Logo Banner
canvas.create_rectangle(
    0.0,
    0.0,
    800.0,
    100.0,
    fill="#17153B",
    outline="")

#Logo Name
canvas.create_text(
    26.0,
    23.0,
    anchor="nw",
    text="WorkCal",
    fill="#FFFFFF",
    font=("Ubuntu Bold", 48 * -1)
)

#Date
canvas.create_text(
    400.0,
    150.0,
    anchor="center",
    text=date.strftime("%a %d/%m"),  # Replace with the text variable if needed
    fill="#000000",
    font=("Ubuntu Bold", 48 * -1),
    tag="target_text",  # Assign a unique tag for easy reference
)

#From
canvas.create_text(
    285.0,
    208.0,
    anchor="nw",
    text="From:",
    fill="#000000",
    font=("Ubuntu Bold", 28 * -1)
)

#To
canvas.create_text(
    304.0,
    254.0,
    anchor="nw",
    text="To:",
    fill="#000000",
    font=("Ubuntu Bold", 28 * -1)
)

#Purpule rec, enter 1
image_image_1 = PhotoImage(
    file="build/assets/image_1.png")
image_1 = canvas.create_image(
    444.0,
    226.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file="build/assets/image_2.png")
image_2 = canvas.create_image(
    444.0,
    226.0,
    image=image_image_2
)


entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    font=("Ubuntu Regular", 24 * -1),
    highlightthickness=0
)
entry_1.place(
    x=385.5,
    y=214.0,
    width=105.0,
    height=22.0
)

#purple rec, enter 2
image_image_3 = PhotoImage(
    file="build/assets/image_3.png")
image_3 = canvas.create_image(
    444.0,
    269.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file="build/assets/image_4.png")
image_4 = canvas.create_image(
    444.0,
    269.0,
    image=image_image_4
)

entry_image_2 = PhotoImage(
    file="build/assets/entry_2.png")
entry_bg_2 = canvas.create_image(
    444.0,
    268.5,
    image=entry_image_2
)

entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    font=("Ubuntu Regular", 24 * -1),
    highlightthickness=0
)
entry_2.place(
    x=385.5,
    y=258.0,
    width=105.0,
    height=22.0
)

#Mid label
canvas.create_text(
    400.0,
    320.0,
    anchor="center",
    text="",
    fill="#000000",
    tag="mid_text",
    font=("Ubuntu Bold", 26 * -1)
)

button_image_1 = PhotoImage(
    file="build/assets/button_1.png")
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [print("button_1 clicked"), canvas.itemconfig((11,), text=""), on_press_submit()],
    relief="flat"
)
button_1.place(
    x=345.0,
    y=366.0,
    width=110.0,
    height=30.55555534362793
)

button_image_2 = PhotoImage(
    file="build/assets/button_2.png")
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [print("button_2 clicked"), canvas.itemconfig((11,), text=""), on_press_next(), entry_1.delete(0, 999), entry_2.delete(0, 999)],
    relief="flat"
)
button_2.place(
    x=428.0,
    y=410.0,
    width=81.0,
    height=26.0
)

button_image_3 = PhotoImage(
    file="build/assets/button_3.png")
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [print("button_3 clicked"), canvas.itemconfig((11,), text=""), on_press_prev(), entry_1.delete(0, 999), entry_2.delete(0, 999)],
    relief="flat"
)
button_3.place(
    x=287.0,
    y=410.0,
    width=110.0,
    height=26.0
)

button_image_4 = PhotoImage(
    file="build/assets/button_4.png")
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command= lambda: [print("button_4 clicked"), canvas.itemconfig((11,), text="")],
    relief="flat",
)
button_4.place(
    x=366.0,
    y=451.0,
    width=68.0,
    height=24.0,
)

window.resizable(False, False)
window.mainloop()
