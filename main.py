import json
import os
import basic
import user
def hoa_don_bh():
        while True:
            case = input("QUAN LY HOA DON: \n \
            Tao hang hoa :'THH' \n \
            Xem hang hoa:'XHH' \n \
            Tao loai hang hoa:'TLHH' \n \
            Xem loai hang hoa:'XLHH' \n \
            Tao hoa don:'C' \n \
            Xem thong tin hoa don:'R' \n \
            In danh sach hoa don:'L' \n \
            Tinh tong doanh thu :'T' \n \
            Tinh tong so luong hang hoa ban ra: 'a' \n \
            Thoat khoi chuong trinh:'E' \n ")

            if case == 'THH':
                basic.tao_hangHoa()

            elif case == 'XHH':
                basic.xem_hangHoa()

            elif case == 'TLHH':
                 basic.tao_loaiHangHoa()        

            elif case == 'XLHH':
                basic.xem_loaiHangHoa()

            elif case == 'C':
                basic.tao_hoaDon()
            elif case == 'R':
                sohoadon_canxem =  basic.view_hoaDon()
                with open('hoadon/' + sohoadon_canxem + '.json', 'r') as f:
                    json.load(f)
                basic.xem_hoa_don(sohoadon_canxem)
            elif case == 'L':
                for index in basic.ds_hoaDon:
                    basic.xem_hoa_don(index)
            elif case == 'T':
                basic.tong_doanh_thu()
            elif case =='a':
                ten_hh = input("Nhap ten sam pham can tinh so luong: ")
                basic.tong_hang_hoa(ten_hh)
            else:
                print("Thoat khoi chuong trinh")
                break

def main():
    while True:
            case = input("Moi ban chon chuc nang chinh cua chuong trinh: \n \
            Tao tai khoan nhan vien :'TNV' \n \
            Update tai khoan nhan vien:'UNV' \n \
            Xoa tai khoan nhan vien:'XNV' \n \
            Xem danh sach nhan vien:'XDSNV' \n \
            Xen danh sách khách hàng:'XDSKH' \n \
            Quan ly hoa don:'QLHD' \n \
            Thoat khoi chuong trinh:'E' \n ")

            if case == 'TNV':
                user.new_NhanVien()

            elif case == 'UNV':
                user.update_NhanVien()

            elif case == 'XNV':
                user.xoa_NhanVien()       

            elif case == 'XDSNV':
                user.read_NhanVien()

            elif case == 'XDSKH':
                user.read_KhachHang()

            elif case == 'QLHD':
                hoa_don_bh()
            else:
                print("Thoat khoi chuong trinh")
                break

main()


