#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def get_user():
    name = input("Фамилия или имя? ")
    age = input("Возраст? ")
    city = input("Город проживания? ")
    interests = input("Хобби (Через запятую)?")

    interests_list = []
    if interests:  # Проверяем, не пустая ли строка
        interests_list = [interest.strip() for interest in interests.split(",") if interest.strip()]

    return {
        "name": name,
        "age": age,
        "city": city,
        "interests": interests_list
    }

def user_profile(name, *interests, **details):
    age = details.get('age')
    city = details.get('city')

    age_str = f", {age} лет" if age is not None else ""
    city_str = f" из {city}" if city is not None else ""
    info_line = f"{name}{age_str}{city_str}."

    if interests:
        interests_line = f" Интересы: {interests}."
    else:
        interests_line = " Интересы не указаны."

    return info_line + interests_line

def main():

    users = []

    while True:
        command = input(">>> ").lower()

        if command == "exit":
            break

        elif command == "add":
            user = get_user()

            users.append(user)

            if len(users) > 1:
                users.sort(key=lambda user: user.get('name', ''))

            print(f"Пользователь {user['name']} добавлен успешно!")


        elif command == "list":

            if not users:

                print("Список пользователей пуст.")

            else:

                print(f"\nСписок пользователей (всего: {len(users)}):")

                print("-" * 60)

                for i, user in enumerate(users, 1):

                    profile = user_profile(

                        user['name'],

                        *user['interests'],

                        age=user['age'] if user['age'] else None,

                        city=user['city'] if user['city'] else None

                    )

                    print(f"{i}. {profile}")



        elif command == "help":

            print("Список команд:\n")
            print("add - добавить пользователя;")
            print("list - вывести список пользователей;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
            return 1

    return 0
if __name__ == "__main__":
    sys.exit(main())