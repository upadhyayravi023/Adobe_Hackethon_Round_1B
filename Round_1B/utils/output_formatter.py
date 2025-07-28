import datetime
import os

def format_output(doc_paths, persona, job, ranked_sections, refined):
    return {
        "metadata": {
            "input_documents": [os.path.basename(p) for p in doc_paths],
            "persona": persona,
            "job_to_be_done": job,
            "processing_timestamp": datetime.datetime.utcnow().isoformat() + "Z"
        },
        "extracted_sections": ranked_sections,
        "sub_section_analysis": refined
    }
