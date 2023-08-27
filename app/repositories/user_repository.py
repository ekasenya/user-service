from typing import Optional

from sqlalchemy import insert

from app.models.user import user_account
from app.repositories.base_sql_alchemy_repository import BaseSqlAlchemyRepository
from app.schemas.user import User, UserInfo


class UserRepository(BaseSqlAlchemyRepository):
    async def create_user(
            self,
            user_name: str,
            first_name: Optional[str],
            last_name: Optional[str],
            email: Optional[str]
    ) -> User:
        insert_command = insert(user_account).values(
            user_name=user_name,
            first_name=first_name,
            last_name=last_name,
            email=email
        ).returning(user_account)

        async with self._db_connection.begin():
            row = (await self._db_connection.execute(insert_command)).one()

        return User(
            user_id=row.user_id,
            user_info=UserInfo(
                user_name=row.user_name,
                first_name=row.first_name,
                last_name=row.last_name,
                email=row.email
            )
        )
