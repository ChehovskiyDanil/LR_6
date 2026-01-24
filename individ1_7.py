#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ =="__main__":
    stations = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break
        elif command == 'add':
            destination = input("Destination: ")
            train = input("Train number: ")
            time = input("Departure time: ")

            station = {
                "Destination": destination,
                      "Train number": train,
                      "Departure time": time
            }
            stations.append(station)

            if len(stations) > 1:
                stations.sort(key=lambda item: item.get('Departure time', ''))
        elif command == 'list':
            line = '=-{}-+-{}-+-{}-+'.format(
                '-' * 30,
                '-' * 15,
                '-' * 20
            )
            print(line)
            print(
                '| {:^30} | {:^15} | {:^20} |'.format(
                    "Destination",
                    "Train number",
                    "Departure time"
                )
            )
            print(line)

            for idx, station in enumerate(stations, 1):
                print(
                    '| {:^30} | {:^15} | {:^20} |'.format(
                        station.get('Destination', ''),
                        station.get('Train number', ''),
                        station.get('Departure time', ''),
                    )
                )

            print(line)
        elif command.startswith('select'):
            city = input("Enter city: ")
            count = 0
            for station in stations:
                if station.get('Destination', station) == city:
                    count += 1
                    print(
                    '| {:^30} | {:^15} | {:^20} |'.format(
                        station.get('Destination', ''),
                        station.get('Train number', ''),
                        station.get('Departure time', ''),
                        ),
                    )
            if count == 0:
                print("Маршруты по ведённому городу не найдены.")

        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить маршрут;")
            print("list - вывести список всех маршрутов;")
            print("select - запросить маршруты по ведённому городу;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)