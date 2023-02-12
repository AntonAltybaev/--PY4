from datetime import datetime
from typing import List


class SocialNetwork:
    """
    Abstract social network
    """

    def __init__(self, name: str, creators: List[str], created_date: datetime.date, servers: List[str],
                 count_of_users: int) -> None:
        self.creators = creators
        self.created_date = created_date
        self.servers = servers
        self.name = name
        self.count_of_users = count_of_users

    def __str__(self) -> str:
        """
        social network string representation
        :return: str
        """
        return f"Social network name: {self.name}, " \
               f"creators: {self.creators}, current number of users: {self.count_of_users}"

    def __repr__(self) -> str:
        """
        social network object representation
        :return: str
        """
        return f"SocialNetwork(name={self.name}, creators={self.creators}, created_date={self.created_date}, " \
               f"servers={self.servers}, count_of_users={self.count_of_users})"

    def add_new_user(self) -> None:
        """
        Add new user to network
        :return: None
        """
        self.count_of_users += 1


class Facebook(SocialNetwork):
    """
    Facebook network
    """

    def __init__(self, name: str, creators: List[str], created_date: datetime.date, servers: List[str],
                 count_of_users: int, instagram_users: int) -> None:
        super().__init__(name, creators, created_date, servers, count_of_users)
        self.instagram_users = instagram_users
        self.__secret_data = "SECRET FACEBOOK DATA"

    def __get_users_statistic(self) -> int:
        """
        get facebook and inst users
        получение статистики только внутри класса для внутринних алгоритмов Facebook
        :return: int
        """
        return self.count_of_users + self.instagram_users

    def __str__(self) -> str:
        """
        facebook string representation
        :return: str
        """
        return f"Facebook: creators-{self.creators}, facebook users-{self.count_of_users}, " \
               f"instagram users-{self.instagram_users}"

    def add_new_user(self) -> None:
        """
        Регистрация происходит сразу и в facebook и в instagram
        :return: None
        """
        self.count_of_users += 1
        self.instagram_users += 1


class VK(SocialNetwork):
    """
    VK network
    """

    def __init__(self, name: str, creators: List[str], created_date: datetime.date, servers: List[str],
                 count_of_users: int, mail_ru_users: int) -> None:
        super().__init__(name, creators, created_date, servers, count_of_users)
        self.mail_ru_users = mail_ru_users
        self.__secret_data = "SECRET VK DATA"

    def __str__(self) -> str:
        """
        vk string representation
        :return: str
        """
        return f"VK: creators-{self.creators}, vk users-{self.count_of_users}, " \
               f"mail users-{self.mail_ru_users}"

    def __iter_through_secret_data(self) -> None:
        """
        Just iter
        просмотр этой информации должен быть доступен только внутри класса
        :return: None
        """
        for data in self.__secret_data:
            print(data)

    def add_new_user(self) -> None:
        """
        Регистрация происходит сразу и в vk и в mail
        :return: None
        """
        self.count_of_users += 1
        self.mail_ru_users += 1
