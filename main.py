import tkinter
import tkinter as tk
import tkinter.messagebox as mb


class SampleApp(object) :
    def __init__(self, master) :
        self._master = master
        master.title("Hello!")
        master.minsize(430, 200)

        self._lbl = tk.Label(master, text="Choose a button")
        self._lbl.pack(side=tk.TOP,expand=True)

        btn_frame = tk.Frame(master)
        btn_frame.pack(side=tk.TOP,padx= 10)

        entry_frame = tk.Frame(master)
        entry_frame.pack(side=tk.BOTTOM, padx=10, pady=10)

        blue_btn = tk.Button(btn_frame, text="Change to Blue", command=self.blue_label)
        blue_btn.pack(side=tk.LEFT)

        green_btn = tk.Button(btn_frame, text="Change to Green", command=self.green_label)
        green_btn.pack(side=tk.LEFT)


        entry_label = tk.Label(entry_frame, text='Change the colour to: ')
        entry_label.pack(side=tk.LEFT)


        self.clr_entry = tk.Entry(entry_frame)
        self.clr_entry.pack(side=tk.LEFT)

        changeIt_btn = tk.Button(entry_frame, text="Change It!",command=self.change_it)
        changeIt_btn.pack(side=tk.LEFT)



    def change_it(self):
        color = self.clr_entry.get()
        try:
            self._lbl.config(text=f'The label is {color}', background=color)
            self._lbl.pack(side=tk.TOP)
        except tkinter.TclError:
            mb.showerror(title='Invalid colour',message=f'{self.clr_entry.get()} is not a colour')


    def green_label(self):
        self._lbl.config(text='The label is green',background='green')
        self._lbl.pack(side=tk.TOP)

    def blue_label(self):
        self._lbl.config(text='The label is blue', background='blue')
        self._lbl.pack(side=tk.TOP)

    def say_hello(self) :
        print('Hello! Thanks for clicking!')


if __name__ == "__main__" :
    root = tk.Tk()
    app = SampleApp(root)
    root.mainloop()