# 🖧 Network Scanning Toolkit

##  Project Description

The **Network Scanning Toolkit** is a Python-based project designed to perform basic network scanning operations. It includes multiple tools that help identify active hosts, scan open ports, and detect devices in a network.

This project is useful for beginners in cybersecurity and networking to understand how network scanning works using simple scripts.

###  Tools Included

* **Ping Scanner** – Checks if hosts are reachable
* **Nmap Scanner** – Performs advanced network and port scanning
* **ARP Scanner** – Detects devices connected to the local network

---

##  How to Install Nmap

###  For Windows

1. Download Nmap from the official website: https://nmap.org/download.html
2. Run the installer and follow the setup instructions
3. Verify installation:

   ```bash
   nmap --version
   ```

###  For Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install nmap
```

###  For Mac

```bash
brew install nmap
```

---

##  How to Run the Programs

###  1. Ping Scanner

```bash
python ping_scanner.py
```

####  What it does:

* Checks if a host is reachable using ICMP (ping)
* Displays average response time

---

###  2. Nmap Scanner

```bash
python nmap_scanner.py
```

####  What it does:

* Uses Nmap to scan open ports
* Identifies services running on ports

---

###  3. ARP Scanner

```bash
python arp_scanner.py
```

####  What it does:

* Scans local network devices
* Displays IP and MAC addresses

---

##  Example Usage

###  Ping Scanner

```bash
Enter IP or Hostname: google.com
Output:
google.com -> Reachable | Avg Time: 24 ms
```

### 🔹 Nmap Scanner

```bash
Enter target: 192.168.1.1
Output:
Port 80 -> Open (HTTP)
Port 443 -> Open (HTTPS)
```

### 🔹 ARP Scanner

```bash
Scanning local network...

Output:
192.168.1.1  ->  AA:BB:CC:DD:EE:FF
192.168.1.5  ->  11:22:33:44:55:66
```

---

##  Requirements

* Python 3.x
* Nmap installed
* Required Python libraries:

```bash
pip install python-nmap
```

---

##  Conclusion

This project demonstrates basic network scanning techniques using Python. It helps in understanding how tools like ping, Nmap, and ARP work in real-world networking and cybersecurity scenarios.