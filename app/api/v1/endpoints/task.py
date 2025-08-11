from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.task import Task, TaskCreate, TaskUpdate
from app.services.task_service import TaskService
from app.db.session import get_async_session

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get("/", response_model=List[Task])
async def list_tasks(session: AsyncSession = Depends(get_async_session)):
    tasks = await TaskService.get_all(session)
    return tasks

@router.post("/", response_model=Task, status_code=status.HTTP_201_CREATED)
async def create_task(task_in: TaskCreate, session: AsyncSession = Depends(get_async_session)):
    task = await TaskService.create(session, task_in)
    return task

@router.get("/{task_id}", response_model=Task)
async def get_task(task_id: int, session: AsyncSession = Depends(get_async_session)):
    task = await TaskService.get_by_id(session, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/{task_id}", response_model=Task)
async def update_task(task_id: int, task_in: TaskUpdate, session: AsyncSession = Depends(get_async_session)):
    task = await TaskService.get_by_id(session, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task = await TaskService.update(session, task, task_in)
    return task

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int, session: AsyncSession = Depends(get_async_session)):
    task = await TaskService.get_by_id(session, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    await TaskService.delete(session, task)
