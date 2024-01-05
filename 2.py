class Luggage:
    def __init__(self, luggage_id, weight, departure_airport, destination_airport, passenger_name):
        self.id = luggage_id
        self.weight = weight
        self.departure_airport = departure_airport
        self.destination_airport = destination_airport
        self.passenger_name = passenger_name

    def query_luggage(self):
        return f"行李ID: {self.id}\n重量: {self.weight} 公斤\n出發機場: {self.departure_airport}\n目的地機場: {self.destination_airport}\n所屬旅客姓名: {self.passenger_name}"

    def update_id(self, new_id):
        self.id = new_id

    def update_weight(self, new_weight):
        self.weight = new_weight

    def update_departure_airport(self, new_departure_airport):
        self.departure_airport = new_departure_airport

    def update_destination_airport(self, new_destination_airport):
        self.destination_airport = new_destination_airport

    def update_passenger_name(self, new_passenger_name):
        self.passenger_name = new_passenger_name


class BoardingPass:
    def __init__(self, passenger_name, boarding_pass_number, boarding_time, gate_number, seat_position, luggage_count, luggage_id):
        self.passenger_name = passenger_name
        self.boarding_pass_number = boarding_pass_number
        self.boarding_time = boarding_time
        self.gate_number = gate_number
        self.seat_position = seat_position
        self.luggage_count = luggage_count
        self.luggage_id = luggage_id

    def print_boarding_pass(self):
        print(f"旅客姓名: {self.passenger_name}\n登機證編號: {self.boarding_pass_number}\n登機時間: {self.boarding_time}\n登機門編號: {self.gate_number}\n座位位置: {self.seat_position}\n行李件數: {self.luggage_count}\n行李ID: {self.luggage_id}")

    def update_passenger_name(self, new_passenger_name):
        self.passenger_name = new_passenger_name

    def update_boarding_pass_number(self, new_boarding_pass_number):
        self.boarding_pass_number = new_boarding_pass_number

    def update_boarding_time(self, new_boarding_time):
        self.boarding_time = new_boarding_time

    def update_gate_number(self, new_gate_number):
        self.gate_number = new_gate_number

    def update_seat_position(self, new_seat_position):
        self.seat_position = new_seat_position

    def update_luggage_count(self, new_luggage_count):
        self.luggage_count = new_luggage_count

    def update_luggage_id(self, new_luggage_id):
        self.luggage_id = new_luggage_id


# 主函式
def main():
    # 建立三個行李物件
    luggage1 = Luggage("L001", 20, "TPE", "JFK", "Alice")
    luggage2 = Luggage("L002", 15, "TPE", "LAX", "Bob")
    luggage3 = Luggage("L003", 25, "TPE", "CDG", "Charlie")

    # 查詢行李資訊
    print("行李1資訊:")
    print(luggage1.query_luggage())
    print("\n行李2資訊:")
    print(luggage2.query_luggage())
    print("\n行李3資訊:")
    print(luggage3.query_luggage())

    # 修改行李資訊
    luggage1.update_weight(22)
    luggage2.update_destination_airport("SFO")
    luggage3.update_passenger_name("David")

    # 再次查詢行李資訊
    print("\n修改後的行李1資訊:")
    print(luggage1.query_luggage())
    print("\n修改後的行李2資訊:")
    print(luggage2.query_luggage())
    print("\n修改後的行李3資訊:")
    print(luggage3.query_luggage())

    # 建立三個登機證物件
    boarding_pass1 = BoardingPass("Alice", "BP001", "12:00 PM", "Gate A", "A12", 2, "L001")
    boarding_pass2 = BoardingPass("Bob", "BP002", "1:30 PM", "Gate B", "B05", 1, "L002")
    boarding_pass3 = BoardingPass("Charlie", "BP003", "3:00 PM", "Gate C", "C08", 3, "L003")

    # 列印登機證資訊
    print("\n登機證1資訊:")
    boarding_pass1.print_boarding_pass()
    print("\n登機證2資訊:")
    boarding_pass2.print_boarding_pass()
    print("\n登機證3資訊:")
    boarding_pass3.print_boarding_pass()

    # 修改登機證資訊
    boarding_pass1.update_seat_position("A15")
    boarding_pass2.update_luggage_count(2)
    boarding_pass3.update_gate_number("Gate D")

    # 再次列印登機證資訊
    print("\n修改後的登機證1資訊:")
    boarding_pass1.print_boarding_pass()
    print("\n修改後的登機證2資訊:")
    boarding_pass2.print_boarding_pass()
    print("\n修改後的登機證3資訊:")
    boarding_pass3.print_boarding_pass()

# 執行主函式
main()