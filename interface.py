
import tkinter as tk
import os

root= tk.Tk()
root.title("KKU senario simulation")

canvas1 = tk.Canvas(root, width = 400, height = 400)
canvas1.pack()

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)



def open_stat():
   
    os.system('cd static && python callScript.py && sumo-gui config_file.sumocfg ')

def open_dyna():
   
    os.system('cd dynamic && python callScript.py && sumo-gui config_file.sumocfg')


def removeEdge ():  
    def open_sumo():
     os.system('cd dynamic && python callScript.py && sumo-gui config_file.sumocfg')

    x1 = entry1.get()
    os.system(f'cd dynamic && netedit -s kku_maps.net.xml --remove-edges.explicit "{x1}"')
    
    label1 = tk.Label(root, text= "edge to remove = " + x1)
    canvas1.create_window(200, 230, window=label1)
    
    button4 = tk.Button(text='open simulation', command=open_sumo, bg='green', fg='white', font=('helvetica', 9, 'bold'))
    canvas1.create_window(200, 260, window=button4)

def reset_net():
    os.system(f'cd dynamic && del kku_maps.net.xml')
    os.system(f'copy kku_maps.net.xml dynamic && cd dynamic && python callScript.py')
    label2 = tk.Label(root, text= "reset route finish !!!", fg='green', font=('helvetica', 9, 'bold'))
    canvas1.create_window(200, 330, window=label2)
    

button1 = tk.Button(text="open sumo static scenario", command=open_stat)
canvas1.create_window(200, 40, window=button1)

button2 = tk.Button(text="open sumo dynamic scenario", command=open_dyna)
canvas1.create_window(200, 80, window=button2)


label3 = tk.Label(root, text= "Test Worst Case")
canvas1.create_window(200, 120, window=label3)

button3 = tk.Button(text='Remove edge', command=removeEdge)
canvas1.create_window(200, 180, window=button3)

button5 = tk.Button(text='Reset route', command=reset_net, bg='red', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 300, window=button5)

root.mainloop()