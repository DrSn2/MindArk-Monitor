# MindArk-Monitor


[![LoopAware](http://icons.iconarchive.com/icons/custom-icon-design/pretty-office-9/64/search-file-icon.png)](http://loopaware.com)

Monitors the [MindArk Career site](http://www.mindark.com/career/current-positions/) for changes, then send notifications to the user.

  - Using headless driver, selenium 3 for python 3, open the job listings site.
  - Search for the class name, jobApplication.
  - If it exists
    - Search for all of class name, jobTitle.
    - For every match
      - Check if already saved.
        - If not saved, then save all relevant info on entry
        - Notify user via email

This was mainly made as a fun excuse to implement gmail, selenium and mysql into a python applicaton, and practice deployment.

### Tech

The solution was developed and tested with the following tech and their respective versions:

* [Python 3.5.2][py352] - Programming language
* [Selenium 3.03][sel303] - Web Browser Automation
* [MySQL Server 5.7.17][mysql5717] - SQL Database
* [Gmail][gm] - Google's mail solution

### Installation

The application requires python 3.4+.

...

Install the dependencies.

```sh
$ cd dillinger
$ npm install -d
$ node app
```

Setup the database schema, tables and create the user

...

### Development

Information for developers.

### Todos

 - Weekly reports instead of duplicate db-entries.

License
----

MIT

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [py352]: <http://loopaware.com>
   [sel303]: <http://loopaware.com>
   [mysql5717]: <http://loopaware.com>
   [gm]: <http://loopaware.com>
