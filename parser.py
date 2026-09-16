import json
import re

def parse_architecture_files():
    # 1. Read the Architecture Documentation Markdown file
    with open('Architecture_Documentation.md', 'r', encoding='utf-8') as f:
        doc_content = f.read()

    # 2. Read the Architecture View PlantUML file
    with open('Architecture_View.md', 'r', encoding='utf-8') as f:
        view_content = f.read()

    # 3. Extract PlantUML diagrams from Architecture_View.md
    diagrams = re.findall(r'@startuml\s+(\w+)(.*?)\n@enduml', view_content, re.DOTALL)
    parsed_diagrams = {}
    for name, code in diagrams:
        parsed_diagrams[name] = code.strip()

    # 4. Extract Key Sections from Architecture_Documentation.md
    doc_sections = {}
    current_heading = "Overview"
    doc_sections[current_heading] = []

    for line in doc_content.split('\n'):
        if line.startswith('#'):
            current_heading = line.lstrip('#').strip()
            doc_sections[current_heading] = []
        else:
            if line.strip():
                doc_sections[current_heading].append(line.strip())

    # 5. Structure everything into a clean JSON dictionary
    structured_data = {
        "project_name": "Space Fractions",
        "description": "Interactive fraction-solving learning tool for 6th-grade students.",
        "target_stack": {
            "language": "Node.js 18",
            "framework": "Express.js 4",
            "database": "PostgreSQL 14",
            "cache": "Redis 6"
        },
        "diagrams": parsed_diagrams,
        "documentation_sections": doc_sections
    }

    # 6. Save the output into a JSON file
    with open('architecture_input.json', 'w', encoding='utf-8') as f:
        json.dump(structured_data, f, indent=2)

    print("Success! Created 'architecture_input.json' in your folder.")

if __name__ == "__main__":
    parse_architecture_files()