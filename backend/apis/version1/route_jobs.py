from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from starlette.status import HTTP_404_NOT_FOUND

from db.session import get_db
from db.models.jobs import Job
from schemas.jobs import JobCreate, ShowJob
from db.repository.jobs import create_new_job, retrieve_job, list_jobs
from typing import List

router = APIRouter()

@router.post("/create-job", response_model=ShowJob)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    owner_id = 1
    job = create_new_job(job=job, db=db, owner_id=owner_id)
    return job

@router.get("/get/{id}", response_model=ShowJob)
def retrieve_job_by_id(id: int, db: Session=Depends(get_db)):
    job = retrieve_job(id=id, db=db)
    if not job:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
        detail=f"Job with id {id} does not exists")
    return job


@router.get("/all", response_model=List[ShowJob])
def retrieve_all_jobs(db:Session = Depends(get_db)):
    jobs = list_jobs(db=db)
    return jobs