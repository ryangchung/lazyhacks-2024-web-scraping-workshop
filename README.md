# LazyHacks 2024 Presentation
Workshop run for LazyHacks 2024 titled "Lazy Data Collection: An Intro to Python Web Scraping".

### Slides
Slides can be found in the `slideshow/` directory. You can compile or preview them using [Marp](https://marp.app/).

To view:
```bash
cd slideshow
npm install
```

You can then run them (instructions from the [Marp repository](https://github.com/marp-team/marp-cli)):
```bash
# Convert slide deck into HTML
npx @marp-team/marp-cli@latest slideshow.md
npx @marp-team/marp-cli@latest slideshow.md -o output.html

# Convert slide deck into PDF
npx @marp-team/marp-cli@latest slideshow.md --pdf
npx @marp-team/marp-cli@latest slideshow.md -o output.pdf

# Convert slide deck into PowerPoint document (PPTX)
npx @marp-team/marp-cli@latest slideshow.md --pptx
npx @marp-team/marp-cli@latest slideshow.md -o output.pptx

# Watch mode
npx @marp-team/marp-cli@latest -w slideshow.md

# Server mode (Pass directory to serve)
npx @marp-team/marp-cli@latest -s ./slides
```

### Demo Code
The code for this workshop can be found in the `demo/` directory. Python3 is required for this demo.

To run:
```bash
pip install selenium
python main.py
```