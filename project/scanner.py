import socket

common_ports = {
    80: "HTTP",
    22: "SSH",
    21: "FTP"
}

target = "127.0.0.1"

print("Starting scan...")

for port in range(1, 101):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)

    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is open")

    s.close()
