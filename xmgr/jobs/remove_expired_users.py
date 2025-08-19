import logging

from config import USER_AUTODELETE_INCLUDE_LIMITED_ACCOUNTS
from xmgr import logger, scheduler
from xmgr.database import GetDB, crud
from xmgr.schemas.admin import Admin
from xmgr.utils import report

SYSTEM_ADMIN = Admin(username="system", is_sudo=True, telegram_id=None, discord_webhook=None)


def remove_expired_users():
    with GetDB() as db:
        deleted_users = crud.autodelete_expired_users(db, USER_AUTODELETE_INCLUDE_LIMITED_ACCOUNTS)

        for user in deleted_users:
            report.user_deleted(
                user.username, SYSTEM_ADMIN, user_admin=Admin.model_validate(user.admin) if user.admin else None
            )
            logger.log(logging.INFO, "Expired user %s deleted." % user.username)


scheduler.add_job(remove_expired_users, "interval", coalesce=True, hours=6, max_instances=1)
