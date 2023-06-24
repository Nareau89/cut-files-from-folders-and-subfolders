from tkinter.ttk import Frame, Style, Label, Button
from tkinter import Tk, BOTH, filedialog, W, E, S, N, messagebox
import shutil
import os
import pygame
pygame.mixer.init()
dir = os.getcwd()

class Window(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent=parent
        self.initiate()
    
    def get_sf(self):
        self.src = filedialog.askdirectory()
        return self.src
    def get_df(self):
        self.dst = filedialog.askdirectory()
        return self.dst
    def play_sound(self):
        self.dir = dir
        pygame.mixer.music.load(f"{self.dir}\\lezdoit.mp3")
        pygame.mixer.music.play()
    def transfer_files(self):
        while(True):
            try:
                src = self.src
                dst = self.dst
            except AttributeError:
                messagebox.showerror("Dude!", "source or destination folder are not assigned.")
            os.chdir(src)
            files = os.listdir(src)
            if os.path.exists(src) and os.path.exists(dst) == True:
                try:
                    for f in files :
                            if os.path.isfile(f):
                                shutil.move(f , dst)
                                print(f"""Transfering file: {f}
from {os.getcwd()} to {dst}. \n""")
                            elif os.path.isdir(f):
                                os.chdir(f)
                                sub = os.listdir()
                                for f in sub:
                                    shutil.move(f , dst)
                                    print(f"""Transfering file: {f}
from {os.getcwd()} to {dst}. \n""")
                                os.chdir(src)
                                continue
                except shutil.Error:
                    messagebox.showerror("Dude!", f"{f} already exists.")
                except AttributeError:
                    messagebox.showerror("Dude!", "source or destination folder are not assigned.")
                break
        self.play_sound()
        messagebox.showinfo("LEZDOIT", "SUCK-CESS!") 
                    
    def initiate(self):
        self.parent.title("High on File 1.1")
        self.style=Style()
        self.style.theme_use("xpnative")
        self.pack(fill=BOTH,expand=1)
        self.columnconfigure(1, weight=1)

        sfbtn=Button(self, text="SOURCE FOLDER", command=self.get_sf)
        sfbtn.grid(row=2, column=0, columnspan=5, rowspan=1, padx=5, pady=4, sticky=E+W+S+N)
        
        dfbtn=Button(self, text="DESTINATION FOLDER", command=self.get_df)
        dfbtn.grid(row=4, column=0, columnspan=5, rowspan=1, padx=5, pady=4, sticky=E+W+S+N)

        lezdoit=Button(self, text="LEZDOIT!", command=self.transfer_files)
        lezdoit.grid(row=6, column=1, columnspan=1, rowspan=1, padx=5, pady=4)
        
def main():
    gui=Tk()
    gui.geometry("300x300")
    app=Window(gui)
    gui.mainloop()

if __name__ == "__main__":
    main()