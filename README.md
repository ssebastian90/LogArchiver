
## Project Description

The Log Archiver is a Python script designed to automate the management of log files. It reads log files from specified directories, archives them based on date patterns found in the filenames, and deletes older log files to help maintain a clean log directory. This tool is useful for systems that generate log files regularly and need to keep them organized.

### Features

- Archive log files by moving them to an 'archive' directory.
- Delete log files older than a specified number of days.
- Supports multiple log directories and flexible date pattern detection.

### How It Works

1. The script reads configuration settings from a `settings.json` file, which includes:
   - Paths to log directories.
   - The number of days to retain log files before deletion.

2. For each specified log directory, the script performs the following actions:
   - Checks if an 'archive' subdirectory exists and creates it if not.
   - Identifies log files based on date patterns in their filenames.
   - Archives log files by moving them to the 'archive' subdirectory if their dates are earlier than the current date.
   - Deletes log files in the 'archive' subdirectory that are older than the specified retention period.

3. The script can be scheduled to run periodically (e.g., using a cron job) to maintain log files automatically.

## Getting Started

Follow these steps to set up and run the Log Archiver:

1. Clone this repository or download the script and `settings.json`.

2. Edit the `settings.json` file to specify the log directories you want to manage and the retention period in days.

3. Install the required Python modules if not already installed:
   ```
   pip install python-dateutil
   ```

4. Run the script:
   ```
   python main.py
   ```

## Configuration

In the `settings.json` file, you can configure the following:

- `"path"`: An array of log directory paths you want to manage.
- `"days_to_subtract"`: The number of days to retain log files in the 'archive' directory before deletion.

```json
{
    "path": ["path/to/log/directory1", "path/to/log/directory2"],
    "days_to_subtract": 30
}
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project uses the `dateutil` library for date parsing.

---

You can create a `README.md` file in your project directory and paste the above content into it. Customize it further to include installation instructions, usage examples, and any other relevant information specific to your project.
