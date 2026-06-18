import requests
import streamlit as st

from config import BOARD_ID


def get_monday_items():

    api_token = st.secrets["MONDAY_API_KEY"]

    headers = {
        "Authorization": api_token
    }

    query = f"""
    {{
        boards(ids: {BOARD_ID}) {{
            items_page(limit: 500) {{
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
