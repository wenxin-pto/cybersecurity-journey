
<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# Analyze Network Traffic with Wireshark

**Project Link:** [View Project](https://learn.nextwork.org/projects/3862c05e-0ab8-4a8e-a203-0917e3da4b43)

**Author:** wenxin  

---

## Project Overview

### Building a SOC analyst portfolio entry

In this project, I am investigating malicious network traffic using Wireshark, extracting indicators of compromise (IOCs), and documenting the findings in an incident report.

## Setting Up Wireshark and Git

### Installation and configuration goals

In this step, I'm setting up wireshark, configuring git and creating and clone my GitHub repository so that I can easily update and store my process

![Image](https://learn.nextwork.org/proud_indigo_wise_yeti/uploads/3862c05e-0ab8-4a8e-a203-0917e3da4b43_x6aff0jc)

### Non-root packet capture configuration

I added my user to the wireshark group so that I can run Wireshark normally without sudo.


## Capturing Live Traffic and Mastering Wireshark Filters

### Learning SOC analyst display filters

In this step, I'm capturing the network traffic and displaying filters to isolate specific protocols so that I can learn how to review the traffic statistics and save evidence to my incident report


![Image](https://learn.nextwork.org/proud_indigo_wise_yeti/uploads/3862c05e-0ab8-4a8e-a203-0917e3da4b43_8bwhlvpe)

### DNS filter and its investigative value

I would use the filter DNS This is useful because it helps to follow the UDP stream of the DNS query which allows the SOC Analyst to read the full contents of a suspicious connection.

## Investigating Real Malware Traffic

### Analyzing a real-world malware PCAP

### Identifying the victim host

## Extracting IOCs and Identifying the Victim

### Compiling indicators of compromise

### Victim details and Wireshark filters used

## Writing the Incident Report and Publishing to GitHub

### Documenting and publishing findings

### Incident report structure and SOC value

### Git workflow for publishing the portfolio

## Mapping Findings to MITRE ATT&CK

### Most relevant ATT&CK technique identified

## Reflections and Takeaways

### Key tools and concepts learned

### Time and challenges

### Personal learning goals

---

*Built with [NextWork](https://learn.nextwork.org) - [View this project](https://learn.nextwork.org/projects/3862c05e-0ab8-4a8e-a203-0917e3da4b43)*
