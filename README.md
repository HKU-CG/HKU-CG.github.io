# Best-practices documentation for modifying the website

## Read this before you push anything!
* Don't use `push -f`. It will overwrite other people's changes. Before you push, make sure you pull the latest version of the website.
* After pushing, check if the website is deployed correctly. If it's successfully deployed, you should see a green tick beside the commit. If it fails, you'll see a red cross. If you see a red cross, click on it and check the error message. If you can't figure out what's wrong, ask someone else for help.
* `.md` files in this repo use YAML format. So it's sensitive to the indentation! If you're not confident enough, copy existing files and modify them.
* After it is deployed, it will take a few minutes for the website to be updated. Make sure you check the website to see if your changes are reflected.

## Run the website locally
* Follow instructions on [this page](https://university.wowchemy.com/getting-started/install-hugo/) to install Go and Hugo
* cd into a directory you want to have the file in
* git clone https://github.com/HKU-CG/HKU-CG.github.io
* cd into the HKU-CG.github.io folder
* run `hugo server`
* Check it is up and running at localhost:1313

## How to add your own profile
* Go to `content/authors`
* Create a new folder with your name, e.g., `Taku-Komura`
* Create a `index.md` file in the folder, you're suggested to copy the `index.md` file from other people's folder and modify it accordingly
* Add your profile picture to the folder, and name it `avatar.jpg` or `avatar.png`
* Important: the variable `authors` and `name` should be the same, they should also match the folder name (except the folder uses hyphen (-) instead of space)
* Important: set the variable `weight` as your start year&month (e.g., 202301) so that the order of people is correct. If you're an alumni, set the `weight` as your graduation -year&month (e.g., -202307)
* Important: set your user_groups as one of the following: `Principal Investigator`, `Postdocs`, `Graduate Students`, `Research Assistant`, `Undergraduate Students`, `Postdoctoral Alumni`, `PhD Alumni`, `Masters Alumni`, `Undergraduate Alumni`, `RA Alumni`

## How to add a publication
* Go to `content/publications`
* Create a new folder with the name of your publication, e.g., `2021-TOG-My-Paper-Title`
* Create a `index.md` file in the folder, you're suggested to copy the `index.md` file from other people's folder and modify it accordingly
* Important: the abstract is a variable, so it should be one line (in Markdown format). If you want to change the line, use `<br>`. Some special symbols need to be escaped, for example, if you want to use `:`, you should type `\:`. Here's a detailed list of [Markdown escaping characters](https://github.com/mattcone/markdown-guide/blob/master/_basic-syntax/escaping-characters.md)
* (optional) add a `featured.jpg` or `featured.png` file to the folder, this will be the thumbnail of your publication

## How to add a news
* Go to `content/talk`
* Create a new folder, e.g., `202307-iccv` and create a `index.md` file in the folder

## How to modify the text on the homepage
* Go to `content/authors/admin/_index.md`

## How to add an image in the text
* Put the image in `static/media`
* Use the following syntax (Markdown) to add the image in the text: `![image name](/media/image.png)`

## How to update the logo
* The big logo: `content/authors/admin/avatar.png`
* The small logo: `assets/images/logo.png`
* The website icon: `assets/images/icon.png`  # can also be .svg

## Website Structure Overview

* The general file structure looks like this: https://wowchemy.com/docs/get-started/#remove-any-unused-example-pages
* You can figure out which folders correspond to which tabs on the menu by looking at menus.toml under config\_default
  * for example the "People" tab can be accessed via <website url>/People-Genetic-Logic-Lab and the web code for the content of the page is found under content/People-Genetic-Logic-Lab
* Individual webpages are built using the index.md or _index.md file in the content folder. There are two types of index file:
  * _index.md: it is a simple functionality that displays the rest of the content from the folder based on the view style chosen. It is flanked by "---" at the start and end of the file. Example:

~~~~
---
title: Publications
# View.
#   1 = List
#   2 = Compact
#   3 = Card
#   4 = Citation
view: 1
# Optional header image (relative to `static/media/` folder).
header:
  caption: ""
  image: ""
---
~~~~
  
  * index.md: It is a widget page (A page that will include widgets). The page is flanked by "+++" at the top and bottom. Example:

 ~~~~
+++
# People
type = "widget_page"
headless = false  # Homepage is headless, other widget pages are not.
+++
 ~~~~

* Widgets

  Widgets are functions which take in parameters and generate html code accordingly. There are 3 parts to a widget:

  **Widget Call:** This is an .md file in the directory where the widget is being called. E.g. publications.md in the home directory under content. It is flanked by "+++" and contains the name of the widget being called (in the example case pages), provides a series of parameters for the function to work (headless, active, weight, title, subtitle) and widget specific parameters (content.filters, design, design.background, custom css). For examples of the widget call function for each of the different widgets see /themes/academic/exampleSite/content/home and open any of the .md files other than index.

  **Widget Function:** A widget function is called based on the widget parameter in the widget call. The widget is code (Go's html/template and text/template libraries) interspersed with code to build it (you have functionality like if statements, loops, etc, for more info see: https://gohugo.io/templates/introduction/). There are two locations where the widgets are found: /themes/academic/layouts/partials/widgets or any custom widgets are found in layouts/partials/widgets

  **Widget Data:** The widget may not have anymore data than the parameters provided in the widget call (this is the case for widgets like featurette) or they might link out to get more information (for example the people widget obtains its information by looping through all authors files and filling in the template using the information provided in the author's index file e.g. Chris Myers/_index.md)

* Partials

  Widgets are a subset of partials. Partials are html files that contain go code and are used to provide the general structure of the web page, e.g the navbar, the citation views, page footer etc. You can go in and edit them too but I suggest leaving them alone for now

* Images

  Any image files not associated with authors should go in the static\media file. It can be called in an html image tag using "/media/example.png"

  Author images go in the file associated with the author and must be named avatar.<extension> e.g. avatar.png or avatar.jpg

* CSS

  like most website there are css files. You can go in and edit them to change the way the page appears. Better practice is to use the file for custom scss located under themes\academic\assests\scss\custom.scss. Be careful overriding anything in here as it can drastically affect the way widgets works

## How To's:

* **Import new references**: 
  For this, please install and use the [Academic Import](https://github.com/wowchemy/hugo-academic-cli/#usage) (for alternate instructions see https://wowchemy.com/docs/managing-content/#create-a-publication) command to import new references into the webpage. Please make sure to use the `--overwrite` (to avoid reference duplicates) flags when importing references using the academic import command. Check out https://github.com/wowchemy/hugo-academic-cli/#usage for more information.
  
 NB: currently use this command to run academic import to ensure no additional quotes are added to tags `pip3 install -U git+https://github.com/wowchemy/hugo-academic-cli.git`
 
 If that isn't working tags can be cleaned up using the cleanup_hugo_tagging.py script (make sure the path is to the publications folder) to clean up the extra "" in tags.

  Talking about tags, [Academic Import](https://github.com/wowchemy/hugo-academic-cli/#usage) will automatically generate tags for all references imported, created from a mixture of keywords and titles extracted from the bib information. However, sometimes this can go a-wire and add weird tags. If any tag has a *"."* or a *"?"* or any other non-alphanumerical value, the site won't build. Please make sure you remove all characters that are not alpha-numerical from tags to run correctly.

## Common error and mistakes

* Folders **must not** have any spaces. Use web-friendly hyphens instead.
