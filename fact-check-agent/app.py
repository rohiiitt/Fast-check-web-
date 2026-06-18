# import streamlit as st
# import os
# import json

# from utils.pdf_reader import extract_text
# from utils.claim_extractor import extract_claims
# from utils.verifier import verify_claim
# from utils.report import classify


# st.set_page_config(
#     page_title="Fact Check Agent",
#     layout="wide"
# )

# st.title("📄 Fact-Check Agent")

# uploaded = st.file_uploader(
#     "Upload PDF",
#     type=["pdf"]
# )


# if uploaded:

#     os.makedirs(
#         "uploads",
#         exist_ok=True
#     )

#     path = os.path.join(
#         "uploads",
#         uploaded.name
#     )

#     with open(
#         path,
#         "wb"
#     ) as f:

#         f.write(
#             uploaded.read()
#         )

#     try:

#         with st.spinner(
#             "Extracting PDF..."
#         ):

#             text = extract_text(
#                 path
#             )

#     except Exception as e:

#         st.error(
#             f"PDF Error: {e}"
#         )

#         st.stop()

#     try:

#         with st.spinner(
#             "Finding claims..."
#         ):

#             raw = extract_claims(
#                 text
#             )

#             claims = json.loads(
#                 raw
#             )

#             if not isinstance(
#                 claims,
#                 list
#             ):

#                 claims = []

#     except Exception as e:

#         st.error(
#             f"Claim extraction failed: {e}"
#         )

#         st.stop()

#     if not claims:

#         st.warning(
#             "No claims found in PDF"
#         )

#         st.stop()

#     rows = []

#     progress = st.progress(
#         0
#     )

#     for i, c in enumerate(
#         claims
#     ):

#         try:

#             claim = c.get(
#                 "claim",
#                 ""
#             )

#             evidence = verify_claim(
#                 claim
#             )

#             result = classify(
#                 claim,
#                 evidence
#             )

#             rows.append({

#                 "Claim":
#                     claim,

#                 "Status":
#                     result["status"],

#                 "Confidence":
#                     f'{result["confidence"]}%',

#                 "Evidence":
#                     " ".join(
#                         evidence
#                     )[:400]
#             })

#         except Exception as e:

#             rows.append({

#                 "Claim":
#                     str(c),

#                 "Status":
#                     "Error",

#                 "Confidence":
#                     "0%",

#                 "Evidence":
#                     str(e)
#             })

#         if len(
#             claims
#         ):

#             progress.progress(
#                 (i + 1)
#                 / len(
#                     claims
#                 )
#             )

#     st.success(
#         f"Processed {len(rows)} claims"
#     )

#     st.dataframe(
#         rows,
#         use_container_width=True
#     )

#     st.download_button(

#         "Download Report",

#         data=json.dumps(
#             rows,
#             indent=2
#         ),

#         file_name=
#             "fact_check_report.json",

#         mime=
#             "application/json"
#     )



import streamlit as st
import os
import json
import ast

from utils.pdf_reader import extract_text
from utils.claim_extractor import extract_claims
from utils.verifier import verify_claim
from utils.report import classify


st.set_page_config(
    page_title="Fact Check Agent",
    layout="wide"
)

st.title("📄 Fact Check Agent")

uploaded = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)


def safe_claim(item):

    if isinstance(item, dict):
        return str(item.get("claim", ""))

    if isinstance(item, str):

        try:

            parsed = ast.literal_eval(item)

            if isinstance(parsed, dict):

                return str(
                    parsed.get(
                        "claim",
                        item
                    )
                )

        except Exception:
            pass

        return item

    return str(item)


if uploaded:

    os.makedirs(
        "uploads",
        exist_ok=True
    )

    path = os.path.join(
        "uploads",
        uploaded.name
    )

    with open(
        path,
        "wb"
    ) as f:

        f.write(
            uploaded.read()
        )

    try:

        with st.spinner(
            "Extracting PDF..."
        ):

            text = extract_text(
                path
            )

    except Exception as e:

        st.error(
            f"PDF Error: {e}"
        )

        st.stop()

    try:

        with st.spinner(
            "Finding claims..."
        ):

            raw = extract_claims(
                text
            )

            claims = json.loads(
                raw
            )

            if not isinstance(
                claims,
                list
            ):

                claims = []

    except Exception as e:

        st.error(
            f"Claim Extraction Error: {e}"
        )

        st.stop()

    if not claims:

        st.warning(
            "No claims found."
        )

        st.stop()

    rows = []

    progress = st.progress(
        0
    )

    for i, item in enumerate(
        claims
    ):

        try:

            claim = safe_claim(
                item
            )

            if not claim:
                continue

            evidence = verify_claim(
                claim
            )

            result = classify(
                claim,
                evidence
            )

            if isinstance(
                result,
                str
            ):

                result = {
                    "status":
                        result,

                    "confidence":
                        0
                }

            rows.append({

                "Claim":
                    claim[:250],

                "Status":
                    result["status"],

                "Confidence":
                    f'{result["confidence"]}%',

                "Evidence":
                    " ".join(
                        evidence
                    )[:300]
            })

        except Exception as e:

            rows.append({

                "Claim":
                    str(item)[:150],

                "Status":
                    "Error",

                "Confidence":
                    "0%",

                "Evidence":
                    str(e)
            })

        progress.progress(
            (i + 1)
            / len(
                claims
            )
        )

    st.success(
        f"Processed {len(rows)} claims"
    )

    st.dataframe(
        rows,
        use_container_width=True
    )

    st.download_button(

        "Download Report",

        data=json.dumps(
            rows,
            indent=2
        ),

        file_name=
        "fact_check_report.json",

        mime=
        "application/json"
    )