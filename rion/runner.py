"""
    This is where the real magic happens
"""

from rion import runner_search
from rion import runner_remove
from rion import runner_installer
from rion import runner_dlist
from rion import runner_freeze
from rion import runner_config
from rion import runner_check
from rion import runner_update
from rion import runner_upgrade
from rion import runner_install


def install(content: list) -> None:
    """
    install a package
    """
    runner_install.runnerable_install()


def update(content: list) -> None:
    """
    updates the package list
    """
    runner_update.runnerable_update(content)


def upgrade(content: list) -> None:
    """
    updates the package list
    """
    runner_upgrade.runnerable_upgrade(content)


def search(content: list) -> None:
    """
    Rion is now looking for packages
    """
    runner_search.runnerable_search("rion.db", content)


def remove(content: list) -> None:
    """
    Rion remove packages
    """
    runner_remove.runnerable_remove("rion.db", content)


def dlist() -> None:
    """
    Rion list packages
    """
    runner_dlist.runnerable_dlist("rion.db")


def freeze(content: list) -> None:
    """
    Rion freeze packages
    """
    runner_freeze.runnerable_freeze(content)


def check(content: list) -> None:
    """
    Rion check packages
    """
    runner_check.runnerable_check(content)


def config(content: list) -> None:
    """
    Rion config packages
    """
    runner_config.runnerable_config(content)


def init() -> None:
    """
    Load install skript
    """
    runner_installer.runnerable_install()
