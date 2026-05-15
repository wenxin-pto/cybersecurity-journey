<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# Analyze Network Traffic with Wireshark

**Project Link:** [View Project](https://learn.nextwork.org/projects/3862c05e-0ab8-4a8e-a203-0917e3da4b43)

**Author:** wenxin  
**Email:** wxxx.ii.nn@gmail.com

---

![Image](https://learn.nextwork.org/proud_indigo_wise_yeti/uploads/3862c05e-0ab8-4a8e-a203-0917e3da4b43_a40vg8mu)

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

In this step, I'm investigating a real malware pcap file from malware-traffic-analysis.net to identify suspicious network activity, analyze potential indicators of compromise (IOCs), and document my findings like a SOC analyst. 

![Image](https://learn.nextwork.org/proud_indigo_wise_yeti/uploads/3862c05e-0ab8-4a8e-a203-0917e3da4b43_0djhq4pj)

### Identifying the victim host

I identified the victim IP address as 172.16.1.66 because it was the internal host generating HTTP and DNS requests and it was different from the known gateway (172.16.1.1) and domain controller (172.16.1.4).

## Extracting IOCs and Identifying the Victim

### Compiling indicators of compromise

In this step, I am extracting Indicators of Compromise (IOCs) from the PCAP by identifying the victim machine, suspicious domains, external IP addresses, HTTP requests, and other network activity using Wireshark filters and TCP stream analysis.

![Image](https://learn.nextwork.org/proud_indigo_wise_yeti/uploads/3862c05e-0ab8-4a8e-a203-0917e3da4b43_6t8ql5dw)

### Victim details and Wireshark filters used

I identified the victim IP address as 172.16.1.66 using the http.request and dns filters to observe outbound traffic and DNS queries. I identified the Windows username as ccollier using the kerberos.CNameString filter in Kerberos authentication packets. I also identified the victim machine hostname from the Kerberos packets and verified network activity through TCP stream analysis.

## Writing the Incident Report and Publishing to GitHub

### Documenting and publishing findings

In this step, I'm writing an incident report so that I can document my investigation findings.

### Incident report structure and SOC value

My report includes sections for victim details, network indicators, suspicious IP addresses, suspicious domains, suspicious URLs, file indicators, key findings, evidence screenshots, and a final conclusion. 

This structure helps SOC teams because it organizes the investigation clearly, makes indicators of compromise (IOCs) easy to identify, and allows analysts to quickly understand what happened, which systems were affected, and what actions should be taken for containment and remediation.

### Git workflow for publishing the portfolio

I used `git add .` to stage all modified files for tracking, `git commit -m "message"` to save a snapshot of the investigation changes with a description, and `git push` to upload the local repository changes to GitHub so the investigation report and evidence could be shared and backed up remotely.

## Mapping Findings to MITRE ATT&CK

### Most relevant ATT&CK technique identified

## Reflections and Takeaways

### Key tools and concepts learned

### Time and challenges

### Personal learning goals

---

*Built with [NextWork](https://learn.nextwork.org) - [View this project](https://learn.nextwork.org/projects/3862c05e-0ab8-4a8e-a203-0917e3da4b43)*
