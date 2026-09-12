from pathlib import Path

wf = Path('.github/workflows/rebuild-promptgpt-library-v2.yml').read_text()
marker = "          python - <<'PY'\n"
start = wf.index(marker) + len(marker)
end = wf.index("\n          PY", start)
block = wf[start:end]
lines = block.splitlines()
code = "\n".join(line[10:] if line.startswith("          ") else line for line in lines)
compile(code, 'promptgpt-library-v2-inline', 'exec')
exec(code, {'__name__': '__main__'})
