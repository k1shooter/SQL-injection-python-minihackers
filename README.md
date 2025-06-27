# SQL-injection-python-minihackers
SQL injection tools by python for restricted purposes.

I cannot upload server-side script. Please edit server-side parameters of yours(base link, columb name, table name, databases...)
## installation
- Python

- requests

## server environment
- mysql database

- php server

- json encoded response

## hack1.py

1. Given table name and columb name of user information

2. Given one sql injection vulnerability

3. Server(task1.php) gets two POST parameters, userid, and passwd. task1.php checks the userid and passwd, and returns the nickname when they are matched.

- extract all user information(userid, nickname, passwd)

- inject query = " SELECT userid, nickname FROM task1_user WHERE userid = '{$userid}' AND passwd = '{$passwd}' "

- no bypassing

result like :

```
[ userid / nickname / passwd ] :
admin / Administrator / very_hard_password!
user / Asdf1234 / qwe123
maratang / MaraTang / maramara
starlight / Niceman / rkskekfkakqktk
glassy / Yona / potato
user2 / dlkbmlkm / password
nomoreidea / Coke / helpme
guest / Supervisor / guest
```

## hack2.py

1. User admin has a 24-length hexadecimal (0-9 and a-f) password. 

2. Given one sql injection vulnerability

3. Server(task2.php) gets two POST parameters, userid, and passwd. task2.php checks the userid and passwd, and tells whether login is successful or not.

4. Users’ credentials are stored in userid and passwd columns of table task2_user

- extract admin's password

- inject query = " SELECT 1 FROM task2_user WHERE userid = '{$userid}' AND passwd = '{$passwd}' "

- Bypass whitespace filtering, paranthesis filtering.

result like :

```
password : 7b58ac86d491df82a37c8db5
```

## hack3.py

1. User admin has a 24-length hexadecimal (0-9 and a-f) password. 

2. Given one sql injection vulnerability

3. Server(task3.php) gets two POST parameters, userid, and passwd. task3.php checks the userid and passwd, and tells whether login is successful or not.

4. Users’ credentials are stored in userid and passwd columns of table task3_user

- extract admin's password

- inject query = " SELECT 1 FROM task3_user WHERE userid = '{$userid}' AND passwd = '{$passwd}' "

- Bypass whitespace filtering, 'like' filtering.

result like :

```
password : 7b58ac86d491df82a37c8db5
```

## hack4.py

1. Assume that you know only database information that you can obtain through the source code, such as the table name (task4_user) and the column name (userid).

2. Assume that the table that you should find is in the same database as the table 'task4_user' (ASSIGN_2).

3. Server(task4.php) gets a single POST parameter, q. task4.php searches task4_user table with search query q, and shows all results that contain q.

- find some secret string stored somewhere. The secret string starts with an exclamation mark (!) and also ends with an exclamation mark.

- inject query = " SELECT userid FROM task4_user WHERE userid LIKE '%{$q}%' "

- no bypassing

result like :

```
The Secret String : !WOW_YOU_FOUND_SECRET!
```
