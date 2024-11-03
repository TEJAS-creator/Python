import pyautogui
import time
import threading
import keyboard  # For detecting key presses
from tkinter import Tk, Label, Button, Entry, StringVar

# Global variable for pause state
paused = False

def auto_clicker(points, interval, duration):
    """
    Auto-clicks at multiple points with pause/resume functionality.

    :param points: List of (x, y) tuples specifying the click positions
    :param interval: Time between clicks (in seconds)
    :param duration: Total time to run the autoclicker (in seconds)
    """
    global paused
    start_time = time.time()
    num_points = len(points)

    while time.time() - start_time < duration:
        if keyboard.is_pressed('p'):  # Press 'p' to toggle pause/resume
            paused = not paused
            time.sleep(0.5)  # Debounce time to avoid rapid toggling

        if not paused:
            for point in points:
                if keyboard.is_pressed('p'):  # Check for pause during loop
                    break
                pyautogui.click(point)
                time.sleep(interval)
                if time.time() - start_time >= duration:
                    break

def start_autoclicker():
    """
    Starts the autoclicker with parameters from the GUI.
    """
    points = [(int(coord.split(',')[0]), int(coord.split(',')[1])) for coord in click_points_var.get().split()]
    interval = float(interval_var.get())
    duration = float(duration_var.get())
    
    print(f"Starting auto-clicker with points {points}, {interval}s interval for {duration}s.")
    
    # Start the autoclicker in a new thread to keep the GUI responsive
    threading.Thread(target=auto_clicker, args=(points, interval, duration)).start()

def create_gui():
    """
    Creates a simple GUI for the autoclicker settings.
    """
    global click_points_var, interval_var, duration_var
    
    root = Tk()
    root.title("Auto Clicker")

    click_points_var = StringVar()
    interval_var = StringVar()
    duration_var = StringVar()

    Label(root, text="Click Points (x,y):").pack()
    Entry(root, textvariable=click_points_var).pack()
    Label(root, text="Interval (seconds):").pack()
    Entry(root, textvariable=interval_var).pack()
    Label(root, text="Duration (seconds):").pack()
    Entry(root, textvariable=duration_var).pack()

    Button(root, text="Start", command=start_autoclicker).pack()

    root.mainloop()

if __name__ == "__main__":
    print("Starting GUI for autoclicker configuration.")
    create_gui()
