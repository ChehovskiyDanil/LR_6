#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def add_route(stations, destination, train_number, departure_time):
    route = {
        "Destination": destination,
        "Train number": train_number,
        "Departure time": departure_time
    }
    stations.append(route)
    sort_routes_by_time(stations)
    return stations


def sort_routes_by_time(stations):
    stations.sort(key=lambda item: item.get('Departure time', ''))
    return stations


def display_routes(stations):
    if not stations:
        print("Список маршрутов пуст.")
        return

    line = '=-{}-+-{}-+-{}-+'.format(
        '-' * 30,
        '-' * 15,
        '-' * 20
    )
    print(line)
    print(
        '| {:^30} | {:^15} | {:^20} |'.format(
            "Пункт назначения",
            "Номер поезда",
            "Время отправления"
        )
    )
    print(line)

    for route in stations:
        print(
            '| {:^30} | {:^15} | {:^20} |'.format(
                route.get('Destination', ''),
                route.get('Train number', ''),
                route.get('Departure time', ''),
            )
        )

    print(line)


def select_routes_by_city(stations, city):
    found_routes = []
    for route in stations:
        if route.get('Destination', '').lower() == city.lower():
            found_routes.append(route)

    return found_routes


def display_selected_routes(routes):
    if not routes:
        print("Маршруты по указанному городу не найдены.")
        return

    line = '=-{}-+-{}-+-{}-+'.format(
        '-' * 30,
        '-' * 15,
        '-' * 20
    )
    print(line)
    print(
        '| {:^30} | {:^15} | {:^20} |'.format(
            "Пункт назначения",
            "Номер поезда",
            "Время отправления"
        )
    )
    print(line)

    for route in routes:
        print(
            '| {:^30} | {:^15} | {:^20} |'.format(
                route.get('Destination', ''),
                route.get('Train number', ''),
                route.get('Departure time', ''),
            )
        )

    print(line)
    print(f"Найдено маршрутов: {len(routes)}")


def display_help():
    print("Список команд:\n")
    print("add - добавить маршрут;")
    print("list - вывести список всех маршрутов;")
    print("select - запросить маршруты по указанному городу;")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")


def main():
    stations = []

    while True:
        command = input("\n>>> ").strip().lower()

        if command == 'exit':
            print("Завершение работы программы.")
            break
        elif command == 'add':
            destination = input("Пункт назначения: ").strip()
            train_number = input("Номер поезда: ").strip()
            departure_time = input("Время отправления: ").strip()

            stations = add_route(stations, destination, train_number, departure_time)
            print("Маршрут успешно добавлен.")

        elif command == 'list':
            display_routes(stations)

        elif command == 'select':
            city = input("Введите город: ").strip()
            selected_routes = select_routes_by_city(stations, city)
            display_selected_routes(selected_routes)

        elif command == 'help':
            display_help()

        else:
            print(f"Неизвестная команда '{command}'", file=sys.stderr)
            print("Введите 'help' для просмотра доступных команд")


if __name__ == "__main__":
    main()