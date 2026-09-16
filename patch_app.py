import re
with open('builder/app.js', 'r') as f:
    content = f.read()

# Update case 'about'
about_old = r"""      case 'about':
        content.innerHTML = `
          <h4 style="font-family:var(--font-serif);margin-bottom:16px;">Our Story & Heritage</h4>
          <form onsubmit="app.saveAboutSettings(event)">
            <div class="form-group">
              <label class="form-label">Our Story (English)</label>
              <textarea id="cfgAboutEn" class="form-textarea" rows="5">${c.aboutUs.en}</textarea>
            </div>
            <div class="form-group">
              <label class="form-label">Our Story (Kurdish)</label>
              <textarea id="cfgAboutKu" class="form-textarea" rows="5">${c.aboutUs.ku || ''}</textarea>
            </div>
            <button type="submit" class="btn btn--primary">Save Changes</button>
          </form>
        `;
        break;"""

about_new = r"""      case 'about':
        content.innerHTML = `
          <h4 style="font-family:var(--font-serif);margin-bottom:16px;">Our Story & Heritage</h4>
          <form onsubmit="app.saveAboutSettings(event)">
            <div class="form-group">
              <label class="form-label">Image URL</label>
              <input type="text" id="cfgAboutImage" class="form-input" value="${c.aboutUs.imageUrl || 'https://images.unsplash.com/photo-1556910103-1c02745aae4d?w=900&auto=format&fit=crop&q=80'}" />
            </div>
            <div class="form-row">
              <div class="form-group">
                <label class="form-label">Eyebrow / Subtitle (EN)</label>
                <input type="text" id="cfgAboutEyebrowEn" class="form-input" value="${c.aboutUs.eyebrowEn || 'Our Heritage'}" />
              </div>
              <div class="form-group">
                <label class="form-label">Eyebrow / Subtitle (KU)</label>
                <input type="text" id="cfgAboutEyebrowKu" class="form-input" value="${c.aboutUs.eyebrowKu || 'کەلەپووری ئێمە'}" />
              </div>
            </div>
            <div class="form-row">
              <div class="form-group">
                <label class="form-label">Main Title (EN)</label>
                <input type="text" id="cfgAboutTitleEn" class="form-input" value="${c.aboutUs.titleEn || 'Crafted with patience, baked with devotion'}" />
              </div>
              <div class="form-group">
                <label class="form-label">Main Title (KU)</label>
                <input type="text" id="cfgAboutTitleKu" class="form-input" value="${c.aboutUs.titleKu || 'بە ئارامگرتن ئامادە کراوە، بە خۆشەویستی برژاوە'}" />
              </div>
            </div>
            <div class="form-group">
              <label class="form-label">Our Story Text (English)</label>
              <textarea id="cfgAboutEn" class="form-textarea" rows="5">${c.aboutUs.en}</textarea>
            </div>
            <div class="form-group">
              <label class="form-label">Our Story Text (Kurdish)</label>
              <textarea id="cfgAboutKu" class="form-textarea" rows="5">${c.aboutUs.ku || ''}</textarea>
            </div>
            <button type="submit" class="btn btn--primary">Save Changes</button>
          </form>
        `;
        break;"""

content = content.replace(about_old, about_new)

# Update saveAboutSettings
save_about_old = r"""  saveAboutSettings(e) {
    e.preventDefault();
    this.config.aboutUs.en = document.getElementById('cfgAboutEn').value.trim();
    this.config.aboutUs.ku = document.getElementById('cfgAboutKu').value.trim();

    this.saveConfig();
    this.renderBranding();
    this.showToast(this.t('toastSaved'), 'success');
  },"""

save_about_new = r"""  saveAboutSettings(e) {
    e.preventDefault();
    this.config.aboutUs.en = document.getElementById('cfgAboutEn').value.trim();
    this.config.aboutUs.ku = document.getElementById('cfgAboutKu').value.trim();
    this.config.aboutUs.imageUrl = document.getElementById('cfgAboutImage').value.trim();
    this.config.aboutUs.eyebrowEn = document.getElementById('cfgAboutEyebrowEn').value.trim();
    this.config.aboutUs.eyebrowKu = document.getElementById('cfgAboutEyebrowKu').value.trim();
    this.config.aboutUs.titleEn = document.getElementById('cfgAboutTitleEn').value.trim();
    this.config.aboutUs.titleKu = document.getElementById('cfgAboutTitleKu').value.trim();

    this.saveConfig();
    this.renderBranding();
    this.showToast(this.t('toastSaved'), 'success');
  },"""

content = content.replace(save_about_old, save_about_new)

with open('builder/app.js', 'w') as f:
    f.write(content)

