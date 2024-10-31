def format_document(doc):
    doc["_id"] = str(doc["_id"])  

    return doc