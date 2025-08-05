# LLM-Powered Shortcut Detector

This repository contains the code for the research project on the abusability of automation apps in the context of Intimate Partner Violence (IPV). This tool uses a Large Language Model (LLM) to detect potentially malicious iOS Shortcuts recipes that can be used for surveillance, harassment, and other forms of abuse.

This work is based on the paper: **"Abusability of Automation Apps in Intimate Partner Violence"** by Shirley Zhang, Paul Chung, Jacob Vervelde, Nishant Korapati, Rahul Chatterjee, and Kassem Fawaz.

- **Project Website:** [https://wiscprivacy.com/publication/abusability-ipv/](https://wiscprivacy.com/publication/abusability-ipv/)
- **Full Paper:** [https://www.annienobear.com/pdfs/sec25cycle2-final113%20%283%29.pdf](https://www.annienobear.com/pdfs/sec25cycle2-final113%20%283%29.pdf)

## Background

Automation applications like iOS Shortcuts, Tasker, and IFTTT are powerful tools that allow users to program new functionalities on their smartphones. While designed for productivity, these "dual-use" apps can be repurposed by abusers, especially in IPV scenarios, to monitor, impersonate, and control their victims. Maliciously crafted automation recipes can function like spyware but are difficult to detect because they are created within legitimate, often pre-installed, applications.

This project provides a tool to systematically analyze iOS Shortcuts recipes and identify those with the potential for abuse.

## Features

- **LLM-Powered Detection:** Leverages a Large Language Model to analyze the text representation of Shortcuts recipes and identify potentially harmful functionalities.
- **Multi-Faceted Attack Detection:** The detector is designed to identify four types of Technology-Facilitated Abuse (TFA) attacks:
  - **Surveillance:** Secretly monitoring or collecting information from a victim's device.
  - **Impersonation:** Sending information from a victim's device to a third party without the victim's consent.
  - **Overloading:** Repeatedly triggering actions to cause a denial of service on a victim's device.
  - **Lockout/Control:** Manipulating device settings to cause confusion or anxiety.
- **Scalable Analysis:** The pipeline can process and analyze a large number of Shortcuts recipes.

## Getting Started

### Prerequisites

- Python 3.8+
- `pip` for installing dependencies
- An API key for a Large Language Model (e.g., OpenAI's GPT-4o or a self-hosted model)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/uwis-privacy/llm-powered-shortcut-detector.git
   cd llm-powered-shortcut-detector
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your LLM API key:**

   Create a `.env` file and add:

   ```env
   OPENAI_API_KEY="your-api-key-here"
   ```

## Usage

The main script, `driver.py`, orchestrates the detection pipeline.

### Single Shortcut Analysis

```bash
python driver.py --type single --input https://www.icloud.com/shortcuts/12312312345
```

### Batch Shortcut Analysis

```bash
python driver.py --type batch --input https://www.icloud.com/shortcuts/12312312345 https://www.icloud.com/shortcuts/12312312245
```

## How it Works

1. **iCloud Link Parsing:** Download shortcuts data.
2. **XML Conversion:** Convert downloaded shortcuts to XML.
3. **YAML Conversion:** Parse XML into YAML for readability.
4. **Code-Based Filtering:** Identify potentially exploitable recipes via static filters.
5. **LLM-Powered Analysis:** Use an LLM to analyze filtered recipes with a structured prompting strategy.
6. **Results:** Output text files containing analysis for each attack scenario.

## Directory Structure

```text
.
├── shortcuts_xml_batch_{timestamp}/
│   ├── {shortcut1}.xml
│   └── {shortcut2}.xml
├── shortcuts_yaml_batch_{timestamp}/
│   ├── {shortcut1}.txt
│   └── {shortcut2}.txt
├── shortcuts_yaml_batch_{timestamp}_analysis_{timestamp}/
│   ├── {shortcut1}.txt
│   └── {shortcut2}.txt
├── shortcuts_yaml_batch_{timestamp}_results/
│   ├── {shortcut1}_spy.txt
│   ├── {shortcut1}_overload.txt
│   ├── {shortcut1}_lockout.txt
│   └── {shortcut1}_impersonation.txt
└── {file_or_folder_name}_result_categories_{timestamp}/
```

## Citation

If you use this work, please cite the original paper:

```bibtex
TBD
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

