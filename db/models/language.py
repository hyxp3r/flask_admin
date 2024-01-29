import sqlalchemy as sa
import sqlalchemy.orm as so
from sqlalchemy import TIMESTAMP, Integer, String
from sqlalchemy.orm import mapped_column, relationship

from db.base import BaseTable


class Individual(BaseTable):

    title  = mapped_column('title', String(length=100) , nullable = False)
    short_title    = mapped_column('short_title', String(length=2) , nullable = False)
