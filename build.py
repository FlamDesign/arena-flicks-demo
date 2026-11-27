"""Builds index.html from src.html: pastes in Flicks Demo Kit v1.1 and the exact Flick tags from flam-links/tags."""
import json, sys
KIT, TAGS = sys.argv[1], sys.argv[2]
s = open('src.html').read().replace('/*KIT*/', open(KIT).read())
tag = lambda slug: open(f'{TAGS}/{slug}/tag.txt').read().strip()
# Some Flicks draw their own "Shop now" as a plain button the kit cannot see; the ad's own button replaces it.
HIDE = ('<script>(function(){var n=0;(function f(){var v=document.querySelector("vertex-player"),r=v&&v.shadowRoot;'
        'if(r&&!r.querySelector("style[data-az]")){var s=document.createElement("style");s.setAttribute("data-az","");'
        's.textContent="button[data-node]:not([data-vertex-diff]){visibility:hidden!important;pointer-events:none!important}";r.appendChild(s)}'
        'if(++n<240)setTimeout(f,250)})()})();</script>')
B = {'westelm': ('West Elm', 'west-elm'), 'mms': ("M&M'S", 'mms'), 'benjerry': ("Ben & Jerry's", 'ben-and-jerrys'),
     'ulta': ('Ulta Beauty', 'ulta-beauty'), 'lego': ('LEGO', 'lego'), 'patagonia': ('Patagonia', 'patagonia'),
     'nike': ('Nike', 'nike'), 'levis': ("Levi's", 'levis'), 'sony': ('Sony', 'sony'), 'yeti': ('YETI', 'yeti'),
     'barkbox': ('BarkBox', 'barkbox'), 'ford': ('Ford', 'ford'), 'lovesac': ('Lovesac', 'lovesac')}
br = {k: {'name': n, 'ar': 'square', 'bg': '#f2f2f2', 'tag': tag(sl) + '\n' + HIDE} for k, (n, sl) in B.items()}
s = s.replace('/*BRANDS*/', json.dumps(br, ensure_ascii=False).replace('</', '<\\/'))
open('index.html', 'w').write(s)
print('index.html', len(s))
