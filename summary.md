# Unix Cheat Sheet

## System

| Command          | Explanation                                                   |
|------------------|---------------------------------------------------------------|
| `uname`          | Displays the operating system name                            |
| `uname -r`       | Shows the kernel release                                      |
| `uptime`         | Tells how long the system has been running                    |
| `hostname`       | Displays the system's network name                            |
| `hostname -i`    | Shows the IP address of the system                            |
| `last reboot`    | Lists the system reboot history                               |
| `date`           | Shows the current date and time                               |
| `timedatectl`    | Used to query and change the system clock and its settings    |
| `cal`            | Displays a calendar                                           |
| `w`              | Shows who is logged in and what they are doing                |
| `whoami`         | Displays the current user's username                          |
| `finger username`| Gives information about the user                              |

## Hardware

| Command                | Explanation                                                  |
|------------------------|--------------------------------------------------------------|
| `dmesg`                | Displays boot-up and system error messages                   |
| `cat /proc/cpuinfo`    | Shows CPU information                                        |
| `cat /proc/meminfo`    | Displays memory information                                  |
| `lshw`                 | Lists hardware configuration                                 |
| `lsblk`                | Lists block devices (like disks and their partitions)        |
| `free -m`              | Shows memory usage in MB                                     |
| `lspci -tv`            | Displays PCI devices in a tree-like diagram                  |
| `lsusb -tv`            | Lists USB devices in a tree-like format                      |
| `dmidecode`            | Shows hardware information from the BIOS                     |
| `hdparm -i /dev/xda`   | Displays the characteristics of a hard disk                  |
| `hdparm -tT /dev/xda`  | Performs a read speed test on a disk device                  |
| `badblocks -s`         | Checks a storage device for bad sectors                      |

## Users

| Command               | Explanation                                                  |
|-----------------------|--------------------------------------------------------------|
| `id`                  | Shows user and group information for the current user        |
| `last`                | Displays last logins of users                                |
| `who`                 | Shows who is logged into the system                          |
| `groupadd "admin"`    | Creates a new user group named admin                         |
| `adduser "Nicolas"`   | Adds a new user named Nicolas                                |
| `userdel "Nicolas"`   | Deletes the user Nicolas                                     |
| `usermod`             | Modifies a user account                                      |

## File Commands

| Command               | Explanation                                                  |
|-----------------------|--------------------------------------------------------------|
| `ls -al`              | Lists files and directories including hidden files with details |
| `pwd`                 | Shows the current directory path                             |
| `mkdir "new_directory"` | Creates a new directory named new_directory                 |
| `mkdir dir1 dir2`     | Creates two directories named dir1 and dir2                  |
| `rm file_name`        | Deletes a file named file_name                               |
| `rm -f filename`      | Forcefully removes a file named filename                     |
| `rm -r directory`     | Recursively deletes a directory and its contents             |
| `rm -rf directory_name`| Forcefully and recursively deletes a directory named directory_name |
| `cp file1 file2`      | Copies file1 to file2                                        |
| `cp -r dir1 dir2`     | Recursively copies dir1 to dir2                              |
| `mv file1 file2`      | Moves or renames file1 to file2                              |
| `ln -s /path/to/file_name linkname` | Creates a symbolic link named linkname to the file   |
| `touch file_name`     | Creates an empty file named file_name or updates its timestamp |
| `cat > file_name`     | Creates or overwrites file_name with input from standard input |
| `head file_name`      | Displays the first 10 lines of file_name                     |
| `tail file_name`      | Shows the last 10 lines of file_name                         |
| `more file_name`      | Views the contents of file_name page by page                 |
| `less file_name`      | Similar to more, but allows backward movement through the file |
| `gpg -c file_name`    | Encrypts file_name                                           |
| `gpg filename.gpg`    | Decrypts filename.gpg                                        |
| `wc`                  | Counts lines, words, and characters in files                  |
| `xargs`               | Builds and executes command lines from standard input        |

## Process Related

| Command               | Explanation                                                  |
|-----------------------|--------------------------------------------------------------|
| `ps`                  | Displays snapshot of current processes                       |
| `ps aux` | grep "telnet"` | Searches for 'telnet' in the list of all running processes   |
| `pmap`                | Shows memory map of processes                                |
| `top`                 | Displays ongoing look at processor activity in real-time     |
| `kill pid`            | Terminates a process with given pid                          |
| `killall proc`        | Kills all processes named proc                               |
| `pkill process_name`  | Sends a signal to a process with its name                    |
| `bg`                  | Puts a job in background                                     |
| `fg`                  | Brings a job to foreground                                   |
| `fg n`                | Brings job number n to the foreground                        |
| `lsof`                | Lists open files and the processes that opened them          |
| `renice 19 PID`       | Changes the priority of a process with PID                   |
| `pgrep firefox`       | Finds the process ID of a running program named firefox      |
| `pstree`              | Displays a tree of processes                                 |

## File Permission

| Command                        | Explanation                                                |
|--------------------------------|------------------------------------------------------------|
| `chmod OCTAL file_name`        | Changes the permission of file_name to OCTAL               |
| `chmod 777 /directory/test.sh` | Sets rwx permissions for owner, group, and others on test.sh |
| `chmod 755 /directory/test.sh` | Sets rwx for owner and rx for group and others on test.sh  |
| `chmod 766 /directory/test.sh` | Sets rw for owner and group, and r for others on test.sh   |
| `chown owner user_file`        | Changes the owner of user_file to owner                    |
| `chown owner-user: owner-group file_name` | Changes both the owner and group of file_name       |
| `chown owner-user: owner-group directory` | Changes both the owner and group of directory      |

## Network

| Command                      | Explanation                                                 |
|------------------------------|-------------------------------------------------------------|
| `ip add show`                | Displays IP addresses and property information              |
| `ip address add 192.168.0.1/24 dev eth0` | Assigns an IP address to a device                        |
| `ifconfig`                   | Displays the network configuration                          |
| `ping host`                  | Sends ICMP ECHO_REQUEST to network hosts                    |
| `whois domain`               | Retrieves domain registration information                   |
| `dig domain`                 | Queries DNS for domain information                          |
| `dig -x host`                | Performs reverse DNS lookup                                 |
| `host google.com`            | Finds the IP address of google.com                          |
| `hostname -i`                | Displays the network address of the host                    |
| `wget file_name`             | Downloads files from the internet                           |
| `netstat -pnltu`             | Displays network connections, routing tables, interface statistics, masquerade connections, and multicast memberships |

## Compression and Archives

| Command                      | Explanation                                                  |
|------------------------------|--------------------------------------------------------------|
| `tar -cf home.tar home`      | Creates an uncompressed tar archive of home directory        |
| `tar -xf files.tar`          | Extracts the files from files.tar                            |
| `tar -zcvf home.tar.gz source_folder` | Creates a gzip compressed tar archive of source_folder |
| `gzip file`                  | Compresses the file using gzip                               |

## Search

| Command                    | Explanation                                                  |
|----------------------------|--------------------------------------------------------------|
| `grep "pattern" files`     | Searches for a pattern in files                              |
| `grep -r pattern dir`      | Recursively searches for a pattern in dir                    |
| `locate file`              | Finds files by name quickly                                  |
| `find /home/ -name "index"`| Searches for files named index in /home/                     |
| `find /home -size +10000k` | Finds files larger than 10000k in /home                      |
| `grep -i`                  | Ignores case for the search                                  |
| `grep -r`                  | Searches directories recursively                             |
| `grep -v`                  | Inverts the search                                           |
| `whereis command`          | Locates the binary, source, and manual page for a command    |

## Login

| Command                   | Explanation                                                  |
|---------------------------|--------------------------------------------------------------|
| `ssh user@host`           | Connects to host as user via SSH                             |
| `ssh -p port_number user@host` | Connects to host on a specific port via SSH                |
| `ssh host`                | Connects to host using the current username via SSH          |
| `telnet host`             | Connects to host using telnet                                |

## File Transfer

| Command                    | Explanation                                                  |
|----------------------------|--------------------------------------------------------------|
| `scp file1.txt server2:/tmp` | Securely copies file1.txt to /tmp on server2                |
| `rsync -a /home/apps /backup/` | Synchronizes /home/apps to /backup/ maintaining permissions |

## Disk Usage

| Command                 | Explanation                                                  |
|-------------------------|--------------------------------------------------------------|
| `df -h`                 | Displays disk space usage in human-readable form             |
| `df -i`                 | Shows inode usage                                             |
| `fdisk -l`              | Lists disk partitions                                         |
| `du -sh`                | Shows disk usage of the current directory in human-readable form |
| `findmnt`               | Lists all mounted file systems                                |
| `mount device-path mount-point` | Mounts a device to a mount point                         |

## Directory Traverse

| Command               | Explanation                                                  |
|-----------------------|--------------------------------------------------------------|
| `pwd`                 | Prints the name of the current working directory             |
| `cd`                  | Changes the current directory to the user's home directory   |
| `cd ..`               | Goes up one directory level                                  |
| `cd /test`            | Changes the current directory to /test                       |
| `cd ~`                | Changes the current directory to the user's home directory   |

## Help

| Command               | Explanation                                                  |
|-----------------------|--------------------------------------------------------------|
| `man command`         | Displays the manual page for command                         |

## Variables

| Command                    | Explanation                                                  |
|----------------------------|--------------------------------------------------------------|
| `env`                      | Displays all environment variables                           |
| `echo $NAME`               | Displays the value of the variable NAME                      |
| `export NAME=value`        | Sets the environment variable NAME to value                  |
| `echo -e`                  | Enables interpretation of backslash escapes in echo          |
| `$PATH`                    | Displays the current path variable                           |
| `$HOME`                    | Shows the home directory of the current user                 |
| `$SHELL`                   | Displays the shell being used                                |
| `set`                      | Lists all shell variables and functions                      |
| `export $VARIABLE`         | Exports the environment variable VARIABLE                    |
| `unset VARIABLE`           | Removes VARIABLE from the environment variables              |
| `PATH=$PATH:/new/added/directory` | Appends /new/added/directory to the PATH variable      |

## LS Options

| Command             | Explanation                                                  |
|---------------------|--------------------------------------------------------------|
| `ls`                | Lists directory contents                                     |
| `-a`                | Includes hidden files while listing                          |
| `-R`                | Lists directories recursively                                |
| `-r`                | Reverses the order of the file list                          |
| `-t`                | Sorts by modification time                                   |
| `-S`                | Sorts by file size                                           |
| `-l`                | Lists in long format                                         |
| `-1`                | Lists one file per line                                      |
| `-m`                | Lists files as a comma-separated list                        |
| `-Q`                | Encloses filenames in double quotes                          |

## Redirection

| Command                    | Explanation                                                  |
|----------------------------|--------------------------------------------------------------|
| `command < file`           | Redirects file as input to command                           |
| `command > file`           | Redirects command's output to file                           |
| `command > /dev/null`      | Discards command's output                                    |
| `command >> file`          | Appends command's output to file                             |
| `command1 \| command2`      | Pipes the output of command1 to the input of command2        |

## System Monitoring and Performance

| Command            | Explanation                                                  |
|--------------------|--------------------------------------------------------------|
| `vmstat`           | Reports virtual memory statistics                            |
| `iostat`           | Displays CPU and input/output statistics for devices         |
| `mpstat`           | Reports individual or combined processor related statistics  |
| `netstat`          | Displays network connections, routing tables, interface stats|
| `ss`               | Utility to investigate sockets                               |
| `iotop`            | Displays a table of current I/O usage by processes           |
| `htop`             | Interactive process viewer, similar to top but more powerful |
| `nmon`             | Performance monitoring tool for Linux                        |

## Disk and File System

| Command                | Explanation                                                  |
|------------------------|--------------------------------------------------------------|
| `blkid`                | Locates/print block device attributes                        |
| `df`                   | Reports file system disk space usage                         |
| `du`                   | Estimates file and directory space usage                     |
| `fsck`                 | Checks and repairs a Linux filesystem                        |
| `mount`                | Mounts a filesystem                                          |
| `umount`               | Unmounts a filesystem                                        |
| `lsblk`                | Lists information about all available or the specified block devices |

## File Searching and Processing

| Command                | Explanation                                                  |
|------------------------|--------------------------------------------------------------|
| `awk`                  | Pattern scanning and processing language                     |
| `sed`                  | Stream editor for filtering and transforming text            |
| `sort`                 | Sorts lines of text files                                    |
| `uniq`                 | Reports or omits repeated lines                              |
| `diff`                 | Compares files line by line                                  |
| `cut`                  | Removes sections from each line of files                     |
| `tr`                   | Translates or deletes characters                             |
| `tee`                  | Reads from standard input and writes to standard output and files |

## Network Utilities

| Command                | Explanation                                                  |
|------------------------|--------------------------------------------------------------|
| `traceroute`           | Traces the route packets take to a network host              |
| `nslookup`             | Queries Internet domain name servers                         |
| `nmap`                 | Network exploration tool and security / port scanner         |
| `curl`                 | Transfers data from or to a server                           |
| `tcpdump`              | Dumps traffic on a network                                   |
| `ip`                   | Show / manipulate routing, devices, policy routing and tunnels |

## System Information and Management

| Command                | Explanation                                                  |
|------------------------|--------------------------------------------------------------|
| `df -h`                | Displays disk space usage in human-readable format           |
| `free`                 | Displays amount of free and used memory in the system        |
| `uname -a`             | Displays all system information                              |
| `lsmod`                | Shows the status of modules in the Linux Kernel              |
| `modprobe`             | Adds or removes modules from the Linux Kernel                |
| `crontab`              | Schedule script to run at specific times                     |
| `sysctl`               | Read or write kernel parameters at runtime                   |
| `useradd` / `usermod`  | Create or modify user accounts                               |
| `groupmod`             | Modify group details                                         |

## Selected Command Examples

| Command                        | Example Usage                                                                                          | Explanation                                                                                           |
|--------------------------------|--------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| `diff file1.txt file2.txt`     | Compare two files                                                                                      | Outputs the lines that are different between the two files.                                          |
| `diff -u file1.txt file2.txt`  | Unified format comparison                                                                              | Shows differences with a few lines of context around the changes, making them easier to understand.  |
| `diff -y file1.txt file2.txt`  | Side-by-side comparison                                                                                | Displays the content of both files next to each other to easily spot differences.                    |
| `diff -i file1.txt file2.txt`  | Ignore case differences                                                                                | Compares files but ignores differences in case between lines.                                         |
| `diff -q file1.txt file2.txt`  | Quick difference check                                                                                 | Checks if files are different without showing the differences.                                        |
| `cut -c1-10 file.txt`          | Extract first 10 characters                                                                            | Displays the first 10 characters of each line in `file.txt`.                                          |
| `cut -d',' -f2 file.csv`       | Extract the second field from a CSV                                                                    | Useful for extracting specific columns from a CSV file.                                               |
| `cut -d':' -f1 /etc/passwd > usernames.txt` | Extract usernames from `/etc/passwd` and save to `usernames.txt` | Extracts the first field (usernames) from the `/etc/passwd` file and saves them to `usernames.txt`.  |
| `cut -d',' -f1,3,5 file.csv`   | Extract multiple specific fields from a CSV                                                            | Extracts the first, third, and fifth fields from each line in `file.csv`.                             |

## Skeleton of a `.sh` Script

A basic shell script starts with a shebang (`#!`) followed by the path to the interpreter that should execute the script. For Bash scripts, this is typically `/bin/bash`.

```bash
#!/bin/bash

# Your commands here
```

## FOR LOOP

```bash
#!/bin/bash

for i in 1 2 3 4 5; do
  echo "Looping ... number $i"
done
```

## IF-ELSE 

```bash
#!/bin/bash

read -p "Enter a number: " number
if [ $number -lt 10 ]; then
  echo "The number is less than 10."
elif [ $number -eq 10 ]; then
  echo "The number is equal to 10."
else
  echo "The number is greater than 10."
fi
```

## WHILE LOOP

```bash
#!/bin/bash

count=1
while [ $count -le 5 ]; do
  echo "Count: $count"
  ((count++))
done
```


## VARIABLES

```bash
#!/bin/bash

# Variable assignment
greeting="Hello, World!"

# Variable usage
echo $greeting
```

## GREP and Pattern Matching

`grep` stands for "Global Regular Expression Print". It is a powerful utility used in Unix and Linux environments for searching text files for lines that match a given regular expression. `grep` can be used to search for simple text matches as well as complex patterns.

Regular expressions (regex) are a sequence of characters that define a search pattern, mainly for use in pattern matching with strings. Here are some basic regex symbols used in `grep` searches:

- `.` (Dot): Matches any single character except a newline.
- `*` (Asterisk): Matches zero or more occurrences of the preceding character.
- `?` (Question mark): Matches zero or one occurrence of the preceding character.
- `()` (Parentheses): Groups characters together. For example, `(ab)*` matches zero or more occurrences of "ab".
- `[]` (Square brackets): Matches any single character contained within the brackets. For example, `[abc]` matches "a", "b", or "c".
- `{}` (Curly braces): Matches a specified number of occurrences of the preceding character. For example, `a{2}` matches "aa".
- `^` (Caret): Matches the start of a line.
- `$` (Dollar sign): Matches the end of a line.
- `|` (Pipe): Acts as an OR operator. For example, `cat|dog` matches "cat" or "dog".

### GREP and Pattern Matching Examples

#### Dot (.)
- **Example:** `grep "e.r" file.txt`
- **Explanation:** Matches any character between "e" and "r". So, it can match "ear", "eer", "e3r", etc.

#### Asterisk (*)
- **Example:** `grep "ea*r" file.txt`
- **Explanation:** Matches zero or more occurrences of the preceding character. So, it can match "er", "ear", "eaar", "eaaar", etc.

#### Question Mark (?)
- **Example:** `grep "ea?r" file.txt`
- **Explanation:** Matches zero or one occurrence of the preceding character. So, it can match "er" and "ear" but not "eaar".

#### Parentheses (())
- **Example:** `grep "(ea)r" file.txt`
- **Explanation:** Groups characters together. This example doesn't effectively demonstrate the utility of parentheses beyond grouping "ea" as a single unit, which is more useful in conjunction with other operators like `|`.

#### Square Brackets ([])
- **Example:** `grep "e[ao]r" file.txt`
- **Explanation:** Matches any single character contained within the brackets. So, it can match "ear" and "eor".

#### Curly Braces ({})
- **Example:** `grep "ea{2}r" file.txt`
- **Explanation:** Matches a specified number of occurrences of the preceding character. So, it matches "eaar" but not "ear" or "eaaar".

#### Caret (^)
- **Example:** `grep "^ear" file.txt`
- **Explanation:** Matches the start of a line. So, it finds lines that start with "ear".

#### Dollar Sign ($)
- **Example:** `grep "ear$" file.txt`
- **Explanation:** Matches the end of a line. So, it finds lines that end with "ear".

#### Pipe (|)
- **Example:** `grep "cat\|dog" file.txt`
- **Explanation:** Acts as an OR operator. It finds lines containing either "cat" or "dog".

These examples provide a foundation for understanding and utilizing basic regex patterns with the `grep` command for powerful text searching and manipulation tasks.

## `[]` vs `[[]]`

- Use `[]` whenever you want your script to be portable across shells.
- Use `[[]]` if you want conditional expressions not supported by `[]` and don't need to be portable.

## Check Number Input

To check if it's a number, you could use a regexp. This should be working:

```bash
re='^[0-9]+$'
if ! [[ $yournumber =~ $re ]] ; then
   echo "error: Not a number" >&2; exit 1
fi
```

If the value is not necessarily an integer, consider amending the regex appropriately; for instance:

- For decimal numbers: `^[0-9]+([.][0-9]+)?$`
- To handle numbers with a sign: `^[+-]?[0-9]+([.][0-9]+)?$`

## Special Variables in Shell

| Special Variable | Description                                           |
|------------------|-------------------------------------------------------|
| `$0`             | The name of the bash script.                          |
| `$1, $2...$n`    | The bash script arguments.                            |
| `$$`             | The process id of the current shell.                  |
| `$#`             | The total number of arguments passed to the script.   |
| `$@`             | The value of all the arguments passed to the script.  |
| `$?`             | The exit status of the last executed command.         |
| `$!`             | The process id of the last executed command.          |

## `exit` vs. `return`

- From `man bash` on `return [n]`:
    > Causes a function to stop executing and return the value specified by `n` to its caller. If `n` is omitted, the return status is that of the last command executed in the function body.

- ... on `exit [n]`:
    > Cause the shell to exit with a status of `n`. If `n` is omitted, the exit status is that of the last command executed. A trap on EXIT is executed before the shell terminates.

Example script to illustrate `exit` vs. `return`:

```bash
#!/bin/bash

retfunc()
{
    echo "this is retfunc()"
    return 1
}

exitfunc()
{
    echo "this is exitfunc()"
    exit 1
}

retfunc
echo "We are still here"
exitfunc
echo "We will never see this"
```
