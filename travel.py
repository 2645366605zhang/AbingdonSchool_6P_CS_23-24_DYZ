from __future__ import annotations
import os
from math import sqrt
from typing import Any, Dict, List
from code_repo.dataStructure import GraphNode as Node
from code_repo.locationLevel import LocationLevel, locationLevels

class Interface:
    def __init__(self) -> None:
        self._map_dict: Dict[str, "TravelMap | CartesianMap"] = {}
        self._current_interface: str = "default"
        self.main()

    def main(self) -> None:
        self.initialize()
        while True:
            os.system("cls")
            if self._current_interface == "mainMenu":
                self.show_main_menu()
            elif self._current_interface == "mapMenu":
                self.show_map_menu()
            elif self._current_interface == "mapsetMenu":
                self.show_mapset_menu()
            self.proceed_user_option()

    def initialize(self) -> None:
        usr_choice = input('Would you like to load a mapset?\nEnter "L" to load, other input to proceed.\n').upper()
        if usr_choice == "L":
            while True:
                mapset_loaded = self.load_mapset(input("Please enter the identifier of the mapset you would like to load: "))
                if mapset_loaded:
                    break
        self._current_interface = "mainMenu"

    def show_main_menu(self) -> None:
        print(f"MAP ORGANIZER   Ver_0.0.1\n\n{self.get_map_string()}\n\n(C)reate map, (S)ave map, (L)oad map, (D)elete map, (M)apset options, (Q)uit\n")

    def show_map_menu(self) -> None:
        pass

    def show_mapset_menu(self) -> None:
        pass

    def proceed_user_option(self) -> None:
        user_choice = input().upper()
        if self._current_interface == "mainMenu":
            if user_choice == "C":
                identifier = input('Please enter the indentifier of the new map, enter "Cancel" to cancel: ')
                name = input('Please enter the name of the new map, enter "Cancel" to cancel: ')
                while True:
                    try:
                        x_size = int(input('Please enter the x-Size of the new map in integer, enter "Cancel" to cancel: '))
                        y_size = int(input('Please enter the y-size of the new map in integer, enter "Cancel" to cancel: '))
                        break
                    except ValueError:
                        print("Invalid value, please try again.")
                while True:
                    try:
                        distance = float(input('Please enter the distance between two "blocks" for the new map in number of unit, enter "Cancel" to cancel: '))
                        break
                    except ValueError:
                        print("Invalid value, please try again.")
                self.create_cartesian_map(identifier, name, x_size, y_size, distance)
            elif user_choice == "S":
                os.makedirs("mapSave", exist_ok=True)
                while True:
                    try:
                        target_map_identifier = input("Please enter the identifier of the map you want to save: ")
                        target_map = self._map_dict[target_map_identifier]
                        break
                    except KeyError:
                        print("Identifier doesn't exist, please try again.")
                map_save_name = input("Please enter the name of the file you want to save to: ")
                if os.path.isfile(f"mapSave/{map_save_name}.map"):
                    if not input("A file with the same name already exists, proceed to overwrite? (y/n): ").upper() == "Y":
                        return
                with open(f"mapSave/{map_save_name}.map", "w", encoding="utf-8") as current_save_file:
                    current_save_file.write(f"{target_map_identifier}\n")
                    current_save_file.write(f"{target_map.get_name()}\n")
                    current_save_file.write(f"{target_map.get_xsize()} {target_map.get_ysize()}\n")
                    current_save_file.write(f"{target_map.get_coordinate_distance()}\n")
                    current_save_file.write(f"{target_map.get_max_digit()}\n")
                    for location_index in range(len(target_map.get_location_list())):
                        print(f"\nstr(targetMap.GetLocationList()[locationIndex]): {str(target_map.get_location_list()[location_index])}\ntargetMap.GetLocationList()[location_index].GetLevel().GetLocalization(): {target_map.get_location_list()[location_index].get_level().get_localization()}\n")
                        current_save_file.write(f"{str(target_map.get_location_list()[location_index])} {target_map.get_location_list()[location_index].get_level().get_localization()}\n")
            elif user_choice == "L":
                pass
            elif user_choice == "D":
                pass
            elif user_choice == "M":
                pass
            elif user_choice == "Q":
                pass
        elif self._current_interface == "mapMenu":
            pass
        elif self._current_interface == "mapsetMenu":
            pass

    def create_cartesian_map(self, identifier: str, name: str, x_size: int, y_size: int, distance: int | float) -> None:
        self._map_dict[identifier] = CartesianMap(name, x_size, y_size, distance)

    def remove_map(self, identifier: str) -> "TravelMap | CartesianMap":
        return self._map_dict.pop(identifier)

    def save_map(self) -> None:
        pass

    def load_map(self) -> None:
        pass

    def save_mapset(self) -> None:
        pass

    def load_mapset(self) -> bool:
        pass

    def get_map_string(self) -> str:
        if len(self._map_dict) == 0:
            return "There isn't any map yet.\nConsider create or load one?"
        map_string_list: List[str] = []
        max_map_name_length = 8
        max_identifier_length = 10
        for map_key in self._map_dict:
            if len(self._map_dict[map_key].get_name()) > max_map_name_length:
                max_map_name_length = len(self._map_dict[map_key].get_name())
        for identifier in self._map_dict:
            if len(identifier) > max_identifier_length:
                max_identifier_length = len(identifier)
        for map_key in self._map_dict:
            map_string_list.append(f"{f'{map_key}':<{max_identifier_length}} | {f'{self._map_dict[map_key].get_name()}':<{max_map_name_length}}")
        map_string_list.insert(0, f"{'Identifier':<{max_identifier_length}} | {'Map Name':<{max_map_name_length}}\n")
        return "\n".join(map_string_list)

class Person:
    def __init__(self, position: int, name: str, symbol: str) -> None:
        self._position: int = position
        self._name: str = name
        self._symbol: str = symbol

    def get_name(self) -> str:
        return self._name
    
    def get_symbol(self) -> str:
        return self._symbol
    
    def get_position(self) -> int:
        return self._position
    
    def move_to(self, position: int) -> int:
        self._position = position
        return self._position

class TravelMap:
    def __init__(self, name: str) -> None:
        self._name: str = name
        self._max_digit: int = -1
        self._location_list: List["Location"] = []
    
    def get_name(self) -> str:
        return self._name
    
    def get_number_of_location(self) -> int:
        return len(self._location_list)
    
    def get_location(self, index: int) -> "Location":
        return self._location_list[index]
    
    def get_location_list(self) -> List["Location"]:
        return self._location_list
    
    def add_location(self, name: str = "Default", level_identifier: str = "NML") -> int:
        if name == "Default":
            name = f"Location{self.get_number_of_location()}"
        self._location_list.append(Location(name, level_identifier))
        return self.get_number_of_location() - 1
    
    def link_location(self, location_index0: int, location_index1: int, distance: float) -> None:
        self.get_location(location_index0).add_route(self.get_location(location_index1), distance)
    
    def set_level(self, index: int, level_identifier: str) -> None:
        self.get_location(index).update_level(level_identifier)
    
    def navigate(self, location_index0: int, location_index1: int) -> List[Any]:
        distances = [float('inf')] * self.get_number_of_location()
        predecessors = [None] * self.get_number_of_location()
        distances[location_index0] = 0
        visited = [False] * self.get_number_of_location()

        for _ in range(self.get_number_of_location()):
            min_distance = float('inf')
            u = None
            for index in range(self.get_number_of_location()):
                if not visited[index] and distances[index] < min_distance:
                    min_distance = distances[index]
                    u = index
            if u is None or u == location_index1:
                break
            visited[u] = True
            for v in range(self.get_number_of_location()):
                route = self.get_location(u).check_route(self.get_location(v))
                if route is not None and not visited[v]:
                    alt = distances[u] + route
                    if alt < distances[v]:
                        distances[v] = alt
                        predecessors[v] = u
        
        path: List[str] = []
        path_id: List[int] = []
        current = location_index1
        while current is not None:
            path.insert(0, str(self.get_location(current)))
            path_id.insert(0, current)
            current = predecessors[current]
            if current == location_index0:
                path.insert(0, str(self.get_location(location_index0)))
                path_id.insert(0, location_index0)
                break
        path_str = " — ".join(path)

        return [distances[location_index1], path_str, path_id]

class CartesianMap(TravelMap):
    def __init__(self, name: str, x_size: int, y_size: int, distance: int | float) -> None:
        super().__init__(name)
        self._x_size: int = x_size
        self._y_size: int = y_size
        self._coordinate_distance: int | float = distance
        self._coordinate_list: List[List[int]] = []
        self._person_dict: Dict[int, Person] = {}
        for x in range(self._x_size):
            x_location_list: List[int] = []
            for y in range(self._y_size):
                x_location_list.append(self.get_number_of_location())
                self.add_location(f"[{self.get_number_of_location()}]: {x}, {y}", "GND")
            self._coordinate_list.append(x_location_list)
        self._max_digit = 1
        for x in range(self._x_size):
            for y in range(self._y_size):
                if len(str(self._coordinate_list[x][y])) > self._max_digit:
                    self._max_digit = len(str(self._coordinate_list[x][y]))
        self.update_link()
    
    def get_xsize(self) -> int:
        return self._x_size
    
    def get_ysize(self) -> int:
        return self._y_size

    def get_coordinate_distance(self) -> int | float:
        return self._coordinate_distance

    def get_max_digit(self) -> int:
        return self._max_digit

    def update_link(self) -> None:
        for x in range(self._x_size):
            for y in range(self._y_size):
                self.get_location(self._coordinate_list[x][y]).clear_local_route()
        for x in range(self._x_size):
            for y in range(self._y_size):
                if x != 0:
                    try:
                        if self.get_location(self._coordinate_list[x][y]).check_route(self.get_location(self._coordinate_list[x - 1][y])) is None:
                            self.link_location(self._coordinate_list[x][y], self._coordinate_list[x - 1][y], self._coordinate_distance)
                    except IndexError:
                        print(f"Coordinate {x}, {y} has index out of range, skip\n")
                    try:
                        if self.get_location(self._coordinate_list[x][y]).check_route(self.get_location(self._coordinate_list[x - 1][y + 1])) is None:
                            self.link_location(self._coordinate_list[x][y], self._coordinate_list[x - 1][y + 1], sqrt(2 * (self._coordinate_distance ** 2)))
                    except IndexError:
                        print(f"Coordinate {x}, {y} has index out of range, skip\n")
                if y != 0:
                    try:
                        if self.get_location(self._coordinate_list[x][y]).check_route(self.get_location(self._coordinate_list[x][y - 1])) is None:
                            self.link_location(self._coordinate_list[x][y], self._coordinate_list[x][y - 1], self._coordinate_distance)
                    except IndexError:
                        print(f"Coordinate {x}, {y} has index out of range, skip\n")
                    try:
                        if self.get_location(self._coordinate_list[x][y]).check_route(self.get_location(self._coordinate_list[x + 1][y - 1])) is None:
                            self.link_location(self._coordinate_list[x][y], self._coordinate_list[x + 1][y - 1], sqrt(2 * (self._coordinate_distance ** 2)))
                    except IndexError:
                        print(f"Coordinate {x}, {y} has index out of range, skip\n")
                if x != 0 and y != 0:
                    try:
                        if self.get_location(self._coordinate_list[x][y]).check_route(self.get_location(self._coordinate_list[x - 1][y - 1])) is None:
                            self.link_location(self._coordinate_list[x][y], self._coordinate_list[x - 1][y - 1], sqrt(2 * (self._coordinate_distance ** 2)))
                    except IndexError:
                        print(f"Coordinate {x}, {y} has index out of range, skip\n")
                try:
                    if self.get_location(self._coordinate_list[x][y]).check_route(self.get_location(self._coordinate_list[x + 1][y + 1])) is None:
                        self.link_location(self._coordinate_list[x][y], self._coordinate_list[x + 1][y + 1], sqrt(2 * (self._coordinate_distance ** 2)))
                except IndexError:
                    print(f"Coordinate {x}, {y} has index out of range, skip\n")
                try:
                    if self.get_location(self._coordinate_list[x][y]).check_route(self.get_location(self._coordinate_list[x + 1][y])) is None:
                        self.link_location(self._coordinate_list[x][y], self._coordinate_list[x + 1][y], self._coordinate_distance)
                except IndexError:
                    print(f"Coordinate {x}, {y} has index out of range, skip\n")
                try:
                    if self.get_location(self._coordinate_list[x][y]).check_route(self.get_location(self._coordinate_list[x][y + 1])) is None:
                        self.link_location(self._coordinate_list[x][y], self._coordinate_list[x][y + 1], self._coordinate_distance)
                except IndexError:
                    print(f"Coordinate {x}, {y} has index out of range, skip\n")
    
    def get_coord_string(self) -> str:
        map_string_list: List[str] = []
        separator_h = "—" * (self._max_digit + 2)
        separator_v = "|"
        separator_c = "|"
        for y in range(self._y_size):
            line_list: List[str] = []
            for x in range(self._x_size):
                line_list.append(f"{f'{self._coordinate_list[x][y]}':^{self._max_digit + 2}}")
            map_string_list.insert(0, separator_v.join(line_list))
        return f"\n{f'{separator_h}{separator_c}' * (self._x_size - 1)}{separator_h}\n".join(map_string_list)
    
    def get_loc_string(self) -> str:
        map_string_list: List[str] = []
        separator_h = "—" * (self._max_digit + 2)
        separator_v = "|"
        separator_c = "|"
        for y in range(self._y_size):
            line_list: List[str] = []
            for x in range(self._x_size):
                line_list.append(f"{f'{self.get_location(self._coordinate_list[x][y]).get_level().get_localization()}':^{self._max_digit + 2}}")
            map_string_list.insert(0, separator_v.join(line_list))
        return f"\n{f'{separator_h}{separator_c}' * (self._x_size - 1)}{separator_h}\n".join(map_string_list)
    
    def get_person_string(self) -> str:
        map_string_list: List[str] = []
        separator_h = "—" * (self._max_digit + 2)
        separator_v = "|"
        separator_c = "|"
        for y in range(self._y_size):
            line_list: List[str] = []
            for x in range(self._x_size):
                line_list.append(f"{f'{self.get_person(self._coordinate_list[x][y]).get_symbol()}':^{self._max_digit + 2}}")
            map_string_list.insert(0, separator_v.join(line_list))
        return f"\n{f'{separator_h}{separator_c}' * (self._x_size - 1)}{separator_h}\n".join(map_string_list)
    
    def link_location(self, location_index0: int, location_index1: int, distance: float) -> None:
        if (self.get_location(location_index0).get_level().get_localization() != "▓" and
            self.get_location(location_index1).get_level().get_localization() != "▓"):
            if (self.get_location(location_index0).get_level().get_localization() == "▒" or
                self.get_location(location_index1).get_level().get_localization() == "▒"):
                self.get_location(location_index0).add_route(self.get_location(location_index1), distance * 1.5)
            else:
                self.get_location(location_index0).add_route(self.get_location(location_index1), distance)
        else:
            self.get_location(location_index0).add_route(self.get_location(location_index1), float('inf'))
    
    def set_level(self, index: int, level_identifier: str) -> None:
        super().set_level(index, level_identifier)
        self.update_link()

    def add_person(self, position: int, name: str, symbol: str) -> None:
        self._person_dict[position] = Person(position, name, symbol)
    
    def get_number_of_person(self) -> int:
        return len(self._person_dict)
    
    def get_person(self, coord_index: int) -> Person:
        if coord_index in self._person_dict:
            return self._person_dict[coord_index]
        return Person(-1, "Null", "")
    
    def move_person(self, person_coord_index: int, dest_coord_index: int) -> None:
        person = self.get_person(person_coord_index)
        self._person_dict[person.move_to(dest_coord_index)] = person
        del self._person_dict[person_coord_index]

class Location(Node):
    def __init__(self, name: str, level_identifier: str) -> None:
        super().__init__(name)
        self._level: LocationLevel = locationLevels[level_identifier]

    def get_level(self) -> LocationLevel:
        return self._level
    
    def add_route(self, node: "Location", distance: float) -> None:
        self.links[node] = distance
        node.links[self] = distance
    
    def clear_local_route(self) -> None:
        self.links = {}

    def check_route(self, node: "Location") -> float | None:
        return self.links.get(node)
    
    def update_level(self, level_identifier: str) -> None:
        self._level = locationLevels[level_identifier]

def main() -> None:
    main_interface = Interface()

if __name__ == "__main__":
    """test_map = TravelMap("Abingdon School")
    test_map.add_location("Amey Theatre")  # 0
    test_map.add_location("Big School")  # 1
    test_map.add_location("Crescent House")  # 2
    test_map.add_location("DT Department")  # 3
    test_map.add_location("Economics Classroom")  # 4
    test_map.add_location("Faringdon Lodge")  # 5
    test_map.add_location("Greening Court")  # 6
    test_map.link_location(0, 1, 2)
    test_map.link_location(0, 3, 3)
    test_map.link_location(3, 6, 1)
    test_map.link_location(4, 5, 1)
    test_map.link_location(1, 4, 4)
    test_map.link_location(1, 5, 3)
    test_map.link_location(2, 5, 2.5)
    navigation_result = test_map.navigate(3, 5)
    print(f'In map "{test_map.get_name()}", such route exists:\nRoute Length: {round(navigation_result[0], 2)}\nRoute Detail: {navigation_result[1]}')"""

    test_map = CartesianMap("CMap", 7, 3, 1)
    test_map.set_level(6, "WAL")
    test_map.set_level(7, "WAL")
    test_map.set_level(8, "COV")
    test_map.set_level(11, "COV")
    start_coordinate = 1
    end_coordinate = 19
    test_map.add_person(start_coordinate, "PLACEHOLDER", "P")
    navigation_result = test_map.navigate(start_coordinate, end_coordinate)
    print(f'In map "{test_map.get_name()}", such route exists:\nRoute Length: {round(navigation_result[0], 2)}\nRoute Detail: {navigation_result[1]}')
    print(f"Raw PathID: {navigation_result[2]}")
    print(f"\n{test_map.get_coord_string()}\n")
    print(f"\n{test_map.get_loc_string()}\n")
    print(f"Move From:\n{test_map.get_person_string()}\n")
    test_map.move_person(start_coordinate, end_coordinate)
    print(f"To:\n{test_map.get_person_string()}\n")
