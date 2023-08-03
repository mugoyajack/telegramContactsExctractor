"""
    A simple program for exctracting contacts from exported telegram json file
"""
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import json
import os


def load_file():
    """
    Load a file from the user's computer.

    :return: None
    """
    # Open a file dialog to let the user choose a file
    file_path = filedialog.askopenfilename()

    # Check if the user has selected a file
    if file_path:
        try:
            # Read the json file
            with open(file_path, "r") as file:
                data = json.load(file)
                # Extract contacts from the json data
                exctract_contacts(data)

        except Exception as e:
            # Show the exception if file is not a valid json file
            messagebox.showerror(
                "Error", "Error occurred while processing the file:\nNot a valid json file")


def exctract_contacts(data):
    """
    Extract contacts from the json data.

    :param data: The json data
    :return: The list of contacts
    """
    # Exctract contacts from the file

    contacts = []
    contacts_data = data.get("contacts", {})
    contacts_list = contacts_data.get("list", [])

    for contact in contacts_list:
        pnumber = contact["phone_number"]
        # Sanitize Phone number
        if pnumber[:2] == "00":
            pnumber = "+"+pnumber[2:]
        contacts.append([contact["first_name"], contact["last_name"], pnumber])

    # Check if contacts are present
    if not contacts_data or not contacts_list:
        messagebox.showinfo("", "No Contacts found in the file")
        return
    else:
        display_contacts(contacts)
        messagebox.showinfo("", "Contacts exctracted successfully")


def display_contacts(data):
    # Clear previous data (if any)
    for item in tree.get_children():
        tree.delete(item)

    # Insert the data into the Treeview widget
    for row in data:
        tree.insert("", "end", values=row)
    # Set background and foreground colors for the Treeview
    tree.tag_configure("odd_row", background="black", foreground="white")
    tree.tag_configure("even_row", background="gray", foreground="white")

    # Apply background and foreground colors to rows
    for idx, item in enumerate(data):
        if idx % 2 == 0:
            tree.item(tree.get_children()[idx], tags=("even_row",))
        else:
            tree.item(tree.get_children()[idx], tags=("odd_row",))

def export_contacts():
    """
    Export contacts to a vcf file.

    :param data: The list of contacts
    :return: None
    """
    # Check if contacts are present
    if not tree.get_children():
        messagebox.showinfo("", "No contacts to export")
        return

    # Open a file dialog to let the user choose a filename
    vcf_path = filedialog.asksaveasfilename()

    # check if the user selected a file
    if vcf_path:
        # Check the file extension and append .vcf if needed
        root, ext = os.path.splitext(vcf_path)
        if ext.lower() != ".vcf":
            vcf_path = root + ".vcf"

        # Save contacts in vcf file
        with open(vcf_path, "w") as file:
            """
            SAMPLE VCARD

            BEGIN:VCARD
            VERSION:2.1
            N:Sparrow;Jack;;;
            FN:Jack Sparrow
            TEL;CELL:+254712345678
            END:VCARD

            """
            # Retrieve the data displayed in the Treeview and use it to create a vcf file
            for item_id in tree.get_children():
                values = tree.item(item_id, 'values')
                fname = values[0]
                lname = values[1]
                pnumber = values[2]

                cont_data = ["BEGIN:VCARD\n", "VERSION:2.1\n", "N:", lname, ";", fname,
                             ";;;\nFN:", fname, " ", lname, "\nTEL;CELL:", pnumber, "\nEND:VCARD\n"]
                file.writelines(cont_data)
def on_closing():
    # Handle the close event
    if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()


# Create the main tkinter window
root = tk.Tk()
root.title("Telegram Contacts Extractor")
root.iconphoto(False, tk.PhotoImage(file='logo.png'))
root.config(bg = "purple")
root.resizable(False, False)
root.protocol("WM_DELETE_WINDOW", on_closing)

# win_width = root.winfo_screenwidth()
win_height = root.winfo_screenheight() - 100
root.geometry("%dx%d" % (600, win_height))


# Create a Treeview widget with columns
tree = ttk.Treeview(root,columns=("First Name", "Last Name",
                    "Phone Number"), show="headings", height=33)

# Set background and foreground colors for the Treeview
tree.tag_configure("odd_row", background="lightgray", foreground="black")
tree.tag_configure("even_row", background="white", foreground="black")

# Set column headings
tree.heading("First Name", text="First Name")
tree.heading("Last Name", text="Last Name")
tree.heading("Phone Number", text="Phone Number")

# Set column widths
tree.column("First Name", width=200)
tree.column("Last Name", width=200)
tree.column("Phone Number", width=200)

tree.place(x=0, y=50)

# Button for loading files
button = tk.Button(root, text="Import JSON File",bg = "blue", fg = "white", command=load_file)
button.place(x=10, y=10)

# Button for saving contacts in a vcf file
button = tk.Button(root, text="Export Contacts",bg = "blue", fg = "white",
                   command=lambda: export_contacts())
button.place(x=450, y=10)


# Start the tkinter event loop
root.mainloop()
