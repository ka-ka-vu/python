# Nguyễn Viết Hoàng Vũ-BTLBTL

san_pham_list = []

def hien_thi_menu():
    print("\n--- QUẢN LÝ SẢN PHẨM ---")
    print("1. Thêm sản phẩm")
    print("2. Hiển thị danh sách sản phẩm")
    print("3. Tìm sản phẩm theo mã")
    print("4. Cập nhật sản phẩm")
    print("5. Xóa sản phẩm")
    print("6. Sắp xếp theo giá")
    print("7. Tìm sản phẩm có giá cao nhất")
    print("8. Tìm sản phẩm có giá thấp nhất")
    print("9. Tìm sản phẩm theo tên")
    print("10. Lọc sản phẩm")
    print("11. Lưu danh sách vào file")
    print("12. Đọc danh sách từ file")
    print("13. Hiển thị sản phẩm lưu trong file")
    print("14. Thống kê kho hàng")
    print("0. Thoát")


def them_san_pham():
    ma = input("Nhập mã sản phẩm: ").strip()
    if not ma:
        return print("Lỗi: Mã sản phẩm không được để trống.")
    if any(sp["ma"] == ma for sp in san_pham_list):
        return print("Lỗi: Mã sản phẩm đã tồn tại.")
    ten = input("Nhập tên sản phẩm: ").strip()
    if not ten:
        return print("Lỗi: Tên sản phẩm không được để trống.")
    try:
        so_luong = int(input("Nhập số lượng tồn: ").strip())
        if so_luong < 0:
            return print("Lỗi: Số lượng không được âm.")
    except ValueError:
        return print("Lỗi: Số lượng phải là số nguyên.")
    try:
        gia = float(input("Nhập giá bán hiện tại: ").strip())
        if gia < 0:
            return print("Lỗi: Giá không được âm.")
    except ValueError:
        return print("Lỗi: Giá phải là số thực.")
    san_pham_list.append({"ma": ma, "ten": ten, "so_luong": so_luong, "gia": gia})
    print("Thêm sản phẩm thành công.")


def hien_thi_danh_sach():
    if not san_pham_list:
        print("Danh sách sản phẩm trống.")
        return
    print("\n{:<10} {:<25} {:<15} {:<15}".format("Mã SP", "Tên sản phẩm", "Số lượng", "Giá bán (VND)"))
    for sp in san_pham_list:
        print("{:<10} {:<25} {:<15} {:<15,.0f}".format(sp["ma"], sp["ten"], sp["so_luong"], sp["gia"]))

def tim_san_pham():
    ma = input("Nhập mã sản phẩm cần tìm: ")
    for sp in san_pham_list:
        if sp["ma"] == ma:
            print("Tìm thấy: ", sp)
            return
    print("Không tìm thấy sản phẩm.")

def cap_nhat_san_pham():
    ma = input("Nhập mã sản phẩm cần cập nhật: ")
    for sp in san_pham_list:
        if sp["ma"] == ma:
            sp["so_luong"] = int(input("Nhập số lượng mới: "))
            sp["gia"] = float(input("Nhập giá bán mới: "))
            print("Đã cập nhật sản phẩm.")
            return
    print("Không tìm thấy sản phẩm.")

def xoa_san_pham():
    ma = input("Nhập mã sản phẩm cần xóa: ")
    for sp in san_pham_list:
        if sp["ma"] == ma:
            print(f"Đã tìm thấy sản phẩm: {sp['ten']} (SL: {sp['so_luong']}, Giá: {sp['gia']:,.0f} VND)")
            xac_nhan = input("Bạn có chắc muốn xóa sản phẩm này? (y/n): ").lower()
            if xac_nhan == "y":
                san_pham_list.remove(sp)
                print("Đã xóa sản phẩm.")
            else:
                print("Hủy xóa sản phẩm.")
            return
    print("Không tìm thấy sản phẩm.")

def sap_xep_theo_gia():
    if not san_pham_list:
        print("Danh sách sản phẩm trống.")
        return
    print("\n--- SẮP XẾP SẢN PHẨM THEO GIÁ ---")
    print("1. Giá tăng dần")
    print("2. Giá giảm dần")
    lua_chon = input("Chọn cách sắp xếp (1-2): ").strip()
    if lua_chon == "1":
        sorted_list = sorted(san_pham_list, key=lambda x: x["gia"])
        print("\n>>> Danh sách sản phẩm theo giá tăng dần:")
    elif lua_chon == "2":
        sorted_list = sorted(san_pham_list, key=lambda x: x["gia"], reverse=True)
        print("\n>>> Danh sách sản phẩm theo giá giảm dần:")
    else:
        print(" Lựa chọn không hợp lệ. Vui lòng chọn 1 hoặc 2.")
        return
    print("{:<10} {:<25} {:<15} {:<15}".format("Mã SP", "Tên sản phẩm", "Số lượng", "Giá bán (VND)"))
    for sp in sorted_list:
        print("{:<10} {:<25} {:<15} {:<15,.0f}".format(sp["ma"], sp["ten"], sp["so_luong"], sp["gia"]))

def san_pham_gia_cao_nhat():
    if not san_pham_list:
        print("Danh sách sản phẩm trống.")
        return
    sp_max = max(san_pham_list, key=lambda x: x["gia"])
    print("Sản phẩm có giá cao nhất:")
    print(f"Mã: {sp_max['ma']}, Tên: {sp_max['ten']}, Giá: {sp_max['gia']:,.0f} VND")

def san_pham_gia_thap_nhat():
    if not san_pham_list:
        print("Danh sách sản phẩm trống.")
        return
    sp_min = min(san_pham_list, key=lambda x: x["gia"])
    print("Sản phẩm có giá thấp nhất:")
    print(f"Mã: {sp_min['ma']}, Tên: {sp_min['ten']}, Giá: {sp_min['gia']:,.0f} VND")

def tim_kiem_theo_ten():
    ten_can_tim = input("Nhập tên sản phẩm cần tìm: ").strip().lower()  
    if not ten_can_tim:
        print(" Tên sản phẩm không được để trống.")
        return
    ket_qua = [sp for sp in san_pham_list if ten_can_tim in sp["ten"].lower()]
    if ket_qua:
        print(f"\n Tìm thấy {len(ket_qua)} sản phẩm phù hợp:")
        print("{:<10} {:<25} {:<15} {:<15}".format("Mã SP", "Tên sản phẩm", "Số lượng", "Giá bán (VND)"))
        for sp in ket_qua:
            print("{:<10} {:<25} {:<15} {:<15,.0f}".format(sp["ma"], sp["ten"], sp["so_luong"], sp["gia"]))
    else:
        print(" Không tìm thấy sản phẩm nào phù hợp.")

def loc_san_pham():
    print("\n--- LỌC SẢN PHẨM ---")
    print("1. Giá lớn hơn một mức")
    print("2. Số lượng thấp hơn một mức")
    lua_chon = input("Chọn tiêu chí lọc (1-2): ")
    if lua_chon == "1":
        muc_gia = float(input("Nhập mức giá tối thiểu: "))
        ket_qua = [sp for sp in san_pham_list if sp["gia"] > muc_gia]
    elif lua_chon == "2":
        muc_so_luong = int(input("Nhập số lượng tối đa: "))
        ket_qua = [sp for sp in san_pham_list if sp["so_luong"] < muc_so_luong]
    else:
        print("Lựa chọn không hợp lệ.")
        return
    if ket_qua:
        print("\nKết quả lọc:")
        print("{:<10} {:<25} {:<15} {:<15}".format("Mã SP", "Tên sản phẩm", "Số lượng", "Giá bán (VND)"))
        for sp in ket_qua:
            print("{:<10} {:<25} {:<15} {:<15,.0f}".format(sp["ma"], sp["ten"], sp["so_luong"], sp["gia"]))
    else:
        print("Không có sản phẩm nào phù hợp.")

import csv

def luu_vao_file():
    try:
        with open("san_pham.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["ma", "ten", "so_luong", "gia"])
            writer.writeheader()
            writer.writerows(san_pham_list)
        print(" Đã lưu danh sách sản phẩm vào file 'san_pham.csv'.")
    except Exception as e:
        print(f" Lỗi khi lưu file: {e}")

def doc_tu_file():
    try:
        with open("san_pham.csv", mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            san_pham_list.clear()
            for row in reader:
                try:
                    row["so_luong"] = int(row["so_luong"])
                    row["gia"] = float(row["gia"])
                    san_pham_list.append(row)
                except ValueError:
                    print(f" Bỏ qua dòng lỗi dữ liệu: {row}")
        print(f" Đã đọc {len(san_pham_list)} sản phẩm từ file.")
    except FileNotFoundError:
        print(" Chưa có file dữ liệu.")
    except Exception as e:
        print(f" Lỗi khi đọc file: {e}")

def hien_thi_file():
    try:
        with open("san_pham.csv", mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            danh_sach = list(reader)
            if not danh_sach:
                print("File không có dữ liệu.")
                return
            print("\n--- DANH SÁCH TRONG FILE ---")
            print("{:<10} {:<25} {:<15} {:<15}".format("Mã SP", "Tên sản phẩm", "Số lượng", "Giá bán (VND)"))
            for sp in danh_sach:
                try:
                    print("{:<10} {:<25} {:<15} {:<15,.0f}".format(
                        sp["ma"], sp["ten"], int(sp["so_luong"]), float(sp["gia"])
                    ))
                except:
                    print(f"Lỗi dữ liệu ở dòng: {sp}")
    except FileNotFoundError:
        print("Chưa có file dữ liệu.")
    except Exception as e:
        print(f"Lỗi khi đọc file: {e}")

def thong_ke_kho():
    if not san_pham_list:
        print("Danh sách sản phẩm trống.")
        return
    tong_so_luong = sum(sp["so_luong"] for sp in san_pham_list)
    tong_gia_tri = sum(sp["so_luong"] * sp["gia"] for sp in san_pham_list)
    print(f"Tổng số lượng sản phẩm: {tong_so_luong}")
    print(f"Tổng giá trị kho hàng: {tong_gia_tri:,.0f} VND")

# Vòng lặp chính
while True:
    hien_thi_menu()
    lua_chon = input("Chọn chức năng (0-13): ")
    
    if lua_chon == "1":
        them_san_pham()
    elif lua_chon == "2":
        hien_thi_danh_sach()
    elif lua_chon == "3":
        tim_san_pham()
    elif lua_chon == "4":
        cap_nhat_san_pham()
    elif lua_chon == "5":
        xoa_san_pham()
    elif lua_chon == "6":
        sap_xep_theo_gia()
    elif lua_chon == "7":
        san_pham_gia_cao_nhat()
    elif lua_chon == "8":
        san_pham_gia_thap_nhat()
    elif lua_chon == "9":
        tim_kiem_theo_ten()
    elif lua_chon == "10":
        loc_san_pham()
    elif lua_chon == "11":
        luu_vao_file()
    elif lua_chon == "12":
        doc_tu_file()
    elif lua_chon == "13":
        hien_thi_file()
    elif lua_chon == "14":
        thong_ke_kho()
    elif lua_chon == "0":
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")