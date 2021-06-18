import csv
import polib

class Const:
    PO_MSGID = "原文"
    PO_MSGID_PLURAL = "原文(複数形)"
    PO_MSGSTR = "翻訳"
    DQ = "\""
    LF = "\n"

class GenModPo:
    def main():
        file_in = open("./mod.csv", "r", encoding="utf-8", errors="", newline="" )

        mod_csv = csv.DictReader(
            file_in, delimiter=",",
            doublequote=True,
            lineterminator="\n",
            quotechar='"',
            skipinitialspace=True)

        mod_po = polib.POFile()

        for row in mod_csv:
            # 単数形のみ
            if row.get(Const.PO_MSGID_PLURAL) == "":
                entry = polib.POEntry(
                    msgid = row.get(Const.PO_MSGID),
                    msgstr = row.get(Const.PO_MSGSTR))
            # 複数形あり
            else:
                entry = polib.POEntry(
                    msgid = row.get(Const.PO_MSGID),
                    msgid_plural = row.get(Const.PO_MSGID_PLURAL),
                    msgstr_plural = {0: row.get(Const.PO_MSGSTR)})

            mod_po.append(entry)

        file_in.close()
        mod_po.save(fpath="mod.po")

    def unused():
        base_po = polib.pofile('ja.po', check_for_duplicates = True)
        entries_to_add = []

        num = 0
        for mod_entry in mod_po:
            if num % 100 == 0:
                print (num, " / ", len(mod_po))
            num = num + 1
            add_entry = True
            for base_entry in base_po:
                # update
                if polib.escape(base_entry.msgid) == polib.escape(mod_entry.msgid):
                    base_entry.msgstr = mod_entry.msgstr
                    base_entry.msgstr_plural = mod_entry.msgstr_plural
                    add_entry = False
                    break
            if add_entry:
                entries_to_add.append(mod_entry)

        for new_entry in entries_to_add:
            base_po.append(new_entry)

        file_out = open('cataclysm-dda.po', 'w', encoding='UTF-8')
        file_out.write(base_po.__unicode__())
        file_out.close()

GenModPo.main()
