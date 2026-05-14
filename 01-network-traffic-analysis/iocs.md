# Indicators of Compromise

## Network Indicators

### Suspicious IP Addresses

| IP Address | Context | Direction |
|-----------|---------|----------|
| 208.95.112.1 | External HTTP communication (ip-api.com) | Outbound |
| 23.215.55.140 | Microsoft Connectivity Test | Outbound |

### Suspicious Domains

| Domain | Resolution | Context |
|--------|-----------|----------|
| default.exp-tas.com | Unknown | Suspicious DNS query|
| ip-api.com | 208.95.112.1 | External IP geolocation service|

### Suspicious URLs

| URL | Method | Context |
|-----|--------|----------|
| http://ip-api.com/json/ | GET | External IP lookup |
| http://www.msftconnecttest.com/connecttest.txt | GET | Windows connectivity check |

## File Indicators

| SHA256 Hash | Filename | Size | Context |
|-------------|----------|------|----------|
| NA | No suspicious file downloaded | NA | No malicious executables identified |

## Notes
Victim IP: 172.16.1.66
- Windows Username: ccollier
- Victim machine communicated with external domains using HTTP and DNS.
- Most traffic appeared benign, though `default.exp-tas.com` was identified as the most unusual domain observed.
- Source PCAP: malware-traffic-analysis.net exercise (2024-07-30)
- Analysis performed with Wireshark on Ubuntu ARM64
