from pypdf import PdfReader, PdfWriter

def merge_pdfs(file_paths, output_path):
    """
    Merges multiple PDF files into a single PDF.

    Args:
        file_paths (list): List of PDF file paths to merge.
        output_path (str): Output file path for the merged PDF.
    """
    writer = PdfWriter()
    for pdf in file_paths:
        try:
            reader = PdfReader(pdf)
            for page in reader.pages:
                writer.add_page(page)
        except Exception as e:
            raise RuntimeError(f"Failed to read {pdf}: {e}")
    try:
        with open(output_path, "wb") as out_file:
            writer.write(out_file)
    except Exception as e:
        raise RuntimeError(f"Failed to write merged PDF: {e}")
