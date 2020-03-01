import subprocess
from tkinter import filedialog, Tk, Pack, Button
import os
import pickle

gui = Tk()
gui.geometry("450x200")
gui.title("Sonic Selector v0.2")


if not os.path.isfile("SGPath.pickle"):
    SGPath = filedialog.askopenfilename(title = "Select Sonic Generations EXE",filetypes = [("Sonic Generations", "SonicGenerations.exe SonicGenerations.fxpipeline.exe")])
    pickle_out = open("SGPath.pickle", "wb")
    pickle.dump(SGPath, pickle_out)
    pickle_out.close()
else:
    with open("SGPath.pickle", "rb") as f:
        SGPath = pickle.load(f)


if not os.path.isfile("HMMPath.pickle"):
    HMMPath = filedialog.askopenfilename(initialdir=SGPath,title = "Select Hedge Mod Manager EXE",filetypes = [("HedgeModManager", "HedgeModManager.exe")])
    pickle_out = open("HMMPath.pickle", "wb")
    pickle.dump(HMMPath, pickle_out)
    pickle_out.close()
else:
    with open("HMMPath.pickle", "rb") as f:
        HMMPath = pickle.load(f)


if not os.path.isfile("SFPath.pickle"):
    SFPath = filedialog.askopenfilename(title = "Select Sonic Forces EXE",filetypes = [("Sonic Forces", "Sonic Forces.exe")])
    pickle_out = open("SFPath.pickle", "wb")
    pickle.dump(SFPath, pickle_out)
    pickle_out.close()
else:
    with open("SFPath.pickle", "rb") as f:
        SFPath = pickle.load(f)


def HMMCallback():
    subprocess.Popen(HMMPath)
    SystemExit()
def SGCallback():
    subprocess.Popen(SGPath)
    SystemExit()
def SFCallback():
    subprocess.Popen(SFPath)
    SystemExit()

SGb = Button(gui, text="Open Sonic Generations", command=SGCallback)
HMMb = Button(gui, text="Open HedgeModManager", command=HMMCallback)
SFb = Button(gui, text="Open Sonic Forces", command=SFCallback)
SGb.pack(pady=15)
HMMb.pack(pady=15)
SFb.pack(pady=15)
gui.mainloop()