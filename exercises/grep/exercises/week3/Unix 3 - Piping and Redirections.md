# Unix 3 - Piping and Redirections

## Tutorial

### Exercise 1

Modify line 1 from the previous example and redirect STDERR (line 2) to a file called file4.

`ls file1 file2 2> file4`

##  Exercise 2

Change the previous command to print line numbers for each user name.

`cat /etc/passwd | cut -d : -f 1 | nl`

### Exercise 3

Change the previous command to get the same output but not using cat command.

`cut -d : -f 1 /etc/passwd | nl`

##  Exercise 4

Store output of the previous command to the file named userlist.

`cut -d : -f 1 /etc/passwd | nl > userlist`

##  Exercise 5

Use echo command and print the following string to STDOUT without double quotes: "backslash -> \"

`echo "backslash -> \\"`

##  Exercise 6

Copy the following script into a text editor. Save the script as simpleifone.sh. Then set its permissions to add x for the user. Next run the script with various arguments and explain how it works.

```bash
#!/bin/bash

#simple if example 
#Paul Sutcliffe

echo  "expecting a single argument "
echo  "command argument \$1 is $1  " 

if [ $1  -eq  1 ] 
then
        echo  "if test is true found 1 that is one "
fi

echo "will now exit"
```

``` bash
chmod u+x simpleifone.sh
./simpleifone.sh 1
```

- Here, if $1 is equal to 1 the then path is executed. Otherwise execution jumps to after the fi statement.

##  Exercise 7

Copy the script into a text editor. Save the script as simpleiftwo.sh. Then set its permissions to add x for the user. Next run the script with various arguments and explain how it works.

```bash
#!/bin/bash

#simple if example 
#Paul Sutcliffe

echo  "expecting a single argument "
echo  "command argument \$1 is $1  " 

if [ $1 -eq 1 ] 
then
        echo  "if test is true found 1 that is one "
else
        echo "if test is false did not find 1 "
fi

echo "will now exit"

```

``` bash
chmod u+x simpleifone.sh
./simpleiftwo.sh 1
```

- Here, if $1 is equal to 1 the then path is executed otherwise the else path is executed. In both cases execution continues from just after the fi statement.

### Exercise 8

Copy the following script into a text editor. Save the script as testfiles.sh. Then set its permissions to add x for the user. Next run the script with various arguments and explain how it works.

```bash
#!/bin/bash

#simple for example 

FILENAMES=`ls` # saves all the filenames in the current directory in a shell variable 

for FILENAME in $FILENAMES # loops through all the filenames; variable FILENAME stores the current one
do
    if [ -f $FILENAME -a -r $FILENAME ] # tests if FILENAME is a file and is readable using file test operators
    then
     echo "$FILENAME is a file and is readable" # if so, prints a message
    fi
done
```

## AWK exercise

Change the previous command and include a day, month and time into the formatted output.

`who | awk '{ print "User "$1" logged in on "$4"."$3" at "$5" from "$6}'`

##  Exercise 1

Use the echo command to create a file called myname which will contain your first name.

`echo "Felix" > myname`

### Exercise 2

Use the echo command again and append your last name to the existing myname file.

`echo "Krull" >> myname`

### Exercise 3

The whoami command prints your effective userid to STDOUT. Use whoami to append your userid to the existing myname file.

`whoami >> myname`

### Exercise 4

The nl command will print line numbers for a given file. Use the nl command to print line number of your myname file and store the output to file called myname.nl

`nl myname > myname.nl`

##  AWK exercise (completely optional)

Create a file called linenumbers which will contain first column (the line numbers) of the myname.nl file

`awk '{ print $1 }' myname.nl > linenumbers`

`cat myname.nl | awk '{ print $1 }'  > linenumbers`

### Exercise 5

Use the ls command to recursively list inode numbers and file names of all files in your home directory.

- The inode number is a unique numerical id for a file and can be disaplyed with option -i.

`ls -i ~/*`

`ls -Ri`

## AWK exercise (completely optional)

Modify your previous command to display only unique inode numbers in descending order.

`ls -i ~/* | awk '{ print $1 }' | sort -unr`

##  Exercise 6

Use the cut command and the Unix /etc/passwd system file to create a list of all users (column 1) and their corresponding home directories (column 6).

`cut -d : -f 1,6 /etc/passwd`

`cat  /etc/passwd | cut -d : -f 1,6`

##  Exercise 7

Run the following command chain on your terminal. NOTE: this command will create/overwrite existing "sh" file in your current working directory!

`echo 'echo "HELLO" 1>&2' > sh; chmod +x sh; ./sh`

- Is the output produced by this command chain STDOUT or STDERR? HINT: you already know how to redirect both file descriptors.

``` bash
$ echo 'echo "HELLO" 1>&2' > sh; chmod +x sh; ./sh > my.out
HELLO
$ cat my.out
$ 
$ 
```

##  Exercise 8

Run the following command chain on your terminal. NOTE: this command will create/overwrite existing "sh" file in your current working directory!

`echo 'cat /etc/anyfile 2>&1' > sh; chmod +x sh; ./sh`

- Is the output produced by this command chain STDOUT or is it STDERR?

- Condition 1) There is no file called anyfile or you don't have read permissions or the file. In this case the error message is directed to STDOUT and ends up going my.out file.

``` bash
$ 
$ echo 'cat /etc/anyfile 2>&1' > sh; chmod +x sh; ./sh > my.out
$ cat my.out
cat: /etc/anyfile: No such file or directory
$ 
```

- Condition 3) There is a non-empty file called /etc/anyfile and you have read permissions for it. The file exits and you can read it so no error is produced. The file is non-empty so it is written to STDOUT. So answer is: if the command produces any output it is written to STDOUT. It never directs its output to STDERR.

``` bash
$ echo 'cat /etc/anyfile 2>&1' > sh; chmod +x sh; ./sh > my.out
$ cat my.out
I am not empty
$ 
```

- Condition 3) There is a empty file called /etc/anyfile and you have read permissions for it. However it is empty so nothing is written to STDOUT.

``` bash
$
$ echo 'cat /etc/anyfile 2>&1' > sh; chmod +x sh; ./sh > my.out
$ cat my.out
```

### Exercise 9

In this exercise we are going to create a simple bash calculator shell script. Your script will accept 2 numbers as arguments upon which an arithmetic calculation will be executed.
The script will allow user to select the arithmetic sign and then calculate the result.
Here is a sample execution of calc.sh script:

```bash
$ cat calc.sh 
#!/bin/bash
PS3="YOUR SELECTION: "
echo PLEASE SELECT ARITHMETIC SIGN:
select sign in "+" "-" "*" "/"
do
   echo Let\'s see....? The answer is: $(($1 $sign $2))
   break
done
```

### Exercise 10

Define a script called create.sh as follows

- check if the only argument passed to the script is a file or a directory
- if the argument is neither a file nor a directory, prompt the user to use it to create either a file or a directory
- (hint: read the solution if you don't know how to do this)

```bash
#!/bin/bash

if [ -d $1 ]
then
 echo "$1 is a directory"
elif [ -f $1 ]
then
 echo "$1 is a file"
else
 echo "$1 does not exist!"
 echo -n "Create(d/f): "
 read choice

 if [ "$choice" == "d" ]
 then
  mkdir $1
 else
  touch $1
 fi
fi
```

### Exercise 11

Define a script called grades.sh as follows

- read a student name from STDIN
- use the only argument passed to the script as the student's mark
- determine and show the grade based on the mark (>= 85: HD, elif >= 75: d, elif >= 65: C, elif >= 50: P, else: Z)
- (hint: read the solution if you don't know how to do this)

```bash
#!/bin/bash
echo -n "Student name: "
read name

if [ $1 -ge 85 ]
then
 grade="HD"
elif (($1 >= 75)) 
then
 grade="D"
elif [ $1 -ge 65 ]
then
 grade="C"
elif [ $1 -ge 50 ]
then
 grade="P"
else
 grade="Z"
fi
echo "$name mark is $1 and grade is $grade"

```

### Exercise 12

Define a script called filewords.sh as follows

- receive a filename as argument (NB: the file contains only a sequence of words and is short)
- copy the content of the file in a shell variable
- use a for loop to print all the words in the file, one per line

```bash
#!/bin/bash

VAR=`cat $1`

for word in $VAR
do
 echo $word
done
```
