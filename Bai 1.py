def nhap_danh_sach():
    danh_sach = []
    
    while True:
        ten = input("Nhap ten mon hang (Nhap x de dung): ")
        if ten.lower() == 'x':
            break
        
        gia = float(input("Nhap gia tien: "))
        danh_sach.append([ten, gia])
    return danh_sach



def tinh_tong(danh_sach):
    tong = 0
    for item in danh_sach:
        tong += item[1]
    return tong



def tim_max(danh_sach):
    max_item = danh_sach[0]
    for item in danh_sach:
        if item[1] > max_item[1]:
            max_item = item
    return max_item



def ghi_file(danh_sach, tong, max_item):
    f = open("ketqua.txt", "w", encoding="utf-8")
    f.write("Danh sach mon hang:\n")
    for item in danh_sach:
        f.write(item[0] + " - " + str(item[1]) + " VND\n")
    f.write("\nTong tien: " + str(tong) + " VND\n")
    f.write("Mon dat nhat: " + max_item[0] + " - " + str(max_item[1]) + " VND\n")
    f.close()


danh_sach = nhap_danh_sach()

if len(danh_sach) == 0:
    print("Danh sach rong!")
else:
    tong = tinh_tong(danh_sach)
    max_item = tim_max(danh_sach)
    ghi_file(danh_sach, tong, max_item)
    print("Da ghi vao file ketqua.txt")