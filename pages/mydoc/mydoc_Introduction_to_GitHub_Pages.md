---
title: Test_Page
tags: [formatting]
keywords: datatables, tables, grids, markdown, multimarkdown, jquery plugins
last_updated: July 16, 2016
datatable: true
summary:
sidebar: mydoc_sidebar
permalink: mydoc_Introduction_to_GitHub_Pages.html
folder: mydoc
---


# General remarks

creating new pages and content for GitHub pages is quiet simple as we can write content in HTML or with Markdown Language (ML) most of the rest will be taggled by the theme, which contains the layout and design information. If you want to manipulate some of the content you can easily do so by creating a local branch, modifying it locally, or directly online in the github repo from which the Website will be posted.


## Creating your first on Page
For you first own website just use an allready existing page as a Template, copy it and modify it. Please keep the header intact and only modify the entries as described later. For the syntax on what is possible see the GitHub own ML guideline which can be found here: https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax. 

For the header it is important that you create a new and if possible unique permalink which will be required as a local link to the page. the naming schema is quite simple, just name it with a .html at the end and without a slash, as slasches indicate directories and subdirectories. For the other entries feel free to add the correct information.

If you have finished your first page, we need to set links and bind it into the infrastructure in such a way that it can be accesed form every page. Here it is quite simple just go into the respective file for the sidebar and edit the respective entry. In our case, the sidebar should be available under "_data/sidebars/my_docsidebar.yml".
Here we need to set a new entry for the sidebar. Depending on wheter you want the page to be a chapter, subchapter or subsubchapter you need to decide where it should be placed inside the hierarchy. for a chapter copy
 """  - title: NFDI4Cat
    output: web, pdf
    folderitems:
    - title: Overview
      url: /mydoc_NFDI4Cat_Overview.html
      output: web, pdf """
