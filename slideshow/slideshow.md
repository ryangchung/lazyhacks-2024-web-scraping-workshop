---
marp: true
author: Ryan Chung
size: 16:9
theme: uncover
class: inverted
style: |
    section {
        margin-left: 0;
        text-align: left;
        justify-content: start;
    }

    ul, ol {
        margin-left: 0;
    }

    section ul p {
        margin-bottom: 0;
    }

    img[alt~="center"] {
        display: block;
        margin: 0 auto;
    }
---
<br />

# Lazy Data Collection: An Intro to Python Web Scraping

December 7th, 2024
By: Ryan Chung
For LazyHacks 2024

---

<br />

### About Me

![bg left:48% height:5in](images/profile.jpg)
* 3rd Year Carleton University Computer Science Student
* Bachelor of Computer Science Student
* Interested in large-scale systems

---
<br />

### Prerequisites for this presentation
- Python3
  - [python.org/downloads](https://www.python.org/downloads/)
- Selenium
  - Once Python is installed:
  - `pip install selenium`

<br/>

![bg right:45% w:50% vertical](images/python-logo.jpg)
![bg right:45% w:25% vertical](images/selenium-logo.png)

---
<br />

### What is Web Scraping?
* **Automated** process of extracting data from websites
* Extract information that you cannot find in plain data
  * Web page, not accessible through an API
* To collect information, you can either:
  * Hard Way: Manually collect information
  * **Lazy Way:** Automate using a script!
    * Do once, never again

---
<br />

### Website to scrape
Link: https://ca.finance.yahoo.com/world-indices/

<br/>

![center w:1000](images/website-scrape.png)

---
<br />

### Visually looking for information
Link: https://ca.finance.yahoo.com/world-indices/

<br/>

![center w:800](images/draw.png)

---
<br />

### How would we automate this?
- Inspect the HTML for the structure (CTRL + Shift + I)

![center w:500](images/real-html.png)

---
<br />

### Selenium

![bg right:33% w:128px](images/selenium-logo.png)

* Automation tool used for web scraping in Python, using a **web browser to render websites**.
* Page navigation and locating elements **like a real user**
* Some other options are tools such as BeautifulSoup do static scraping (only HTML)

---
<br />

### Project Setup
Let's set up our a project to start this workshop!
1. Create a folder called `demo/`
2. Create a `main.py` file within the folder
3. Add the following code to the `main.py` file:

```python
print("Hello, World!")
```

4. Run the file (within the directory): `python main.py`

---
<br />

### Code Code Code...

---
<br />

### Thanks for listening!
Any questions?
<br />
<br />
**Feel free to out during the event if you would like to talk about anything, including choosing a university major, career, or growing in tech!**