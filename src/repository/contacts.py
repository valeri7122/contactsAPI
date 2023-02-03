from datetime import datetime
from typing import List
from sqlalchemy import or_
from sqlalchemy.orm import Session
from src.database.models import Contact
from src.schemas import ContactModel, ContactUpdate, ContactStatusUpdate


async def get_contacts(skip: int, limit: int, db: Session) -> List[Contact]:
    return db.query(Contact).offset(skip).limit(limit).all()


async def get_contact(first_name: str, last_name: str, email: str, db: Session) -> List[Contact]:
    return db.query(Contact).filter(or_(Contact.first_name == first_name,
     Contact.last_name == last_name, Contact.email == email)).all()


async def get_contact_by_birthday(db: Session) -> List[Contact]:
    now = datetime.now().date()
    year_now = now.year
    query_list = []
    result = db.query(Contact).all()
    for res in result:
        b_list = res.birthday.split("-")
        if 0 <= (datetime(year_now, int(b_list[1]), int(b_list[2])).date()-now).days <= 7:
            query_list.append(res)
    return query_list
      

async def create_contact(body: ContactModel, db: Session) -> Contact:
    contact = Contact(first_name=body.first_name, last_name=body.last_name,
     email=body.email, phone=body.phone, birthday=body.birthday)
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


async def remove_contact(contact_id: int, db: Session) -> Contact | None:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact


async def update_contact(contact_id: int, body: ContactUpdate, db: Session) -> Contact | None:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        contact.first_name=body.first_name,
        contact.last_name=body.last_name,
        contact.email=body.email,
        contact.phone=body.phone, 
        contact.birthday=body.birthday
        contact.done=body.done
        db.commit()
    return contact


async def update_status_contact(contact_id: int, body: ContactStatusUpdate, db: Session) -> Contact | None:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        contact.done = body.done
        db.commit()
    return contact