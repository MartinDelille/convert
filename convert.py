import io
import csv
import codecs

inputFile = "Articles.txt"
outputFile = "Qarticles.txt"

params = {
        "600": ("600", "3"),
        "601": ("601", "4"),
        "602": ("602", "5"),
        "603": ("603", "6"),
        "605": ("605", "7"),
        "81": ("601", "4"),
        "87": ("601", "4"),
        "82": ("602", "5"),
        "83": ("603", "6"),
        "85": ("605", "7"),
        "80": ("700", "R"),
        "86": ("800", "8")
}

def encodeToLatin1(data):
    for line in data:
        yield line.encode('latin-1', errors='ignore')

with io.open(inputFile, 'r', encoding='utf-16') as csvfile:
    reader = csv.reader(encodeToLatin1(csvfile), delimiter=';', quotechar='|')

    with open(outputFile, 'w') as outputFile:
        writer = csv.writer(outputFile, delimiter=';')
        header = True
        i = 0
        for row in reader:
            if header:
                writer.writerow(["ACLE1", "DESAPRES", "", "", "", "", "", "", "", "CODESSFAMILLE", "CODEFAMILLE", "CODEVENTILVT", "POIDS"])
                header = False
            else:
                newRow = []
                newRow.append(row[0])
                newRow.append((row[4] + " " + row[5]).strip())
                newRow.append(row[6])
                newRow.append(row[1])
                newRow.append("")
                newRow.append("")
                newRow.append("")
                newRow.append("")
                newRow.append("")
                newRow.append(row[3])
                for k, t in params.items():
                    if row[0].startswith(k):
                        newRow.append(t[0])
                        newRow.append(t[1])
                        break
                else:
                    newRow.append("")
                    newRow.append("")
                newRow.append(row[2])
                writer.writerow(newRow)
                i += 1
