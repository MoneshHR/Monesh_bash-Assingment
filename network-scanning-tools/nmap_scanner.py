# Import required modules
import subprocess   # To run nmap command
import platform     # To check OS
import sys          # For exit handling


# Check if Nmap is installed
def check_nmap():
    try:
        subprocess.run(
            ['nmap', '--version'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        return True
    except:
        return False


# Perform scan
def run_scan(target, choice):
    command = ['nmap']

    # Scan options
    if choice == '1':
        command += ['-sn']                 # Host discovery
    elif choice == '2':
        command += ['-p', '1-1000']        # Default port scan
    elif choice == '3':
        ports = input("Enter custom port range (e.g., 20-80): ")
        command += ['-p', ports]           # Custom port range
    elif choice == '4':
        command += ['-sV']                 # Service detection
    elif choice == '5':
        command += ['-O']                  # OS detection
    else:
        print("Invalid choice")
        sys.exit()

    command.append(target)

    try:
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=60
        )
        return result.stdout

    except subprocess.TimeoutExpired:
        print("Scan timed out")
        sys.exit()
    except Exception as e:
        print("Error:", e)
        sys.exit()


# Display results
def display_results(output):
    print("\n=== SCAN RESULTS ===\n")
    print(output)


# Save results to file
def save_to_file(output):
    choice = input("Do you want to save results to file? (y/n): ").lower()

    if choice == 'y':
        filename =input("Enter the filename")

        try:
            with open(filename, "w") as file:
                file.write(output)

            print(f"Results saved to {filename}")

        except Exception as e:
            print("Error saving file:", e)


# Main execution
if __name__ == "__main__":
    print("=== Nmap Scanner ===")

    if not check_nmap():
        print("Nmap is not installed!")
        sys.exit()

    target = input("Enter target IP or network (e.g., 192.168.1.1 or 192.168.1.0/24): ")

    print("\nSelect Scan Type:")
    print("1. Host Discovery (-sn)")
    print("2. Port Scan (1-1000)")
    print("3. Custom Port Range Scan")
    print("4. Service Version Detection (-sV)")
    print("5. OS Detection (-O)")

    choice = input("Enter choice (1-5): ")

    output = run_scan(target, choice)
    display_results(output)
    save_to_file(output)