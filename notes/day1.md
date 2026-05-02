# Day 1 – Operating Systems

## Key Concepts

* OS acts as a bridge between hardware and the user
* Linux is widely used in cybersecurity
* Legacy systems are vulnerable due to lack of updates

## Security Insights

* OS security includes file protection and user authentication
* BIOS/UEFI can be a target since it’s not always scanned
* Outdated systems increase risk of attacks

## System Components

* Boot process: BIOS/UEFI → Bootloader → OS
* Interfaces:

  * GUI (visual)
  * CLI (command-based)

## Reflection

Understanding OS basics helps explain how attackers interact with systems and why Linux is commonly used in cybersecurity.


## Gobuster (Directory Brute Forcing)

Gobuster is a tool used to discover hidden files and directories on a web server.

It works by:

* Taking a wordlist (a list of possible directory names)
* Sending requests to a target website
* Checking which paths exist based on the server response

### Example

gobuster -u http://example.com -w wordlist.txt dir

### Key Idea

Attackers use Gobuster to find hidden pages such as:

* /admin
* /login
* /backup

These pages may not be publicly linked but can expose sensitive functionality or data.

### Why It Matters

Finding hidden directories helps attackers:

* Identify entry points
* Discover misconfigured or unprotected pages
* Gain access to sensitive areas of a system
