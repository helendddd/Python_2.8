#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Использовать словарь, содержащий следующие ключи:
# название пункта назначения рейса; номер рейса; тип самолета.
# Написать программу, выполняющую следующие действия: ввод с клавиатуры
# данных в список, состоящий из словарей заданной структуры;
# записи должны быть размещены в алфавитном порядке по названиям
# пунктов назначения; вывод на экран пунктов назначения и номеров рейсов,
# обслуживаемых самолетом, тип которого введен с клавиатуры;
# если таких рейсов нет, выдать на дисплей соответствующее сообщение.


def add_flight():
    destination = input("Введите название пункта назначения: ")
    flight_number = input("Введите номер рейса: ")
    plane_type = input("Введите тип самолета: ")

    new_flight = {
        'destination': destination,
        'flight number': flight_number,
        'type of plane': plane_type
    }

    flights.append(new_flight)
    flights.sort(key=lambda x: x['destination'])


def list_flights():
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 20
    )
    print(line)

    print(
        '| {:^4} | {:^30} | {:^20} | {:^20} |'.format(
            "No",
            "Пункт назначения",
            "Номер рейса",
            "Тип самолета"
        )
    )

    print(line)

    for idx, flight in enumerate(flights, 1):
        print(
            '| {:>4} | {:<30} | {:<20} | {:>20} |'.format(
                idx,
                flight.get('destination', ''),
                flight.get('flight number', ''),
                flight.get('type of plane', 0)
            )
        )
    print(line)


def find_flights():
    find_type = input("Введите тип самолета для поиска: ")
    found = []

    for flight in flights:
        if flight['type of plane'] == find_type:
            found.append(flight)

    if not found:
        print(f"Рейсов на самолете типа '{find_type}' не найдено.")
    else:
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 20
        )
        print(line)

        print(
            '| {:^4} | {:^30} | {:^20} | {:^20} |'.format(
                "No",
                "Пункт назначения",
                "Номер рейса",
                "Тип самолета"
            )
        )

        print(line)

        for idx, found_flight in enumerate(found, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:>20} |'.format(
                    idx,
                    found_flight.get('destination', ''),
                    found_flight.get('flight number', ''),
                    found_flight.get('type of plane', 0)
                )
            )
        print(line)


if __name__ == '__main__':
    flights = []

    print(">>> Выберите нужную команду: add, list, find или exit ")

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            add_flight()

        elif command == 'list':
            list_flights()

        elif command == 'find':
            find_flights()
