Day 3 Summary

Linux directories:
- /home → user folders
- /bin → executable programs
- /etc → system configuration files
- /tmp → temporary files (often targeted by attackers)
- /mnt → mounted devices like USB drives

Useful commands:
- find → search for files/directories using criteria like name, size, or modification time
- -name, -iname → search by filename (* = wildcard)
- -mtime / -mmin → search by modification time
- touch → create a file
- ls -a → show hidden files
- ls -l → detailed file info
- ls -la → detailed info including hidden files
- chmod → change file permissions (rwx)
- chown → change file or directory ownership

Permissions:
- rwx = read, write, execute
- Example: chmod g+w, o-r access.txt gives group write access and removes read access from others.

Root & sudo:
- Root user has full system control but logging in as root is risky.
- sudo temporarily gives admin privileges while improving security and accountability.

User management commands:
- Typically used with sudo
- useradd → create users
- userdel → delete users
- usermod → modify users/groups
- -g = primary group
- -G = secondary groups

Documentation requirements:
- Include command screenshots/output, explanations, project summary, permission details (chmod, ls -la), interpretation of the 10-character permission string, and hidden file information.
