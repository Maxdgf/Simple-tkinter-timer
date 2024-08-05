import tkinter as tk
from tkinter import *

class TimerApp:
    def __init__(self, master):
        self.master = master
        master.title("Easy Timer")
        master.geometry("800x800")

        self.label = tk.Label(master, text="Easy Timer", font=("Arial", 30))
        self.label.pack()
        
        #self.description_label = tk.Label(master, text="input minutes here:")
        #self.description_label.pack(pady=30)
        
       # self.time_scale = tk.Scale(master, orient="horizontal", from_=0, to=1000)
        #self.time_scale.pack()
        
        #self.time_input = tk.Entry(master, width=30)
        #self.time_input.pack(pady=20)
        
        #self.time_data = self.time_input.get()
        #self.time_int = int(self.time_data)
        #self.time_left = self.time_int()
        self.time_left = 60
        self.time_function = self.format_time(self.time_left)
        self.running = False
        
        #self.apply_button = tk.Button(master, width=30, bg="yellow", text="apply")
        #self.apply_button.pack()

        self.time_label = tk.Label(master, text=self.time_function, font=("Impact", 50))
        self.time_label.pack(pady=200)

        self.start_button = tk.Button(master, text="Start", command=self.start_timer, width=10, bg="green")
        self.start_button.pack()

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_timer, width=10, bg="red")
        self.stop_button.pack()

        self.reset_button = tk.Button(master, text="Destroy", command=self.reset_timer, width=10, bg="orange")
        self.reset_button.pack()
        
        self.exit_button = tk.Button(master, text="exit", bg="red", command=self.exit_app)
        self.exit_button.place(x=0, y=0)
    

    def format_time(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        return f"{minutes:02}:{seconds:02}"

    def update_timer(self):
        if self.running:
            if self.time_left > 0:
                self.time_left -= 1
                self.time_label.config(text=self.format_time(self.time_left))
                self.master.after(1000, self.update_timer) 
            else:
                self.stop_timer()

    def start_timer(self):
        if not self.running:
            self.running = True
            self.update_timer()

    def stop_timer(self):
        self.running = False

    def reset_timer(self):
        self.stop_timer()
        self.time_left = 0 
        self.time_label.config(text=self.format_time(self.time_left))
        
    def exit_app(self):
    	root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    timer_app = TimerApp(root)
    root.mainloop()
