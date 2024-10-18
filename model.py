# from rules import latest_financial_index, total_revenue_5cr_flag, borrowing_to_revenue_flag, iscr_flag
# import json


# def probe_model_5l_profit(data: dict):
#     """
#     Evaluate various financial flags for the model.

#     :param data: A dictionary containing financial data.
#     :return: A dictionary with the evaluated flag values.
#     """
#     lastest_financial_index_value = latest_financial_index(data)

#     total_revenue_5cr_flag_value = total_revenue_5cr_flag(
#         data, lastest_financial_index_value
#     )

#     borrowing_to_revenue_flag_value = borrowing_to_revenue_flag(
#         data, lastest_financial_index_value
#     )

#     iscr_flag_value = iscr_flag(data, lastest_financial_index_value)

#     return {
#         "flags": {
#             "TOTAL_REVENUE_5CR_FLAG": total_revenue_5cr_flag_value,
#             "BORROWING_TO_REVENUE_FLAG": borrowing_to_revenue_flag_value,
#             "ISCR_FLAG": iscr_flag_value,
#         }
#     }


# if __name__ == "__main__":
#     # data = json.loads("t.json")
#     # print(data)
#     with open("data.json", "r") as file:
#         content = file.read()
#         # convert to json
#         data = json.loads(content)
#         print(probe_model_5l_profit(data["data"]))
import json
import logging
from typing import Dict, Any
from rules import (
    latest_financial_index,
    iscr_flag,
    total_revenue_5cr_flag,
    borrowing_to_revenue_flag,
    total_revenue,
    total_borrowing,
    iscr
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def probe_model_5l_profit(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Evaluate various financial flags for the model and provide detailed calculations.

    :param data: A dictionary containing financial data.
    :return: A dictionary with the evaluated flag values and detailed calculations.
    """
    latest_financial_index_value = latest_financial_index(data)
    logger.info(f"Using financial data index: {latest_financial_index_value}")

    revenue = total_revenue(data, latest_financial_index_value)
    borrowing_ratio = total_borrowing(data, latest_financial_index_value)
    iscr_value = iscr(data, latest_financial_index_value)

    total_revenue_5cr_flag_value = total_revenue_5cr_flag(
        data, latest_financial_index_value)
    borrowing_to_revenue_flag_value = borrowing_to_revenue_flag(
        data, latest_financial_index_value)
    iscr_flag_value = iscr_flag(data, latest_financial_index_value)

    return {
        "flags": {
            "TOTAL_REVENUE_5CR_FLAG": total_revenue_5cr_flag_value,
            "BORROWING_TO_REVENUE_FLAG": borrowing_to_revenue_flag_value,
            "ISCR_FLAG": iscr_flag_value,
        },
        "calculations": {
            "total_revenue": revenue,
            "borrowing_to_revenue_ratio": borrowing_ratio,
            "iscr": iscr_value,
        },
        "financial_index_used": latest_financial_index_value
    }


if __name__ == "__main__":
    try:
        with open("data.json", "r") as file:
            content = file.read()
            data = json.loads(content)
            result = probe_model_5l_profit(data["data"])
            print(json.dumps(result, indent=2))
    except Exception as e:
        logger.error(f"Error processing data: {str(e)}")
