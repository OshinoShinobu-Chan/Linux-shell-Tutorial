import os
import yaml

subfolder = os.listdir('./docs')

nav = [{"初级篇": []}, {"中级篇": []}, {"高级篇": []}, {"附录": []}]

for folder in subfolder:
    if os.path.isdir(os.path.join('./docs', folder)):
        chapter = []
        files = os.listdir(os.path.join('./docs', folder))
        for file in files:
            if file.endswith('.md') and file != 'index.md':
                chapter.append({file[:-3]: os.path.join(folder, file)})
        if len(chapter) > 0:
            for item in nav:
                if folder in item:
                    item[folder] = chapter


mkdocs = {}
with open('./mkdocs.yml', 'r', encoding='utf-8') as f:
    mkdocs = yaml.load(f, Loader=yaml.FullLoader)
    mkdocs['nav'] = nav

with open('./mkdocs.yml', 'w', encoding='utf-8') as f:
    yaml.dump(mkdocs, f, allow_unicode=True, default_flow_style=False, sort_keys=False)  