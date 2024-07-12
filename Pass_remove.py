import os
from PyPDF2 import PdfReader, PdfWriter

def remove_password(input_file, output_folder, password):
    try:
        # Create a PdfReader object
        reader = PdfReader(input_file)
        
        # Check if the PDF is encrypted
        if reader.is_encrypted:
            reader.decrypt(password)
        
        # Create a PdfWriter object
        writer = PdfWriter()
        
        # Add all pages to the writer object
        for page_num in range(len(reader.pages)):
            writer.add_page(reader.pages[page_num])
        
        # Define the output file path
        output_file = os.path.join(output_folder, f"{os.path.basename(input_file)}")
        
        # Write the decrypted PDF to the output file
        with open(output_file, 'wb') as out_pdf:
            writer.write(out_pdf)
        
        print(f"Successfully removed password from {input_file} and saved to {output_file}")
    
    except Exception as e:
        print(f"Failed to remove password from {input_file}: {e}")

def process_pdfs_in_folder(input_folder, output_folder, password):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # List all PDF files in the input folder
    pdf_files = [os.path.join(input_folder, file) for file in os.listdir(input_folder) if file.endswith('.pdf')]
    
    for input_file in pdf_files:
        # Remove password protection and save to the output folder
        remove_password(input_file, output_folder, password)

# Folder containing the encrypted PDF files
input_folder = r"C:\Users\Mansi Sareen\Documents\MyProjects\The Big Catch"

# Folder to save the decrypted PDFs
output_folder = r"C:\Users\Mansi Sareen\Documents\MyProjects\Decrypted Files\The Big Catch"

# Password for the PDF files
password = "BBDPJ7234A"

# Process the PDF files
process_pdfs_in_folder(input_folder, output_folder, password)
