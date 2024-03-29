from abc import ABC
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
    DUNGEON_MASTER = 100
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
    marketplace_keys: dict[int, str] = field(default_factory=dict)

    def __str__(self) -> str:
        return self.name


@dataclass
class Admin(User):
    pass
