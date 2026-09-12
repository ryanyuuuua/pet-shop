from pathlib import Path

wf = Path('.github/workflows/rebuild-promptgpt-library-v2.yml').read_text()
marker = "          python - <<'PY'\n"
start = wf.index(marker) + len(marker)
end = wf.index("\n          PY", start)
block = wf[start:end]
lines = block.splitlines()
code = "\n".join(line[10:] if line.startswith("          ") else line for line in lines)
# The extracted builder embeds JavaScript regexes such as /\s+/g. Python's
# re.sub replacement-string parser treats those backslashes as replacement
# escapes, so switch the generated substitution to a callable replacement.
code = code.replace(
    's, n = re.subn(pattern, block + "const syn=", s, count=1, flags=re.S)',
    's, n = re.subn(pattern, lambda _: block + "const syn=", s, count=1, flags=re.S)'
)
compile(code, 'promptgpt-library-v2-inline', 'exec')
exec(code, {'__name__': '__main__'})

# Always apply the v3 UX layer after a library rebuild so future rebuilds keep
# human-readable titles and the AI prompt customizer.
upgrade_path = Path('promptgpt/upgrade_v3_titles_customizer.py')
upgrade_code = upgrade_path.read_text()
compile(upgrade_code, str(upgrade_path), 'exec')
exec(upgrade_code, {'__name__': '__main__'})
