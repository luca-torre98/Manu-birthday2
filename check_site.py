"""Static, dependency-free checks run in GitHub Actions before publishing."""
from pathlib import Path
from html.parser import HTMLParser
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    'index.html', 'style.css', 'script.js',
    'assets/teatro-opera.png',
    'assets/beethoven-fur-elise.mp3',
    'assets/favicon.svg',
]

class LocalLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if 'id' in attributes:
            self.ids.add(attributes['id'])
        for key in ('src', 'href'):
            val = attributes.get(key, '')
            if val and not val.startswith(('http:', 'https:', 'mailto:', 'data:', '#', '/')):
                self.refs.append(val.split('?', 1)[0].split('#', 1)[0])


def main():
    errors = []
    for item in REQUIRED:
        path = ROOT / item
        if not path.is_file() or path.stat().st_size == 0:
            errors.append(f'File assente o vuoto: {item}')

    if not errors:
        html = (ROOT / 'index.html').read_text(encoding='utf-8')
        css = (ROOT / 'style.css').read_text(encoding='utf-8')
        js = (ROOT / 'script.js').read_text(encoding='utf-8')
        parser = LocalLinks()
        parser.feed(html)
        for ref in parser.refs:
            if not (ROOT / ref).is_file():
                errors.append(f'Riferimento HTML non trovato: {ref}')
        for match in re.finditer(r'url\(\s*["\']?([^\)"\']+)', css):
            ref = match.group(1).strip()
            if not ref.startswith(('data:', 'http:', 'https:', '/', '#', '%23')):
                if not (ROOT / ref).is_file():
                    errors.append(f'Riferimento CSS non trovato: {ref}')
        for element in re.findall(r"getElementById\(['\"]([^'\"]+)", js):
            if element not in parser.ids:
                errors.append(f'ID richiesto da JavaScript non trovato: {element}')
        if not (ROOT / 'assets/beethoven-fur-elise.mp3').read_bytes()[:3] == b'ID3':
            errors.append('Il file audio non sembra un MP3 valido')
        if (ROOT / 'assets/teatro-opera.png').read_bytes()[:8] != b'\x89PNG\r\n\x1a\n':
            errors.append('Lo sfondo non sembra un PNG valido')
        if 'src="assets/beethoven-fur-elise.mp3"' not in html:
            errors.append('Audio non collegato alla pagina')
        if re.search(r'(?<![\w/])/(?:assets|style\.css|script\.js)', html + css + js):
            errors.append('Sono stati trovati possibili percorsi assoluti non adatti a GitHub Pages')
    if errors:
        print('\n'.join('ERRORE: ' + e for e in errors), file=sys.stderr)
        return 1
    print('OK: pagina, CSS, JavaScript, immagini e audio sono pronti per GitHub Pages.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
