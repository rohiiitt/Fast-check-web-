import re


def classify(claim, evidence):

    score = 10

    claim = claim.lower()

    if "%" in claim:
        score += 25

    if "$" in claim:
        score += 20

    years = re.findall(
        r"\b(19\d{2}|20\d{2})\b",
        claim
    )

    score += len(years) * 15

    numbers = re.findall(
        r"\d+",
        claim
    )

    score += min(
        len(numbers) * 10,
        30
    )

    score += min(
        len(claim.split()) // 5,
        20
    )

    score = min(
        score,
        100
    )

    if score >= 70:

        status = "Verified"

    elif score >= 40:

        status = "Inaccurate"

    else:

        status = "False"

    return {

        "status":
            status,

        "confidence":
            score
    }