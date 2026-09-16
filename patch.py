import re
with open('builder/body.html', 'r') as f:
    content = f.read()

# Remove the badge
content = re.sub(r'<span class="hero__badge-fresh"[^>]*>.*?</span>\n?\s*', '', content)

with open('builder/body.html', 'w') as f:
    f.write(content)

