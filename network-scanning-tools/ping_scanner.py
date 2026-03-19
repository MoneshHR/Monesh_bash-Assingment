# Import modules required for network scanning
import subprocess   # To run system commands like ping
import platform     # To detect operating system (Windows/Linux/Mac)
import re           # To extract data using regular expressions
import sys          # To handle system exit in case of errors


def scan_host(host):
    param = '-n' if platform.system().lower() == 'windows' else '-c'

    try:
        result = subprocess.run(
            ['ping', param, '4', host],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=10
        )
        return result

    except subprocess.TimeoutExpired:
        print(f"{host} -> Request timed out")
        return None
    except Exception as e:
        print(f"{host} -> Error:", e)
        return None


def parse_output(output):
    match = re.search(r'Average = (\d+ms)', output)
    return match.group(1) if match else None


def display_results(host, result):
    if result and result.returncode == 0:
        avg_time = parse_output(result.stdout)
        print(f"{host} -> Reachable", end="")

        if avg_time:
            print(f" | Avg Time: {avg_time}")
        else:
            print()
    else:
        print(f"{host} -> Unreachable")


if __name__ == "__main__":
    print("=== Ping Scanner ===")
    
    choice = input("Scan multiple hosts? (y/n): ").lower()

    # Single host
    if choice == 'n':
        host = input("Enter IP or Hostname: ")
        result = scan_host(host)
        display_results(host, result)

    # Multiple hosts
    elif choice == 'y':
        hosts = input("Enter multiple IPs/hostnames (comma separated): ")
        host_list = hosts.split(',')

        for host in host_list:
            host = host.strip()
            result = scan_host(host)
            display_results(host, result)

    else:
        print("Invalid choice")
        sys.exit()