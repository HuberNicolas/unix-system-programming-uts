# USP - Lecture Summary

## Argument vs. Options

The general syntax of a Unix command is:

command \[options\] \[arguments\]

- command is the command name
- The options are typically preceded by a “-” and modify the behaviour of the command
- The arguments identify the data (usually a file or files) upon which the command performs

ls -l (-l is OPTION)

ls / (/ is ARGUMENT)

## Help

`man`

`man mv`


## Navigation

`pwd` or `cd`

  

## Removing files
- when you use command rm, YOU CAN'T UNDO

- you can use **recursive**(-r) and **force**(-f) modes to remove non-empty directories and sub-directories

- you can soften it with **interactive**(-i) mode

```
rm -rf /home/kmfoskey/Junk , or 

cd /home/kmfoskey

rm -rf Junk 

rm -rfi Junk
```


## File permissions

```
chmod 705 public_html (u/g/o; absolute)

chmod u+rwx,o+rx public_html (relative)

```

To change the permissions of a file or files use the chmod command. There two ways to express the permissions, firstly, symbolic and secondly, numeric. We will first use the symbolic method. Using this method the characters "u,g,o,a" have the following meanings:

1. "u" stands for the user who owns the file.
2. "g" stands for the other members of the owners group.
3. "o" stands for all other users.
4. "a" stands for all users.

The permissions can be one of:

1. "r" read permission
2. "w" write permission
3. "x" execute permission

The characters "+,-,=" have the following meanings:

1. "+" adds the permission specified
2. "-" removes the permission specified
3. "=" adds the permission specified and removes any not specified

To show how all of this fits together we give some examples. In each case chmod acts on the file named "filename".

1. chmod u+x filename   adds execute permission for the owner of the file.
2. chmod u-x filename   removes execute permission for the owner of the file .
3. chmod u=x filename   adds execute permission and removes read and write permissions for the owner of the file.
4. chmod g+rx filename   adds read and execute permission for the owners group members.
5. chmod g-rx filename   removes read and execute permission for the owners group members.
6. chmod o+rx filename   adds read and execute permission for other users of the file.
7. chmod a+rxw filename   adds read, write and execute permission for all users of the file.
8. chmod a+w filename   adds write permission for all users of the file.


The file permissions can be represented and manipulated numerically as a three digit octal number. The first digit (the left most one) provides the permissions for the owner of the file. The second digit, the permissions for the members of the owners group and the last digit provides the permissions for all other users. The permissions have the following values:

1. read permission has value 4
2. write permission has value 2
3. execute permission has value 1

A actual permission digit is calculated by adding the numeric values of the permissions that are set.

1. If the file's owner has read write an execute permissions the first digit will be 7.
2. If the file's owner has only read and write permissions the first digit will be 6.
3. If the file's owner has no permissions set the first digit will be 0.

The other to digits are similarly decided. So for example:

1. 754 means the owner has read write and execute permissions. The owners group has read and execute permissions and all other users have read permissions.
2. 640 means the owner has read and write permissions the owners group has read permissions and other users have no permissions.

Exercise 4. What does the numeric permission 764 mean ?

Solution

The owner has read write and execute permissions since 7=4+2+1. The owners group has read and write since 6=4+2. All other users have read permissions.

To change the file permissions numerically use the chmod command, for example:

1. chmod 640 f1 changers the permissions of the file "f1".
2. chmod 640 f* changes the permissions for all files in a directory starting with "f".


## More commands

  
```
cp (to copy)

ls (to list)

find (to find)

lp and lpr (to print)

tar (to pack)

gzip (to compress)

command line filters: tail, head, sort…
```


# Run a shell script

```
#!/bin/bash 

#Hello world example 

echo "Hello, World!"

```

`chmod +x HelloWorld.sh`

`./HelloWorld.sh`



---



## Basic Commands

```
cat // outputs its input

head // list first rows (-5 -> print first 5 rows)

tail // print last rows

sort // outputs its input (sorted)

wc // prints newline, word, and byte count for ecah file (each char counts as a byte, including newlines)$

echo // outputs its arguments as a line of text

; // entering multiple commands using a single line

read // read one line form the standard input
```



```
read NAME;
echo "Hello $NAME";
```

## Shell variables

A _shell variable_ is a memory storage area that can be used to hold a value which can then be used by the current shell

```
MY_VAR=massimo // create

echo $MY_VAR // read

massimo

unset MY_VAR // remove

```

## Environment Variables

_The environment_ or the _environment variables_ are a special sub-set of the shell variables that is made visible to all programs executed under that shell

```
env // read
export MY_VAR // add
```

### Path Environment Variables

```
echo $PATH
PATH=$PATH:. // adding current folder to path
```


## Shell  scripting:

`#!/usr/bin/env bash` is more portable than `#!/bin/bash`


## Loops and Conditional

``` bash
#!/bin/bash 
# Simple bash example for shell variables, for and if
echo
LIST=`ls`
echo $LIST
echo
for FILENAME in $LIST;
do
	echo $FILENAME
	if test $FILENAME == "food2.txt"; # or if [ ... ]
	then
		echo "Food list found!";
	fi
done
```

``` bash
if test condition
then
  commands
fi


if [ condition ]
then
  commands
fi
```

**if** _some_condition_**; then**
...
**else**
...
**fi**

- **fi** means **end of the if** construction.

#### Other tests

There are many variations of these tests.

1. -eq tests for integer equal to
2. -ne tests for integer not equal to
3. -gt tests for integer greater than
4. -ge tests for integer greater than or equal to
5. -lt tests for integer less than
6. -le tests for integer less than or equal to

#### String tests

1. == tests for string equal to
2. != tests for string not equal to

#### Other tests

1. if [ -n $astring ];then tests for string uninitialized.
2. if [ -f $filename ];then tests for file existence.

``` bash
#!/bin/bash
if [ $2 = 0 ];
then echo 'Argument 2 is 0'
fi
```

You can also use double brackets ie \[\[ some_expression \]\]. This suppresses file path name expansions. Or as noted in the lectures you can use the **test** command.


``` bash
if [ "$a" = "$b" ]; then
  echo "Strings are equal."
fi

if [ "$x" -gt "$y" ]; then
	echo "X is greater than Y."
fi

if [ -n "$var" ]; then
	echo "Var is not empty."
fi

if [ -e "$file" ]; then
	echo "File exists."
fi


if [ "$x" -gt 10 ] && [ "$y" -lt 20 ]; then
	echo "X is greater than 10 AND Y is less than 20."
fi

if [ "$x" -gt 20 ] || [ "$y" -lt 5 ]; then
  echo "X is greater than 20 OR Y is less than 5."
fi


if [[ "$filename" == *.txt ]]; then
	echo "Filename ends with '.txt'."
fi

```


- `test` is a command that evaluates a conditional expression. Use `test` when you want a clear syntax that is strictly POSIX compliant, ensuring compatibility across various Unix-like systems.
- `[` is a synonym for `test` with a requirement that it must be followed by a closing `]`. It's more commonly used than `test` for conditions because it visually separates the condition from the rest of the code. It's suitable for most conditional checks where advanced features like regex matching or pattern matching are not needed.
- `[[` is a Bash keyword that offers more advanced features than `[` or `test`, including pattern matching, regular expression matching, and it does not word-split variables, so it's safer to use with variables that may contain spaces or special characters. It's not POSIX compliant, so its use is preferred when you are sure your script will run in a Bash environment.


```bash
# TEST
# Check if a variable is equal to a specific value
if test "$a" = "hello"; then
  echo "a is hello"
fi

# Check if a file does not exist
if test ! -e "$filename"; then
  echo "$filename does not exist."
fi
```


``` bash
# []
# Check if two variables are equal
if [ "$a" = "$b" ]; then
  echo "a equals b"
fi

# Numerical comparison
if [ "$x" -lt "$y" ]; then
  echo "x is less than y"
fi

# Check if a directory exists
if [ -d "$dirname" ]; then
  echo "$dirname exists."
fi
```

``` bash
# [[]]
# Pattern matching
if [[ "$filename" == *.txt ]]; then
  echo "$filename ends with '.txt'"
fi

# Regular expression matching
if [[ "$response" =~ ^[Yy] ]]; then
  echo "You answered yes"
fi

# Complex logical conditions without quoting issues
if [[ -d "$dir" && ! -L "$dir" ]]; then
  echo "$dir is a directory and not a symlink"
fi
```

---

## Piping

Pipe is used to pass output to another **program or utility**.


- **Standard input**(or STDIN, file descriptor: 0) from the keyboard

- **Standard output**(or STDOUT, file descriptor: 1) to the screen

- **Standard error**(or STDERR , file descriptor: 2), also to the screen, but with a special meaning: it conveys error messages


_Piping_ is the process of redirecting the standard output of one command to the standard input of another one

``` bash
ls -l | wc -l
```
Tells you how many files and directories are in the current directory (NB: plus one, since ls –l produces an extra line)

  
## Redirection

Redirect is used to pass output to either a **file or stream**.

Standard input, output and error can also be redirected to files

Be aware that it’s only the standard output to be redirected, not the standard error

```
ls –l >l.txt // saves the file listing in long format to file l.txt; if file exists, overwrites it

cat <l.txt // redirects the input of cat to come from file l.txt

ls –l >>l.txt // appends the file listing in long format to existing file l.txt; if file doesn’t exist, creates it
```


```
ls –l 1> l.txt // std ouput to text

cat 0< l.txt // redirects the input of catto come from file l.txt

ls non_existing.txt 2> l.txt // A way to redirect the standard error

cat l.txt non_existing.txt > l.txt 2>&1 // A way to redirect the standard output and error, & is needed before 1, otherwise bash thinks it is a filename
```


## Commands and STDIN

```
sort // then ENTER, then enter a list, then CTRL+D (^D)
```


```
wc –w food2.txt // food2.txt passed as argument

wc -w < food2.txt // food2 is kind of typed in

ls -l food2.txt massimo > l.txt // if standard error is not redirected, l.txt is empty

> l.txt // creates an empty file (!)
```


## Globbing

* \* any string, including null
* ? any single char
* \[...\] any one of the enclosed characters
```
ls *.txt
cat *
ls *.??
ls food[1-3].txt
```


## Special parameters

 - \* expands to the positional parameters with which the script (or a new shell) are called (i.e. the script’s arguments) as a single string. The separator (default: a space) can be chosen

- 1 - 9 each expands to one positional parameter (more than nine is possible)

- @ expands to the positional parameters, as separate strings

- \# expands to the number of positional parameters

- ? expands to the _exit status_ of the most recently executed command 

- $ expands to the process ID of the script (or shell)

- 0 expands to the name of the script (or shell)

```
## file named s.sh
#! /bin/sh
echo $*
echo $2
echo $#
echo $$
echo $0
exit 5

// call script
s.sh alpha 100

echo $* --> alpha 100
echo $2 --> 100
echo $# --> 2
echo $$ --> 20391
echo $0 --> ./s.sh

$? --> 5
```


## Arithmetic expansion

`$(( ))`

## Quoting

- \\ escape
- ' single quotes (strongest) -> cannot be nested
- " double quotes -> "The value of variable A is $A"


## Commands

```
cut // Cut columns out of input (“vertical” cutting, opposed to the “horizontal” cutting of head/tail)
awk // search for, match patterns, and perform actions on files
grep // regex
sed // stream editor, editos the input based on regular expressions - great for replacements
sort // sort
uniq // find double lines
join // join files based on a common field; pairs lines from two files that have a common field
paste // merge two files side by side (horizontally)
split // split large files (logs) into smaller ones, default 1000 lines
tr // translate, delete and squeez
```


```
sort datei.txt | uniq // sort and delete double lines
sort datei.txt | uniq -d // only show doubled lines
sort datei.txt | uniq -u // only show single lines
sort datei.txt | uniq -c // count
cat datei1 datei2 datei3 | sort | uniq > datei.txt

```

In summary, `join` is used for combining files based on a matching field (requiring sorted files), while `paste` simply merges lines from files side by side based on their line order, without any requirement for the files to be sorted.

---
## GREP

grep –E, where available, should be the same as egrep

-c prints the count of the matching lines for each argument file 

-l prints the name of each argument file containing matching lines


### Repetition

_How many times?_

- `?` The preceding item must be there 0 times or 1 time
- `*` 0 or more times 
	→ regex `.*` matches 0 or as many characters 
- `+` 1 or more times 
	→ regex `.+` matches 1 or as many characters
- `{n}` n times
- `{n,m}` at least n times, but not more than m times


## Operators

- `()` group a sequence (behave as one)
- `|` or 

## Bracket expressions

- `[]` matches any char in that list
- `^` in front of list: matches any char that is not in that list: \[^A-Z\] anything except upper letter

## Anchor

- `^`- beginning
- `$`- end
- `\b` forces the match to take place at the edge of a word

## POSIX notation

- `[:alnum:]` is `[:digit:]` or `[:alpha:]`
- `[:alpha:]` is any letter
- `[:blank:]` is a space or tab
- `[:cntrl:]` is any control character
- `[:digit:]` is any of 0 1 2 3 4 5 6 7 8 9
- `[:graph:]` is not `[:alnum:]` nor `[:punct:]`
- `[:lower:]` is low case characters in a to z
- `[:print:]` is any printable character
- `[:punct:]` is any punctuation character " \# \$ % & ' ( ) * + , - . / : ; < = > ? @ [ \\ ] ^ _ \` { | } ~
- `[:space:]` is any of :CR FF HT NL VT SPACE
- `[:upper:]` is upper case A to Z
- `[:xdigit:]` is any hexadecimal digit a b c d e f A B C D E F 0 1 2 3 4 5 6 7 8 9

put them into brackets when using in grep:

`grep -E "[[:punct:]]" /course/linuxgym/vimdata/hermit.txt > punct.txt`

## GREP exits status

- 0 any matchings lines found
- 1 did not found anything
- 2 error

## xargs

If you want to find files matched by multiple regex’s, you can cascade grep commands using **xargs**:

`grep –l 'this' * | xargs grep –l 'that'`

xargs is a general-purpose Unix command that converts its standard input into **arguments** for the following command

## Unix File System

- Information stored on disks, SSDs, USB drives, ... and organised as files
- Collection on files is called file system (or filesystem)
- Unix and Linux can use many different types of filesystems (thats why they are popular)
- Disk, SSDs, USB drives often divided into sections called partitions (due to protection and logical separation)
- Storage area in a single partition is called volume, which uses _one_ type of filesystem
- TB (old, 10^...) vs. TiB (new 2^...)
- Unix: Files from all volumes/filesystem are organized into a single view called virtual filesystem. (:= filesystem from before)
- No matter how many partitions we're using: Always included in hierarchy
- This consistent interface allows the user to view the directory tree on the running system as a single entity (even when the tree is made up on a number of diverse file system types)

## Partition

- file `mtab` in `/etc` provides information about which filesystems are currently mounted (has 6 fields, last 2 not so important)
  - device name (e.g., hdb2): hard disk, the second one, the second partition
  - directory where that filesystem starts (e.g, `/boot`)
  - type
  - options (rw -> read and write, ro -> only read, like CD-ROM)
  - frequency of dump operations (0 means ignore that fs)
  - order of which `fsck` will check that filesystem (0 means ignore that fs)

## Unix conventions

- `/etc` system data
- `/sys` system software
- `/boot` kernel, usually one file
- `/bin` system commands


## Phyiscal strucutre of a partition

  1. Boot Blook (used if partition is bootable yes/no)
  2. "Superblock" (information about the layout of the blocks, e.g., how large are the blocks)
     1. Block: unit of disk size that can be allocated (minimum amount of space we can assign, typically between 512 and 8192 bytes)
  3. "i-list" (Long array of bits of information; List/Array of the i-nodes; Every file or directory has one inode; inode == pointers)
  4. Storage space (blocks occupied by data + free blocks)
  

- Pointer is an address to a block in the partition
