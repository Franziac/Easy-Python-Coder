
from os import path
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
import os 
icon_path = os.path.dirname(os.path.realpath(__file__))
root.iconbitmap(icon_path + r"\icon\favicon.ico")
root.title("Easy Python Coder")
root.configure(bg="#404142")

frame4=tk.Frame(root,bg="#404142")
frame=tk.Frame(root,bg="#404142")
frame5=tk.Frame(root,bg="#404142")
frame6=tk.Frame(root,bg="#404142")
frame8=tk.Frame(root,bg="#404142")
frame2=tk.Frame(root,bg="#404142")
frame7=tk.Frame(root,bg="#404142")
frame3=tk.Frame(root,bg="#404142")
building_frame=tk.Frame(root,bg="#404142")
frame9=tk.Frame(root,bg="#404142")
frame10=tk.Frame(root,bg="#404142")
frame11=tk.Frame(root,bg="#404142")

def_buttons_frame=tk.Frame(root,bg="#404142")
def_print_text_frame=tk.Frame(root,bg="#404142")
def_print_buttons_frame=tk.Frame(root,bg="#404142")
def_print_advanced_text_frame=tk.Frame(root,bg="#404142")
def_print_advanced_buttons_frame=tk.Frame(root,bg="#404142")
def_input_text_frame=tk.Frame(root,bg="#404142")
def_input_buttons_frame=tk.Frame(root,bg="#404142")
def_var_text_frame=tk.Frame(root,bg="#404142")
def_var_buttons_frame=tk.Frame(root,bg="#404142")
def_if_text_frame=tk.Frame(root,bg="#404142")
def_if_buttons_frame=tk.Frame(root,bg="#404142")

if_buttons_frame=tk.Frame(root,bg="#404142")
if_print_text_frame=tk.Frame(root,bg="#404142")
if_print_buttons_frame=tk.Frame(root,bg="#404142")
if_print_advanced_text_frame=tk.Frame(root,bg="#404142")
if_print_advanced_buttons_frame=tk.Frame(root,bg="#404142")
if_input_text_frame=tk.Frame(root,bg="#404142")
if_input_buttons_frame=tk.Frame(root,bg="#404142")
if_var_text_frame=tk.Frame(root,bg="#404142")
if_var_buttons_frame=tk.Frame(root,bg="#404142")


def_if_print_text_frame=tk.Frame(root,bg="#404142")
def_if_print_buttons_frame=tk.Frame(root,bg="#404142")
def_if_print_advanced_text_frame=tk.Frame(root,bg="#404142")
def_if_print_advanced_buttons_frame=tk.Frame(root,bg="#404142")
def_if_input_text_frame=tk.Frame(root,bg="#404142")
def_if_input_buttons_frame=tk.Frame(root,bg="#404142")
def_if_var_text_frame=tk.Frame(root,bg="#404142")
def_if_var_buttons_frame=tk.Frame(root,bg="#404142")


grid_frame2=tk.Frame(root,bg="#404142")

#def_input_commands=""




text=""
def_var_input=tk.Entry(root,bg="#404142")
def_print_input=tk.Entry(root,bg="#404142")
def_input_input=tk.Entry(root,bg="#404142")
def_input_input2=tk.Entry(root,bg="#404142")
def_input_input3=tk.Entry(root,bg="#404142")

if_var_input=tk.Entry(root,bg="#404142")
if_print_input=tk.Entry(root,bg="#404142")
if_input_input=tk.Entry(root,bg="#404142")
if_input_input2=tk.Entry(root,bg="#404142")
if_input_input3=tk.Entry(root,bg="#404142")
if_input_name=tk.Entry(root,bg="#404142")
if_input_commands=tk.Entry(root,bg="#404142")
def_if_input_name=tk.Entry(root,bg="#404142")
def_if_input_commands=tk.Entry(root,bg="#404142")
def_if_var_input=tk.Entry(root,bg="#404142")

def_if_print_input=tk.Entry(root)
#cancel_button,add_button,build="","",""
#Add and Cancel---------------------------------------------------------------------------------------------------------------
def add(button):
        if(button=="print"):
                global text
                
                text="print('{}')".format(print_input.get())+"\n"
            
                print_text.grid_forget()
                print_cancel_button.grid_forget()
                print_add_button.grid_forget()
                print_input.grid_forget()
                print_advanced_button.grid_forget()
                print_button.pack(fill=tk.X)
                input_button.pack(fill=tk.X)
                var_button.pack(fill=tk.X)
                def_button.pack(fill=tk.X)
                
                textbox.insert(tk.INSERT,text)
        if(button=="input"):
                #global input_input
                
                if(input_input3.get()=="str"):
                    text="{} = input('{}')".format(input_input.get(),input_input2.get())+"\n"
                elif(input_input3.get()=="int"):
                    text="{} = int(input('{}'))".format(input_input.get(),input_input2.get())+"\n"
                elif(input_input3.get()=="float"):
                    text="{} = float(input('{}'))".format(input_input.get(),input_input2.get())+"\n"
               
                ##Lisää else

                
                input_text.grid_forget()
                input_type.grid_forget()
                input_name.grid_forget()
                input_cancel_button.grid_forget()
                input_add_button.grid_forget()
                
                input_input.grid_forget()
                input_input2.grid_forget()
                input_input3.grid_forget()
                print_button.pack(fill=tk.X)
                input_button.pack(fill=tk.X)
                var_button.pack(fill=tk.X)
                def_button.pack(fill=tk.X)
                textbox.insert(tk.INSERT,text)
                
        
        if(button=="var"):
            text="{} \n".format(var_input.get())
            var_text.grid_forget()
            var_cancel_button.grid_forget()
            var_add_button.grid_forget()
            var_input.grid_forget()
            print_button.pack(fill=tk.X)
            input_button.pack(fill=tk.X)
            var_button.pack(fill=tk.X)
            def_button.pack(fill=tk.X)
            textbox.insert(tk.INSERT,text)
        if(button=="def"):
            end=False
            i=0
            while(end==False):
                    
                    i+=1
                    def_input_commands.insert('{}.0'.format(i),"\t")
                    
                    if(i > 20):
                            end=True
            text="def {} (): \n{}\n#You can call the function with {}()".format(def_input_name.get(),def_input_commands.get("1.0",tk.END),def_input_name.get())
            def_text_name.grid_forget()
            def_text_commands.grid_forget()
            def_cancel_button.grid_forget()
            def_add_button.grid_forget()
            def_input_name.grid_forget()
            def_input_commands.grid_forget()
            def_print_button.grid_forget()
            def_input_button.grid_forget()
            def_var_button.grid_forget()
            def_if_button.grid_forget()
            print_button.pack(fill=tk.X)
            input_button.pack(fill=tk.X)
            var_button.pack(fill=tk.X)
            def_button.pack(fill=tk.X)
            if_button.pack(fill=tk.X)
            textbox.insert(tk.INSERT,text)
        if(button=="if"):
                    
                    end=False
                    i=0
                    while(end==False):
                            
                            i+=1
                            if_input_commands.insert('{}.0'.format(i),"\t")
                           
                            if(i > 20):
                                    end=True
                    text="if ({}): \n{}\n".format(if_input_name.get(),if_input_commands.get("1.0",tk.END))
                    if_text_name.grid_forget()
                    if_text_commands.grid_forget()
                    if_cancel_button.grid_forget()
                    if_add_button.grid_forget()
                    if_input_name.grid_forget()
                    if_input_commands.grid_forget()
                    if_print_button.grid_forget()
                    if_input_button.grid_forget()
                    if_var_button.grid_forget()
                    print_button.pack(fill=tk.X)
                    input_button.pack(fill=tk.X)
                    var_button.pack(fill=tk.X)
                    def_button.pack(fill=tk.X)
                    if_button.pack(fill=tk.X)
                    textbox.insert(tk.INSERT,text)
        frame3.tkraise()
        frame7.tkraise()
        frame2.tkraise()
def cancel(button):
        global def_var_input,def_print_input, if_var_input,if_print_input, if_input_name,if_input_commands,def_if_input_name,def_if_input_commands
        if(button=="print"): 
                #global print_cancel_button,print_add_button
                print_text.grid_forget()
                print_cancel_button.grid_forget()
                print_add_button.grid_forget()
                print_advanced_button.grid_forget()
                print_input.grid_forget()
                print_button.pack(fill=tk.X)
                input_button.pack(fill=tk.X)
                var_button.pack(fill=tk.X)
                def_button.pack(fill=tk.X)
                if_button.pack(fill=tk.X)
        elif(button=="input"):
                #global input_cancel_button,add_button
                input_text.grid_forget()
                input_name.grid_forget()
                input_type.grid_forget()
                input_cancel_button.grid_forget()
                input_add_button.grid_forget()
                
                input_input.grid_forget()
                input_input2.grid_forget()
                input_input3.grid_forget()
                print_button.pack(fill=tk.X)
                input_button.pack(fill=tk.X)
                var_button.pack(fill=tk.X)
                def_button.pack(fill=tk.X)
                if_button.pack(fill=tk.X)
        elif(button=="var"):
            var_text.grid_forget()
            var_cancel_button.grid_forget()
            var_add_button.grid_forget()
            var_input.grid_forget()
            print_button.pack(fill=tk.X)
            input_button.pack(fill=tk.X)
            var_button.pack(fill=tk.X)
            def_button.pack(fill=tk.X)
            if_button.pack(fill=tk.X)
        elif(button=="def"):
            def_text_name.grid_forget()
            def_text_commands.grid_forget()
            def_cancel_button.grid_forget()
            def_add_button.grid_forget()
            def_input_name.grid_forget()
            def_input_commands.grid_forget()
            def_print_button.grid_forget()
            def_input_button.grid_forget()
            def_var_button.grid_forget()
            def_if_button.grid_forget()

            def_print_text.grid_forget()
            def_print_cancel_button.grid_forget()
            def_print_add_button.grid_forget()
            def_print_input.grid_forget()
            def_print_advanced_button.grid_forget()

            def_input_text.grid_forget()
            def_input_text_name.grid_forget()
            def_input_type.grid_forget()
            def_input_cancel_button.grid_forget()
            def_input_add_button.grid_forget()
            def_input_input.grid_forget()
            def_input_input2.grid_forget()
            def_input_input3.grid_forget()

            def_var_text.grid_forget()
            def_var_cancel_button.grid_forget()
            def_var_add_button.grid_forget()
            def_var_input.grid_forget()

            if_text_name.grid_forget()
            if_text_commands.grid_forget()
            if_cancel_button.grid_forget()
            if_add_button.grid_forget()

            def_if_text_name.grid_forget()
            def_if_text_commands.grid_forget()
            def_if_print_button.grid_forget()
            def_if_input_button.grid_forget()
            def_if_var_button.grid_forget()
            def_if_cancel_button.grid_forget()
            def_if_add_button.grid_forget()
            def_if_input_name.grid_forget()
            def_if_input_commands.grid_forget()

            
            print_button.pack(fill=tk.X)
            input_button.pack(fill=tk.X)
            var_button.pack(fill=tk.X)
            def_button.pack(fill=tk.X)
            if_button.pack(fill=tk.X)
        elif(button=="if"):
            if_text_name.grid_forget()
            if_text_commands.grid_forget()
            if_cancel_button.grid_forget()
            if_add_button.grid_forget()
            if_input_name.grid_forget()
            if_input_commands.grid_forget()
            if_print_button.grid_forget()
            if_input_button.grid_forget()
            if_var_button.grid_forget()

            if_print_text.grid_forget()
            if_print_cancel_button.grid_forget()
            if_print_add_button.grid_forget()
            if_print_input.grid_forget()
            if_print_advanced_button.grid_forget()

            if_input_text.grid_forget()
            if_input_text_name.grid_forget()
            if_input_type.grid_forget()
            if_input_cancel_button.grid_forget()
            if_input_add_button.grid_forget()
            if_input_input.grid_forget()
            if_input_input2.grid_forget()
            if_input_input3.grid_forget()

            if_var_text.grid_forget()
            if_var_cancel_button.grid_forget()
            if_var_add_button.grid_forget()
            if_var_input.grid_forget()
            
            print_button.pack(fill=tk.X)
            input_button.pack(fill=tk.X)
            var_button.pack(fill=tk.X)
            def_button.pack(fill=tk.X)
            if_button.pack(fill=tk.X)
        frame3.tkraise()
        frame7.tkraise()
        frame2.tkraise()
        frame5.tkraise()
def advanced(button):
    if(button=="print"):
        
        global print_advanced_input, print_advanced_input2
        print_text.grid_forget()
        print_cancel_button.grid_forget()
        print_add_button.grid_forget()
        print_advanced_button.grid_forget()
        print_input.grid_forget()
        print_advanced_input=tk.Entry(frame8)
        print_advanced_input2=tk.Entry(frame8)
        print_advanced_text.grid()
        print_advanced_input.grid()
        print_advanced_variables.grid(row=2)
        print_advanced_input2.grid()
        print_advanced_add_button.grid(row=0,column=1)
        print_advanced_cancel_button.grid(row=0,column=0)
        frame11.tkraise()
        frame8.tkraise()
def advanced_add(button):
        if(button=="print"):
                global text
                        
                text="print('{}'.format({}))".format(print_advanced_input.get(),print_advanced_input2.get())+"\n"
                    
                print_text.grid_forget()
                print_advanced_cancel_button.grid_forget()
                print_advanced_add_button.grid_forget()
                print_advanced_input.grid_forget()
                print_advanced_input2.grid_forget()
                print_advanced_text.grid_forget()
                print_advanced_variables.grid_forget()
                print_button.pack(fill=tk.X)
                input_button.pack(fill=tk.X)
                var_button.pack(fill=tk.X)
                def_button.pack(fill=tk.X)
                
                textbox.insert(tk.INSERT,text)
                frame11.tkraise()
        frame4.tkraise()
        frame3.tkraise()
        frame7.tkraise()
        frame2.tkraise()
        frame5.tkraise()
def advanced_cancel(button):
        if(button=="print"):
                print_text.grid_forget()
                print_advanced_cancel_button.grid_forget()
                print_advanced_add_button.grid_forget()
                print_advanced_input.grid_forget()
                print_advanced_input2.grid_forget()
                print_advanced_text.grid_forget()
                print_advanced_variables.grid_forget()
                print_button.pack(fill=tk.X)
                input_button.pack(fill=tk.X)
                var_button.pack(fill=tk.X)
                def_button.pack(fill=tk.X)
        frame3.tkraise()
        frame7.tkraise()
        frame2.tkraise()
        frame5.tkraise()
        frame4.tkraise()
#print----------------------------------------------------------------------------------------------
def cmd_print():
    
    global print_input
    print_button.pack_forget()
    input_button.pack_forget()
    var_button.pack_forget()
    def_button.pack_forget()
    if_button.pack_forget()

    print_text.grid()
    print_input=tk.Entry(frame7)
    print_input.grid(row=4)
    print_cancel_button.grid(row=5,column=0)
    print_add_button.grid(row=5,column=1)
    print_advanced_button.grid(row=5,column=2)
    
    frame3.tkraise()
    frame7.tkraise()
#----------------------------------------------------------------------------------------------
#input----------------------------------------------------------------------------------------------
def cmd_input():
        global input_input,input_input2,input_input3
        print_button.pack_forget()
        input_button.pack_forget()
        var_button.pack_forget()
        def_button.pack_forget()
        if_button.pack_forget()
        
        input_input=tk.Entry(grid_frame2)
        input_input2=tk.Entry(grid_frame2)
        input_input3=tk.Entry(grid_frame2)
        input_name.grid()
        input_input.grid()
        input_text.grid()
        input_input2.grid()
        input_type.grid()
        input_input3.grid()
        input_cancel_button.grid(row=6)
        input_add_button.grid(row=6,column=1)
        grid_frame2.tkraise()
        frame5.tkraise()
#var-------------------------------------------------------------------------------------------------------------
def cmd_var():
    global var_input
    print_button.pack_forget()
    input_button.pack_forget()
    var_button.pack_forget()
    def_button.pack_forget()
    if_button.pack_forget()
    
    var_input=tk.Entry(frame9)
    var_text.grid()
    var_input.grid()
    var_cancel_button.grid(row=5)
    var_add_button.grid(row=5,column=1)

    frame9.tkraise()
    frame10.tkraise()
#def----------------------------------------------------------------------------------------------------------
def cmd_def():
    global def_input_name, def_input_commands
    print_button.pack_forget()
    input_button.pack_forget()
    var_button.pack_forget()
    def_button.pack_forget()
    if_button.pack_forget()
    def_input_name=tk.Entry(frame9,bg="#727272",fg="white",bd=0)
    def_input_commands=tk.Text(frame9,width=50, height=10,bg="#727272",fg="white",bd=0)
    def_text_name.grid()
    def_input_name.grid()
    def_text_commands.grid()
    def_input_commands.grid()
    def_cancel_button.grid(row=5)
    def_add_button.grid(row=5,column=1)
    def_print_button.grid(row=5,column=2)
    def_input_button.grid(row=5,column=3)
    def_var_button.grid(row=5,column=4)
    def_if_button.grid(row=5,column=5)
    frame9.tkraise()
    def_buttons_frame.tkraise()
def def_print():
        
    global def_print_input
    def_print_button.grid_forget()
    def_input_button.grid_forget()
    def_var_button.grid_forget()
    def_if_button.grid_forget()
    
    def_print_text.grid()
    def_print_input=tk.Entry(def_print_text_frame)
    def_print_input.grid(row=4)
    def_print_cancel_button.grid(row=5,column=0)
    def_print_add_button.grid(row=5,column=1)
    def_print_advanced_button.grid(row=5,column=2)
    
    def_print_text_frame.tkraise()
    def_print_buttons_frame.tkraise()

def def_input():
        global def_input_input,def_input_input2,def_input_input3
        def_print_button.grid_forget()
        def_input_button.grid_forget()
        def_var_button.grid_forget()
        def_if_button.grid_forget()
        
        
        def_input_input=tk.Entry(def_input_text_frame)
        def_input_input2=tk.Entry(def_input_text_frame)
        def_input_input3=tk.Entry(def_input_text_frame)
        def_input_text_name.grid()
        def_input_input.grid()
        def_input_text.grid()
        def_input_input2.grid()
        def_input_type.grid()
        def_input_input3.grid()
        def_input_cancel_button.grid(row=6)
        def_input_add_button.grid(row=6,column=1)
        
        def_input_text_frame.tkraise()
        def_input_buttons_frame.tkraise()
        
def def_var():
    global def_var_input
    def_print_button.grid_forget()
    def_input_button.grid_forget()
    def_var_button.grid_forget()
    def_if_button.grid_forget()
    
    def_var_input=tk.Entry(def_var_text_frame)
    def_var_text.grid()
    def_var_input.grid()
    def_var_cancel_button.grid(row=5)
    def_var_add_button.grid(row=5,column=1)

    def_var_text_frame.tkraise()
    def_var_buttons_frame.tkraise()

def def_if():
    global def_if_input_name, def_if_input_commands
    def_print_button.grid_forget()
    def_input_button.grid_forget()
    def_var_button.grid_forget()
    def_if_button.grid_forget()
    def_if_input_name=tk.Entry(def_if_text_frame,bg="#727272",fg="white",bd=0)
    def_if_input_commands=tk.Text(def_if_text_frame,width=50, height=10,bg="#727272",fg="white",bd=0)
    def_if_text_name.grid()
    def_if_input_name.grid()
    def_if_text_commands.grid()
    def_if_input_commands.grid()
    def_if_cancel_button.grid(row=1)
    def_if_add_button.grid(row=1,column=1)
    def_if_print_button.grid(row=1,column=2)
    def_if_input_button.grid(row=1,column=3)
    def_if_var_button.grid(row=1,column=4)
def def_if_print():
        
    global def_if_print_input
    def_if_print_button.grid_forget()
    def_if_input_button.grid_forget()
    def_if_var_button.grid_forget()
    

    def_if_print_text.grid()
    def_if_print_input=tk.Entry(def_if_print_text_frame)
    def_if_print_input.grid(row=4)
    def_if_print_cancel_button.grid(row=5,column=0)
    def_if_print_add_button.grid(row=5,column=1)
    def_if_print_advanced_button.grid(row=5,column=2)
    
    def_if_print_text_frame.tkraise()
    def_if_print_buttons_frame.tkraise()
def def_if_input():
        global def_if_input_input,def_if_input_input2,def_if_input_input3
        def_if_print_button.grid_forget()
        def_if_input_button.grid_forget()
        def_if_var_button.grid_forget()
        
        
        def_if_input_input=tk.Entry(def_if_input_text_frame)
        def_if_input_input2=tk.Entry(def_if_input_text_frame)
        def_if_input_input3=tk.Entry(def_if_input_text_frame)
        def_if_input_text_name.grid()
        def_if_input_input.grid()
        def_if_input_text.grid()
        def_if_input_input2.grid()
        def_if_input_type.grid()
        def_if_input_input3.grid()
        def_if_input_cancel_button.grid(row=6)
        def_if_input_add_button.grid(row=6,column=1)
        
        def_if_input_text_frame.tkraise()
        def_if_input_buttons_frame.tkraise()

def def_if_var():
    global def_if_var_input
    def_if_print_button.grid_forget()
    def_if_input_button.grid_forget()
    def_if_var_button.grid_forget()
    
    def_if_var_input=tk.Entry(def_if_var_text_frame)
    def_if_var_text.grid()
    def_if_var_input.grid()
    def_if_var_cancel_button.grid(row=5)
    def_if_var_add_button.grid(row=5,column=1)

    def_if_var_text_frame.tkraise()
    def_if_var_buttons_frame.tkraise()
def show_buttons():
        def_print_button.grid(row=5,column=2)
        def_input_button.grid(row=5,column=3)
        def_var_button.grid(row=5,column=4)
        def_if_button.grid(row=5,column=5)

def if_show_buttons():
        def_if_print_button.grid(row=1,column=2)
        def_if_input_button.grid(row=1,column=3)
        def_if_var_button.grid(row=1,column=4)
        
def def_add(button):
        if(button=="print"):
                global text,def_input_commands
                        
                text="print('{}')\n".format(def_print_input.get())
                    
                def_print_text.grid_forget()
                def_print_cancel_button.grid_forget()
                def_print_add_button.grid_forget()
                def_print_input.grid_forget()
                def_print_advanced_button.grid_forget()

                show_buttons()
                
                def_input_commands.insert(tk.INSERT,text)
                frame4.tkraise()
        if(button=="input"):
                #global input_input
                
                if(def_input_input3.get()=="str"):
                    text="{} = input('{}')\n".format(def_input_input.get(),def_input_input2.get())
                elif(def_input_input3.get()=="int"):
                    text="{} = int(input('{}'))\n".format(def_input_input.get(),def_input_input2.get())
                elif(def_input_input3.get()=="float"):
                    text="{} = float(input('{}'))\n".format(def_input_input.get(),def_input_input2.get())
                

                
                def_input_text.grid_forget()
                def_input_type.grid_forget()
                def_input_text_name.grid_forget()
                def_input_cancel_button.grid_forget()
                def_input_add_button.grid_forget()
                
                def_input_input.grid_forget()
                def_input_input2.grid_forget()
                def_input_input3.grid_forget()
                show_buttons()
                def_input_commands.insert(tk.INSERT,text)
        if(button=="var"):
                text="{} \n".format(def_var_input.get())
                def_var_text.grid_forget()
                def_var_cancel_button.grid_forget()
                def_var_add_button.grid_forget()
                def_var_input.grid_forget()
                show_buttons()
                def_input_commands.insert(tk.INSERT,text)
        if(button=="if"):
                    end=False
                    i=0
                    while(end==False):
                            
                            i+=1
                            def_if_input_commands.insert('{}.0'.format(i),"\t")
                            if(i > 20):
                                    end=True
                    text="if ({}): \n{}\n".format(def_if_input_name.get(),def_if_input_commands.get("1.0",tk.END))
                    def_if_text_name.grid_forget()
                    def_if_text_commands.grid_forget()
                    def_if_cancel_button.grid_forget()
                    def_if_add_button.grid_forget()
                    def_if_input_name.grid_forget()
                    def_if_input_commands.grid_forget()
                    def_if_print_button.grid_forget()
                    def_if_input_button.grid_forget()
                    def_if_var_button.grid_forget()
                    show_buttons()
                    def_input_commands.insert(tk.INSERT,text)
        if(button=="if print"):
                
                        
                text="print('{}')\n".format(def_if_print_input.get())
                    
                def_if_print_text.grid_forget()
                def_if_print_cancel_button.grid_forget()
                def_if_print_add_button.grid_forget()
                def_if_print_input.grid_forget()
                def_if_print_advanced_button.grid_forget()
                if_show_buttons()
                #if_var_button.grid(row=5,column=5)
                
                def_if_input_commands.insert(tk.INSERT,text)
                frame4.tkraise()
        if(button == "if input"):
                
                if(def_if_input_input3.get()=="str"):
                        text="{} = input('{}')\n".format(def_if_input_input.get(),def_if_input_input2.get())
                elif(def_if_input_input3.get()=="int"):
                        text="{} = int(input('{}'))\n".format(def_if_input_input.get(),def_if_input_input2.get())
                elif(def_if_input_input3.get()=="float"):
                        text="{} = float(input('{}'))\n".format(def_if_input_input.get(),def_if_input_input2.get())
                
                def_if_input_text.grid_forget()
                def_if_input_type.grid_forget()
                def_if_input_text_name.grid_forget()
                def_if_input_cancel_button.grid_forget()
                def_if_input_add_button.grid_forget()
                
                def_if_input_input.grid_forget()
                def_if_input_input2.grid_forget()
                def_if_input_input3.grid_forget()
                if_show_buttons()

                def_if_input_commands.insert(tk.INSERT,text)
                frame4.tkraise()
        if(button=="if var"):
                
                        
                text="{}\n".format(def_if_var_input.get())
                    
                def_if_var_text.grid_forget()
                def_if_var_cancel_button.grid_forget()
                def_if_var_add_button.grid_forget()
                def_if_var_input.grid_forget()
                if_show_buttons()
               
                
                def_if_input_commands.insert(tk.INSERT,text)
                frame4.tkraise()
def def_cancel(button):
        if(button=="print"): 
                global def_if_print_input
                def_print_text.grid_forget()
                def_print_cancel_button.grid_forget()
                def_print_add_button.grid_forget()
                def_print_advanced_button.grid_forget()
                def_print_input.grid_forget()
                show_buttons()
                frame4.tkraise()
        elif(button=="input"):
                #global input_cancel_button,add_button
                def_input_text.grid_forget()
                def_input_text_name.grid_forget()
                def_input_type.grid_forget()
                def_input_cancel_button.grid_forget()
                def_input_add_button.grid_forget()
                
                def_input_input.grid_forget()
                def_input_input2.grid_forget()
                def_input_input3.grid_forget()
                show_buttons()
                #if_var_button.grid(row=5,column=5)
                
        elif(button=="var"):
            def_var_text.grid_forget()
            def_var_cancel_button.grid_forget()
            def_var_add_button.grid_forget()
            def_var_input.grid_forget()
            show_buttons()
           # if_var_button.grid(row=5,column=5)
        elif(button=="if"):
            def_if_text_name.grid_forget()
            def_if_text_commands.grid_forget()
            def_if_print_button.grid_forget()
            def_if_input_button.grid_forget()
            def_if_var_button.grid_forget()
            def_if_cancel_button.grid_forget()
            def_if_add_button.grid_forget()
            def_if_input_name.grid_forget()
            def_if_input_commands.grid_forget()

            def_if_print_text.grid_forget()
            def_if_print_cancel_button.grid_forget()
            def_if_print_add_button.grid_forget()
            def_if_print_input.grid_forget()
            def_if_print_advanced_button.grid_forget()

            def_if_input_text.grid_forget()
            def_if_input_type.grid_forget()
            def_if_input_text_name.grid_forget()
            def_if_input_cancel_button.grid_forget()
            def_if_input_add_button.grid_forget()
                
            def_if_input_input.grid_forget()
            def_if_input_input2.grid_forget()
            def_if_input_input3.grid_forget()

            def_if_var_text.grid_forget()
            def_if_var_cancel_button.grid_forget()
            def_if_var_add_button.grid_forget()
            def_if_var_input.grid_forget()
                
            show_buttons()
            #if_var_button.grid(row=5,column=5)
        elif(button=="if print"):
                def_if_print_text.grid_forget()
                def_if_print_cancel_button.grid_forget()
                def_if_print_add_button.grid_forget()
                def_if_print_input.grid_forget()
                def_if_print_advanced_button.grid_forget()
                if_show_buttons()
        elif(button=="if input"):
                def_if_input_text.grid_forget()
                def_if_input_type.grid_forget()
                def_if_input_text_name.grid_forget()
                def_if_input_cancel_button.grid_forget()
                def_if_input_add_button.grid_forget()
                
                def_if_input_input.grid_forget()
                def_if_input_input2.grid_forget()
                def_if_input_input3.grid_forget()
                if_show_buttons()
        elif(button =="if var"):
                def_if_var_text.grid_forget()
                def_if_var_cancel_button.grid_forget()
                def_if_var_add_button.grid_forget()
                def_if_var_input.grid_forget()

                if_show_buttons()
def def_advanced(button):
    if(button=="print"):
        
        global def_print_advanced_input, def_print_advanced_input2
        def_print_text.grid_forget()
        def_print_cancel_button.grid_forget()
        def_print_add_button.grid_forget()
        def_print_advanced_button.grid_forget()
        def_print_input.grid_forget()
        def_print_advanced_input=tk.Entry(def_print_advanced_text_frame)
        def_print_advanced_input2=tk.Entry(def_print_advanced_text_frame)
        def_print_advanced_text.grid()
        def_print_advanced_input.grid()
        def_print_advanced_variables.grid(row=2)
        def_print_advanced_input2.grid()
        def_print_advanced_add_button.grid(row=0,column=1)
        def_print_advanced_cancel_button.grid(row=0,column=0)
        def_print_advanced_buttons_frame.tkraise()
        def_print_advanced_text_frame.tkraise()
def def_advanced_add(button):
    if(button=="print"):
        global text
                
        text="print('{}'.format({}))".format(def_print_advanced_input.get(),def_print_advanced_input2.get())+"\n"
            
        def_print_text.grid_forget()
        def_print_advanced_cancel_button.grid_forget()
        def_print_advanced_add_button.grid_forget()
        def_print_advanced_input.grid_forget()
        def_print_advanced_input2.grid_forget()
        def_print_advanced_text.grid_forget()
        def_print_advanced_variables.grid_forget()
        def_print_button.grid(row=5,column=2)
        def_input_button.grid(row=5,column=3)
        def_var_button.grid(row=5,column=4)
        
        def_input_commands.insert(tk.INSERT,text)
        frame11.tkraise()
        frame4.tkraise()


def def_advanced_cancel(button):
    if(button=="print"):
        def_print_text.grid_forget()
        def_print_advanced_cancel_button.grid_forget()
        def_print_advanced_add_button.grid_forget()
        def_print_advanced_input.grid_forget()
        def_print_advanced_input2.grid_forget()
        def_print_advanced_text.grid_forget()
        def_print_advanced_variables.grid_forget()
        def_print_button.grid(row=5,column=2)
        def_input_button.grid(row=5,column=3)
        def_var_button.grid(row=5,column=4)
        
        frame11.tkraise()
        frame4.tkraise()



def def_if_advanced(button):
    if(button=="print"):
        
        global def_if_print_advanced_input, def_if_print_advanced_input2
        def_if_print_text.grid_forget()
        def_if_print_cancel_button.grid_forget()
        def_if_print_add_button.grid_forget()
        def_if_print_advanced_button.grid_forget()
        def_if_print_input.grid_forget()
        def_if_print_advanced_input=tk.Entry(def_if_print_advanced_text_frame)
        def_if_print_advanced_input2=tk.Entry(def_if_print_advanced_text_frame)
        def_if_print_advanced_text.grid()
        def_if_print_advanced_input.grid()
        def_if_print_advanced_variables.grid(row=2)
        def_if_print_advanced_input2.grid()
        def_if_print_advanced_add_button.grid(row=0,column=1)
        def_if_print_advanced_cancel_button.grid(row=0,column=0)
        def_if_print_advanced_buttons_frame.tkraise()
        def_if_print_advanced_text_frame.tkraise()
def def_if_advanced_add(button):
    if(button=="print"):
        global text
                
        text="print('{}'.format({}))".format(def_if_print_advanced_input.get(),def_if_print_advanced_input2.get())+"\n"
            
        def_if_print_text.grid_forget()
        def_if_print_advanced_cancel_button.grid_forget()
        def_if_print_advanced_add_button.grid_forget()
        def_if_print_advanced_input.grid_forget()
        def_if_print_advanced_input2.grid_forget()
        def_if_print_advanced_text.grid_forget()
        def_if_print_advanced_variables.grid_forget()
        if_show_buttons()
        
        def_if_input_commands.insert(tk.INSERT,text)
        def_if_print_advanced_text_frame.tkraise()
        def_if_print_advanced_buttons_frame.tkraise()


def def_if_advanced_cancel(button):
    if(button=="print"):
        def_if_print_text.grid_forget()
        def_if_print_advanced_cancel_button.grid_forget()
        def_if_print_advanced_add_button.grid_forget()
        def_if_print_advanced_input.grid_forget()
        def_if_print_advanced_input2.grid_forget()
        def_if_print_advanced_text.grid_forget()
        def_if_print_advanced_variables.grid_forget()
        if_show_buttons()
        
        def_if_print_advanced_buttons_frame.tkraise()
        def_if_print_advanced_text_frame.tkraise()
#If------------------------------------------------------------------------------------------------------
def cmd_if():
    global if_input_name, if_input_commands
    print_button.pack_forget()
    input_button.pack_forget()
    var_button.pack_forget()
    def_button.pack_forget()
    if_button.pack_forget()
    if_input_name=tk.Entry(frame9,bg="#727272",fg="white",bd=0)
    if_input_commands=tk.Text(frame9,width=50, height=10,bg="#727272",fg="white",bd=0)
    if_text_name.grid()
    if_input_name.grid()
    if_text_commands.grid()
    if_input_commands.grid()
    if_cancel_button.grid(row=5)
    if_add_button.grid(row=5,column=1)
    if_print_button.grid(row=5,column=2)
    if_input_button.grid(row=5,column=3)
    if_var_button.grid(row=5,column=4)
    
    frame9.tkraise()
    if_buttons_frame.tkraise()
def if_print():
        
    global if_print_input
    if_print_button.grid_forget()
    if_input_button.grid_forget()
    if_var_button.grid_forget()

    if_print_text.grid()
    if_print_input=tk.Entry(if_print_text_frame)
    if_print_input.grid(row=4)
    if_print_cancel_button.grid(row=5,column=0)
    if_print_add_button.grid(row=5,column=1)
    if_print_advanced_button.grid(row=5,column=2)
    
    if_print_text_frame.tkraise()
    if_print_buttons_frame.tkraise()

def if_input():
        global if_input_input,if_input_input2,if_input_input3
        if_print_button.grid_forget()
        if_input_button.grid_forget()
        if_var_button.grid_forget()
        
        
        if_input_input=tk.Entry(if_input_text_frame)
        if_input_input2=tk.Entry(if_input_text_frame)
        if_input_input3=tk.Entry(if_input_text_frame)
        if_input_text_name.grid()
        if_input_input.grid()
        if_input_text.grid()
        if_input_input2.grid()
        if_input_type.grid()
        if_input_input3.grid()
        if_input_cancel_button.grid(row=6)
        if_input_add_button.grid(row=6,column=1)
        
        if_input_text_frame.tkraise()
        if_input_buttons_frame.tkraise()
        
def if_var():
    global if_var_input
    if_print_button.grid_forget()
    if_input_button.grid_forget()
    if_var_button.grid_forget()
    
    if_var_input=tk.Entry(if_var_text_frame)
    if_var_text.grid()
    if_var_input.grid()
    if_var_cancel_button.grid(row=5)
    if_var_add_button.grid(row=5,column=1)

    if_var_text_frame.tkraise()
    if_var_buttons_frame.tkraise()

def if_add(button):
        if(button=="print"):
                global text,if_input_commands
                        
                text="print('{}')\n".format(if_print_input.get())
                    
                if_print_text.grid_forget()
                if_print_cancel_button.grid_forget()
                if_print_add_button.grid_forget()
                if_print_input.grid_forget()
                if_print_advanced_button.grid_forget()
                if_print_button.grid(row=5,column=2)
                if_input_button.grid(row=5,column=3)
                if_var_button.grid(row=5,column=4)
                
                if_input_commands.insert(tk.INSERT,text)
                frame4.tkraise()
        if(button=="input"):
                #global input_input
                
                if(if_input_input3.get()=="str"):
                    text="{} = input('{}')\n".format(if_input_input.get(),if_input_input2.get())+"\n"
                elif(if_input_input3.get()=="int"):
                    text="{} = int(input('{}'))\n".format(if_input_input.get(),if_input_input2.get())+"\n"
                elif(if_input_input3.get()=="float"):
                    text="{} = float(input('{}'))\n".format(if_input_input.get(),if_input_input2.get())+"\n"


                
                if_input_text.grid_forget()
                if_input_type.grid_forget()
                if_input_text_name.grid_forget()
                if_input_cancel_button.grid_forget()
                if_input_add_button.grid_forget()
                
                if_input_input.grid_forget()
                if_input_input2.grid_forget()
                if_input_input3.grid_forget()
                if_print_button.grid(row=5,column=2)
                if_input_button.grid(row=5,column=3)
                if_var_button.grid(row=5,column=4)
                if_input_commands.insert(tk.INSERT,text)
        if(button=="var"):
                text="{} \n".format(if_var_input.get())
                if_var_text.grid_forget()
                if_var_cancel_button.grid_forget()
                if_var_add_button.grid_forget()
                if_var_input.grid_forget()
                if_print_button.grid(row=5,column=2)
                if_input_button.grid(row=5,column=3)
                if_var_button.grid(row=5,column=4)
                if_input_commands.insert(tk.INSERT,text)
def if_cancel(button):
        if(button=="print"): 
            #global print_cancel_button,print_add_button
                if_print_text.grid_forget()
                if_print_cancel_button.grid_forget()
                if_print_add_button.grid_forget()
                if_print_advanced_button.grid_forget()
                if_print_input.grid_forget()
                if_print_button.grid(row=5,column=2)
                if_input_button.grid(row=5,column=3)
                if_var_button.grid(row=5,column=4)
                frame4.tkraise()
        elif(button=="input"):
                #global input_cancel_button,add_button
                if_input_text.grid_forget()
                if_input_text_name.grid_forget()
                if_input_type.grid_forget()
                if_input_cancel_button.grid_forget()
                if_input_add_button.grid_forget()
                
                if_input_input.grid_forget()
                if_input_input2.grid_forget()
                if_input_input3.grid_forget()
                if_print_button.grid(row=5,column=2)
                if_input_button.grid(row=5,column=3)
                if_var_button.grid(row=5,column=4)
                
        elif(button=="var"):
            if_var_text.grid_forget()
            if_var_cancel_button.grid_forget()
            if_var_add_button.grid_forget()
            if_var_input.grid_forget()
            if_print_button.grid(row=5,column=2)
            if_input_button.grid(row=5,column=3)
            if_var_button.grid(row=5,column=4)
def if_advanced(button):
    if(button=="print"):
        
        global if_print_advanced_input, if_print_advanced_input2
        if_print_text.grid_forget()
        if_print_cancel_button.grid_forget()
        if_print_add_button.grid_forget()
        if_print_advanced_button.grid_forget()
        if_print_input.grid_forget()
        if_print_advanced_input=tk.Entry(if_print_advanced_text_frame)
        if_print_advanced_input2=tk.Entry(if_print_advanced_text_frame)
        if_print_advanced_text.grid()
        if_print_advanced_input.grid()
        if_print_advanced_variables.grid(row=2)
        if_print_advanced_input2.grid()
        if_print_advanced_add_button.grid(row=0,column=1)
        if_print_advanced_cancel_button.grid(row=0,column=0)
        if_print_advanced_buttons_frame.tkraise()
        if_print_advanced_text_frame.tkraise()
def if_advanced_add(button):
    if(button=="print"):
        global text
                
        text="print('{}'.format({}))".format(if_print_advanced_input.get(),if_print_advanced_input2.get())+"\n"
            
        if_print_text.grid_forget()
        if_print_advanced_cancel_button.grid_forget()
        if_print_advanced_add_button.grid_forget()
        if_print_advanced_input.grid_forget()
        if_print_advanced_input2.grid_forget()
        if_print_advanced_text.grid_forget()
        if_print_advanced_variables.grid_forget()
        if_print_button.grid(row=5,column=2)
        if_input_button.grid(row=5,column=3)
        if_var_button.grid(row=5,column=4)
        
        if_input_commands.insert(tk.INSERT,text)
        frame11.tkraise()
        frame4.tkraise()
def if_advanced_cancel(button):
    if(button=="print"):
        if_print_text.grid_forget()
        if_print_advanced_cancel_button.grid_forget()
        if_print_advanced_add_button.grid_forget()
        if_print_advanced_input.grid_forget()
        if_print_advanced_input2.grid_forget()
        if_print_advanced_text.grid_forget()
        if_print_advanced_variables.grid_forget()
        if_print_button.grid(row=5,column=2)
        if_input_button.grid(row=5,column=3)
        if_var_button.grid(row=5,column=4)
        frame11.tkraise()
        frame4.tkraise()
#Build---------------------------------------------------------------------------------------------------
def file(text):
        destination=filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("Python","*.py"),("All Files","*.*")))
        if(destination !=""):
                createFile(destination,text)
def createFile(dest,text):
    global build
    if not(path.isfile(dest)):
        f = open(dest+".py",'w')
        f.write(textbox.get("1.0", tk.END))
        f.close()
        building_frame.tkraise()
        build.grid(row=10,column=1)
        root.after(1000,close_building)
def close_building():
    build.grid_forget()
    frame4.tkraise()
    frame2.tkraise()
    frame.tkraise()
    frame6.tkraise()

build = tk.Label(building_frame,text='Building was successful',width=30,height=3,font='Arial 18',bg="green")
#Frame 1--------------------------------------------------------------------------------------------
title = tk.Label(frame,text='Easy Python Coder',font='Arial 18',bg="#404142",fg="#efa207")
title.grid(row=0,column=0)

#Buttons--------------------------------------------------------------------------------------------
border_width=0.5

print_button = tk.Button(frame2,text="Print", command=cmd_print,bg="#727272",fg="#efa207",relief="solid",bd=border_width)
print_button.pack(fill=tk.X)

print_text = tk.Label(frame7,text='What to print?',bg="#404142",fg="#efa207")
print_cancel_button = tk.Button(frame3,text="Cancel", command=lambda: cancel("print"),bg="#727272",relief="solid",bd=border_width,fg="#efa207")
print_add_button = tk.Button(frame3,text="Add", command = lambda: add("print"),bg="#727272",relief="solid",bd=border_width,fg="#efa207")
print_advanced_button = tk.Button(frame3,text="Advanced", command = lambda: advanced("print"),bg="#727272",relief="solid",bd=border_width,fg="#efa207")
print_advanced_text = tk.Label(frame8,text='What to print(mark places for variables with {}',bg="#404142",fg="#efa207")
print_advanced_variables = tk.Label(frame8,text='What variables do you want them to represent?',bg="#404142",fg="#efa207")
print_advanced_cancel_button = tk.Button(frame11,text="Cancel", command=lambda: advanced_cancel("print"),bg="#727272",relief="solid",bd=border_width,fg="#efa207")
print_advanced_add_button = tk.Button(frame11,text="Add", command = lambda: advanced_add("print"),bg="#727272",relief="solid",bd=border_width,fg="#efa207")


input_button = tk.Button(frame2,text="Input", command=cmd_input,bg="#727272",fg="#efa207",relief="solid",bd=border_width)
input_button.pack(fill=tk.X)

input_text = tk.Label(grid_frame2,text='What do you want it to ask?',bg="#404142",fg="#efa207")
input_name = tk.Label(grid_frame2,text='What is the name of the input?',bg="#404142",fg="#efa207")
input_type = tk.Label(grid_frame2,text='What type is the input(int,float or str)',bg="#404142",fg="#efa207")
input_cancel_button = tk.Button(frame5,text="Cancel", command=lambda: cancel("input"),bg="#727272",relief="solid",bd=border_width,fg="#efa207")
input_add_button = tk.Button(frame5,text="Add", command = lambda: add("input"),bg="#727272",relief="solid",bd=border_width,fg="#efa207")


var_button = tk.Button(frame2,text="Variable", command=cmd_var,bg="#727272",fg="#efa207",relief="solid",bd=border_width)
var_button.pack(fill=tk.X)

var_text = tk.Label(frame9,text='Variable name and value',bg="#404142",fg="#efa207")
var_cancel_button = tk.Button(frame10,text="Cancel", command=lambda: cancel("var"),bg="#727272",relief="solid",bd=border_width,fg="#efa207")
var_add_button = tk.Button(frame10,text="Add", command = lambda: add("var"),bg="#727272",relief="solid",bd=border_width,fg="#efa207")


def_button = tk.Button(frame2,text="Function", command=cmd_def,bg="#727272",fg="#efa207",relief="solid",bd=border_width)
def_button.pack(fill=tk.X)

def_text_name = tk.Label(frame9,text='Function name',bg="#404142",fg="#efa207")
def_text_commands = tk.Label(frame9,text='Commands inside the function',bg="#404142",fg="#efa207")
def_cancel_button = tk.Button(def_buttons_frame,text="Cancel", command=lambda: cancel("def"),bg="#727272",relief="solid",bd=border_width,fg="#efa207")
def_add_button = tk.Button(def_buttons_frame,text="Add", command = lambda: add("def"),bg="#727272",relief="solid",bd=border_width,fg="#efa207")
def_print_button = tk.Button(def_buttons_frame,text="Print", command = def_print,bg="#727272",relief="solid",bd=border_width,fg="#efa207")
def_input_button = tk.Button(def_buttons_frame,text="Input", command = def_input,bg="#727272",relief="solid",bd=border_width,fg="#efa207")
def_var_button = tk.Button(def_buttons_frame,text="Variable", command = def_var,bg="#727272",relief="solid",bd=border_width,fg="#efa207")
def_if_button = tk.Button(def_buttons_frame,text="If", command = def_if,bg="#727272",relief="solid",bd=border_width,fg="#efa207",padx=10)


def_print_text = tk.Label(def_print_text_frame,text='What to print?',bg="#404142",fg="#efa207")
def_print_cancel_button = tk.Button(def_print_buttons_frame,text="Cancel", command=lambda: def_cancel("print"),bg="#727272",relief="solid",bd=border_width,fg="#efa207")
def_print_add_button = tk.Button(def_print_buttons_frame,text="Add", command = lambda: def_add("print"),bg="#727272",relief="solid",bd=border_width,fg="#efa207")
def_print_advanced_button = tk.Button(def_print_buttons_frame,text="Advanced", command = lambda: def_advanced("print"),bg="#727272",relief="solid",bd=border_width,fg="#efa207")
def_print_advanced_text = tk.Label(def_print_advanced_text_frame,text='What to print(mark places for variables with {}',bg="#404142",fg="#efa207")
def_print_advanced_variables = tk.Label(def_print_advanced_text_frame,text='What variables do you want them to represent?',bg="#404142",fg="#efa207")
def_print_advanced_cancel_button = tk.Button(def_print_advanced_buttons_frame,text="Cancel", command=lambda: def_advanced_cancel("print"),bg="#727272",relief="solid",bd=border_width,fg="#efa207")
def_print_advanced_add_button = tk.Button(def_print_advanced_buttons_frame,text="Add", command = lambda: def_advanced_add("print"),bg="#727272",relief="solid",bd=border_width,fg="#efa207")

def_input_text = tk.Label(def_input_text_frame,text='What do you want it to ask?',bg="#404142",fg="#efa207")
def_input_text_name = tk.Label(def_input_text_frame,text='What is the name of the input?',bg="#404142",fg="#efa207")
def_input_type = tk.Label(def_input_text_frame,text='What type is the input(int,float or str)',bg="#404142",fg="#efa207")
def_input_cancel_button = tk.Button(def_input_buttons_frame,text="Cancel", command=lambda:def_cancel("input"),bg="#727272",relief="solid",bd=border_width,fg="#efa207")
def_input_add_button = tk.Button(def_input_buttons_frame,text="Add", command =lambda: def_add("input"),bg="#727272",relief="solid",bd=border_width,fg="#efa207")

def_var_text = tk.Label(def_var_text_frame,text='Variable name and value',bg="#404142",fg="#efa207")
def_var_cancel_button = tk.Button(def_var_buttons_frame,text="Cancel", command=lambda: def_cancel("var"),bg="#727272",relief="solid",bd=border_width,fg="#efa207")
def_var_add_button = tk.Button(def_var_buttons_frame,text="Add", command = lambda: def_add("var"),bg="#727272",relief="solid",bd=border_width,fg="#efa207")


def_if_text_name = tk.Label(def_if_text_frame,text='If what',bg="#404142",fg="#efa207")
def_if_text_commands = tk.Label(def_if_text_frame,text='Then do',bg="#404142",fg="#efa207")
def_if_cancel_button = tk.Button(def_if_buttons_frame,text="Cancel", command=lambda: def_cancel("if"),bg="#727272",relief="solid",bd=border_width,fg="#efa207")
def_if_add_button = tk.Button(def_if_buttons_frame,text="Add", command = lambda: def_add("if"),bg="#727272",relief="solid",bd=border_width,fg="#efa207")
def_if_print_button = tk.Button(def_if_buttons_frame,text="Print", command = def_if_print,bg="#727272",relief="solid",bd=border_width,fg="#efa207")
def_if_input_button = tk.Button(def_if_buttons_frame,text="Input", command = def_if_input,bg="#727272",relief="solid",bd=border_width,fg="#efa207")
def_if_var_button = tk.Button(def_if_buttons_frame,text="Variable", command = def_if_var,bg="#727272",relief="solid",bd=border_width,fg="#efa207")

def_if_print_text = tk.Label(def_if_print_text_frame,text='What to print?',bg="#404142",fg="#efa207")
def_if_print_cancel_button = tk.Button(def_if_print_buttons_frame,text="Cancel", command=lambda: def_cancel("if print"),bg="#727272",relief="solid",bd=border_width,fg="#efa207")
def_if_print_add_button = tk.Button(def_if_print_buttons_frame,text="Add", command = lambda: def_add("if print"),bg="#727272",relief="solid",bd=border_width,fg="#efa207")
def_if_print_advanced_button = tk.Button(def_if_print_buttons_frame,text="Advanced", command = lambda: def_if_advanced("print"),bg="#727272",relief="solid",bd=border_width,fg="#efa207")
def_if_print_advanced_text = tk.Label(def_if_print_advanced_text_frame,text='What to print(mark places for variables with {}',bg="#404142",fg="#efa207")
def_if_print_advanced_variables = tk.Label(def_if_print_advanced_text_frame,text='What variables do you want them to represent?',bg="#404142",fg="#efa207")
def_if_print_advanced_cancel_button = tk.Button(def_if_print_advanced_buttons_frame,text="Cancel", command=lambda: def_if_advanced_cancel("print"),bg="#727272",relief="solid",bd=border_width,fg="#efa207")
def_if_print_advanced_add_button = tk.Button(def_if_print_advanced_buttons_frame,text="Add", command = lambda: def_if_advanced_add("print"),bg="#727272",relief="solid",bd=border_width,fg="#efa207")

def_if_input_text = tk.Label(def_if_input_text_frame,text='What do you want it to ask?',bg="#404142",fg="#efa207")
def_if_input_text_name = tk.Label(def_if_input_text_frame,text='What is the name of the input?',bg="#404142",fg="#efa207")
def_if_input_type = tk.Label(def_if_input_text_frame,text='What type is the input(int,float or str)',bg="#404142",fg="#efa207")
def_if_input_cancel_button = tk.Button(def_if_input_buttons_frame,text="Cancel", command=lambda:def_cancel("if input"),bg="#727272",relief="solid",bd=border_width,fg="#efa207")
def_if_input_add_button = tk.Button(def_if_input_buttons_frame,text="Add", command =lambda: def_add("if input"),bg="#727272",relief="solid",bd=border_width,fg="#efa207")

def_if_var_text = tk.Label(def_if_var_text_frame,text='Variable name and value',bg="#404142",fg="#efa207")
def_if_var_cancel_button = tk.Button(def_if_var_buttons_frame,text="Cancel", command=lambda: def_cancel("if var"),bg="#727272",relief="solid",bd=border_width,fg="#efa207")
def_if_var_add_button = tk.Button(def_if_var_buttons_frame,text="Add", command = lambda: def_add("if var"),bg="#727272",relief="solid",bd=border_width,fg="#efa207")


if_button = tk.Button(frame2,text="If", command=cmd_if,bg="#727272",fg="#efa207",relief="solid",bd=border_width)
if_button.pack(fill=tk.X)

if_text_name = tk.Label(frame9,text='If what',bg="#404142",fg="#efa207")
if_text_commands = tk.Label(frame9,text='Then do',bg="#404142",fg="#efa207")
if_cancel_button = tk.Button(if_buttons_frame,text="Cancel", command=lambda: cancel("if"),bg="#727272",relief="solid",bd=border_width,fg="#efa207")
if_add_button = tk.Button(if_buttons_frame,text="Add", command = lambda: add("if"),bg="#727272",relief="solid",bd=border_width,fg="#efa207")
if_print_button = tk.Button(if_buttons_frame,text="Print", command = if_print,bg="#727272",relief="solid",bd=border_width,fg="#efa207")
if_input_button = tk.Button(if_buttons_frame,text="Input", command = if_input,bg="#727272",relief="solid",bd=border_width,fg="#efa207")
if_var_button = tk.Button(if_buttons_frame,text="Variable", command = if_var,bg="#727272",relief="solid",bd=border_width,fg="#efa207")

if_print_text = tk.Label(if_print_text_frame,text='What to print?',bg="#404142",fg="#efa207")
if_print_cancel_button = tk.Button(if_print_buttons_frame,text="Cancel", command=lambda: if_cancel("print"),bg="#727272",relief="solid",bd=border_width,fg="#efa207")
if_print_add_button = tk.Button(if_print_buttons_frame,text="Add", command = lambda: if_add("print"),bg="#727272",relief="solid",bd=border_width,fg="#efa207")
if_print_advanced_button = tk.Button(if_print_buttons_frame,text="Advanced", command = lambda: if_advanced("print"),bg="#727272",relief="solid",bd=border_width,fg="#efa207")
if_print_advanced_text = tk.Label(if_print_advanced_text_frame,text='What to print(mark places for variables with {}',bg="#404142",fg="#efa207")
if_print_advanced_variables = tk.Label(if_print_advanced_text_frame,text='What variables do you want them to represent?',bg="#404142",fg="#efa207")
if_print_advanced_cancel_button = tk.Button(if_print_advanced_buttons_frame,text="Cancel", command=lambda: if_advanced_cancel("print"),bg="#727272",relief="solid",bd=border_width,fg="#efa207")
if_print_advanced_add_button = tk.Button(if_print_advanced_buttons_frame,text="Add", command = lambda: if_advanced_add("print"),bg="#727272",relief="solid",bd=border_width,fg="#efa207")

if_input_text = tk.Label(if_input_text_frame,text='What do you want it to ask?',bg="#404142",fg="#efa207")
if_input_text_name = tk.Label(if_input_text_frame,text='What is the name of the input?',bg="#404142",fg="#efa207")
if_input_type = tk.Label(if_input_text_frame,text='What type is the input(int,float or str)',bg="#404142",fg="#efa207")
if_input_cancel_button = tk.Button(if_input_buttons_frame,text="Cancel", command=lambda:if_cancel("input"),bg="#727272",relief="solid",bd=border_width,fg="#efa207")
if_input_add_button = tk.Button(if_input_buttons_frame,text="Add", command =lambda: if_add("input"),bg="#727272",relief="solid",bd=border_width,fg="#efa207")

if_var_text = tk.Label(if_var_text_frame,text='Variable name and value',bg="#404142",fg="#efa207")
if_var_cancel_button = tk.Button(if_var_buttons_frame,text="Cancel", command=lambda: if_cancel("var"),bg="#727272",relief="solid",bd=border_width,fg="#efa207")
if_var_add_button = tk.Button(if_var_buttons_frame,text="Add", command = lambda: if_add("var"),bg="#727272",relief="solid",bd=border_width,fg="#efa207")




#TextBox----------------------------------------------------------------------------------------------------
textbox=tk.Text(frame4,height=42,bg="#727272",fg="white",border=0)
textbox.pack(fill=tk.BOTH)

#Top Menu-----------------------------------------------------------------------------------------------------------

menu = tk.Menu(root)
root.config(menu=menu)

build_menu=tk.Menu(menu)
build_menu.add_command(label='Build',command=lambda: file(text))

menu.add_cascade(label="Build",menu=build_menu)
#Project Name------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------------


frame.place(relx=0.5,rely=0, anchor=tk.N)
frame2.place(x=5,y= 100,anchor=tk.W)
grid_frame2.place(x=30,y= 100,anchor=tk.W)
frame3.place(x=43,y=105)
frame4.place(relx=0.95,y=35, anchor= tk.NE)
frame5.place(x=90,y=180,anchor=tk.W)
frame6.place(relx=0.80,y=20, anchor=tk.E)
frame7.place(x=55,y=80, anchor=tk.W)
frame8.place(x=55,y=60,anchor=tk.W)
building_frame.place(relx=0.5,rely=0.5,anchor=tk.CENTER)
frame9.place(x=55,y=80)
frame10.place(x=80,y=125)
frame11.place(x=135,y=100)

def_buttons_frame.place(x=55,y=310)
def_print_text_frame.place(x=700,y=90)
def_print_buttons_frame.place(x=690,y=135)
def_print_advanced_text_frame.place(x=600,y=90)
def_print_advanced_buttons_frame.place(x=690,y=175)
def_input_text_frame.place(x=700,y=80)
def_input_buttons_frame.place(x=760,y=205)
def_var_text_frame.place(x=700,y=120)
def_var_buttons_frame.place(x=725,y=165)
def_if_text_frame.place(x=50, y= 380)
def_if_buttons_frame.place(x=50,y=610)

if_buttons_frame.place(x=55,y=310)
if_print_text_frame.place(x=700,y=90)
if_print_buttons_frame.place(x=690,y=135)
if_print_advanced_text_frame.place(x=600,y=90)
if_print_advanced_buttons_frame.place(x=690,y=175)
if_input_text_frame.place(x=700,y=80)
if_input_buttons_frame.place(x=760,y=205)
if_var_text_frame.place(x=700,y=120)
if_var_buttons_frame.place(x=725,y=165)


def_if_print_text_frame.place(x=700,y=290)
def_if_print_buttons_frame.place(x=690,y=335)
def_if_print_advanced_text_frame.place(x=600,y=290)
def_if_print_advanced_buttons_frame.place(x=690,y=375)
def_if_input_text_frame.place(x=700,y=280)
def_if_input_buttons_frame.place(x=760,y=405)
def_if_var_text_frame.place(x=700,y=320)
def_if_var_buttons_frame.place(x=725,y=365)

root.state("zoomed")
#root.attributes("-fullscreen",True)
#root.resizable(False,False)
root.minsize(1280,720)
root.mainloop()
input()
