---
title: Test_Page
tags: [formatting]
keywords: datatables, tables, grids, markdown, multimarkdown, jquery plugins
last_updated: July 16, 2016
datatable: true
summary:
sidebar: mydoc_sidebar
permalink: n4cat_soft_Protege.html
folder: mydoc
---

# Protégé 5.6 

## General Aspects

|Aspect                                |Description                                                                        |
|:-------------------------------------|:----------------------------------------------------------------------------------|
|Main Function                         |General ontology editing tool with Reasoners, SPARQL and other features implemented|
|Repository/Website                    |https://protege.stanford.edu/products.php                                          |
|Additional Repos/Development Platfroms|https://github.com/protegeproject                                                  |
|License                               |BSD 2-Clause "Simplified" License                                                  |
|Software Documentation                |https://protegewiki.stanford.edu/wiki/ProtegeDesktopUserDocs                       |
|Issue/Support Contacts                |https://protege.stanford.edu/support.php#mailing-lists; https://github.com/protegeproject/protege-distribution/issues|
|Programming environemt                |Java                                                                               |
|(Optional) Found Literature/Projects  |                                                                                   |


### General Description

Example:
General Editig tool with multiple plugins for reasoners, visualisations a.s.o. It is the go to software for starters and often serves as a validation tool even after changing to other editing software. Thus it is considered basicly as a benchmark in the fashion, that if an Ontology cant be opend and handeled with protege, it is not sufficent for the regular consumer.

### Known Issues:
(please always contact the founders of a specific software and wait for their response before publishing an issue here. Please also link to any issue you have send to them, to allow later contributors to check whether they arte solved)

Several plugins are faulty, such as the fact++ Reasoner, which needs a special patch to be able o run. It has a unique owl2 syntax and interpreation format which advanced from the regular owl-manchester syntax into an openly defined structure, which often requires workarounds, such as using SWRL-rules for representing left hand side logic.


