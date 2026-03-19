# Import required modules
import subprocess   # To run system command (arp)
import platform     # To detect OS
import re           # To parse output
import sys          # For exit handling


# Get ARP table
def get_arp_table():
    try:
        command = "arp -a"

        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            shell=True
        )

        return result.stdout

    except Exception as e:
        print("Error fetching ARP table:", e)
        sys.exit()


# Parse IP and MAC addresses
def parse_arp_output(output):
    entries = []

    # Works for Windows, Linux, Mac formats
    pattern = r'(\d+\.\d+\.\d+\.\d+)[\s\-]+([a-fA-F0-9:-]{17})'
    matches = re.findall(pattern, output)

    for ip, mac in matches:
        entries.append((ip, mac))

    return entries


# Display results
def display_results(entries):
    print("\n=== ARP TABLE ===")
    print(f"{'IP Address':<20} {'MAC Address'}")
    print("-" * 35)

    for ip, mac in entries:
        print(f"{ip:<20} {mac}")

    print(f"\nTotal Entries: {len(entries)}")


# Save results to file
def save_to_file(entries):
    choice = input("Do you want to save results to file? (y/n): ").lower()

    if choice == 'y':
        filename = "arp_results.txt"

        try:
            with open(filename, "w") as file:
                file.write("IP Address\tMAC Address\n")
                file.write("-" * 35 + "\n")

                for ip, mac in entries:
                    file.write(f"{ip}\t{mac}\n")

                file.write(f"\nTotal Entries: {len(entries)}")

            print(f"Results saved to {filename}")

        except Exception as e:
            print("Error saving file:", e)


# Main execution
if __name__ == "__main__":
    print("=== ARP Scanner ===")
    print("Scanning ARP table...\n")

    output = get_arp_table()
    entries = parse_arp_output(output)

    if not entries:
        print("No ARP entries found")
        sys.exit()

    display_results(entries)
    save_to_file(entries)