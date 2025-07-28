import re

def segment_headings(parsed_docs):
    segmented = {}
    for path, pages in parsed_docs.items():
        segments = []
        for page in pages:
            for block in page['blocks']:
                if block[4].strip():
                    text = block[4].strip()
                    if len(text.split()) < 20 and text.isupper():
                        segments.append({
                            "document": path,
                            "page": page["page"],
                            "title": text,
                            "content": "",
                        })
                    else:
                        if segments:
                            segments[-1]["content"] += " " + text
        segmented[path] = segments
    return segmented