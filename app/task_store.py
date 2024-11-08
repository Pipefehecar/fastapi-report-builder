from typing import Dict

class TaskStore:
    _tasks: Dict[str, Dict[str, str or int]] = {}

    @classmethod
    def get_task(cls, task_id: str) -> Dict:
        return cls._tasks.get(task_id)

    @classmethod
    def create_task(cls, task_id: str) -> None:
        cls._tasks[task_id] = {"status": "pending", "progress": 0}

    @classmethod
    def update_task(cls, task_id: str, status: str, progress: int) -> None:
        if task_id in cls._tasks:
            cls._tasks[task_id]["status"] = status
            cls._tasks[task_id]["progress"] = progress 