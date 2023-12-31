from tkinter import *
from tkdial import *
import time, math

torpedo_list = [
    "Type 1",
    "Type 2"
]

torpedo_speed = {
    "Type 1": 40,
    "Type 2": 60
}



root = Tk()
root.title("Computer")
root.attributes('-alpha', 0.75)
root.attributes('-topmost', True)

# == Functions ==

def torpedo_velocity (torpedo_name):
    return torpedo_speed[torpedo_name]
    

def gyro_calculate(gyro_box, impact_dial, torpedo_v, bearing_angle, bow_angle, target_v):
    defl = math.asin( (float(target_v) / float(torpedo_v)) * math.sin( math.radians(float(bow_angle)) ) )
    defl = round(math.degrees(defl),2)
    print(f"Deflection Angle: {defl}")
    gyro_box.delete(0, END)
    gyro_box.insert(0, str(float(bearing_angle) - defl))
    impact_dial.set(float(bow_angle) + defl)


# == Element Setups ==
left_dial = Meter(root, fg="#242424", radius=250, start=180, end=-180,
               major_divisions=30, minor_divisions=3, border_width=0, text_color="white",
               start_angle=270, end_angle=360, scale_color="white", axis_color="cyan",
               needle_color="white",  scroll_steps=3)
left_dial.set(0)


torpedo_type_lab = Label(master=root, text="Torpedo")
torpedo_var = StringVar(root)
torpedo_var.set(torpedo_list[0])
torpedo_box = OptionMenu(root, torpedo_var, *torpedo_list)

target_v_lab = Label(master=root, text="Target Velocity")
target_v_box = Entry(root)

bearing_angle_lab = Label(master=root, text="Bearing Angle")
bearing_angle_box = Entry(root)

bow_angle_lab = Label(master=root, text="Angle Off Bow")
bow_angle_box = Entry(root)


impact_dial = Meter(root, fg="#242424", radius=250, start=180, end=-180,
               major_divisions=30, minor_divisions=3, border_width=0, text_color="white",
               start_angle=270, end_angle=360, scale_color="white", axis_color="cyan",
               needle_color="white",  scroll_steps=3)
impact_dial.set(0)

time_lab = Label(master=root, text="Time On Target")
time_box = Entry(root)

periscope = Button(master=root, text="Periscope Slaving")


gyro_lab = Label(master=root, text="Gyro")
gyro_box = Entry(root)
gyro_button = Button(master=root, text="Calculate", command=lambda: gyro_calculate(gyro_box, impact_dial, torpedo_velocity(torpedo_var.get()), bearing_angle_box.get(), bow_angle_box.get(), target_v_box.get()))

# == Layouts ==
left_dial.grid(row=0, column=1, rowspan=4, pady=5)

gyro_lab.grid(row=0, column = 2)
gyro_box.grid(row=0, column = 3)
gyro_button.grid(row=1, column=2, columnspan=2, sticky=N)

torpedo_type_lab.grid(row = 0, column = 4, sticky=N)
torpedo_box.grid(row = 0, column = 5, sticky=N)
target_v_lab.grid(row = 1, column = 4, sticky=N)
target_v_box.grid(row = 1, column = 5, sticky=N)
bearing_angle_lab.grid(row = 2, column = 4, sticky=N)
bearing_angle_box.grid(row = 2, column = 5, sticky=N)
bow_angle_lab.grid(row = 3, column = 4, sticky=N)
bow_angle_box.grid(row = 3, column = 5, sticky=N)

impact_dial.grid(row=4, column=1, pady=7)
time_lab.grid(row=4, column=2)
time_box.grid(row=4, column=3)
periscope.grid(row=4, column=4, columnspan=2)
"""
window = tk.Toplevel(root)
window.title("Bearing")
window.attributes('-alpha', 0.75)
window.attributes('-topmost', True)

bearing_angle = tk.StringVar(master=window, value="Bearing: -")
bearing = tk.Label(master=window, textvariable=bearing_angle)
bearing.pack()

def update_bearing(val):
    bearing_angle.set(360 - val)

dial = tkd.Dial(master=window, start=0, end=360, scroll_steps=2, radius=100, command=lambda: update_bearing(dial.get()))
dial.set(20)
dial.pack()
"""

root.mainloop()
