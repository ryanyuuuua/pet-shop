from pathlib import Path

site_path = Path('promptgpt/gemini.html')
site = site_path.read_text()

# Only run the legacy V2 builder when the site is still on the old 1000-prompt
# structure. The current curated site is already V2 and must not be rebuilt
# from assumptions that target the old markup.
if 'Curated Prompt Library' not in site or 'const ALL=buildLibrary()' not in site:
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
else:
    print('CURATED_V2_ALREADY_PRESENT=SKIP_LEGACY_REBUILD')

# Always apply the V3 UX layer so both fresh rebuilds and existing Curated V2
# sites keep human-readable titles and the AI prompt customizer.
upgrade_path = Path('promptgpt/upgrade_v3_titles_customizer.py')
upgrade_code = upgrade_path.read_text()
compile(upgrade_code, str(upgrade_path), 'exec')
exec(upgrade_code, {'__name__': '__main__'})
