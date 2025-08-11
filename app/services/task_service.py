from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate

class TaskService:
    @staticmethod
    async def get_all(session: AsyncSession) -> List[Task]:
        result = await session.execute(select(Task))
        return result.scalars().all()

    @staticmethod
    async def get_by_id(session: AsyncSession, task_id: int) -> Optional[Task]:
        result = await session.execute(select(Task).where(Task.id == task_id))
        return result.scalars().first()

    @staticmethod
    async def create(session: AsyncSession, task_in: TaskCreate) -> Task:
        task = Task(**task_in.dict())
        session.add(task)
        await session.commit()
        await session.refresh(task)
        return task

    @staticmethod
    async def update(session: AsyncSession, task: Task, task_in: TaskUpdate) -> Task:
        task_data = task_in.dict(exclude_unset=True)
        for key, value in task_data.items():
            setattr(task, key, value)
        session.add(task)
        await session.commit()
        await session.refresh(task)
        return task

    @staticmethod
    async def delete(session: AsyncSession, task: Task) -> None:
        await session.delete(task)
        await session.commit()
