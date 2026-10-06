$content = Get-Content code.html -Raw -Encoding UTF8
$content = $content -replace '(?s)<div class="grid grid-cols-1 lg:grid-cols-12 gap-16 items-center">\s*<div class="lg:col-span-6 flex flex-col gap-10">', '<div class="max-w-4xl mx-auto">
        <div class="flex flex-col gap-10">'
$content = $content -replace '(?s)</div>\s*<div class="lg:col-span-6">\s*<div class="w-full aspect-\[4/5\] p-2 border border-heritage-border bg-white">\s*<img class="w-full h-full object-cover grayscale opacity-90 contrast-125"[^>]*>\s*</div>\s*</div>\s*</div>', '</div>
      </div>'
Set-Content code.html -Value $content -Encoding UTF8

$content2 = Get-Content about.html -Raw -Encoding UTF8
$content2 = $content2 -replace '(?s)<!-- New Studio Image Section -->.*?</div>', ''
Set-Content about.html -Value $content2 -Encoding UTF8
