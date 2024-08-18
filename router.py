from fastapi import APIRouter, Depends
from repository import TaskRepository
from typing import Annotated
from schemas import STaskAdd, STaskGet, STaskId

router = APIRouter(
    prefix="/tasks",
    tags=["Таски"]
)

@router.get("")
async def get_tasks() -> list[STaskGet]:
    task_models = await TaskRepository.find_all()
    return task_models

@router.post("")
async def add_task(task: Annotated[STaskAdd, Depends()]) -> STaskId:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}