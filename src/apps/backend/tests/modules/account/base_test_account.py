import unittest

from typing import Callable

from modules.config.config_service import ConfigService
from modules.account.account_service_manager import AccountServiceManager
from modules.account.internal.store.account_repository import AccountRepository
from modules.logger.logger_manager import LoggerManager

class BaseTestAccount(unittest.TestCase):
  def setup_method(self, method: Callable) -> None:
    print(f"Executing:: {method.__name__}")
    ConfigService.load_config()
    LoggerManager.mount_logger()
    AccountServiceManager.create_rest_api_server()

  def teardown_method(self, method: Callable) -> None:
    print(f"Executed:: {method.__name__}")
    AccountRepository.account_db.delete_many({})
