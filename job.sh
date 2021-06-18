wget https://docs.google.com/spreadsheets/d/1FRi2SYbTpyhduzmoVmI6R06VCvZfuhnkHkqrV5LUXCs/export?format=csv -O mod.csv
python gen.py
msgfmt cataclysm-dda.po -o cataclysm-dda.mo
