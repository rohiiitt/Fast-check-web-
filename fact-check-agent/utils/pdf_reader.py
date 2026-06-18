# import fitz
# def extract_text(path):
#  doc=fitz.open(path)
#  return "".join([p.get_text() for p in doc])



import fitz
import re


def extract_text(pdf_path):

    text_parts = []

    try:

        with fitz.open(pdf_path) as doc:

            for page_num in range(len(doc)):

                try:

                    page = doc[page_num]

                    page_text = page.get_text("text")

                    if page_text:

                        page_text = re.sub(
                            r"\s+",
                            " ",
                            page_text
                        ).strip()

                        text_parts.append(
                            page_text
                        )

                except Exception as e:

                    print(
                        f"Skipping page {page_num + 1}: {e}"
                    )

                    continue

    except Exception as e:

        raise Exception(
            f"Could not read PDF: {e}"
        )

    final_text = "\n".join(
        text_parts
    )

    if not final_text.strip():

        raise Exception(
            "No readable text found in PDF"
        )

    return final_text
