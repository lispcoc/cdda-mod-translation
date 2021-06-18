wget https://docs.google.com/spreadsheets/d/1FRi2SYbTpyhduzmoVmI6R06VCvZfuhnkHkqrV5LUXCs/export?format=csv -O mod.csv
wget https://raw.githubusercontent.com/CleverRaven/Cataclysm-DDA/master/lang/po/ja.po -O ja.po
python gen.py
msgcat mod.po ja.po -o cataclysm-dda.po --use-first
msgfmt cataclysm-dda.po -o cataclysm-dda.mo
mv cataclysm-dda.* release
