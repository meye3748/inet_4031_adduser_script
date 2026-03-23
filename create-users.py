#!/usr/bin/python3

# INET4031
# Luke Meyer
# Data Created: 03-20-2026
# Date Last Modified: 03-20-2026

# os is used to run Linux system commands from inside the python script.
# re is used for regular expression matching to identify lines that should be skipped.
# sys is used to read each line of input from standard input.
import os
import re
import sys


def main():
    for line in sys.stdin:

        # This regular expression checks whether a line starts with "#".
        # The # character marks a comment line in the input file, so those lines should be ignored.
        match = re.match("^#",line)

        # Removes whitespace and newline characters and split the line into fields using ":" as the separator.
        fields = line.strip().split(':')

        # Skip any line that is a comment or does not contain exactly 5 required fields.
        if match or len(fields) != 5:
            continue

        # Store the user account information from the input line.
	# These values match the user data needed to create the account and build the GECOS field.
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        # Split the last field into a list of group names so the user can be added to each one.
        groups = fields[4].split(',')

        # Display which user account is currently being created.
        print("==> Creating account for %s..." % (username))
        # Build the adduser command that creates the user account with a disabled password and
	# sets the user's GECOS information.
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        # Run the adduser command to create the new account.
        print(cmd)
        os.system(cmd)

        # Display that the script is now setting the password for the new user.
        print("==> Setting the password for %s..." % (username))
        # Build a command that sends the password twice into passwd through sudo so the user's
	# password can be set automatically.
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        # Run the password command for the user.
        print(cmd)
        os.system(cmd)

        for group in groups:
            # Only add the user to a group if the group field is not "-".
	    # A dash means the user should not be assigned to any additional groups.
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                print(cmd)
                os.system(cmd)

if __name__ == '__main__':
    main()
