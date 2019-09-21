
import datetime
import hashlib
import shutil
import sys
import json
import os
import basic

class user():
    id = None
    status = None
    email = None
    account_name = None
    create_date = None
    def __init__(self,id,account_name):
        self.id = id
        self.account_name = account_name
        now = datetime.datetime.now()
        self.create_date = now.strftime("%d/%m/%Y, %H:%M:%S")
        
    def tao_NhanVien(self,status,email,password):
        self.password = password
        self.email = email
        str_to_save = str(self.id) + "#" + str(self.status) + "#" + str(self.email) + "#" + str(self.password) + "#" + str(self.account_name) + "#" + str(self.create_date) + '\n'
        print(str_to_save)
        with open('Data/nhanvien.csv', 'a') as f:
            str_to_save = f.write(str_to_save)

    def tao_KhachHang(self,phone):
        self.phone = phone
        str_to_save = str(self.id) + "#" + str(self.phone) + "#" + str(self.account_name) + "#" + str(self.create_date) + '\n'
        print(str_to_save)
        with open('Data/khachhang.csv', 'a') as f:
            str_to_save = f.write(str_to_save) 




nhanVien_List = []
def load_NhanVien():
    with open('Data/tao_NhanVien.csv', 'r') as f:
        line = f.readline()
        while line:
            str_to_reads = line.split("#")
            if len(str_to_reads) > 1:
                list_NhanVien = {}
                list_NhanVien["status"] = str_to_reads[1]
                list_NhanVien["email"] = str_to_reads[2]
                list_NhanVien["password"] = str_to_reads[3]
                nhanVien_List.append(list_NhanVien)
            line = f.readline()
    return  nhanVien_List


khachHang_List = []
def load_KhachHang():
    with open('Data/tao_KhachHang.csv', 'r') as f:
        line = f.readline()
        while line:
            str_to_reads = line.split("#")
            if len(str_to_reads) > 1:
                list_KhachHang = {}
                list_KhachHang["phone"] = str_to_reads[2]
                khachHang_List.append(list_KhachHang)
            line = f.readline()
    print("list_KhachHang:", khachHang_List)
    return  khachHang_List



def read_NhanVien():
    read_NhanVien =[]
    with open('Data/tao_NhanVien.csv', 'r') as f:
        line = f.readline()
        while line:
            str_to_reads = line.split("#")
            if len(str_to_reads) > 1:
                list_NhanVien = {}
                list_NhanVien["id"] = str_to_reads[0]
                list_NhanVien["status"] = str_to_reads[1]
                if int(list_NhanVien["status"]) == 1:
                    list_NhanVien["status"] = 'active'
                else:
                    list_NhanVien["status"] = 'inactive'
                list_NhanVien["email"] = str_to_reads[2]
                list_NhanVien["account_name"] = str_to_reads[4]
                list_NhanVien["create_date"] = str_to_reads[5]
                if list_NhanVien["create_date"].endswith('\n'):
                    list_NhanVien["create_date"] = list_NhanVien["create_date"][0:len(list_NhanVien["create_date"])-1]
                read_NhanVien.append(list_NhanVien)
            line = f.readline()
    print("__________________________________________DANH SACH NHAN VIEN__________________________________________")
    print("+-------+---------------+-------------------------+-------------------------+-------------------------+")
    print("|  STT  |     Status    |        Email            |          Name           |        Create Date      |")
    print("+-------+---------------+-------------------------+-------------------------+-------------------------+")
    for lines in read_NhanVien:
        print("|",lines["id"].center(5),"|",
        lines["status"].ljust(13),"|",
        lines["email"].ljust(23),"|",
        lines["account_name"].ljust(23),"|",
        lines["create_date"].center(23),"|")
    print("+-------+---------------+-------------------------+-------------------------+-------------------------+")





def read_KhachHang():
    read_KhachHang =[]
    with open('Data/tao_KhachHang.csv', 'r') as f:
        line = f.readline()
        while line:
            str_to_reads = line.split("#")
            if len(str_to_reads) > 1:
                list_KhachHang = {}
                list_KhachHang["id"] = str_to_reads[0]
                list_KhachHang["phone"] = str_to_reads[1]
                list_KhachHang["account_name"] = str_to_reads[2]
                list_KhachHang["create_date"] = str_to_reads[3]
                if list_KhachHang["create_date"].endswith('\n'):
                    list_KhachHang["create_date"] = list_KhachHang["create_date"][0:len(list_KhachHang["create_date"])-1]
                read_KhachHang.append(list_KhachHang)
            line = f.readline()

    print("______________________________DANH SACH KHACH HANG___________________________")
    print("+-------+---------------+-------------------------+-------------------------+")
    print("|  STT  |     Phone     |        Email            |        Create Date      |")
    print("+-------+---------------+-------------------------+-------------------------+")
    for lines in read_KhachHang:
        print("|",lines["id"].center(5),"|",
        lines["phone"].ljust(13),"|",
        lines["account_name"].ljust(23),"|",
        lines["create_date"].center(23),"|")
    print("+-------+---------------+-------------------------+-------------------------+")






def new_NhanVien():
    load_NhanVien()
    email = input("Nhap email cua ban: ")
    count = 0
    for nhanVien in nhanVien_List:
        if email.upper() == nhanVien["email"].upper():
            count += 1
    if count > 0:
        print("Ten dang nhap da ton tai!", email)
    else:
        id_list = basic.get_id('Data/tao_NhanVien.csv')

        idNew = int(id_list["id"]) + 1

        account_name = input("Nhap tai khoan nhan vien: ")
        password_text = input("Nhap mat khau: ")
        password_encode = hashlib.md5(password_text.encode()).hexdigest()
        print(password_encode)
        print(idNew,1,email,password_encode,account_name,'')
        sellerAcc = user(idNew,account_name)
        sellerAcc.tao_NhanVien(1,email,password_encode)
    


def new_KhachHang(msisdn):
    load_KhachHang()
    phone = input("Nhap so dien thoai cua ban: ")
    count = 0
    for khachHang in khachHang_List:
        if phone == khachHang["phone"]:
            count += 1
    if count > 0:
        print("Ten dang nhap da ton tai!!!", phone)
    else:
        id_list = basic.get_id('Data/tao_KhachHang.csv')
        print(id_list["id"])
        idNew = int(id_list["id"]) + 1
        account_name = input("Nhap tai khoan cua ban: ")
        print(idNew,1,account_name,'')
        sellerAcc = user(idNew,account_name)
        sellerAcc.tao_KhachHang(phone)



def xoa_NhanVien():
    shutil.copy('Data/tao_NhanVien.csv', 'Data/NhanVien_back.csv')
    email = input("Nhap tai khoan nhan vien ma ban muon xoa: ")
    with open('Data/NhanVien_back.csv', 'r') as f:
        with open('Data/tao_NhanVien.csv', 'w') as wfile:
            line = f.readline()
            while line:
                str_to_reads = line.split("#")
                if len(str_to_reads) > 1:
                    if email.upper() == str_to_reads[2].upper():
                        email = str_to_reads[2]
                        newline = line.replace("#1#", "#0#")
                        newline = wfile.write(newline)
                    else:
                        line = wfile.write(line)
                line = f.readline()
        wfile.closed


def update_NhanVien():
    shutil.copy('Data/tao_NhanVien.csv', 'Data/NhanVien_back.csv')
    email = input("Nhap tai khoan muon update: ")
    with open('Data/NhanVien_back.csv', 'r') as f:
        with open('Data/tao_NhanVien.csv', 'w') as wfile:
            line = f.readline()
            while line:
                str_to_reads = line.split("#")
                if len(str_to_reads) > 1:
                    if email.upper() == str_to_reads[2].upper():
                        id = str_to_reads[0]
                        status = str_to_reads[1]
                        email = str_to_reads[2]
                        password_text = input("Nhap password moi neu ban muon thay doi:")
                        if len(password_text) > 1:
                            password = hashlib.md5(password_text.encode()).hexdigest()
                        else:
                            password = str_to_reads[3]
                        name = input("Nhap ten nguoi dung moi neu ban muon thay doi:")
                        if len(name) > 1:
                            account_name = name
                        else:
                            account_name = str_to_reads[4]
                        create_date = str_to_reads[5]
                        str_to_save = str(id) + "#" + str(status) + "#" + str(email) + "#" + str(password) + "#" + str(account_name) + "#" + str(create_date)
                        print("str_to_save:", str_to_save)
                        line = wfile.write(str_to_save)
                    else:
                        print("newSellerList 2:", line)
                        line = wfile.write(line)
                line = f.readline()
        wfile.closed
