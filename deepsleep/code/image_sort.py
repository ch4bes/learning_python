#! /usr/bin/env python3

import shutil, os
import tkinter as tk
from PIL import Image, ImageTk

main_dir = '~/deepsleep/images'
master_dir = main_dir + '/master'
sorted_dir = main_dir + '/sorted'
temp_dir = sorted_dir + '/temp'
skipped_dir = sorted_dir + '/skipped'

in_bed_dir = sorted_dir + '/in'
asleep_dir = in_bed_dir + '/asleep'
awake_dir = in_bed_dir + '/awake'

out_bed_dir = sorted_dir + '/out'
in_room_dir = out_bed_dir + '/in'
out_room_dir = out_bed_dir + '/out'

def main():
    
    os.chdir(main_dir) # change current working dir to main_dir

    i=0
    
    for image in os.listdir(master_dir): # for [image] in master_dir:

        i+=1
        
        master_filepath = master_dir + '/' + image
        print('copying master image #' + str(i)) # print statements for debugging, can be removed
        shutil.copy(master_filepath, temp_dir) # copy [image] to temp_dir
        print('done')
        temp_filepath = temp_dir + '/' + image

        print('running prompt cycle ' + str(i) + '...')
        prompts(temp_filepath) # run prompt cycle
        print('done')

def prompts(filepath):
        
    os.chdir(temp_dir) # change current working dir to temp_dir
    
    root = tk.Tk()
    root.title(filepath)
    
    w = 640
    h = 500
    cv = tk.Canvas(root, width=w, height=h)
    cv.pack(fill='both', expand='yes')
    
    PIL_file = Image.open(filepath)
    width_org, height_org = PIL_file.size # get size of orig image file
    resize_factor = 0.5
    width = int(width_org * resize_factor)
    height = int(height_org * resize_factor)
    resized_PIL = PIL_file.resize((width,height), Image.ANTIALIAS)
    imagefile = ImageTk.PhotoImage(resized_PIL)
    
    cv.create_image(w//2, h//2, image=imagefile, anchor='center')

    promptOne(filepath,root)
    # root.mainloop() needs to go somewhere

def promptOne(filepath,root):    
    prompt1 = 'Is subject [in bed]? or [out of bed]? or [skip]'
    p1 = tk.Message(root, aspect=1500, text=prompt1)
    p1.pack()
    
    button1a = tk.Button(root, text='In bed', width=12, command=lambda: in_bed)
    button1a.pack()
    button1b = tk.Button(root, text='Out of bed', width=12, command=lambda: out_bed)
    button1b.pack()
    button1c = tk.Button(root, text='Skip', width=12,  command=lambda: skip1)
    button1c.pack()
    
    

def in_bed(filepath,root):
    promptTwoA(filepath,root)
def promptTwoA(filepath,root):
    prompt2A = 'is subject [asleep]? or [awake]? or [skip]'
    p2A = tk.Message(root, aspect=1500, text=prompt2A)
    p2A.pack()

    button2Aa = tk.Button(root, text='Asleep', width=12, command=lambda: asleep)
    button2Aa.pack()
    button2Ab = tk.Button(root, text='Awake', width=12, command=lambda: awake)
    button2Ab.pack()
    button2Ac = tk.Button(root, text='Skip', width=12, command=lambda: skip2a)
    button2Ac.pack()
def asleep(filepath):                
    shutil.move(filepath, asleep_dir) # move [image] to asleep_dir
def awake(filepath):
    shutil.move(filepath, awake_dir) # move [image] to awake_dir
def skip2a(filepath):
    shutil.copy(filepath, skipped_dir) # copy [image] to skipped_dir
    shutil.move(tfilepath, in_bed_dir) # move [image] to in_bed_dir

def out_bed(filepath,root):
    promptTwoB(filepath,root)
def promptTwoB(filepath,root):
    prompt2B = 'is subject [in room]? or [out of room]? or [skip]'
    p2B = tk.Message(root, aspect=1500, text=prompt2B)
    p2B.pack()

    button2Ba = tk.Button(root, text='In room', width=12, command=lambda: in_room)
    button2Ba.pack()
    button2Bb = tk.Button(root, text='Out of room', width=12, command=lambda: out_room)
    button2Bb.pack()
    button2Bc = tk.Button(root, text='Skip', width=12, command=lambda: skip2b)
    button2Bc.pack()
def in_room(filepath):                
    shutil.move(filepath, in_room_dir) # move [image] to in_room_dir
def out_room(filepath):
    shutil.move(filepath, out_room_dir) # move [image] to out_room_dir
def skip2b(filepath):
    shutil.copy(filepath, skipped_dir) # copy [image] to skipped_dir
    shutil.move(filepath, out_bed_dir) # move [image] to out_bed_dir

def skip1(filepath):
    shutil.move(filepath, skipped_dir) # move [image] to skipped_dir
        
if __name__ == '__main__':
    main()
