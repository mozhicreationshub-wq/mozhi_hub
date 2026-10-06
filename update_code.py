import re
with open('code.html', 'r', encoding='utf-8') as f:
    content = f.read()

target = '''      <div class="grid grid-cols-1 lg:grid-cols-12 gap-16 items-center">
        <div class="lg:col-span-6 flex flex-col gap-10">'''
repl = '''      <div class="max-w-4xl mx-auto">
        <div class="flex flex-col gap-10">'''
content = content.replace(target, repl)

target2 = '''        </div>
        
        <div class="lg:col-span-6">
          <div class="w-full aspect-[4/5] p-2 border border-heritage-border bg-white">
            <img class="w-full h-full object-cover grayscale opacity-90 contrast-125" src="https://images.unsplash.com/photo-1497215728101-856f4ea42174?q=80&w=1470&auto=format&fit=crop" alt="Classic architecture and timeless digital structure"/>
          </div>
        </div>
      </div>'''
repl2 = '''        </div>
      </div>'''
content = content.replace(target2, repl2)

with open('code.html', 'w', encoding='utf-8') as f:
    f.write(content)
