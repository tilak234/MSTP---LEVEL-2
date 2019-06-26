# Project 1: Student Report Generation
### by Tilak Babu

## What it is and does

Python small project that produces data for N no.of Students Data along with marks, then analysis that data and produce a report with Total Students,Highest,Lowest,Average Mark and First,Second,Third,Failed Student count

To secure that report, We can Encrypt that file as well as Decrypt

## Required Libraries and Dependencies

Python 3.x is required to run this project. The Python executable should be in
your default path, which the Python installer should have set.

## Project contents

This project consists for the following files and folders:

* dataGen.py - python script to Generate Student data
* reportGen.py - python script to analyse and Generate Report
* encryption.py - for encrypt the report
* decryption.py - for decrypt the report
* names.py - contains the first name and last name for generating random names
* key.py - admin can set a key for encryption and decryption purpose.


- StudentData - Student Data files will be created here.
- ReportData - Report files will be created here.
- Encryption - for Encryption files
- Decryption - for Dectyption files

## How to Run Project

Download the project zip file to you computer and unzip the file.

Open the text-based interface for your operating system (e.g. the terminal in Linux, the command prompt in Windows).

Navigate to the project directory and type in the following command:

Step 1: Generate Student Data, will ask you to enter howmany students data needed. you can enter as you like
```
$ python dataGen.py
Howmany students data needed???4000
StudentData20181025180938.csv Generated Successfully
```

Step 2: Generate a report and analyse the student data. will ask you to enter file name. You can give already generated StudentData file name.
```
$ python reportGen.py
Enter file name - StudentData20181025180938.csv
Report20181025181036.txt Generated Successfully
```

Step 3: Encrypt the report file. enter already generated report file name.

```
$ python encryption.py
Enter file name to Encrypt - Report20181025181036.txt
Encrypted Successfully
```

Step 4: Decrypt the Encrypted file.

```
$ python decryption.py
Enter file name to Decrypt - enc.txt
Decrypted Successfully
```