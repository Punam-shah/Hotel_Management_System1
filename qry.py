from assignment.connection import db


class Check_in:
    def __init__(self):
        self.database = db()

    def add(self, date, name, address, contact, no_of_days, payment):
        qry = "INSERT INTO hotel_management_system (Date ,Name, Address, Contact, No_of_days,Payment_method) VALUES (%s,%s,%s,%s,%s,%s)"
        values = (date, name, address, contact, no_of_days, payment)
        self.database.uid(qry, values)
        return True

    def show(self, key):
        qry = "SELECT * FROM hotel_management_system WHERE Name LIKE '" + key + "%'"
        all_data = self.database.show(qry)
        return all_data

    def search(self, key):
        qry = "SELECT * FROM room WHERE Name LIKE '" + key + "%'"
        all_data = self.database.show(qry)
        return all_data

    def update(self, row, date, name, address, contact, no_of_days, payment):
        qry = "UPDATE hotel_management_system SET Date = %s, Name = %s, Address = %s, Contact = %s, No_of_days = %s, Payment_method = %s WHERE id = %s"
        values = (date, name, address, contact, no_of_days, payment, row)
        self.database.uid(qry, values)
        return True

    def delete(self, date):
        qry = "DELETE FROM hotel_management_system Where Date = %s"
        self.database.uid(qry, (date,))

    def check_out(self, date, name, room_no):
        qry = "INSERT INTO check_out (Date ,Name,Room_no) VALUES (%s,%s,%s)"
        values = (date, name,  room_no)
        self.database.uid(qry, values)
        return True

    def add_room(self, name, room_no, room_type):
        qry = "INSERT INTO room (Name, Room_no, Room_Type) VALUES (%s,%s,%s)"
        values = (name, room_no, room_type)
        self.database.uid(qry, values)
        return True

    def show_room(self):
        qry = "SELECT * FROM room"
        all_data = self.database.show(qry)
        return all_data

    def show_all(self):
        qry = "SELECT hotel_management_system.id, hotel_management_system.Date, hotel_management_system.Name, hotel_management_system.Address, hotel_management_system.Contact, hotel_management_system.No_of_days, hotel_management_system.Payment_method, room.Room_no, room.Room_Type FROM hotel_management_system JOIN room ON hotel_management_system.Name = room.Name"
        all = self.database.show(qry)
        return all

    def delete1(self, name):
        qry = "DELETE FROM hotel_management_system Where Name = %s"
        self.database.uid(qry, (name,))

    def delete2(self, name, room_no):
        qry = "DELETE FROM room Where Name = %s and Room_no=%s "
        self.database.uid(qry, (name, room_no))


    def add_guest(self, name, room_no, date):
        qry = "INSERT INTO guest_list (Name, Room_no, Date) VALUES (%s,%s,%s)"
        values = (name, room_no, date)
        self.database.uid(qry, values)
        return True

    def show_guest(self):
        qry = "SELECT guest_list.Name, guest_list.Room_no, guest_list.Date, check_out.Date FROM guest_list JOIN check_out ON guest_list.Name = check_out.Name"
        all_data = self.database.show(qry)
        return all_data

    def update_room(self, row, name, room_no, room_type):
        qry = "UPDATE room SET Name = %s, Room_no = %s, Room_Type = %s WHERE id = %s "
        values = (name, room_no, room_type, row)
        self.database.uid(qry, values)
        return True

    def show_1(self, key):
        qry = "SELECT hotel_management_system.id, hotel_management_system.Date, hotel_management_system.Name, hotel_management_system.Address, hotel_management_system.Contact, hotel_management_system.No_of_days, hotel_management_system.Payment_method, room.Room_no, room.Room_Type FROM hotel_management_system JOIN room ON hotel_management_system.Name = room.Name WHERE hotel_management_system.Name LIKE '" + key + "%'"
        all = self.database.show(qry)
        return all


