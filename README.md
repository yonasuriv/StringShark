![String Shark Logo](https://github.com/user-attachments/assets/90e11ba2-bbcd-4b77-a3e9-0b7c006ee223)

StringShark is a simple yet powerful command-line utility developed in Python, designed to offer seamless compatibility with Linux, macOS, and Windows. It enables efficient searches for keywords, secrets, or variables within files and directories, and offers flexible search parameters and the ability to replace identified matches with new values.

## Features
- **Fast Keyword Search:** Search for any string, keyword, or variable across multiple files and directories.
- **Flexible Match Modes:** Support for case-sensitive, case-insensitive, partial, and whole-word matching.
- **Optional Replace Functionality:** Easily replace any matched keywords with a new value in the files.
- **Cross-Platform Compatibility:** Works on Linux, macOS, and Windows, with OS-specific installation and functionality.

## Installation

### Linux and macOS

1. Clone the repository 

```bash
git clone https://github.com/yonasuriv/stringshark && cd stringshark
```

2. Run the following command to install the script:

   ```bash
   python SETUP -i
   ```

   This will:
   - Make the script executable.
   - Move it to `$HOME/.local/bin`, making it accessible from anywhere in the terminal.

### Windows

1. Clone the repository 

```bash
git clone https://github.com/yonasuriv/stringshark;
```

2. Enter the repo

```bash
cd stringshark
```

3. Run the following command:

   ```bash
   python SETUP -i
   ```

   This will:
   - Make the script executable.
   - Move it to `C:/Program Files/sshark`.
   - Add `C:/Program Files/sshark` to your system `PATH`, allowing you to run the script from any terminal window.

### Uninstallation

To uninstall `stringshark` from your system, simply run the uninstall command:

```bash
python SETUP -u
```

This will remove the script from your system and revert any changes made during installation (such as removing it from `/usr/bin/` or `C:/Program Files/`).

## Usage

After installing `stringshark`, you can use it directly from the terminal. Here are some examples of how to use it:

```
sshark <MODE> <KEYWORD> <OPTIONAL ARGUMENT>
```

### Arguments:

- **`-md` (Default Match Mode):** Case-insensitive partial match.
- **`-mc`:** Case-sensitive match.
- **`-mw`:** Case-insensitive whole-word match.
- **`-me`:** Case-sensitive whole-word match. (exact match)
- **`-r "replace_value"` (Optional):** Replace the matched keyword with a new value.
- **`-p "path"` (Optional):** Specify the directory or file path to search. Defaults to the current directory if omitted.

### Examples:

1. **Search for a keyword (case-insensitive, partial match) in the current directory:**

   ```bash
   sshark -md "password"                 	 # Search for "password" (case-insensitive)
   ```

   or 

   ```bash
   sshark -md "password"
   ```

2. **Search for a case-sensitive keyword in all files:**

   ```bash
   sshark -mc "API_KEY"
   ```

3. **Search and replace a keyword across a directory:**

   ```bash
   sshark -md "secret_key" -r "new_secret_key" -p /path/to/directory
   ```

4. **Search for a whole-word keyword and replace it (case-insensitive):**

   ```bash
   sshark -mw "username" -r "new_username"
   ```

   or 

   
   ```bash
   sshark -mw "variable" -r "new_variable"

## How It Works

<p align="center">
    <img src="https://github.com/user-attachments/assets/f3600e08-a64f-4f2c-924f-41b01f489466" alt="Example Demo" style="width: 500px;"/>
</p>

1. **Search Mode:**
   StringShark walks through all directories and files, searching for the given keyword. The keyword can be matched using different modes:
   - Default (case-insensitive and partial match).
   - Case-sensitive match.
   - Whole-word matching (case-insensitive or case-sensitive).

2. **Replacement:**
   If the `-r` argument is provided, StringShark will replace the matched keyword with the specified replacement string. It will print a summary of the changes made, including the filename and line number.

3. **Cross-Platform Functionality:**
   The script handles file encodings and paths in a cross-platform way, so it works on Linux, macOS, and Windows. For Windows users, the script can be invoked from any terminal once installed.

## Requirements

- **Linux/macOS:** Python 3.x is required.
- **Windows:** Python 3.x must be installed and added to the system's PATH.
  - **Optional:** For colored terminal output on Windows, install `colorama` by running:

    ```bash
    pip install colorama
    ```

## License

StringShark is released under the MIT License. See [LICENSE](./LICENSE) for details.

## Contributing

We welcome contributions! If you find any issues or have suggestions for improvements, feel free to submit a pull request or open an issue.
