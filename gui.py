import tkinter as tk
from tkinter import ttk
from merger import merge_pdfs
from splitter import split_all_pages, split_page_range, split_custom_pages
from extras import select_files, save_file, select_directory, show_error, show_info

def launch_app():
    app = tk.Tk()
    app.title("PDF Merger & Splitter - PyTools")
    app.geometry("520x420")
    app.iconbitmap("assets/icon.ico")
    app.resizable(False, False)

    tab_control = ttk.Notebook(app)

    # Merge Tab
    merge_tab = ttk.Frame(tab_control)
    tab_control.add(merge_tab, text="Merge PDFs")

    def handle_merge():
        files = select_files()
        if not files or len(files) < 2:
            show_error("Please select at least two PDF files to merge.")
            return
        output = save_file()
        if not output:
            return
        try:
            merge_pdfs(files, output)
            show_info("PDFs merged successfully.")
        except Exception as e:
            show_error(str(e))

    ttk.Button(merge_tab, text="Select PDFs & Merge", command=handle_merge).pack(pady=40)

    # Split Tab
    split_tab = ttk.Frame(tab_control)
    tab_control.add(split_tab, text="Split PDF")

    def handle_split_all():
        file = select_files(multiple=False)
        if not file:
            show_error("No PDF file selected.")
            return
        out_dir = select_directory()
        if not out_dir:
            show_error("No output folder selected.")
            return
        try:
            split_all_pages(file, out_dir)
            show_info("PDF split into individual pages.")
        except Exception as e:
            show_error(str(e))

    def handle_split_range():
        file = select_files(multiple=False)
        if not file:
            show_error("No PDF file selected.")
            return
        out_dir = select_directory()
        if not out_dir:
            show_error("No output folder selected.")
            return
        try:
            start = int(start_entry.get())
            end = int(end_entry.get())
            if start > end or start < 1:
                show_error("Invalid page range.")
                return
            split_page_range(file, out_dir, start, end)
            show_info("PDF split by range.")
        except ValueError:
            show_error("Please enter valid numbers for start and end pages.")
        except Exception as e:
            show_error(str(e))

    def handle_split_custom():
        file = select_files(multiple=False)
        if not file:
            show_error("No PDF file selected.")
            return
        out_dir = select_directory()
        if not out_dir:
            show_error("No output folder selected.")
            return
        try:
            pages = [int(x.strip()) for x in custom_entry.get().split(",") if x.strip().isdigit()]
            if not pages:
                show_error("Please enter valid page numbers (e.g. 1,3,5).")
                return
            split_custom_pages(file, out_dir, pages)
            show_info("PDF split by custom pages.")
        except Exception as e:
            show_error(str(e))

    ttk.Button(split_tab, text="Split All Pages", command=handle_split_all).pack(pady=10)

    # Range input
    range_frame = ttk.Frame(split_tab)
    range_frame.pack(pady=5)
    ttk.Label(range_frame, text="Start:").pack(side=tk.LEFT)
    start_entry = ttk.Entry(range_frame, width=5)
    start_entry.pack(side=tk.LEFT, padx=5)
    ttk.Label(range_frame, text="End:").pack(side=tk.LEFT)
    end_entry = ttk.Entry(range_frame, width=5)
    end_entry.pack(side=tk.LEFT, padx=5)
    ttk.Button(split_tab, text="Split Range", command=handle_split_range).pack(pady=10)

    # Custom input
    custom_frame = ttk.Frame(split_tab)
    custom_frame.pack(pady=5)
    ttk.Label(custom_frame, text="Pages (e.g. 1,3,5):").pack(side=tk.LEFT)
    custom_entry = ttk.Entry(custom_frame, width=20)
    custom_entry.pack(side=tk.LEFT, padx=5)
    ttk.Button(split_tab, text="Split Custom", command=handle_split_custom).pack(pady=10)

    tab_control.pack(expand=1, fill="both")
    app.mainloop()