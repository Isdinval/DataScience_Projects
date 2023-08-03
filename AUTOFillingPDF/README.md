Welcome to my PDF Auto-Filling Python script repository! This project is designed to streamline the process of automatically filling PDF forms with data, making it faster and more efficient to manage documents that require repetitive information.

# About the Script
The Python script in this repository leverages the powerful PyPDF2 library to interact with PDF files. It offers the following functionalities:

* Form Field Filling: The script reads a source PDF file, extracts its form fields, and then populates these fields with user-provided data from a dictionary.
* Checkbox Detection: The script can also detect checkboxes within the PDF and determine whether they are checked or unchecked.
* Customization: Users can easily adapt the script to work with different PDF templates and data structures, making it suitable for a wide range of PDF auto-filling tasks.

# How to Use
* Setting Up: Ensure you have Python and the required libraries (PyPDF2) installed. Clone this repository to your local machine.
* Configuring Data: Prepare a dictionary with key-value pairs, where the keys represent the form field names in the PDF, and the values contain the data you want to populate.
* Filling PDFs: Execute the script, providing the path to your source PDF and the desired output destination. The script will automatically fill the form fields and create a new PDF with the data.
* Checkbox Detection: In addition to form field filling, the script also includes a function to detect checkboxes within the PDF, making it suitable for working with PDFs that contain interactive elements.
