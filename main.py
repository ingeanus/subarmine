import tkinter as tk
import tkdial as tkd
import time, math

root = tk.Tk()
root.title("Computer")
root.attributes('-alpha', 0.75)
root.attributes('-topmost', True)

target_v_lab= tk.Label(master=root, text="Target Velocity")
target_v = tk.Entry(master=root)
target_v_lab.pack()
target_v.pack()
torpedo_v_lab= tk.Label(master=root, text="Torpedo Velocity")
torpedo_v = tk.Entry(master=root)
torpedo_v_lab.pack()
torpedo_v.pack()
bow_angle_lab = tk.Label(master=root, text="Bow Angle")
bow_angle = tk.Entry(master=root)
bow_angle_lab.pack()
bow_angle.pack()
deflection_angle = tk.StringVar(master=root, value="Deflection Angle: -")
deflection_angle_lab = tk.Label(textvariable=deflection_angle)
deflection_angle_lab.pack()

def create_circle(x, y, r): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    canvas.create_oval(x0, y0, x1, y1)

canvas = tk.Canvas(master=root, width=200, height=200)
create_circle(100,100,75)
canvas.pack()

def handle_click(label):
    target_val = float(target_v.get())
    bow_val = float(bow_angle.get())
    torpedo_val = float(torpedo_v.get())
    defl = math.acos( (torpedo_val * math.cos(bow_val * math.pi/180)) / target_val ) * 180/math.pi
    label.set(f"Deflection Angle: {defl}")

    x = math.cos(defl * math.pi/180)
    y = math.sin(defl * math.pi/180)
    print((x,y))
    angle = [100,100, math.floor(100+x*75),math.floor(100-y*75)]
    print(angle)
    canvas.create_line(angle, fill="black")
    canvas.create_line([100,100, 175,100], fill="black")
    
calculate = tk.Button(master=root, text="Calculate", command=lambda: handle_click(deflection_angle))
calculate.pack()

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

root.mainloop()
