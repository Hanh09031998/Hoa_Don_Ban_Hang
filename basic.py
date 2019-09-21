import os
import json
import datetime

now = datetime.datetime.now()
date_time = now.strftime("%d.%m.%Y_%H.%M.%S")
date_dir = now.strftime("%d_%m_%Y")
hoa_don = {'soHoaDon':'',
        'ngayHoaDon':'',
        'tenKhachHang':'',
        'hangHoaDaMua':'',
        'tongTien':''}

hang_hoa = {'tenHangHoa' : '',
        'soLuong' : '',
        'donGia' :'',
        'thanhTien' : ''}

ds_hoaDon = []
ds_hangHoa = []
ds_loaiHangHoa = []

def load_loaihanghoa_luckhoidong():
    files = os.listdir("danhmuc/")
    if "loaihanghoa.csv" not in files:
        return

    with open('danhmuc/loaihanghoa.csv', 'r') as f:
        line = f.readline()
        while line:
            str_to_reads = line.split("#")
            #print("str_to_reads:", str_to_reads)
            if len(str_to_reads) > 1:
                loaihanghoa = {}
                loaihanghoa["id"] = str_to_reads[0]
                tenloai = str_to_reads[1]
                if tenloai.endswith('\n'):
                    tenloai = tenloai[0:len(tenloai)-1]
                loaihanghoa["ten"] = tenloai
                ds_loaiHangHoa.append(loaihanghoa)
            line = f.readline()
    #print("ds_loaiHangHoa:", ds_loaiHangHoa)

load_loaihanghoa_luckhoidong()

def load_hanghoa_luckhoidong():
    files = os.listdir("danhmuc/")
    if "hanghoa.csv" not in files:
        return
    with open('danhmuc/hanghoa.csv', 'r') as f:
        line = f.readline()
        while line:
            str_to_reads = line.split("#")
            #print("str_to_reads:", str_to_reads)
            if len(str_to_reads) > 1:
                hanghoa = {}
                hanghoa["id"] = str_to_reads[0]
                hanghoa["ten"] = str_to_reads[1]
                hanghoa["giaban"] = str_to_reads[2]
                hanghoa["loaihanghoa_id"] = str_to_reads[3]

                if hanghoa["loaihanghoa_id"].endswith('\n'):
                    hanghoa["loaihanghoa_id"] = hanghoa["loaihanghoa_id"][0:len(hanghoa["loaihanghoa_id"])-1]
                ds_loaiHangHoa.append(hanghoa)
            line = f.readline()
    #print("danhsachhanghoa:", ds_loaiHangHoa)

load_hanghoa_luckhoidong()

def xem_loaiHangHoa(id = None):
    if id is None:
        id = input("xin moi nhap id loai hang hoa:")
    for loai in ds_loaiHangHoa:
        if loai["id"] == id:
            print("loai hang hoa: ", loai)
            return loai

def tao_loaiHangHoa():
    data = {}
    id = input("xin moi nhap id loai hang hoa:")
    tim_id_daco = xem_loaiHangHoa(id)
    if tim_id_daco is not None:
        print("Da ton tai Ma loai hang hoa nay. Xin moi ban thu hien chu nang khac")
        return

    data["id"] = id
    data["ten"] = input("xin moi nhap ten loai hang hoa:")
    ds_loaiHangHoa.append(data)
    str_to_save = data["id"] + "#" + data["ten"] + '\n'
    with open('danhmuc/loaihanghoa.csv', 'a') as f:
	    data = f.write(str_to_save)

def tao_hangHoa():
    data = {}
    id = input("xin moi nhap id hang hoa:")
    tim_id_daco = xem_loaiHangHoa(id)
    if tim_id_daco is not None:
        print("Da ton tai Ma loai hang hoa nay. Xin moi ban thu hien chu nang khac")
        return
    data["id"] = id
    data["ten"] = input("xin moi nhap ten hang hoa:")
    data["giaban"] = input("xin moi nhap gia ban:")
    loaihanghoa_id = input("xin moi nhap ma loai hang hoa:")
	
    #co_hienthi_danhsachloai = False
    tim_idloai_daco = xem_loaiHangHoa(loaihanghoa_id)
  
    while tim_idloai_daco is None:
        print("Danh sach loai hang hoa:")
        for loaihanghoai in ds_loaiHangHoa:
            print(loaihanghoai["id"])
    loaihanghoa_id = input("xin moi nhap ma loai hang hoa:")
    tim_idloai_daco = xem_loaiHangHoa(loaihanghoa_id)
	
  
    data["loaihanghoa_id"] = loaihanghoa_id
    ds_hangHoa.append(data)
    str_to_save = data["id"] + "#" + data["ten"] + '#' + data["giaban"] + "#" +  data["loaihanghoa_id"] + '\n'
    with open('danhmuc/hanghoa.csv', 'a') as f:
         data = f.write(str_to_save)


def xem_hangHoa(id = None):
    if id is None:
        id = input("xin moi nhap id hang hoa:")
    for hanghoa in ds_hangHoa:
        if hanghoa["id"] == id:
            print(hanghoa)
            return hanghoa

def nhap_hoaDon():
    hoa_don['soHoaDon'] = input("Moi ban nhap so hoa don: ")
    hoa_don['ngayHoaDon'] = date_time
    hoa_don['tenKhachHang'] = input("Moi ban nhap ten khach hang: ")
    hoa_don['hangHoaDaMua'] = []


def nhap_hangHoa():
    id = input("Moi ban nhap id cua hang hoa can mua: ")
    id_hangHoa = check_id_hangHoa(id)
    #print("=====ID===", id_hangHoa)
    while id_hangHoa is None:
        xem_id_hangHoa()
        id_exit = input("Ban da nhap sai id cua hang hoa, xin moi nhap lai: ")
        id_hangHoa = check_id_hangHoa(id_exit)
    while id_hangHoa is not None:
        data = load_id_hangHoa(int(id_hangHoa))
        hang_hoa["tenHangHoa"] = data[0]
        #print("---Ten: ", hang_hoa["tenHangHoa"])
        hang_hoa["soLuong"] = int(input("Moi ban nhap so luong hang hoa can mua: "))
        hang_hoa["donGia"] = int(data[1])
        #print("---Gia: ", hang_hoa["donGia"])
        hang_hoa['thanhTien'] = hang_hoa['soLuong']* hang_hoa['donGia']
        #print("---Tien: ", hang_hoa["thanhTien"])
        break


id_list = []
def get_id(path):
    id_dict = {}
    if os.stat(path).st_size == 0:
        id_dict["id"] = '0'
        id_list.append(id_dict)
        return id_dict
    else:
        with open(path, 'r') as f:
            line = f.readline()
            while line:
                str_to_reads = line.split("#")
                # print(str_to_reads[0])
                id_dict["id"] = str_to_reads[0]
                line = f.readline()
            id_list.append(id_dict)
        # print(id_dict["id"])
        return id_dict


def tao_hoaDon():
        nhap_hoaDon()
        while True:
            nhap_hangHoa()
            hoa_don['hangHoaDaMua'] = ds_hangHoa.append(hang_hoa.copy())
            #hoa_don['hangHoaDaMua'].append(hang_hoa.copy())
            choose = input("Ban co muon nhap tiep hang hoa can mua khong?(c/k):")
            if choose =='k':
                    print("Da nhap het mat hang can mua")
                    break
        ds_hoaDon.append(hoa_don.copy())
        hoa_don['tongTien'] = tong_tien()

        filename = "HD_" + date_time +".json"
        with open('hoadon/' + filename, 'w') as f:
            json.dump(hoa_don, f)
        data = open("hoadon/ds_HD.txt", "a")
        data.write("HD_" + date_time +"\n")


def tong_tien():
        tien = 0
        for tongTien in ds_hangHoa:
            tien += tongTien['thanhTien']
        return tien

def tong_doanh_thu():
        doanhThu = 0
        for doanhthu in ds_hoaDon:
                doanhThu += doanhthu['tongTien']
        print('Tong doanh thu cua cua hang la: ', doanhThu)

def tong_hang_hoa(ten_hh):
        soLuong = 0
        doanhSoBan = 0
        for hoadon in ds_hoaDon:
                for dem in hoadon['hangHoaDaMua']:
                        if dem['tenHangHoa'] == ten_hh:
                                soLuong += dem['soLuong']
                                doanhSoBan+=dem['thanhTien']
                                break
        print("Tong so hang hoa ban ra: ", soLuong)
        print("Doanh so ban: ", doanhSoBan)

def xem_hoa_don(hDon):
        stt = 0
        print("********************HOA DON MUA HANG*************************")
        print("So hoa don: " + str(hDon['soHoaDon']))
        print("Ngay hoa don: " + str(hDon['ngayHoaDon']))
        print("Nguoi mua hang: " + str(hDon['tenKhachHang']))
        print("                  Danh sach hang hoa                          ")
        print("+-----+--------------------+----------+----------+-----------+")
        print("| STT |   TEN HANG HOA     |  DON GI  | SO LUONG | THANH TIEN|")
        print("+-----+--------------------+----------+----------+-----------+")
        for hHoa in hDon['hangHoaDaMua']:
                stt+=1
                print("|" + str(stt).rjust(5,' ')
                        +"|" + str(hHoa['tenHangHoa']).rjust(20,' ')
                        +"|" + str(hHoa['donGia']).rjust(10,' ')
                        +"|" + str(hHoa['soLuong']).rjust(10,' ')
                        +"|" + str(hHoa['thanhTien']).rjust(11,' ')+ "|")
                print("+-----+--------------------+----------+----------+-----------+")
        print("|                                TONG TIEN:      |"
                + str(hDon['tongTien']).rjust(11,' ')+ "|")
        print("+-----+--------------------+----------+----------+-----------+")

def view_hoaDon():
    sohoadon_canxem = ''
    while not os.path.isfile('hoadon/'+ sohoadon_canxem +'.json'):
        sohoadon_canxem = input("Moi ban nhap so hoa don can xem:")  
    return sohoadon_canxem


def check_id_hangHoa(id):
    with open("danhmuc/hanghoa.csv", "r") as f:
        line = f.readline()
        while(line):
            tring_to_reads = line.split("#")
            hang_hoa = {}
            hang_hoa["id"] = tring_to_reads[0]
            if int(hang_hoa["id"]) == int(id):
                return hang_hoa["id"]
            line = f.readline()


def xem_id_hangHoa():
    files = os.listdir("danhmuc/")
    if "hanghoa.csv" not in files:
        return
    with open('danhmuc/hanghoa.csv', 'r') as f:
        line = f.readline()
        print("ID-----Ten Hang Hoa------------Gia Ban--Ma Loai")
        while line:
            string_to_reads = line.split("#")
            if len(string_to_reads) > 1:
                hang_hoa = {}
                hang_hoa["id"] = string_to_reads[0]
                hang_hoa["ten"] = string_to_reads[1]
                hang_hoa["giaban"] = string_to_reads[2]
                hang_hoa["id_loai"] = string_to_reads[3]
                if hang_hoa["id_loai"].endswith('\n'):
                    hang_hoa["id_loai"] = hang_hoa["id_loai"][0:len(hang_hoa["id_loai"])-1]
                print( hang_hoa["id"],"\t",hang_hoa["ten"].ljust(15),"\t",hang_hoa["giaban"],"\t",hang_hoa["id_loai"] )
            line = f.readline()
    return xem_id_hangHoa


def load_id_hangHoa(id):
    files = os.listdir("danhmuc/")
    if "hanghoa.csv" not in files:
        return
    with open('danhmuc/hanghoa.csv', 'r') as f:
        line = f.readline()
        while line:
            string_to_reads = line.split("#")
            if len(string_to_reads) > 1:
                if int(string_to_reads[0]) == id:
                    hang_hoa = {}
                    hang_hoa["id"] = string_to_reads[0]
                    hang_hoa["ten"] = string_to_reads[1]
                    hang_hoa["giaban"] = string_to_reads[2]
                    hang_hoa["id_loai"] = string_to_reads[3]
                    if hang_hoa["id_loai"].endswith('\n'):
                        hang_hoa["id_loai"] = hang_hoa["id_loai"][0:len(hang_hoa["id_loai"])-1]
            line = f.readline()

    return hang_hoa["ten"],hang_hoa["giaban"]
