import os
import json
import datetime
from utils.pdf_parser import extract_text_from_pdfs
from utils.heading_segmenter import segment_headings
from utils.relevance_ranker import rank_sections
from utils.output_formatter import format_output

INPUT_FOLDER = "sample_docs"

persona = "PhD Researcher in Computational Biology"
job = "Prepare a comprehensive literature review focusing on methodologies, datasets, and performance benchmarks"

if __name__ == "__main__":
    pdf_paths = [os.path.join(INPUT_FOLDER, f) for f in os.listdir(INPUT_FOLDER) if f.endswith(".pdf")]
    parsed_docs = extract_text_from_pdfs(pdf_paths)
    segmented_docs = segment_headings(parsed_docs)
    ranked_sections, refined_subsections = rank_sections(segmented_docs, persona, job)
    output_json = format_output(pdf_paths, persona, job, ranked_sections, refined_subsections)

    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(output_json, f, indent=2, ensure_ascii=False)