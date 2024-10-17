# StringShark

StringShark is a powerful command-line tool to quickly search for keywords, secrets, or variables in files and directories. It offers flexible search options (case-sensitive, whole-word matching, etc.) and allows you to replace matches with new values, all in a cross-platform manner. Fully compatible with Linux, macOS, and Windows, StringShark is a must-have for developers, security professionals, and sysadmins.

## Features
- **Fast Keyword Search:** Search for any string, keyword, or variable across multiple files and directories.
- **Flexible Match Modes:** Support for case-sensitive, case-insensitive, partial, and whole-word matching.
- **Optional Replace Functionality:** Easily replace any matched keywords with a new value in the files.
- **Cross-Platform Compatibility:** Works on Linux, macOS, and Windows, with OS-specific installation and functionality.

## Installation

### Linux and macOS

1. Download or clone the `stringshark` script.
2. Run the following command to install the script:

   ```bash
   ./SETUP -i
   ```

   This will:
   - Make the script executable.
   - Move it to `/usr/bin/`, making it accessible from anywhere in the terminal.

### Windows

1. Download or clone the `stringshark` script.
2. Open the command prompt or PowerShell as Administrator.
3. Run the following command:

   ```bash
   ./SETUP -i
   ```

   This will:
   - Make the script executable.
   - Move it to `C:/Program Files/sshark`.
   - Add `C:/Program Files/sshark` to your system `PATH`, allowing you to run the script from any terminal window.

### Uninstallation

To uninstall `stringshark` from your system, simply run the uninstall command:

```bash
./SETUP -u
```

This will remove the script from your system and revert any changes made during installation (such as removing it from `/usr/bin/` or `C:/Program Files/`).

## Usage

After installing `stringshark`, you can use it directly from the terminal. Here are some examples of how to use it:

```bash
sshark [-md|-mc|-mw|-me] "keyword" [-r "replace_value"] [-p "path"]
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
   sshark "password"
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
   
      ```bash
   sshark -mw "variable" -r "new_variable"
   ```

## How It Works

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
