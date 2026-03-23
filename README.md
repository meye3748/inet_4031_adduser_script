# INET4031 Add Users Script and User List

## Program Description

This program automates the process of creating Linux user accounts from an input file. Instead of manually running Linux commands for every user, the script reads each line of input, extracts the user's account information, creates the account, sets the password, and adds the user to any listed groups.
A system administrator would need to run commands like adduser, passwd, and group-assignment commands manually for each user. This script uses those same Linux commands, but automates the process so multiple users can be created quickly and consistently from one file.

## Program User Operation

This program reads user account data from standard input. Each valid line in the input file contains five fields separated by colons. The script processes each line, skips invalid or comment lines, creates the user account, sets the password, and adds the user to requested groups. The user should make sure the script is executable and the run it with input redirection.

### Input File Format
Each line in the input file must contain 5 colon separated fields in this order,
username:password:last_name:first_name:groups

If a line begins with "#", it is treated as a comment and skipped.
If a line doesn't contain exaclt 5 fields, it is ignored.
If the user should not be added to any groups, use "-" in the groups field.

### Command Excuction
Before running the script, the user may need to make it executable.
Run the script, ./create-users.py < create-users.input
The script reads each line from the input file, creates the user with adduser, sets the password using passwd, and then adds the user to any listed groups.

### "Dry Run"
A dry run allows the user to test the script without actually creating accounts or changing the system. This is useful fro checking that the generated commands are correct before running them for real.
To do a dry run, the user can temporarily comment out the "os.system(cmd) lines and uncomment the print(cmd) lines. This will display the commands that would be executed without making any changes to the system.
