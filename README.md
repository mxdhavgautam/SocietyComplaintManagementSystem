### About
The purpose of this project is to help manage the many complaints of a residential area or society. It is capable of keeping records of lodged complaints and keep track of their status, i.e., pending or resolved.

The idea for this program was inspired after seeing how in a residential area, a lot of the complaint records regarding plumbing/wood work or any such thing are maintained in a register or notebook and keeping those records up to date is a tedious and inefficient task and how that system needed a refresh. This program streamlines the same process while utilizing concepts such as **Database Management, Error Handling,** and **File Handling.**
- Database Management: All complaints and their statuses are stored and managed in a MySQL Database.
- Error Handling: Use of Try and Except statements + Errors formatted to a user understandable syntax while maintaining program execution on encountering the same.
- File Handling: All complaints entered are saved in the form of a record in a "log file" in the same directory of the program as a data backup.

This is designed to maintain efficiency in keeping track of various complaints and their status. It makes all the complaints readily available to be tapped into which corresponds to a happy and efficient society.

It is a **user-friendly program** with an **easy-to-understand source code**.

### BuildNotes/Readme

1. This program requires **Python 3.5 or above, MySQL Community 8.0.x or above, and Python MySQL Connector as well as pymysql (both installed using pip)** to be installed and working to function properly. Edits to both the `sql-tablescreation-final.py` and `main-final.py` files are needed to change MySQL credentials according to user specific values for the program to work, namely:
- the host, user and passwd values from `db = cntr.connect(host = 'localhost' , user = 'xyz' , passwd = '1234')` in line 3 of `sql-tablescreation-final.py`.
- the same in line 9, `mycon=mysql.connector.connect(host = 'localhost', user = 'xyz', password = '1234', database = 'comp_sys')`, of `main-final.py`.

2. The `sql-tablescreation-final.py` file is **REQUIRED** to be run **ONLY ONCE** before running the `main-final.py` python file, which as it's name suggests is the main program.

3. Any subsequent reruns of the `sql-tablescreation-final.py` file after the first successful execution **will** yield an error saying table already exists. This is known, and is intended behavior.

4. To have a clean slate/fresh install, you will have to manually delete the tables and database, as well as the `comp-log.txt` file before re-running the `sql-tablescreation-final.py` program.