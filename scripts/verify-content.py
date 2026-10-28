import pathlib,json,re
root=pathlib.Path(__file__).resolve().parents[1]
data=json.loads((root/'assets/course-data.js').read_text(encoding='utf8')[14:-2])
assert len(data['lectures'])==9
sections=lambda n:{s['title']:s['body'] for s in data['lectures'][n-1]['sections']}
assert r'\Delta z' in sections(8)['Increment simulation']
assert r'dx=a(x,t)dt+b(x,t)dz' in sections(9)['Local conditional moments']
assert r'dx_t=a(x_t,t)dt+b(x_t,t)dW_t' in sections(9)['Local conditional moments']
assert r'\varepsilon_1=u' in sections(9)['Correlated normals']
assert all('W_' not in case[1] and 'Z(' in case[1] for case in data['dependence'])
assert r'W_2' in data['exercises'][10]['answers'][0]['body']
assert not any(')^+' in s['body'] or 'X^+' in s['body'] for l in data['lectures'] for s in l['sections'])
assert [e['number'] for e in data['exercises']]==list(range(1,21))
parts=[4,4,5,4,5,4,5,5,6,6,5,5,4,5,5,5,5,5,5,5]
assert [len(e['answers']) for e in data['exercises']]==parts
assert sum(parts)==97
assert all(a.get('prompt','').strip() for e in data['exercises'] for a in e['answers'])
assert all(e.get('question','').strip() for e in data['extra'])
assert [e[0] for e in data['dependence']]==list('abcdefghi')
assert all(e.get('reasoning','').count('<li>')>=2 for e in data['exercises'])
assert all(any(s['body'].count('<li>')>=5 for s in l['sections']) for l in data['lectures'])
figures=[src for l in data['lectures'] for s in l['sections'] for src in re.findall(r'<img src="([^"]+)"',s['body'])]
assert len(figures)==8 and all((root/src).is_file() for src in figures)
coverage=json.loads((root/'downloads/source-coverage.json').read_text())
assert len(coverage)==11 and sum(s['pages'] for s in coverage)==261
for source in coverage[:9]:
    assert [p for g in source['groups'] for p in range(g['first'],g['last']+1)]==list(range(1,source['pages']+1))
for name in ['index.html','formula-sheet.html','assets/course-data.js','downloads/FM9578A-notes.md']:
    text=(root/name).read_text(encoding='utf8')
    for forbidden in ['CPSC','hinge loss','Huber loss','k-means','naive Bayes','LASSO']:
        assert forbidden.lower() not in text.lower(),(name,forbidden)
    for formula in re.findall(r'\$\$[\s\S]+?\$\$|\$[^$\n]+?\$',text):
        if name.endswith('.html'):assert '<' not in formula,('Unescaped mathematical inequality',formula)
assert (root/'downloads/FM9578A-formula-sheet.pdf').read_bytes().startswith(b'%PDF')
print('PASS content: 9 lectures; 20 questions/97 subparts; 9 dependence cases; 261 mapped pages; subject isolation; math escaping; PDF present.')
