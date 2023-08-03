# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 16:08:32 2023

@author: Olivi
"""
# =============================================================================
# LIBRAIRIES
# =============================================================================
import PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.generic import BooleanObject, NameObject, IndirectObject
import json
from argparse import ArgumentParser
from pathlib import Path


                
# =============================================================================
# FUNCTIONS
# =============================================================================

def set_need_appearances_writer(writer: PdfFileWriter):
    # See 12.7.2 and 7.7.2 for more information: http://www.adobe.com/content/dam/acom/en/devnet/acrobat/pdfs/PDF32000_2008.pdf
    try:
        catalog = writer._root_object
        # get the AcroForm tree
        if "/AcroForm" not in catalog:
            writer._root_object.update({
                NameObject("/AcroForm"): IndirectObject(len(writer._objects), 0, writer)
            })

        need_appearances = NameObject("/NeedAppearances")
        writer._root_object["/AcroForm"][need_appearances] = BooleanObject(True)
        # del writer._root_object["/AcroForm"]['NeedAppearances']
        return writer

    except Exception as e:
        print('set_need_appearances_writer() catch : ', repr(e))
        return writer


# =============================================================================
# INIT
# =============================================================================
source_pdf_path = r"C:\Users\Olivi\OneDrive\Documents\AUTOFillingPDF\MES MS015 - Prefilled-2.pdf"
dest_pdf_path = r"C:\Users\Olivi\OneDrive\Documents\AUTOFillingPDF\outputpdf.pdf"



# =============================================================================
# READ PDF FIELD
# =============================================================================
# METHOD 1 : read field (get the first one)
reader = PdfFileReader(source_pdf_path)
page = reader.pages[0]
fields = reader.get_form_text_fields()
fields == {"key": "value", "key2": "value2"}
print(fields)

# METHOD 2 : read field (get the first one)
reader.get_fields()
# print(fields)



# =============================================================================
# CREATE DICTIONNARY TO CHANGE ELEMENTS INSIDE THE PDF : KEY : VALUE
# =============================================================================
data_dict = {
    "TA_NameCompany": "Tax7 Accountants",
    "TA_Phone" : "0280651116",
    "App_FirstGivName" : "DummyFirst",
    "App_FamName" : "DummyLast",
    "App_DOB1" : "01",
    "App_DOB2" : "01",
    "App_DOB3" : "1980",
    "App_Phone" : "0400999999",
    "App_Email1" : "dummy@dummy.com.au",
    "App_Add2" : "1 Dummyland Road",
    "App_Add4" : "Dummyland NSW",
    "App_PC" : "2000",
    "App_POAdd2" : "PO BOX Q28",
    "App_POAdd4" : "Queen Victoria Building NSW",
    "App_POPC" : "1230",
    "FY1" : "22",
    "FY2" : "23",
    "Dec_FullName" : "DummyFirst DummyLast",
    "Dec_Date1" : "27",
    "Dec_Date2" : "07",
    "Dec_Date3" : "2023",
}



# =============================================================================
# WRITE PDF
# =============================================================================
writer = PdfFileWriter()
set_need_appearances_writer(writer)

writer.updatePageFormFieldValues(page, fields=data_dict)
writer.addPage(page)

# write "output" to PyPDF2-output.pdf
dest_pdf_path = r"C:\Users\Olivi\OneDrive\Documents\AUTOFillingPDF\outputpdf.pdf"

with open(dest_pdf_path, "wb") as fh:
    writer.write(fh)

# =============================================================================
# DETECT CHECKBOXES
# =============================================================================
def detect_checkboxes(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        num_pages = pdf_reader.getNumPages()

        for page_num in range(num_pages):
            page = pdf_reader.getPage(page_num)
            if '/Annots' not in page:
                continue

            annotations = page['/Annots']
            for annotation in annotations:
                if isinstance(annotation, PyPDF2.generic.IndirectObject):
                    # Resolve the IndirectObject reference to get the actual annotation object
                    annotation = pdf_reader.getObject(annotation)

                if '/Type' in annotation and annotation['/Type'] == '/Annot':
                    # The object is an annotation (including checkboxes)

                    if '/Subtype' in annotation and annotation['/Subtype'] == '/Widget':
                        # The object is a form field (including checkboxes)

                        if '/MK' and '/AS' in annotation:

                            mk_dict = annotation['/MK'].getObject()
                            if '/CA' in mk_dict:
                                # The /CA key specifies the annotation's normal caption (off-state caption).
                                # The /AS key specifies the annotation's appearance state.
                                ca_value = mk_dict['/CA']
                                as_value = annotation['/AS']
                                print(ca_value)
                                print(as_value)
                                if ca_value == '4' and as_value == '/Yes':
                                    # '/8' indicates the normal state (unchecked) and '/4' indicates the appearance state for the checked checkbox.
                                    print("Checkbox is checked on page", page_num + 1)
                                elif ca_value == '4' and as_value == '/Off':
                                    # '/l' and '/n' are also common values for checkbox states.
                                    print("Checkbox is not checked on page", page_num + 1)
                                print("  ")

            
                        
detect_checkboxes(source_pdf_path)

