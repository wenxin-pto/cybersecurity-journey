# Network Traffic Analysis Investigation

## Case Overview

Investigation of a suspicious network traffic capture from a Windows host on the 172.16.1.0/24 network. The goal is to identify malicious activity, determine the scope of compromise, and extract indicators of compromise for blocking and detection.

## Victim Details

- **Hostname**: DESKTOP-SKBR25F (identified from NBNS/DHCP traffic)
- **IP Address**:  172.16.1.66 (identified from conversations)
- **MAC Address**: 00:1e:64:ec:f3:08 (identified from Ethernet headers)
- **Windows User Account**: ccolier (identified from Kerberos traffic)

## Investigation Steps

1. Opened the PCAP in Wireshark and reviewed Statistics > Conversations to identify all hosts
2. Filtered for HTTP requests (`http.request`) to identify external connections
3. Filtered for DNS queries (`dns`) to identify suspicious domain lookups
4. Followed TCP streams on suspicious connections to examine payloads
5. Used File > Export Objects > HTTP to extract any downloaded files
6. Identified victim host details using DHCP/NBNS/Kerberos filters

## Key Findings

(Document what happened in chronological order based on timestamps in the PCAP)

1. [0.673872] – Victim host performed HTTP connectivity check to `http://www.msftconnecttest.com/connecttest.txt`
2. [38.605448] – Victim host 172.16.1.66 queried suspicious domain default.exp-tas.com
3. [78.006964] – Victim made HTTP GET request to http://ip-api.com/json/
4. No malicious executable downloads or confirmed C2 callback traffic were identified in the PCAP.

## Indicators of Compromise

See [iocs.md] for the complete list.

## Conclusion

The host 172.16.1.66 appears to have been compromised based on suspicious outbound DNS and HTTP activity observed in the PCAP. The victim communicated with the suspicious domain `default.exp-tas.com` and made external HTTP requests to `ip-api.com/json/`, which may indicate reconnaissance or command-and-control related behavior.

The investigation identified the victim IP address, Windows user account (`ccollier`), MAC address, suspicious domains, and outbound HTTP traffic using Wireshark filters such as `dns`, `http.request`, and `kerberos.CNameString`.

No malicious executable files were directly observed being downloaded in the HTTP object list, but the traffic pattern suggests possible malware activity or post-compromise network communication.

## Tools Used

- Wireshark (packet analysis)
- malware-traffic-analysis.net (PCAP source)
