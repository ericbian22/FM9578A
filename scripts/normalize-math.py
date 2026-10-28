import re,pathlib
root=pathlib.Path(__file__).resolve().parents[1]
p=root/'formula-sheet.html'
s=p.read_text(encoding='utf8')
s=re.sub(r'\$\$[\s\S]+?\$\$|\$[^$\n]+?\$',lambda m:m.group(0).replace('<','&lt;').replace('>','&gt;'),s)
p.write_text(s,encoding='utf8')
p=root/'assets/site.css'
p.write_text(p.read_text(encoding='utf8').replace("@import url('');",''),encoding='utf8')
