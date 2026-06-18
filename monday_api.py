import requests
import streamlit as st

from config import BOARD_ID


def get_monday_items():

    api_token = st.secrets["MONDAY_API_KEY"]

    headers = {
        "Authorization": api_token
    }

    from datetime import datetime

    today = datetime.now().strftime("%Y-%m-%d")

    query = f"""
    {{
        boards(ids: {BOARD_ID}) {{
            items_page(
                limit: 500,
                query_params: {{
                    rules: [
                        {{
                            column_id: "date_mkr2q53p",
                            compare_value: ["{today}"],
                            operator: greater_than_or_equals
                        }}
                    ]
                }}
            ) {{
                items {{
                    id
                    name
                    column_values {{
                        id
                        text
                    }}
                }}
            }}
        }}
    }}
    """

    response = requests.post(
        "https://api.monday.com/v2",
        json={"query": query},
        headers=headers
    )

    data = response.json()

    return data["data"]["boards"][0]["items_page"]["items"]
