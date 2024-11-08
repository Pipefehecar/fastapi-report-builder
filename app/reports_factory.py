from abc import ABC, abstractmethod
from app.task_store import TaskStore

class Report(ABC):
    @abstractmethod
    def generate_report(self, task_id: str, context: dict):
        pass

class PaymentReport(Report):
    """
    Generate a report list of payments already made
    """
    def generate_report(self, task_id: str, context: dict):
        try:
            TaskStore.update_task(task_id, "processing", 10)
            start_date = context["start_date"]
            end_date = context["end_date"]
            # ... proceso del reporte ...
            TaskStore.update_task(task_id, "completed", 100)
        except Exception as e:
            TaskStore.update_task(task_id, "error", 0)
            raise e

class PendingForPaymentReport(Report):
    """
    Generate a report list of payments pending
    """
    def generate_report(self, task_id: str, context: dict):
        try:
            TaskStore.update_task(task_id, "processing", 10)
            company_id = context["company_id"]
            # ... proceso del reporte ...
            TaskStore.update_task(task_id, "completed", 100)
        except Exception as e:
            TaskStore.update_task(task_id, "error", 0)
            raise e

class UserReport(Report):
    """
    Generate a report list of users
    """
    def generate_report(self, task_id: str, context: dict):
        try:
            TaskStore.update_task(task_id, "processing", 10)
            company_id = context["company_id"]
            # ... proceso del reporte ...
            TaskStore.update_task(task_id, "completed", 100)
        except Exception as e:
            TaskStore.update_task(task_id, "error", 0)
            raise e

class FormReport(Report):
    """
    Generate a report list of forms
    """
    def generate_report(self, task_id: str, context: dict):
        try:
            TaskStore.update_task(task_id, "processing", 10)
            status = context["status"]
            # ... proceso del reporte ...
            TaskStore.update_task(task_id, "completed", 100)
        except Exception as e:
            TaskStore.update_task(task_id, "error", 0)
            raise e

# Factory para crear el tipo de reporte correcto
class ReportFactory:
    @staticmethod
    def create_report(report_type: str) -> Report:
        if report_type == "user":
            return UserReport()
        elif report_type == "payment":
            return PaymentReport()
        elif report_type == "pending_for_payment":
            return PendingForPaymentReport()
        elif report_type == "form":
            return FormReport()
        else:
            raise ValueError(f"Report type not found: {report_type}")
