# Telegram Contacts Extractor

## About
Telegram Contacts Extractor is a simple program that allows you to extract contacts from an exported Telegram JSON file and save them in a VCF (vCard) file. This program makes it easy to backup and manage your Telegram contacts.

## Prerequisites
Before using the Telegram Contacts Extractor, make sure you have Python installed on your system.

## Usage
0. **Clone the Repository**:

    ```
    git clone https://github.com/mugoyajack/telegramContactsExctractor.git
    ```
1. **Export Your Telegram Data**:
   - Open Telegram Desktop.
   - Access settings from the sidebar and click on it.
   - Click on "Advanced."
   - Click on "Export Telegram Data" at the bottom of the settings page.
   - Check the "Contacts list" field and uncheck the rest of the options.
   - Scroll down and specify the download path. Select "Machine-readable JSON."
   - Click on "Export."

2. **Run the App**:
   - Open a terminal or command prompt.
   - Navigate to the directory where `telegramContactsExtractor.py` is located.
   - Run the app using the following command:
     ```
     python telegramContactsExtractor.py
     ```

3. **Import JSON File**:
   - Click on the "Import JSON file" button in the app.
   - Select the exported Telegram JSON file and click "Open."

4. **Export Contacts to VCF**:
   - After successful import, click on the "Export Contacts" button.
   - Provide a filename for the VCF file and save it.

## Files
- `telegramContactsExtractor.py`: The main extractor script.
- `sample.json`: A sample exported Telegram data JSON file.
- `sample.vcf`: A sample VCF output of the exported data.

**Contributing:**
Contributions to Telegram Contacts Extractor are welcome! If you have any ideas for improvements or find any issues, feel free to open an issue or submit a pull request.

**License:**
This project is licensed under the GNU GENERAL PUBLIC LICENSE License - see the [LICENSE](https://github.com/mugoyajack/telegramContactsExctractor/blob/main/LICENSE) file for details.

**Disclaimer:**
Telegram Contacts Extractor is a third-party application and is not affiliated with Telegram or its developers. Please ensure that you comply with Telegram's terms of service and respect the privacy of the users whose data you extract using this application.

**Author:**
Mugoya Jackson (@mugoyajack)

**Project Repository:**
[GitHub Project Repository](https://github.com/mugoyajack/telegramContactsExctractor.git)