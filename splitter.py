from pypdf import PdfReader, PdfWriter
import os

def split_all_pages(input_path, output_dir):
    """
    Splits each page of the PDF into separate files.
    """
    try:
        reader = PdfReader(input_path)
        for i, page in enumerate(reader.pages):
            writer = PdfWriter()
            writer.add_page(page)
            output_path = os.path.join(output_dir, f"page_{i+1}.pdf")
            with open(output_path, 'wb') as out_file:
                writer.write(out_file)
    except Exception as e:
        raise RuntimeError(f"Failed to split all pages: {e}")

def split_page_range(input_path, output_dir, start, end):
    """
    Splits a range of pages from the PDF into a single file.
    """
    try:
        reader = PdfReader(input_path)
        writer = PdfWriter()
        num_pages = len(reader.pages)
        if start < 1 or end > num_pages or start > end:
            raise ValueError("Invalid page range.")
        for i in range(start - 1, end):
            writer.add_page(reader.pages[i])
        output_path = os.path.join(output_dir, f"pages_{start}_to_{end}.pdf")
        with open(output_path, 'wb') as out_file:
            writer.write(out_file)
    except Exception as e:
        raise RuntimeError(f"Failed to split page range: {e}")

def split_custom_pages(input_path, output_dir, pages):
    """
    Splits custom pages from the PDF into separate files.
    """
    try:
        reader = PdfReader(input_path)
        num_pages = len(reader.pages)
        for i in pages:
            if i < 1 or i > num_pages:
                raise ValueError(f"Page number {i} is out of range.")
            writer = PdfWriter()
            writer.add_page(reader.pages[i - 1])
            output_path = os.path.join(output_dir, f"page_{i}.pdf")
            with open(output_path, 'wb') as out_file:
                writer.write(out_file)
    except Exception as e:
        raise RuntimeError(f"Failed to split custom pages: {e}")