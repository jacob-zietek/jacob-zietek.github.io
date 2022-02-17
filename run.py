import os

markdown_files = [x for x in os.listdir(".") if x.endswith(".md")]

# Code to fix links in index.md
index = open("index.md", "r")

print(index.read())


# Code to fix include statements in _config.yml 

os.system('git add .')
os.system('git commit -a -m "Pushing to repo"')
os.system('git push')
