import json
from datetime import datetime
from enum import Enum
from typing import List, Dict, Optional

class TaskStatus(Enum)
    PENDING = "pendiente"
    IN_PROGRESS = "en_progreso"
    COMPLETED = "completado"
    BLOCKED = "bloqueado"

class TaskPriority(Enum):
    HIGH = "alta"
    MEDIUM = "media"
    LOW = "baja"

class Task:
    def __init__(self, task_id: str, name: str, owner: str, priority: TaskPriority):
        self.task_id = task_id
        self.name = name
        self.owner = owner
        self.priority = priority
        self.status = TaskStatus.PENDING
        self.created_at = datetime.now().isoformat()
        self.completed_at: Optional[str] = None
        self.progress = 0
        self.dependencies: List[str] = []
        self.risks: List[str] = []
        self.deliverables: List[str] = []

    def to_dict(self) -> Dict:
        return {
            "id": self.task_id,
            "nombre": self.name,
            "propietario": self.owner,
            "estado": self.status.value,
            "prioridad": self.priority.value,
            "progreso": f"{self.progress}%",
            "creada": self.created_at,
            "completada": self.completed_at,
            "dependencias": self.dependencies,
            "riesgos": self.risks,
            "entregables": self.deliverables
        }

class OrchestratorTracker:
    def __init__(self, objective: str):
        self.objective = objective
        self.tasks: Dict[str, Task] = {}
        self.created_at = datetime.now().isoformat()
        self.status = "activo"

    def add_task(self, task_id: str, name: str, owner: str, priority: TaskPriority) -> Task:
        task = Task(task_id, name, owner, priority)
        self.tasks[task_id] = task
        return task

    def update_task_status(self, task_id: str, status: TaskStatus):
        if task_id in self.tasks:
            self.tasks[task_id].status = status
            if status == TaskStatus.COMPLETED:
                self.tasks[task_id].completed_at = datetime.now().isoformat()
                self.tasks[task_id].progress = 100

    def update_task_progress(self, task_id: str, progress: int):
        if task_id in self.tasks and 0 <= progress <= 100:
            self.tasks[task_id].progress = progress

    def add_risk(self, task_id: str, risk: str):
        if task_id in self.tasks:
            self.tasks[task_id].risks.append(risk)

    def add_deliverable(self, task_id: str, deliverable: str):
        if task_id in self.tasks:
            self.tasks[task_id].deliverables.append(deliverable)

    def get_progress_summary(self) -> Dict:
        total = len(self.tasks)
        completed = sum(1 for t in self.tasks.values() if t.status == TaskStatus.COMPLETED)
        in_progress = sum(1 for t in self.tasks.values() if t.status == TaskStatus.IN_PROGRESS)
        blocked = sum(1 for t in self.tasks.values() if t.status == TaskStatus.BLOCKED)
        
        return {
            "objetivo": self.objective,
            "total_tareas": total,
            "completadas": completed,
            "en_progreso": in_progress,
            "bloqueadas": blocked,
            "porcentaje_completado": f"{(completed/total*100):.1f}%" if total > 0 else "0%",
            "fecha_actualización": datetime.now().isoformat()
        }

    def export_to_json(self, filepath: str):
        data = {
            "tracker": {
                "objetivo": self.objective,
                "estado": self.status,
                "creado": self.created_at,
                "resumen": self.get_progress_summary(),
                "tareas": [task.to_dict() for task in self.tasks.values()]
            }
        }
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def display_progress(self):
        summary = self.get_progress_summary()
        print(f"\n{'='*60}")
        print(f"ORQUESTADOR - SEGUIMIENTO DE PROGRESO")
        print(f"{'='*60}")
        print(f"Objetivo: {summary['objetivo']}")
        print(f"Completado: {summary['porcentaje_completado']}")
        print(f"Tareas: {summary['completadas']}/{summary['total_tareas']} | En progreso: {summary['en_progreso']} | Bloqueadas: {summary['bloqueadas']}")
        print(f"Actualizado: {summary['fecha_actualización']}")
        print(f"{'='*60}\n")