export http_proxy="http://kitayama.tetsuya.pfu%40jp.fujitsu.com:1223334444@yto.proxy.nic.fujitsu.com:8080"
export https_proxy="http://kitayama.tetsuya.pfu%40jp.fujitsu.com:1223334444@yto.proxy.nic.fujitsu.com:8080"

wget https://docs.google.com/spreadsheets/d/1FRi2SYbTpyhduzmoVmI6R06VCvZfuhnkHkqrV5LUXCs/export?format=csv -O mod.csv
python gen.py
msgcat mod.po ja.po -o cataclysm-dda.po
msgfmt cataclysm-dda.po -o cataclysm-dda.mo
