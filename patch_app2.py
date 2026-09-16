import re
with open('builder/app.js', 'r') as f:
    content = f.read()

branding_old = r"""    // Story section
    const storyTextEl = document.getElementById('storyText');
    if (storyTextEl) storyTextEl.textContent = story;"""

branding_new = r"""    // Story section
    const storyTextEl = document.getElementById('storyText');
    if (storyTextEl) storyTextEl.textContent = story;

    const storyEyebrow = isKu ? (c.aboutUs.eyebrowKu || c.aboutUs.eyebrowEn || 'کەلەپووری ئێمە') : (c.aboutUs.eyebrowEn || 'Our Heritage');
    const storyTitle = isKu ? (c.aboutUs.titleKu || c.aboutUs.titleEn || 'بە ئارامگرتن ئامادە کراوە، بە خۆشەویستی برژاوە') : (c.aboutUs.titleEn || 'Crafted with patience, baked with devotion');
    const storyImageUrl = c.aboutUs.imageUrl || 'https://images.unsplash.com/photo-1556910103-1c02745aae4d?w=900&auto=format&fit=crop&q=80';

    const eyebrowEl = document.querySelector('[data-i18n="storyEyebrow"]');
    if (eyebrowEl) eyebrowEl.textContent = storyEyebrow;
    
    const titleEl = document.querySelector('[data-i18n="storyTitle"]');
    if (titleEl) titleEl.textContent = storyTitle;
    
    const imgEl = document.querySelector('.story__img');
    if (imgEl) imgEl.src = storyImageUrl;"""

content = content.replace(branding_old, branding_new)

with open('builder/app.js', 'w') as f:
    f.write(content)

