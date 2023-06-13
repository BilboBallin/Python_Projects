#Ubuntu: pip install PyPDF2 (einfach in der Konsole)
# Gleiches gilt dann für die anderen OS mit Ubuntu shell

from PyPDF2 import PdfMerger
import sys

#PDF-Dateien die für den Merge in Betracht gezogen werden sollen.
#Dabei bleibt die Reihenfolge für das resultierende MergedPDF.
pdfs = ['1.pdf', '2.pdf', '3.pdf'] 

merger = PdfMerger()

for pdf in pdfs: #kleine fancy Schleife
    merger.append(pdf)

#Endergebnis: Alle betrachteten PDF-Dateien wurden zu einer einheitlichen
#		großen MergedPDF-Dateie zusammengefügt. Nice.
merger.write('merged.pdf')
merger.close()
