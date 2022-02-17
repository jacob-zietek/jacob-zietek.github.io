# Hey, welcome to the documentation for this site.

## Why is this a thing?

I wanted a place to write my thoughts into markdown files and have them automatically uploaded to a website. I guess other people have had this thought before because [Jekyll](https://jekyllrb.com/) is a thing. It does all of the markdown &rarr; HTML stuff for you 👍:. There are some things that need to be configured every time you add a markdown file still, so the [run.py](https://github.com/jacob-zietek/jacob-zietek.github.io/blob/main/run.py) script automates adding the links to [index.md](https://github.com/jacob-zietek/jacob-zietek.github.io/blob/main/index.md) and [_config.yml](https://github.com/jacob-zietek/jacob-zietek.github.io/blob/main/_config.yml).

If you want to configure this for yourself:

- Change the URL link in [run.py](https://github.com/jacob-zietek/jacob-zietek.github.io/blob/main/run.py) to your own
- Add your own markdown files to the repository 
- Run `python3 run.py`, this will automatically set up [index.md](https://github.com/jacob-zietek/jacob-zietek.github.io/blob/main/index.md) and [_config.yml](https://github.com/jacob-zietek/jacob-zietek.github.io/blob/main/_config.yml) for you and push the changes

Special thanks to this guy &rarr;  https://nicolas-van.github.io/easy-markdown-to-github-pages/
