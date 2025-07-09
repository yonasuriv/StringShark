import os
import sys
import platform
import subprocess

# Define colors and icons as in the original script
YELLOW = "\033[0;33m"
RESET = "\033[0m"

BG = "\n🔵 "
YG = "\n🟡 "
OG = "\n🟠 "
RG = "\n🔴 "
GG = "\n🟢 "

# Paths
WIN_INSTALL_PATH = "C:/Program Files/sshark"
UNIX_INSTALL_PATH = os.path.expanduser("~/.local/bin")

# Detect the OS
def detect_os():
    os_name = platform.system()

    global OS, LINUX, MAC, WINDOWS
    if os_name == "Linux":
        OS = "Linux"
        LINUX = f"🐧{YELLOW}Linux{RESET}"
    elif os_name == "Darwin":
        OS = "Mac"
        MAC = f"🍎{YELLOW}Mac{RESET}"
    elif os_name == "Windows":
        OS = "Windows"
        WINDOWS = f"🪟{YELLOW}Windows{RESET}"
    else:
        OS = f"UNKNOWN:{os_name}"

# Function to add directory to the PATH on Windows
def add_to_path_windows():
    try:
        subprocess.run([
            "powershell", "-Command", 
            f"[System.Environment]::SetEnvironmentVariable('Path', [System.Environment]::GetEnvironmentVariable('Path', 'User') + ';{WIN_INSTALL_PATH}', 'User')"
        ], check=True)
        print(f"\n   Added {WIN_INSTALL_PATH} to the PATH")
    except subprocess.CalledProcessError:
        print(RG + "Failed to add to PATH")

# Installation function
def install_sshark():
    detect_os()  # Ensure OS is detected before installation

    print(f"{BG}Installing StringShark 🦈...")

    # Make sshark executable (This assumes a file called "sshark" exists in the current directory)
    os.chmod('sshark', 0o755)

    # Handle based on OS
    if OS == "Linux":
        print(f"{OG}Detected OS: {LINUX}")
        try:
            subprocess.run(["sudo", "cp", "-f", "sshark", UNIX_INSTALL_PATH], check=True)
            print(f"{GG}sshark installed successfully to {UNIX_INSTALL_PATH}")
        except subprocess.CalledProcessError:
            print(f"{RG}Failed to install sshark")
            sys.exit(1)
    
    elif OS == "Mac":
        print(f"{OG}Detected OS: {MAC}")
        try:
            subprocess.run(["sudo", "cp", "-f", "sshark", UNIX_INSTALL_PATH], check=True)
            print(f"{GG}sshark installed successfully to {UNIX_INSTALL_PATH}")
        except subprocess.CalledProcessError:
            print(f"{RG}Failed to install sshark")
            sys.exit(1)

    elif OS == "Windows":
        print(f"{OG}Detected OS: {WINDOWS}")
        try:
            subprocess.run(["cp", "-f", "sshark", WIN_INSTALL_PATH], check=True)
            print(f"{GG}sshark installed successfully to {WIN_INSTALL_PATH}")
            add_to_path_windows()
        except subprocess.CalledProcessError:
            print(f"{RG}Failed to install sshark")
            sys.exit(1)

    else:
        print("🔴 Unknown or unsupported OS.")
        sys.exit(1)

# Uninstallation function
def uninstall_sshark():
    detect_os()  # Ensure OS is detected before uninstallation

    print(f"{OG}Uninstalling StringShark 🦈...")

    # Handle based on OS
    if OS in ["Linux", "Mac"]:
        print(f"{OG}Detected OS: {LINUX}")
        if os.path.isfile(f"{UNIX_INSTALL_PATH}/sshark"):
            try:
                subprocess.run(["sudo", "rm", f"{UNIX_INSTALL_PATH}/sshark"], check=True)
                print(f"{GG}sshark successfully removed from {UNIX_INSTALL_PATH}")
            except subprocess.CalledProcessError:
                print("🔴 Failed to remove sshark")
                sys.exit(1)
        else:
            print(f"🔴 sshark not found in {UNIX_INSTALL_PATH}")

    elif OS == "Windows":
        print(f"{OG}Detected OS: {WINDOWS}")
        if os.path.isfile(f"{WIN_INSTALL_PATH}/sshark"):
            try:
                subprocess.run(["rm", f"{WIN_INSTALL_PATH}/sshark"], check=True)
                print(f"{GG}sshark successfully removed from {WIN_INSTALL_PATH}")
            except subprocess.CalledProcessError:
                print("🔴 Failed to remove sshark")
                sys.exit(1)
        else:
            print(f"🔴 sshark not found in {WIN_INSTALL_PATH}")
    else:
        print("🔴 Unknown or unsupported OS.")
        sys.exit(1)

# Main function to handle arguments
def main():
    if len(sys.argv) < 2:
        print(f"{YG}Usage: {sys.argv[0]} [-i|-I for install] [-u|-U for uninstall]")
        sys.exit(1)

    if sys.argv[1] in ['-i', '-I']:
        install_sshark()
    elif sys.argv[1] in ['-u', '-U']:
        uninstall_sshark()
    else:
        print(f"{YG}Usage: {sys.argv[0]} [-i|-I for install] [-u|-U for uninstall]")
        sys.exit(1)

if __name__ == "__main__":
    main()
