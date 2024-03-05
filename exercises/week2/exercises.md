Exercise 1. Briefly read the man pages for the ls command. What do the following options do "-l", "-1" "-a" ?


man ls
/ -l
/ -1
/-a # use n for next
OUT: -l: Evaluate  the  file  information and file type for all symbolic links (whether named on the command line or en‐
                 countered in a file hierarchy) to be those of the file referenced by the link, and not the  link  itself;  how‐
                 ever,  ls shall write the name of the link itself and not the file referenced by the link. When -L is used with
                 -l, write the contents of symbolic links in the long format (see the STDOUT section).

OUT: -1: (The numeric digit one.) Force output to be one entry per line.  This option does not disable long  format  output.  (Long
                 format output is enabled by -g, -l (ell), -n, and -o; and disabled by -C, -m, and -x.)

OUT: -a: Write out all directory entries, including those whose names begin with a <period> ('.').

Exercise 2. Open the man pages for the bash shell ie "man bash" search for "Pattern Matching".
man sh
/ Pattern Matching

Exercise 3. Find out the full path name of your home directory (please note: if you are running these commands in our Ed environment, your home directory is just "/home").
pwd
OUT: /home

Exercise 4. Use the ls command to list all the files in your home directory.
ls
OUT: 

Exercise 5. Change directory to the parent of your home directory and use the ls command to list all the files in that directory.
cd .. && ls
OUT: bin  boot  build  course  dev  etc  home  lib  lib64  mnt  opt  proc  root  run  sbin  services  srv  sys  tmp  usr  var

Exercise 6. Use 3 different ways to change directory to you home directory.
cd 
cd ~
cd /home

Exercise 7. Create a directory called "usp1skills" in your home directory.
mkdir usp1skills
OUTPUT: usp1skills

Exercise 8. Create the empty file called "longfilename12345" in the "usp1skills" directory.
cd usp1skills && touch longfilename12345


Exercise 9. Run the ls command to list the files in the usp1skills directory.
ls
ls ./usp1skills
OUT: longfilename12345

Exercise 10. What does the "file" command do? You probably haven't encountered it yet, but you have seen a method to find out about it.
man file
OUTPUT: file — determine file type

Exercise 11. Run the "file" command using the file "longfilename12345" as its argument. Use the tab key to save yourself some typing.
cd ~
cd usp1skills
file fTAB
OUT: longfilename12345: empty

Exercise 12. Rename (move) the file "longfilename" to become "lfn".
mv longfilename12345 lfn


Exercise 13. Use the touch command to create the 2 files "1100.txt" "llOO.txt" in the "usp1skills" directory. The first is numeric 1100, the second is lower case LL upper case oo. These look very similar in the typeface of the terminal.
touch 1100.txt llOO.txt

Exercise 14. Delete the 2 files "1100.txt" "llOO.txt".
rm 1100.txt llOO.txt

Exercise 15. Create the 9 files "gaa1 gaa2 gaa3 gbb4 5bbg hbb1 hbb2 hbb3 bb2" in the "usp1skills" directory.
touch gaa1 gaa2 gaa3 gbb4 5bbg hbb1 hbb2 hbb3 bb2

Exercise 16. Create the directory "sub1" in the "usp1skills" directory.
mkdir sub1

Exercise 17. Copy the file gaa1 to the "sub1" directory.
cp gaa1 ./sub1/

Exercise 18. Copy all the files in the "usp1skills" that end in "2" to the "sub1" directory.
cp ./*2 sub1/

Exercise 19. Create the directory "subh" in the "usp1skills" and copy all the files in the "usp1skills" that start with "h" to it.
mkdir subh
cp ./h* subh/

Exercise 20. Make a directory called "subh2" in the "usp1skills" directory. Copy the "subh" directory and its contents to directory "subh2". To do this you need to use the -r option with the cp command. Use the ls command to confirm that the files copied.
mkdir subh2
cp -ri ./subh subh2/
ls subh2/
OUT: subh
ls subh2/subh
OUT: hbb1 hbb2 hbb3

Exercise 21. Delete the "subh2" directory.
rm -r subh2

Exercise 22. This exercise is a comprehensive recap of the file globbing presented in the Tutorial (more advanced options):


Create multiple directories, sub1 to sub9 using one command.
mkdir sub{1..9}
OUT: mkdir: cannot create directory ‘sub1’: File exists
Create the following files (f1 f2 f22 f33 fa fb fa2 fb2 f2b f2a faa fbb) using one command.
touch f1 f2 f22 f33 fa fb fa2 fb2 f2b f2a faa fbb

copy all files starting with f and followed by a digit to sub1
cp ./f[0-9]* sub1/

copy all files starting with f and followed by a lowercase letter to sub2
cp ./f[a-z]* sub2/

copy all files starting with f and followed by two lowercase letters to sub3
cp ./f[a-z][a-z]* sub3/

copy all files starting with f and followed by two digits to sub4
cp ./f[0-9][0-9]* sub4/

copy all files starting with f and followed by letter lowercase and a digit to sub5
cp ./f[a-z][0-9]* sub5/

copy all files starting with f and followed by any character to sub6
cp ./f? sub6/ # do not use ?*

copy all files starting with f and followed by letter lowercase and any character to sub7
cp ./f[a-z]?* sub7/

copy all files starting with f and followed by two characters to sub8
cp ./f[a-z][a-z] sub8/

copy all files starting with f and followed by any characters (zero or many) to sub9
cp ./f* sub9/

copy sub1 directory and its content into /home/sub2 directory
cp -R sub1 ~/sub2 # use R and not r

list the current directory and all its contents recursively
ls -R
