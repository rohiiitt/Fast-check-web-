import re


def verify_claim(claim):

    evidence = []

    claim = claim.lower()

    score = 0

    if "%" in claim:

        evidence.append(
            "Statistical statement detected"
        )

        score += 30

    if "$" in claim:

        evidence.append(
            "Financial value detected"
        )

        score += 20

    years = re.findall(
        r"\b(19\d{2}|20\d{2})\b",
        claim
    )

    if years:

        evidence.append(
            f"Contains year {years[0]}"
        )

        score += 25

    nums = re.findall(
        r"\d+",
        claim
    )

    if len(nums) > 1:

        evidence.append(
            "Multiple numeric indicators"
        )

        score += 20

    if len(claim.split()) > 15:

        evidence.append(
            "Long factual statement"
        )

        score += 10

    if score >= 60:

        evidence.append(
            "High confidence pattern"
        )

    elif score >= 30:

        evidence.append(
            "Medium confidence pattern"
        )

    else:

        evidence.append(
            "Low confidence pattern"
        )

    return evidence