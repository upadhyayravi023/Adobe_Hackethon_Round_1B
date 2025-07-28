from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def rank_sections(segmented_docs, persona, job):
    full_prompt = persona + " " + job
    sections = []
    for doc, blocks in segmented_docs.items():
        for block in blocks:
            section = {
                "document": doc,
                "page": block["page"],
                "section_title": block["title"],
                "content": block["content"]
            }
            sections.append(section)

    corpus = [s["content"] for s in sections] + [full_prompt]
    vectorizer = TfidfVectorizer(stop_words="english")
    X = vectorizer.fit_transform(corpus)
    scores = cosine_similarity(X[-1], X[:-1]).flatten()

    for i, score in enumerate(scores):
        sections[i]["score"] = score

    sections = sorted(sections, key=lambda x: x["score"], reverse=True)
    ranked = [
        {
            "document": s["document"],
            "page_number": s["page"],
            "section_title": s["section_title"],
            "importance_rank": i + 1
        }
        for i, s in enumerate(sections[:5])
    ]

    refined = [
        {
            "document": s["document"],
            "page_number": s["page"],
            "refined_text": s["content"][:500]  # Truncated summary
        }
        for s in sections[:5]
    ]

    return ranked, refined