from tkinter import filedialog, messagebox

def select_files(title="Select PDF files", filetypes=[("PDF Files", "*.pdf")], multiple=True):
    """
    Opens a file dialog to select one or more PDF files.
    """
    if multiple:
        files = filedialog.askopenfilenames(title=title, filetypes=filetypes)
        return list(files) if files else []
    file = filedialog.askopenfilename(title=title, filetypes=filetypes)
    return file if file else None

def save_file(title="Save PDF", defaultextension=".pdf"):
    """
    Opens a file dialog to select a save location for a PDF.
    """
    file = filedialog.asksaveasfilename(title=title, defaultextension=defaultextension, filetypes=[("PDF Files", "*.pdf")])
    return file if file else None

def select_directory(title="Select Output Folder"):
    """
    Opens a dialog to select a directory.
    """
    directory = filedialog.askdirectory(title=title)
    return directory if directory else None

def show_error(message):
    """
    Shows an error message dialog.
    """
    messagebox.showerror("Error", message)

def show_info(message):
    """
    Shows an information message dialog.
    """
    messagebox.showinfo("Success", message)