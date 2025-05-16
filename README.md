# PDF Merger & Splitter - PyTools

A simple, user-friendly desktop application to merge and split PDF files using Python and Tkinter.

## Features

- **Merge PDFs:** Select and combine multiple PDF files into one.
- **Split PDFs:** 
  - Split all pages into separate files.
  - Extract a range of pages into a new PDF.
  - Extract custom pages as individual PDFs.
- **Intuitive GUI:** No command-line required.

## Requirements

- Python 3.8 or newer
- [pypdf](https://pypdf.readthedocs.io/en/latest/) (see `requirements.txt`)

## Installation

1. **Clone or Download this Repository**

2. **Install Dependencies**

   Open a terminal in the project folder and run:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Application**

   ```
   python main.py
   ```

2. **Use the GUI:**
   - **Merge PDFs:** Go to the "Merge PDFs" tab, select your files, and choose where to save.
   - **Split PDFs:** Go to the "Split PDF" tab and choose your splitting method.

## File Structure

```
PDF_Merger_Splitter/
│
├── README.md
├── main.py
├── gui.py
├── merger.py
├── splitter.py
├── extras.py
├── requirements.txt
```

## Troubleshooting

- If you see errors about missing modules, ensure you installed requirements with `pip install -r requirements.txt`.
- For issues with PDFs, make sure your files are not password-protected or corrupted.

## License

MIT License

---

**Enjoy using PDF Merger & Splitter!**
