import csv
import polib

class Const:
    PO_MSGID = "原文"
    PO_MSGSTR = "翻訳"
    DQ = "\""
    LF = "\n"

po = polib.pofile('sabun.po')

with open('sabun.csv', 'w') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    #todo 複数形と単数形で分ける
    for entry in po:
        if entry.msgid_plural == "":
            writer.writerow([entry.msgctxt, entry.msgid, entry.msgid_plural, entry.msgstr])
        else:
            writer.writerow([entry.msgctxt, entry.msgid, entry.msgid_plural, entry.msgstr_plural[0]])
