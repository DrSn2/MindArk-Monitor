# MindArk-Monitor

[![Quick Overview Schematic](./docs/images/mamon-20170114.png)](./docs/MindArk-Monitor-Design.pdf)

Monitors the [MindArk Career site](http://www.mindark.com/career/current-positions/) for changes, then send notifications to the user.

  - Using headless driver, selenium 3 for python 3, open the job listings site.
  - Search for the class name, 'jobApplication'.
  - If it exists
    - Search for jobentries.
    - For every entry
      - Check if already saved, and stored version is less than 7 days old.
        - If not saved or saved is too old, then save all relevant info on entry
        - Notify user via email

This was mainly created as a fun excuse to implement gmail, selenium and mysql into a python applicaton, and practice deployment.

### Tech

The solution was developed and tested with the following tech and their respective versions:

* [Python 3.5.2][py352] - Programming language
* [Selenium 3.03][sel303] - Web Browser Automation
* [PhantomJS 2.1][pjs21] - Headless Web Browser
* [MySQL Server 5.7.17][mysql5717] - SQL Database
* [Gmail][gm] - Google's mail solution

### Design

[![Flow Chart](./docs/images/mamon-flow-20170114.png)](./docs/MindArk-Monitor-Design.pdf)

[![Classes Schematic](./docs/images/mamon-classes-20170114.png)](./docs/MindArk-Monitor-Design.pdf)

See the [docs folder](./docs) for more.

### Installation

#### Install the dependencies.

* [Python 3.4][py352] or newer
* [Selenium 3][py352] or newer
* [PhantomJS 2.1][py352] or newer
* [MySQL Server 5.7.17][py352] or newer

#### Install python libraries

##### Selenium library
```sh
pip install selenium
```
[Official installation documentation](http://selenium-python.readthedocs.io/installation.html)
##### PyMySQL library
```sh
pip install pymysql
```
[Official installation documentation](https://github.com/PyMySQL/PyMySQL)

##### Setup the database schema, tables and create the user

###### The Database Schema

```sql
CREATE SCHEMA `mamonitor` DEFAULT CHARACTER SET utf8 ;
```

###### The Job Entries Table

```sql
CREATE TABLE `mamonitor`.`jobentries` (
  `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  `found` DATETIME NOT NULL,
  `name` NVARCHAR(255) NOT NULL,
  `description` TEXT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  INDEX `nameindex` (`name` ASC));
```

###### The Log Table

```sql
CREATE TABLE `mamonitor`.`log` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `created` DATETIME NOT NULL,
  `message` VARCHAR(255) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC));
```
###### Create the User

Create a MySQL user called 'mam_user'.

Then grant 'SELECT', 'UPDATE' and 'INSERT' rights to the entire 'mamonitor'-schema.

##### Create or use an existing Gmail Account with low security settings.

You now have to [allow "less secure apps"](https://www.google.com/settings/security/lesssecureapps) to be used with the account.

My email notificatin solution is based on an [article](http://naelshiab.com/tutorial-send-email-python/) talking about the native smtp library in python 3+.

##### Set up the Config File
Copy the conf-template.

Insert the correct values.


*Note: phantomjs value should be the executable path, relative or absolute. e.g. './pjs.exe'

### Todos

 - Weekly reports.
  - The current solution is to age the entries, adding them as new entries after 7 days.

License
----

MIT

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [py352]: <https://www.python.org/>
   [sel303]: <http://www.seleniumhq.org/>
   [pjs21]: <http://phantomjs.org/>
   [mysql5717]: <https://www.mysql.com/>
   [gm]: <https://mail.google.com>
