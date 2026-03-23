from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing import Optional

class Base(DeclarativeBase):
    pass

class Student(Base):
    __tablename__='student'
    id:Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement = True)
    name:Mapped[str]
    email:Mapped[str | None] = mapped_column(unique=True)
    course:Mapped[str]
    age:Mapped[int]
    def __repr__(self) -> str:
        return f"Student(id={self.id!r}, email={self.email!r}, name={self.name!r}, course={self.course!r}, age={self.age!r})"