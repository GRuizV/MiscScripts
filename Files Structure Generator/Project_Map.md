# Project Directory

📁 PBA/
├── 📄 LICENSE
├── 📄 Loose Notes.md
├── 📄 README.md
├── 📁 config
│   └── 📄 bill_templates.json
├── 📁 data
│   ├── 📄 ground truth total.md
│   ├── 📄 ground_truth.json
│   ├── 📁 input_pdfs
│   │   └── "Testing PDFs for app working"
│   └── 📁 textract_output
│       ├── 📄 2025-07-22_1035_cb23bdf6_BC - MC - 02 - FEB-2025.pdf.json
│       ├── 📄 UI_analyzeDocResponse.json
│       └── 📄 textract parsed tables (BC - MC - 02 - FEB-2025).md
├── 📁 docs
│   ├── 📄 00 Project Overview.md
│   ├── 📄 01 Development Plan & Milestones.md
│   ├── 📄 02 Project logbook.md
│   ├── 📁 architecture
│   │   ├── 📄 2025.07.17 - Architecture Diagram.drawio.xml
│   │   ├── 📄 2025.07.18 - Architecture Diagram.PNG
│   │   └── 📁 preliminar files
│   │       ├── 📄 2025.06.03 - Draft de Arquitectura.md
│   │       └── 📄 2025.06.03 - First Architecture Draft.jfif
│   ├── 📁 context_maintenance
│   │   ├── 📄 context_handover_model.md
│   │   ├── 📄 session_handover_template.md
│   │   └── 📁 sessions
│   │       └── 📄 2025-07-25_handover.md
│   └── 📁 planning
├── 📁 experiments
│   └── "Old experiments from the early stages of the project"
├── 📄 requirements.txt
├── 📄 routes.txt
├── 📁 src
│   ├── 📁 core
│   │   └── 📄 extract_expenses.py
│   ├── 📁 db
│   ├── 📁 ingestion
│   │   └── 📄 upload_to_s3.py
│   ├── 📁 llm_interference
│   ├── 📁 notifications
│   └── 📁 textract
│       ├── 📄 parse_textract_output.py
│       └── 📄 trigger_textract.py
└── 📁 tests
    ├── 📁 extraction_testing_data
    │   ├── 📄 BC - MC - 02 - FEB - 2025 - Ground Truth.xlsx
    │   ├── 📄 extraction_ground_truth.json
    │   ├── 📁 extraction_test_results
    │   │   └── 📄 extracted.json
    │   └── 📄 ground_truth_data_extraction.py
    ├── 📄 test_extract_expenses.py
    ├── 📄 test_parser.py
    ├── 📄 test_textract.py
    ├── 📄 test_upload.py
    └── 📄 test_validation_expenses.py



## Modules Index

- extract_expenses.py:
    * load_template(template_name: str) -> dict
    * normalize_value(value: str) -> str
    * parse_amount(value: str) -> float  # Convert amount string to float, keeping negatives as negatives.
    * parse_date(value: str) -> str
    * header_matches(expected: list, actual: list) -> bool  # Check if actual table header contains all expected headers in order.
    * classify_currency(table: list, template: dict) -> str  # Determine if table is foreign or domestic based on template currency_split rules.
    * extract_expenses_from_tables(tables: list, template_name) -> dict  # Extract normalized expense rows from parsed tables based on template.

- upload_to_s3.py:
    * upload_file(file_path: str, s3_key: str) -> str  # Uploads a file to the configured S3 bucket.

- parse_textract_output.py:
    * parse_textract_tables(textract_json: dict) -> list  # Parses Textract JSON output and extracts tables as 2D lists.
    * parse_textract_file(json_file_path: str) -> list  # Load a Textract JSON file and parse its tables.

- trigger_textract.py:
    * run_textract_analysis(s3_key: str, save_to: str, poll_interval: int) -> dict  # Asynchronously analyzes a PDF in S3 using Textract's start_document_analysis.

- ground_truth_data_extraction.py: File to manually get the verified ground truth data to compare with

- test_extract_expenses.py:
    * main() -> None

- test_parser.py:

- test_textract.py:

- test_upload.py:

- test_validation_expenses.py:
    * load_json(path) -> None
    * compare_records(extracted, ground_truth) -> None  # Compare records row by row (aligned by index).
    * validate_bucket(bucket, extracted, ground_truth) -> None
    * main() -> None
