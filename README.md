# LLM-Powered Shortcut Detector

This repository contains the code for the research project on the abusability of automation apps in the context of Intimate Partner Violence (IPV). This tool uses a Large Language Model (LLM) to detect potentially malicious iOS Shortcuts recipes that can be used for surveillance, harassment, and other forms of abuse.

This work is based on the paper: **"Abusability of Automation Apps in Intimate Partner Violence"** by Shirley Zhang, Paul Chung, Jacob Vervelde, Nishant Korapati, Rahul Chatterjee, and Kassem Fawaz.

- **Project Website:** [https://wiscprivacy.com/publication/abusability-ipv/](https://wiscprivacy.com/publication/abusability-ipv/)
- **Full Paper:** [https://www.annienobear.com/pdfs/sec25cycle2-final113%20%283%29.pdf](https://www.annienobear.com/pdfs/sec25cycle2-final113%20%283%29.pdf)

## Background

[cite_start]Automation applications like iOS Shortcuts, Tasker, and IFTTT are powerful tools that allow users to program new functionalities on their smartphones. [cite: 1101, 1102] [cite_start]While designed for productivity, these "dual-use" apps can be repurposed by abusers, especially in IPV scenarios, to monitor, impersonate, and control their victims. [cite: 1107] [cite_start]Maliciously crafted automation recipes can function like spyware but are difficult to detect because they are created within legitimate, often pre-installed, applications. [cite: 1140, 1141]

This project provides a tool to systematically analyze iOS Shortcuts recipes and identify those with the potential for abuse.

## Features

-   [cite_start]**LLM-Powered Detection:** Leverages a Large Language Model to analyze the text representation of Shortcuts recipes and identify potentially harmful functionalities. [cite: 1159, 1529]
-   **Multi-Faceted Attack Detection:** The detector is designed to identify four types of Technology-Facilitated Abuse (TFA) attacks:
    -   [cite_start]**Surveillance:** Secretly monitoring or collecting information from a victim's device. [cite: 1238]
    -   [cite_start]**Impersonation:** Sending information from a victim's device to a third party without the victim's consent. [cite: 1240, 1345]
    -   [cite_start]**Overloading:** Repeatedly triggering actions on a victim's device to cause a denial of service. [cite: 1242]
    -   [cite_start]**Lockout/Control:** Manipulating a victim's device settings to cause confusion or anxiety. [cite: 1244]
-   [cite_start]**Scalable Analysis:** The pipeline is designed to process and analyze a large number of Shortcuts recipes. [cite: 1612]

## Getting Started

### Prerequisites

-   Python 3.8+
-   `pip` for installing Python packages
-   An API key for a Large Language Model (e.g., OpenAI's GPT-4o or a self-hosted model like Qwen2.5-Coder)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/uwis-privacy/llm-powered-shortcut-detector.git](https://github.com/uwis-privacy/llm-powered-shortcut-detector.git)
    cd llm-powered-shortcut-detector
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: The `requirements.txt` file would likely include libraries such as `requests`, `pyyaml`, `pandas`, and a client library for the LLM you choose to use.)*

3.  **Configure your LLM API Key:**
    Create a `.env` file in the root directory and add your API key:
    ```
    OPENAI_API_KEY="your-api-key-here"
    ```

## Usage

The main driver script, `driver.py`, orchestrates the entire detection pipeline. The pipeline consists of data preparation, filtering, and LLM-based analysis.

### 1. Data Preparation

The detector works with Shortcuts recipes in iCloud link. 

### 2. Running the Detector (`driver.py`)

The `driver.py` script likely takes the following arguments:

-   An input directory containing the XML representations of the Shortcuts.
-   An output directory to store the analysis results.
-   The type of attack to scan for.

**Example Usage:**
#### Single Shortcut Analysis

To analyze a single shortcut, you can call the `main` function in `driver.py` with the iCloud link and `type='single'`.

**Example:**

```python
if __name__ == "__main__":
    main('https://www.icloud.com/shortcuts/12312312345', 'single')
```
#### Batch Shortcut Analysis

To analyze multiple shortcuts in a batch, you can call the `main` function with a list of iCloud links and `type='batch'`.

**Example:**

```python
if __name__ == "__main__":
    main(['https://www.icloud.com/shortcuts/12312312345', 'https://www.icloud.com/shortcuts/12312312245'], 'batch')
```

## How it Works
The detection pipeline follows these steps:

1. iCloud Link Parsing: The script takes an iCloud link (or a list of links) and downloads the shortcut data.

2. XML Conversion: The downloaded shortcut is converted into a machine-readable XML format.

3. YAML Conversion: The XML file is then parsed into a more concise YAML format. This is done to retain the essential information, like action UUIDs and metadata, in a more human-readable format.

4. Code-Based Filtering: A preliminary code-based filter is used to identify recipes that are potentially exploitable. This is done by checking for the presence of attack-specific operations.

5. LLM-Powered Analysis: The filtered recipes are then passed to the Groq LLM-based detector. The detector uses a multi-round, step-by-step prompting strategy for each of the four attack scenarios to minimize hallucinations and produce a detailed analysis.

6. Results: The final output is a set of text files for each shortcut, with each file containing the analysis for a specific attack scenario.

## Directory Structure
When you run the `driver.py` script, it will create a number of directories to store the intermediate and final results. The directory structure will look something like this:

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
│   ├── {shortcut1}_impersonation.txt
│   ├── {shortcut2}_spy.txt
│   ├── ...
└── {file_or_folder_name}_result_categories_{timestamp}/

- `shortcuts_xml_batch_{timestamp}`: Contains the downloaded shortcuts in XML format. 
- `shortcuts_yaml_batch_{timestamp}`: Contains the shortcuts converted to YAML format. 
- `shortcuts_yaml_batch_{timestamp}_analysis_{timestamp}`: Contains the results of the code-based filtering. 
- `shortcuts_yaml_batch_{timestamp}_results`: Contains the final analysis from the LLM for each shortcut and each attack scenario. 
- `{file_or_folder_name}_result_categories_{timestamp}`: Contains a summary of the analysis results.

## Citation
If you use this work, please cite the original paper:
```
TBD
```

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.