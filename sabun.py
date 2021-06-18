import csv
import polib

class Const:
    PO_MSGID = "原文"
    PO_MSGSTR = "翻訳"
    DQ = "\""
    LF = "\n"

original_po = polib.pofile('ja.po')
mod_po = polib.pofile('cataclysm-dda.po')
entries_to_add = []

print (len(mod_po))
i = 0
flag = False
for mod_entry in mod_po:
    if i % 100 == 0:
        print(i, len(entries_to_add))
    i=i+1
    add_entry = True
    for base_entry in original_po:
        if polib.escape(base_entry.msgid) == polib.escape(mod_entry.msgid):
            add_entry = False
            break
    if add_entry:
        entries_to_add.append(mod_entry)

with open('sabun.csv', 'w') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    #todo 複数形と単数形で分ける
    for entry in entries_to_add:
        writer.writerow([entry.msgid, entry.msgstr])
