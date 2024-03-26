# Unix 2 - Scripting basics

## Tutorial

###  Exercise 1

- Create the empty files "f1 f2 f3 g1 g2 g3 g4 g5" in the ~/usp2 directory. View the permission settings for the files you created.

```bash
mkdir ~/usp2
cd ~/usp2
touch f1 f2 f3 g1 g2 g3 g4 g5
ls -l
```

### Exercise 2

- Change the file permissions for the file "f1" in the directory "~/usp2" so that no user has write permission, do this in such a way that the other permissions remain unchanged.

```bash
cd ~/usp2
chmod a-w f1
ls -l
```

### Exercise 3

Restore the permissions for the file "f1" in the directory "~/usp2" to there original settings.

```bash
chmod u+w,g+w f1
ls -l
```

## Exercises

### Exercise 1

Write a script that outputs your name. So if your name is "Joe Smith". The script should echo "Joe Smith" to the screen.

```bash
#!/bin/bash
#This is a script to print Joe Smiths name.
echo 'Joe Smith'
```

### Exercise 2

Write a script that prompts the user for a name and writes the result to the screen.

```bash
#!/bin/bash
#This is a script get a users name using the  read command
echo 'Enter your name'
read NAME
echo $NAME 
```

### Exercise 3

Write a script that takes one argument and echoes that argument to the screen.

``` bash
#!/bin/bash
#This is script echoes its first argument. 
echo $1
```

##  Exercise 4

Write a script that outputs its own name, the number of arguments past to it and values of all the arguments past to it. Hint, use the $0, $# and $* variables.

```bash
#!/bin/bash 
echo $0
echo $#
echo $*
```

### Exercise 5

Write a script call makaexe.sh that takes one argument, a file name. The script should change the file permissions of that file to add user execute permission. (Please note that the Ed Stem terminal does not allow you to remove the user's "rw" permissions!! This is not standard Unix behaviour.)

```bash
#!/bin/bash 
chmod u+x $1```bash
```

### Exercise 6

Write a script called private.sh that takes one argument, a file name. The script should remove read write and execute permissions from the group and all other users.

```bash
#!/bin/bash 
chmod g-rwx,o-rwx  $1
```

### Exercise 7

Write a script call changename.sh that takes two arguments. The first is the file name of an existing file. The second is a new name for the file. The script should use the mv command to change the file's name.

```bash
#!/bin/bash 
mv $1 $2
```

##  Exercise 8

Write a script called makallexe.sh that adds execute permissions to all the files ending in ".sh" that exist in its current working directory.

```bash
#!/bin/bash 
chmod u+x *.sh
```

### Exercise 9

Write a script called sum.sh that takes one command line argument which is a file name. The script should display a summary of the named file. It should provide the following data:

```bash
#!/bin/bash 
echo 'File Name:'  
echo $1
echo 'Details:' 
ls -l $1
echo 'Lines, Words, Bytes:' 
wc $1
echo 'File Type:'
file $1
echo 'File Starts With:' 
head -3 $1
echo 'File Ends With:' 
tail -2 $1
```

## Exercises

##  Q1b. Hello World
Write a shell script that prints "Hello World" to the screen. The script should print exactly what is specified but without the double inverted commas. Call your script ex1.sh

```bash
#!/bin/bash

echo "Hello World"
```

### Q2b. Hello script argument

Write a script that prints Hello <Your_Name>. Your Name should be supplied as an argument to your script. The script should be called ex2.sh

```bash
#!/bin/bash

echo "Hello $1"
```

### Q3b. Hello script prompt

Write a script that prompts the user to enter their name and then reads in whatever the user types in as their name. The script should then print Hello <Entered_Name>  The script should be named ex3.sh

```bash
#!/bin/bash

echo -n "Enter your name:"
read NAME
echo "Hello $NAME"
```

### Q4b. Print Script Arguments

Write a shell script called ex4.sh that takes at least 3 arguments. If the number of arguments is less than 3 the script should print "Insufficient arguments" and exit, returning a value of 1 to the shell.

- If the script received three or more arguments it should print all arguments on one line and then return a value of 0 to the shell.

```bash
#!/bin/bash

if [[ $# -lt 3 ]]; then
echo "Insufficient arguments"
        exit 1
fi

echo $*
exit 0
```

### Q5b. String Comparison

Write a script that takes two string arguments. It should be named ex5.sh

- If the script does not receive two arguments (either too few or too many) it should print "Script requires exactly two arguments", then exit returning a value of 1 to the bash shell.
- If the first argument is greater than the second your script should print "The first argument is greater than the second", then exit returning a value of 0 to the bash shell.
- If the second argument is greater than the first your script should print "The second argument is greater than the first", then exit returning a value of 0 to the bash shell.
- If the two arguments are identical the script should print "The two arguments are equal", then exit returning a value of 0 to the bash shell.

```bash
#!/bin/bash

if [[ $# -ne 2 ]]; then
   echo "Script requires exactly two arguments"
   exit 1
fi

if [[ $1 > $2 ]]; then
   echo "The first argument is greater than the second"
   exit 0
fi

if [[ $2 > $1 ]]; then
   echo "The second argument is greater than the first"
   exit 0
fi

echo "The two arguments are equal"
exit 0
```

### Q6b. Integer Comparison

Write a script that takes two integer arguments. It should be named ex6.sh You can assume that the script always receives two arguments and they are always integers.

- If the first integer argument is greater than the second your script should print "The first argument is greater than the second", then exit returning a value of 0 to the bash shell.
- If the second integer argument is greater than the first your script should print "The second argument is greater than the first", then exit returning a value of 0 to the bash shell.
- If the two integer arguments are identical the script should print "The two arguments are equal", then exit returning a value of 0 to the bash shell.

```bash
#!/bin/bash

if [[ $1 -gt $2 ]]; then
echo "The first argument is greater than the second"
exit 0
fi

if [[ $2 -gt $1 ]]; then
        echo "The second argument is greater than the first"
        exit 0
fi 

if [[ $1 -eq $2 ]]; then
echo "The two arguments are equal"
exit 0
fi

# should never make it to here 
exit 1
```

### Q7b. While loop

Write a script that prints the numbers from 1 to 10, each on a separate line, using a while loop. Call your script ex7.sh

```bash
#!/bin/bash
NUM=1

while [[ $NUM -le 10 ]]; do
    echo $NUM
    NUM=$((NUM+1))
done
```

### Q8b. For loop

Write a script ex8.sh that uses a for loop to print all the arguments to the script, each on a separate line and then exit returning 0. If there are no arguments the script should print "Insufficient Arguments" and exit returning 1.

```bash
#!/bin/bash

if [[ $# -lt 1 ]]; then
    echo "Insufficient Arguments"
    exit 1
fi

for i in $*
do
    echo $i
done
```

### Q9b. String Concatenation (Advanced)

Write a shell script that takes at least one argument. If no arguments are supplied the script should quietly exit without printing anything. Your script should concatenate all of the arguments into one string with no spaces separating them. Print the concatenated string. Your script should be named ex9.sh.

```bash
#!/bin/bash
#
if [[ $# -eq 0 ]]; then
exit 0
fi
all_args=""
for arg in $*; do
all_args=$all_args$arg
done
echo $all_args
```

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

# Unix 3 - GREP

## Tutorial

### Exercise 1a

Basic use of grep to find lines within a file. Print every line of box.sh which contains a comment.
`grep '#' box.sh`

### Exercise 1b

How many lines contain a comment ?

`grep -c '#' box.sh`
`grep '#' box.sh | wc -l`

### Exercise 2

Look at wild-cards. Print every line that the file 'whois.sh' with the symbol '@', followed by the string 'whois' followed by a '.', then four other characters, followed by another a '.', followed by one or more characters, followed by ';;', followed by the end of the line.

`grep -E '@whois\..{4}\..+;;$' whois.sh`

1. The dot character, '.', means any single character to grep and egrep. When we want it to mean a literal '.' we use '\\.' (without the quotes).
2. {n} means the preceding pattern is matched n times.
3. \+ means the preceding pattern is matched one or more times.
4. $ means the end of line.
5. The @ and ; characters have no special meaning to grep so we can simply write then as literals.

### Exercise 3

Words versus strings. Print every line that contains the string 'start' then print every line that contains the word 'start' in the file stopwatch.sh

`grep 'start' stopwatch.sh`

`grep -w 'start' stopwatch.sh`

### Exercise 4

Creating the 'or' operation 1. Print every line of the file gameoflife.sh which contains either $1 or $2 (Remember what these variables represent?).

`grep '\$[12]' gameoflife.sh`

### Exercise 5

Creating the 'or' operation 2. Print every line of randomcard.sh which contains either a number or begins with 'echo'.

`grep -E '[0-9]|^echo' randomcard.sh`

### Exercise 6

Creating the 'and' operation. Print every line of towers.sh which contains both '$' and a comment. (Note, the $ sign can be within a comment.)

`grep '\$' towers.sh | grep '#'`

### Exercise 7

Case insensitive. We want to find every instance of the string 'row' in box.sh. We don't care about the case of the letters.

`grep -i 'row' box.sh`

## Exercises

### Exercise 1

Pick a file and print every line that contains a comment.

`grep '#' box.sh`

### Exercise 2

Pick a few files and use grep to print every line within them that contains both code and a comment.

`grep -E '^[^#]+#'  homework.sh`

### Exercise 3

Run the command 'head -1 *'. You'll notice that it prints out the first line of every file. This can be useful if we have a bunch of scripts and we want to make sure they are pointing to the right interpreter. The problem is, it has listed non script files as well. Can you think of a way we could modify the command above to make it better? You could use file globbing ie 'head -1*.sh' however as we know, unix is an extensionless system so scripts may not necessarily have a '.sh' extension. Instead I would like you to use grep and come up with an expression that will print the first line but only if it is the path to an interpreter (note: it could be the path to any interpreter, not just /bin/bash.)

`grep -E '^#!'  filename`

### Exercise 4

Within the script towers.sh we can see that several variables have been set that control the overall behavior of the script. Those variables have been set as all upper case. We would like to see how those variables have been used throughout the script. First off use grep to print every line of towers.sh which contains a word which is all uppercase. Now see if you can extend this into two commands, the first of which prints only lines where the variable is being used and the second of which prints only lines where the variable is being set.

`grep -E '^[^#]*[A-Z_]+\b='  towers.sh`

### Exercise 5

One of these scripts is printing data to a logfile called '/root/backup.log' Your aim is to identify which one it is. Your command should only print the name of the file to the screen. (hint: there may be a command line option for grep that can help)

`grep -E -l '/root/backup.log' *`

### Exercise 6

There are different command line options that can be used to modify the behaviour of grep. Remember where you can find these? You are going to need some of these. First off I would like you to use one of these options to print every line of x that does not contain a space. Now I would like you to use another option as well to list every one of these bash scripts that contains a line without a space on it.

`grep -E -v -l '(\ )|^$' *`

### Exercise 7

homework.sh is an interesting script. Run it then have a look at the code. You'll probably notice that it is fairly cryptic. Looking at the code it would be very hard to figure out what it is doing. Print out every line which contains a '[' followed by a character followed by a ']'. Now modify it to print only lines that contain a '[' followed by a digit followed by a ']'. (note: you may have to escape certain characters.)

`grep -E '\[[0-9]\]' homework.sh`

### Exercise 8

Do a search for all lines in stopwatch.sh which contain the string '()'. This will give us 7 lines of output. One of them is the odd one out however. We are now going do do a search for every line in stopwatch.sh which contains characters, followed by '()', followed by 0 or more spaces, followed by '{'. This will leave us with some interesting output. Any idea what these may be? (You haven't learnt about them but if you're interested then Google is your friend, or ask your tutor)

`grep -E '^[^(\(\))]+\(\)(\s)*\{'  stopwatch.sh`

### Exercise 9

You will remember from a previous tutorial we can do mathematical expressions in bash. Use grep to print a report of how many times a mathematical expression is carried out in each script. (note: some of greps command line arguments may come in useful)

`grep -E -c '\(\(.+\)\)' *`

### Exercise 10

Here is a complex regular expression (delimited by the two / characters). See if you can figure out what it's going to match. (Think about how you could break it up. Think about what sample data you may run through it to test your theories.)

`/\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b/`

an email address in uppercase.

### Exercise 11

recap and practice. Assume that you are given a file called demo.txt with suitable content (you can create one yourself). Provide the grep command solutions to the following tasks:

- find the matching lines with one digit at the begining of the line `grep -E '^[0-9]' demo.txt`
- find the matching lines with 2 or 3 digits at the end of the line `grep -E '[0-9]{2,3}$' demo.txt`
- find the matching lines with ^ at the begining of the line `grep '^\^' demo.txt`
- find the matching lines with $ at the end of the line `grep '\$$' demo.txt`
- find the matching lines blank lines `grep '^$' demo.txt`
- find the matching lines none-blank lines `grep -v '^$' demo.txt`
- find the matching lines with white-space at the end of the line `grep -E '( )$' demo.txt`
- find the matching lines with escape at the begining of the line `grep '^\\' demo.txt`
- find the matching lines with # and a digit on the same line `grep '#' demo.txt | grep '[0-9]'`
- find the matching lines with # and four-digits and column : on the same line `grep '#' demo.txt | grep -E '[0-9]{4}' | grep ':'`
- find the matching lines with # or two upper-cases `grep -E '#|[A-Z]{2}' demo.txt`
- find the matching lines with #, or a column or a digit `grep -e '#' -e ':' -e '[0-9]' demo.txt`

### Q1. Simple string search with grep

In the directory /course/linuxgym/vimdata there is a file named hermit.txt. Use grep to list all the lines that have the string the in them. Using redirection, put the lines into a file called the_string.txt

`grep -E the /course/linuxgym/vimdata/hermit.txt > the_string.txt`

### Q2. Word search with grep

In the directory /course/linuxgym/vimdata there is a file named hermit.txt. Use grep to list all the lines that have the word the in them. Using redirection, put the lines into a file called the_word.txt

Hint: There are at least two acceptable ways of performing this task.

- (a) Use word boundaries such as \b around the word.
- (b) Use a grep option that automatically treats the search string as a word.

`grep -E "\bthe\b" /course/linuxgym/vimdata/hermit.txt > the_word.txt`

`grep -E -w "the" /course/linuxgym/vimdata/hermit.txt > the_word.txt`

### Q3. Harder Word Search with grep

In the directory /course/linuxgym/vimdata there is a file named hermit.txt. Use grep to list all the lines that have the word the in them at least twice. Using redirection, put the lines into a file called the_words.txt

Hint: The regular expression that meets this criteria consists of the word the followed by zero or more occurrences of any character followed by the word the again.

Hint: father does not contain the word the ,it contains the string the

`grep -E "\bthe\b.*\bthe\b" /course/linuxgym/vimdata/hermit.txt > the_words.txt`

### Q4. Select line by first character

In the directory /course/linuxgym/vimdata there is a file named hermit.txt. Use grep to list all the lines that begin with either T or t Redirect the output of your selection to a file called tees.txt

`grep -E "^(T|t)" /course/linuxgym/vimdata/hermit.txt > tees.txt`

`grep -E "^[Tt]" /course/linuxgym/vimdata/hermit.txt > tees.txt`

### Q5. Punctuation Search

In the directory /course/linuxgym/vimdata there is a file named hermit.txt. Use grep to list all the lines that have any punctuation in them. Using redirection, put the lines into a file called punct.txt

`grep -E "[[:punct:]]" /course/linuxgym/vimdata/hermit.txt > punct.txt`

### Q6. Restricted punctuation search

In the directory /course/linuxgym/vimdata there is a file named hermit.txt. Use grep to list all the lines that have any punctuation in them, except for lines that have full stops (aka periods). Redirect the output to a file called no_periods.txt

Hint. To solve this problem you might look at doing the selection in stages using pipelining. Additionally, you could look at any grep command line options that do reverse selections. That is they select lines that don't match the regular expression.

`grep -E "[[:punct:]]" /course/linuxgym/vimdata/hermit.txt | grep -E -v "\."  > no_periods.txt`

### Q7. Counting blank Lines

In the directory /course/linuxgym/vimdata there is a file named hermit.txt. Use grep to provide a count of all the blank lines. Using redirection, put the count into a file called count_blanks.txt

Hints:

(1) Blank lines can come in two types. The first type consists of simply a carriage return \n i.e. ascii 13 or 0D(hex) and nothing else. The second type consists of one or more space and/or tab characters. All of the blank lines in hermit.txt are of the first type.  

(2) Consider using the metacharacters for the beginning and end of a line in your regular expression.

- Method 1 (uses command line option -c to get count)

`grep -E -c "^$" /course/linuxgym/vimdata/hermit.txt > count_blanks.txt`

- Method 2 (uses piping and wc -l to get a count of the blank lines)

`grep -E  "^$" /course/linuxgym/vimdata/hermit.txt | wc -l > count_blanks.txt`

- Method 3 (obscure but correct, get all non matching lines (-v) to the regular expression  ^.+$ which is a regular expression for all lines that have one or more characters in them)

`grep -E -v -c "^.+$" /course/linuxgym/vimdata/hermit.txt > count_blanks.txt`

### Q8. Select by Line beginning

In the directory /course/linuxgym/vimdata there is a file named hermit.txt. Use grep to select all lines the begin with a capital letter. Using redirection, put the selected lines into a file called caps.txt

`grep -E "^[A-Z]" /course/linuxgym/vimdata/hermit.txt > caps.txt`

### Q9. Select non-matching lines

In the directory /course/linuxgym/vimdata there is a file named hermit.txt. Use grep to list all the non-blank lines that do NOT begin with a capital. Note that there are a considerable number of lines that begin with a space followed by a capital letter. These should be included in your selection. Redirect the output into a file called nocaps.txt

Hint: There are several ways of doing this.

(a) You could use a grep command line option to select all non matching lines. Look at grep --help to find the correct option)

(b) You could use a non matching character class such as [^A-Z].

Note that some approaches will select blank lines while other approaches might not.  Approaches that select blank lines will require further filtering to remove blank lines.

- Method 1 Select all lines that do not begin with a capital letter. Note that lines that begin with NO character at all, that is, blank lines are also filtered out.

`grep -E "^[^A-Z]" /course/linuxgym/vimdata/hermit.txt > nocaps.txt`

- Method 2 Use the grep command line option to return all lines that do not have a Capital as the first character of the line. Note that in this case blank lines ARE selected, so it is necessary to filter them out using a pipe and grep -E -v  

`grep -E -v "^[A-Z]" /course/linuxgym/vimdata/hermit.txt | grep -E -v "^$" > nocaps.txt`

### Q10. Find Files containing a specific string

There is a directory called /course/linuxgym/gutenberg with a number of files in it. Use grep to list all files that have the name Simon in them. You may have to do some research to find out how to get grep to do this. Note that the actual lines containing the name Simon are not to be listed, just the names of the files. Direct the output to a file called simon_files.txt

`grep -l "\bSimon\b" /course/linuxgym/gutenberg/* > simon_files.txt`

### Q11. Select Files

Use ls, piping and grep to list all files in /course/linuxgym/gutenberg that have a 2 and a 7 in any order in the filename. Direct the output into a file called 27.txt

`ls /course/linuxgym/gutenberg/* | grep -E "(2.*7|7.*2)" > 27.txt`

### Q.12 Validating numbers entered into a bash script

Copy the scaffold file into a file called q12.sh Set the variable $re as a regular expression so that the script detects positive or negative integers. That is, the data entered can optionally begin with a - sign, but must only consist of integers after that. Note that a leading positive sign is not accepted.

If the script detects a positive or negative integer it should print "You entered an integer", otherwise it should print "You did not enter an integer"

IMPORTANT: While the bash shell understands quantifiers like *,? and + and the beginning and end of line anchors (^ and $) it does not understand \d for digits. Use [0-9] or [[:digit:]] instead.

`re="^-?[0-9]+$"`

### Q13. Validating Floating Point numbers

This is similar to the previous question except that the user is prompted to enter a positive floating point number. The numbers expected by the script must always have at least one digit before the decimal point. Note that in some cases this may be a zero. There must be at least two digits after the decimal point. The digits after the decimal point may also possibly be zeroes, but in all cases there must be at least two digits.

IMPORTANT: While the bash shell understands quantifiers like *,? and + and the beginning and end of line anchors (^ and $) it does not understand \d for digits. Use [0-9] or [[:digit:]] instead.

`re="^[0-9]+\.[0-9][0-9]+"`
