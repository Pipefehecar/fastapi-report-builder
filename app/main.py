# main.py
from fastapi import APIRouter, FastAPI, BackgroundTasks
from uuid import uuid4
from .task_store import TaskStore
from .reports_factory import ReportFactory
from schemas import TaskRequest

app = FastAPI(
    title="File Processor API",
    description="API for processing files",
    version="1.0.0"
)

@app.get("/healthCheck", summary="Health Check endpoint")
async def healthCheck():
    return {"status": "File Procesator is ok!"}

@app.post("/execute_task/", summary="Execute task")
async def execute_task(request: TaskRequest, background_tasks: BackgroundTasks):
    task_id = str(uuid4())
    TaskStore.create_task(task_id)
    report = ReportFactory.create_report(request.report_type)
    background_tasks.add_task(report.generate_report, task_id, request.context)
    return {"task_id": task_id, "status": "Task is in progress"}

@app.get("/task_status/{task_id}", summary="Get task status")
async def task_status(task_id: str):
    task = TaskStore.get_task(task_id)
    if not task:
        return {"error": "Task not found"}

    response = {"task_id": task_id, "status": task["status"], "progress": task["progress"]}
    TaskStore.delete_task(task_id)
    return response
