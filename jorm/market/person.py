from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum

from .infrastructure import Warehouse


@dataclass
class Account:
    email: str
    hashed_password: str
    phone_number: str = ""
    is_verified_email: bool = False


class UserPrivilege(Enum):
    DUNGEON_MASTER = 0
    BASIC = 1
    ADVANCED = 2
    PRO = 3


@dataclass
class User(ABC):
    user_id: int = -1
    name: str = "UNNAMED"
    privilege: UserPrivilege = UserPrivilege.BASIC
    warehouses: list[Warehouse] = field(default_factory=list)
    profit_tax: float = 0.0

    def __str__(self) -> str:
        return self.name


@dataclass
class Admin(User):
    pass
