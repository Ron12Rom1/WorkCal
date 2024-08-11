from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from datetime import datetime as _dt
from datetime import timedelta



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\ronro\Documents\Coding\VisualStudio\Python\Prigects\WorkCalender\build\assets\frame0")

date = _dt.today()

def change_mid_text(new_text, is_error=False):
    """Updates the mid label text."""
    target_text = canvas.find_withtag("mid_text")  # Find the text element with the tag
    canvas.itemconfig(target_text, text=new_text) 
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
    target_text = canvas.find_withtag("target_text")  # Find the text element with the tag
    canvas.itemconfig(target_text, text=date.strftime("%a %d/%m")) 
    change_mid_text("Moved to previous day")

def update_text_on_button_click():
    """Updates the text of the target text element to 'No' when clicked."""
    target_text = canvas.find_withtag("target_text")  # Find the text element with the tag
    canvas.itemconfig(target_text, text="No") 

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("800x500")
window.title("WorkCal")
window.configure(bg="#FFFFFF")


canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=500,
    width=800,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)

canvas.place(x=0, y=0)

canvas.create_rectangle(
    0.0,
    0.0,
    800.0,
    100.0,
    fill="#17153B",

    outline="",
)

canvas.create_text(
    26.0,
    23.0,
    anchor="nw",
    text="WorkCal",
    fill="#FFFFFF",
    font=("Ubuntu Bold", 48 * -1),
)

# Target text element (can be modified to change other text elements)
canvas.create_text(
    400.0,
    150.0,
    anchor="center",
    text=date.strftime("%a %d/%m"),  # Replace with the text variable if needed
    fill="#000000",
    font=("Ubuntu Bold", 48 * -1),
    tag="target_text",  # Assign a unique tag for easy reference
)

canvas.create_text(
    285.0,
    208.0,
    anchor="nw",
    text="From:",
    fill="#000000",
    font=("Ubuntu Bold", 28 * -1),
)

canvas.create_text(
    304.0,
    254.0,
    anchor="nw",
    text="To:",
    fill="#000000",
    font=("Ubuntu Bold", 28 * -1),
)

canvas.create_rectangle(
    375.0,
    209.0,
    513.0,
    244.0,
    fill="#C8ACD6",
    outline="")

canvas.create_rectangle(
    379.0,
    214.0,
    509.0,
    239.0,
    fill="#FFFFFF",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    444.0,
    226.5,
    image=entry_image_1
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

canvas.create_rectangle(
    375.0,
    252.0,
    513.0,
    287.0,
    fill="#C8ACD6",
    outline="")

canvas.create_rectangle(
    379.0,
    257.0,
    509.0,
    282.0,
    fill="#FFFFFF",
    outline="")

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    444.0,
    269.5,
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

label_1 = canvas.create_text(
    400.0,
    320.0,
    anchor="center",
    text="test text",
    fill="#000000",
    tag="mid_text",
    font=("Ubuntu Bold", 26 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=345.0,
    y=366.0,
    width=110.0,
    height=30.55555534362793
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [print("button_2 clicked"), on_press_next()],
    relief="flat"
)
button_2.place(
    x=428.0,
    y=410.0,
    width=81.0,
    height=26.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [print("button_3 clicked"), on_press_prev()],
    relief="flat"
)
button_3.place(
    x=287.0,
    y=410.0,
    width=110.0,
    height=26.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command= lambda: [print("button_4 clicked")],
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