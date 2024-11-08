from typing import Literal
from pydantic import BaseModel

class TaskRequest(BaseModel):
    """
    Request to generate a report
    """
    # enum for the report type
    report_type: Literal["payment", "pending_for_payment", "form", "user"]
    context: dict
