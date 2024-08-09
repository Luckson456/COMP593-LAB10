"""
Description:
  Graphical user interface that displays the official artwork for a
  user-specified Pokemon, which can be set as the desktop background image.

Usage:
  python poke_image_viewer.py
"""
from tkinter import *
from tkinter import ttk
import os
import poke_api
import image_lib
import ctypes
import inspect
from tkinter import Tk,PhotoImage

# Get the script and images directory
script_name=inspect.getframeinfo(inspect.currentframe()).filename
script_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(script_dir, 'images')

# TODO: Create the images directory if it does not exist
if not os.path.exists(images_dir):
  os.makedirs(images_dir)
# Create the main window
root = Tk()
root.title("Pokemon Viewer")
root.geometry('600x600')
root.minsize(500,500)
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)

# TODO: Set the icon
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("COMP593.PokeImageViewer")
root.iconbitmap(os.path.join(script_dir,'poke_ball.ico'))

# TODO: Create frames
frm=ttk.Frame(root)
frm.columnconfigure(0,weight=1)
frm.rowconfigure(0,weight=1)
frm.grid(sticky=NSEW)


# TODO: Populate frames with widgets and define event handler functions
image_path=os.path.join(script_dir,'poke_ball.png')
photo=PhotoImage(file=image_path)
root.iconphoto(True,photo)

lbl_image=ttk.Label(frm,image=photo)
lbl_image.grid(row=0,column=0, padx=10, pady=10)

def handel_set_desktop():
  selected_pokemon=cbox_poke_sel.get()
  if selected_pokemon:
    image_url=poke_api.get_pokemon_image_url(selected_pokemon)
    image_file=os.path.join(images_dir,f"{selected_pokemon}.ico")
    image_lib.download_image(image_url,image_file)
    image_lib.set_desktop_background_image(image_file)

  btn_set_desktop=ttk.Button(frm,text="Set as Desktop Background",command=handel_set_desktop)
  btn_set_desktop.grid(row=1,column=0,padx=10,pady=10)
def handel_poke_sel(event):
  selected_pokemon=cbox_poke_sel.get()
  if selected_pokemon:
    image_url=poke_api.get_pokemon_image_url(selected_pokemon)
    image_file=os.path.join(images_dir,f"{selected_pokemon}.ico")
    image_lib.download_image(image_url,image_file)
    new_photo=PhotoImage(file=image_file)
    lbl_image.configure(image=new_photo)
    lbl_image.image=new_photo
    
pokemon_list = [poke_api.get_pokemon_info(pokemon) for pokemon in range(1, 151)]
cbox_poke_sel=ttk.Combobox(frm,values=pokemon_list)
cbox_poke_sel.grid(row=2,column=0,padx=10,pady=10)
cbox_poke_sel.bind('<<ComboboxSelected>>',handel_poke_sel)

root.mainloop()