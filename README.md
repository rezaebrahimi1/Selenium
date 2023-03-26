# Selenium
I used this python code to automate manual tests which are performed by QA team.

# Description

## Directories explenation

### base
This dorectory contains common methods that are used in this project frequently. these are diffrent methods that application wants to perform on different elements of web pages for testing or scraping purpose.

## feature
This directory contains two sub-directories:

** scenarios
Define your test scenarios here. Put all scenarios related to a page in a direcory with appropriate name. Also scenario go_to_page help to land to differnet pages of your web applications.  

** steps
Define detail steps related to scenarios here. Each step calls a method which is determined in page_classes directory in root of project.

## page_classes
Define all related operations can be performed on a page for testing or scraping purpose. These operations are used in steps sections. Also since these operations have been used repeatedly through the project, i deploy a common_method class that mentioned earlier.
