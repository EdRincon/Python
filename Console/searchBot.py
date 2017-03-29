#Busca un texto en todos los archivos de texto de la carpeta e imprime el path absoluto
#Falta que busque archivos en una path a especificar por input y tanto en las archivos en la carpeta como en los de las subcarpetas


import re, os, docx, PyPDF2

print('Palabra a buscar')
palabra = input()
x = 0
docxPatt = re.compile('\w+.docx')
txtPatt = re.compile('\w+.txt')
pdfPatt = re.compile('\w+.pdf')
RC = re.compile(palabra)

for filename in os.listdir('.'):
    nRC = re.compile('\w+(.txt|.docx|.pdf)')
    mo1 = nRC.search(filename)

    if txtPatt.match(filename):
        text = open (filename , 'r')
        texto = text.readlines()

        for wol in texto:
            mo = RC.search(wol)

            if mo != None:
                print(wol)
                print(os.path.abspath('.') + '\\' + filename)
                x = 1
                break

        if x == 1:
            break
        
    elif docxPatt.match(filename):
        doc = docx.Document(filename)
        
        for i in range (len(doc.paragraphs)):
            par = doc.paragraphs[i].text
            mo2 = RC.search(par)

            if mo2 != None:
                print(par)
                print(os.path.abspath('.') + '\\' + filename)
                x = 1
                break
        
        if x == 1:
            break

    elif pdfPatt.match(filename):
        pdfFileObj = open(filename, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        
        for i in range (int(pdfReader.numPages)):
            pag = pdfReader.getPage(i).extractText()
            mo2 = RC.search(pag)

            if mo2 != None:
                print(pag)
                print(os.path.abspath('.') + '\\' + filename)
                x = 1
                break
        
        if x == 1:
            break

    
print('done')
