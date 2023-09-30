from tkinter import *
import pygame
import os 
root = Tk()
root.title("Music Player")
root.geometry("500*300")
#intializing the pygame music mixer to allow us to play audio
pygame.mixer.init()
#Running the program
root.mainloop()