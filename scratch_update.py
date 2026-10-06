import os

target_content = '''            <div>
              <h4 class="font-display text-2xl mb-2">Studio Email</h4>
              <a href="mailto:hello@mozhidigital.com" class="font-body text-lg text-heritage-muted hover:text-heritage-green transition-colors">hello@mozhidigital.com</a>
            </div>
            <div>
              <h4 class="font-display text-2xl mb-2">Headquarters</h4>
              <p class="font-body text-lg text-heritage-muted leading-relaxed">
                100 Digital Avenue, Suite 404<br>
                San Francisco, CA 94107
              </p>
            </div>'''

replacement_content = '''            <div>
              <h4 class="font-display text-2xl mb-2">Studio Email</h4>
              <a href="mailto:mozhicreationshub@gmail.com" class="font-body text-lg text-heritage-muted hover:text-heritage-green transition-colors">mozhicreations@gmail.com</a>
            </div>
            <div>
              <h4 class="font-display text-2xl mb-2">Instagram</h4>
              <a href="https://www.instagram.com/mozhi.creations/" target="_blank" rel="noopener noreferrer" class="font-body text-lg text-heritage-muted hover:text-heritage-green transition-colors flex items-center gap-2">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-instagram"><rect width="20" height="20" x="2" y="2" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" x2="17.51" y1="6.5" y2="6.5"/></svg>
                @mozhi.creations
              </a>
            </div>'''

files = ['contact.html', 'about.html']
for file in files:
    try:
        with open(file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        if target_content in content:
            content = content.replace(target_content, replacement_content)
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Successfully updated {file}")
        else:
            print(f"Target content not found in {file}")
    except Exception as e:
        print(f"Error processing {file}: {e}")
