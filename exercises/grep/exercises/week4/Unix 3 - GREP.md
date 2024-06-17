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
