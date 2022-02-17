import os

markdown_files = [x for x in os.listdir(".") if x.endswith(".md")]

# Code to fix links in index.md
index = open("index.md", "r")
index_lines = index.read().split('\n')
print(f"Fixing: ... {index_lines}")
print("")
index_lines = index_lines[:index_lines.index("Links:")+1]
for f in markdown_files: index_lines.append(f' - {f}')
print('\n'.join(index_lines))
print("")
# Code to fix include statements in _config.yml 

config = open("_config.yml", "r")
config_lines = config.read().split('\n')
print(f"Fixing: ... {config_lines}")
print("")
config_lines = config_lines[:config_lines.index("include:")+1]
for f in markdown_files: config_lines.append(f' - {f}')
print('\n'.join(config_lines))
print("")

index = open("index.md", "w")
index.write('\n'.join(index_lines))

config = open("_config.yml", "w")
config.write('\n'.join(config_lines))

index.close()
config.close()

os.system('git add .')
os.system('git commit -a -m "Pushing to repo"')
os.system('git push')
