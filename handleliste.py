import tkinter as tk

def add_item(event=None):
	item = entry.get()
	if item:
		listbox.insert(tk.END, item)
		entry.delete(0, tk.END)

def remove_item(event=None):
	selected = listbox.curselection()
	if selected:
		listbox.delete(selected)

#Hovedvindu
root = tk.Tk()
root.title("Shopping List")

#Listbox (Display items)
listbox = tk.Listbox(root, width=50)
listbox.pack (padx=10, pady=10)

#User input entry
entry = tk.Entry(root, width=50)
entry.pack(padx=10, pady=5)

entry.bind("<Return>", add_item)

root.bind("<BackSpace>", remove_item)

#Create buttons
add_button = tk.Button(root, text='Add Item', command=add_item)
add_button.pack(padx=10, pady=5)

remove_button = tk.Button(root, text='Remove Item', command=remove_item)
remove_button.pack(padx=10, pady=5)

#Run
root.mainloop()
