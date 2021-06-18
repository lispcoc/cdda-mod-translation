# -*- coding: utf-8 -*-
import csv
import polib
import datetime

class Const:
    PO_MSGCTXT = "msgctxt"
    PO_MSGID = "msgid"
    PO_MSGID_PLURAL = "msgid_plural"
    PO_MSGSTR = "msgstr"
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

        mod_po = polib.POFile(
            check_for_duplicates = True
        )

        for row in mod_csv:
            # 単数形のみ
            msgctxt = row.get(Const.PO_MSGCTXT)
            if msgctxt == "":
                msgctxt = None
            msgid = row.get(Const.PO_MSGID)
            msgid_plural = row.get(Const.PO_MSGID_PLURAL)
            msgstr = row.get(Const.PO_MSGSTR)
            if row.get(Const.PO_MSGID_PLURAL) == "":
                entry = polib.POEntry(
                    msgctxt = msgctxt,
                    msgid = msgid,
                    msgstr = msgstr)
            # 複数形あり
            else:
                entry = polib.POEntry(
                    msgctxt = msgctxt,
                    msgid = msgid,
                    msgid_plural = msgid_plural,
                    msgstr_plural = {0: msgstr})

            mod_po.append(entry)

        file_in.close()

        # ヘッダの生成
        dt_now = datetime.datetime.now()
        mod_po.metadata = {
            'Project-Id-Version': 'cataclysm-dda mod',
            'Report-Msgid-Bugs-To': 'https://github.com/lispcoc ',
            'POT-Creation-Date': dt_now.isoformat(),
            'PO-Revision-Date': dt_now.isoformat(),
            'Last-Translator': 'N/A',
            'Language-Team': 'N/A',
            'MIME-Version': '1.0',
            'Content-Type': 'text/plain; charset=utf-8',
            'Content-Transfer-Encoding': '8bit',
        }

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
