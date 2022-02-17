import os

markdown_files = [x for x in os.listdir(".") if x.endswith(".md")]

# Code to fix links in index.md
index = open("index.md", "r")

index_lines = index.read().split('\n')

print(f"Fixing: ... {index_lines}")

index_lines[:index_lines.index("Links:")]

for f in markdown_files: index_lines.append(f' - {f}')

print(index_lines)



# Code to fix include statements in _config.yml 

os.system('git add .')
os.system('git commit -a -m "Pushing to repo"')
os.system('git push')
