from pathlib import Path
from urllib.request import urlopen
import json, subprocess, tempfile

SHA = 'e687bd3cd85ae2d903313222b12f5e3587b0d81d'
LIVE = f'https://rawcdn.githack.com/ryanyuuuua/pet-shop/{SHA}/promptgpt/gemini.html'
SRC = f'https://raw.githubusercontent.com/ryanyuuuua/pet-shop/{SHA}/promptgpt/gemini.html'

def get(url):
    with urlopen(url, timeout=30) as r:
        assert r.status == 200, (url, r.status)
        return r.read().decode('utf-8')

live = get(LIVE)
src = get(SRC)
assert live == src
for marker in [
    'Curated Prompt Library', 'gemini-3.8-flash', 'const ALL=buildLibrary()',
    'function _friendlyTitle', '_friendlyTitle(c[0],focus,m[0])',
    'id="customNeed"', '幫我改成我需要嘅版本',
    'async function customizeCurrentPrompt', 'copyCustom', 'pg-fav-v2'
]:
    assert marker in live, marker
assert 'Array.from({length:1000}' not in live

script = live.split('<script>',1)[1].split('</script>',1)[0]
start = script.index('const C=')
marker = 'const ALL=buildLibrary();'
end = script.index(marker,start) + len(marker)
segment = script[start:end]
runtime = '''
console.log('RUNTIME_QA='+JSON.stringify(window.__PROMPTGPT_QA));
console.log('RUNTIME_ALL='+ALL.length);
console.log('TITLE_SAMPLE='+ALL.slice(0,8).map(x=>x.title).join(' || '));
const bad=/Master Build|Expert Audit|Strategy First|Production Ready|Optimization|Research Backed|Rapid MVP|A\\/B Experiment|Reverse Engineer|Decision Framework|Troubleshoot|SOP System/;
if(ALL.length!==2048)process.exit(21);
if(window.__PROMPTGPT_QA.minQuality<94)process.exit(22);
if(window.__PROMPTGPT_QA.categories!==64)process.exit(23);
if(ALL.some(p=>bad.test(p.title)))process.exit(24);
if(!ALL.some(p=>p.title.includes('完整製作：')))process.exit(25);
if(!ALL.some(p=>p.title.includes('專業檢查並改善：')))process.exit(26);
console.log('FRIENDLY_TITLE_RUNTIME=PASS');
'''
with tempfile.TemporaryDirectory() as td:
    td = Path(td)
    runtime_file = td/'runtime.js'
    runtime_file.write_text('global.window={};\n'+segment+runtime)
    out = subprocess.run(['node', str(runtime_file)], check=True, text=True, capture_output=True)
    print(out.stdout, end='')
    compile_file = td/'compile.js'
    compile_file.write_text('new Function('+json.dumps(script)+'); console.log("FULL_SCRIPT_SYNTAX=PASS");')
    out2 = subprocess.run(['node', str(compile_file)], check=True, text=True, capture_output=True)
    print(out2.stdout, end='')

print('LIVE_HTTP_STATUS=200')
print('SOURCE_HTTP_STATUS=200')
print('CDN_MATCHES_SOURCE=PASS')
print('V3_CDN_MARKERS=PASS')
print('PROMPTGPT_V3_VERIFY=PASS')
