import re
import json


def extract_claims(text):

    claims = []

    text = text.replace("\n", " ")

    sentences = re.split(
        r"[.!?]",
        text
    )

    for sentence in sentences:

        sentence = sentence.strip()

        if len(sentence) < 20:
            continue

        has_number = bool(
            re.search(
                r"\d",
                sentence
            )
        )

        has_percent = "%" in sentence

        has_money = bool(
            re.search(
                r"\$|₹",
                sentence
            )
        )

        has_year = bool(
            re.search(
                r"\b(19\d{2}|20\d{2})\b",
                sentence
            )
        )

        if (
            has_number
            or has_percent
            or has_money
            or has_year
        ):

            claims.append({

                "claim":
                sentence[:250]
            })

    unique = []

    seen = set()

    for c in claims:

        if c["claim"] not in seen:

            unique.append(c)

            seen.add(
                c["claim"]
            )

    return json.dumps(
        unique[:20]
    )