from tkinter import *
import random 
root=Tk()
root.title("1D List")
root.geometry("400x400")
label_list=Label(root)
label_sorted_list=Label(root)
label_list.place(relx=0.5,rely=0.2,anchor=CENTER)
label_sorted_list.place(relx=0.5,rely=0.6,anchor=CENTER)
list_items=["Bag","snacks","ball","disk","bottle","bat"]
def generate_list():
    random_list=random.sample(range(0,5),1)
    label_list["text"]="the list of items is  "+str(list_items)
    label_sorted_list["text"]="Put item number "+str(random_list)+" in the bag"
button1=Button(root, text="Which item to put in the bag", command=generate_list)
button1.place(relx=0.5,rely=0.4,anchor=CENTER)
root.mainloop()

