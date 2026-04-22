def chuan_hoa(ten):
    ten = ten.strip()             
    tu = ten.split()               
    
    ket_qua = ""
    for t in tu:
        ket_qua += t.capitalize() + " "   
    
    return ket_qua.strip()


def lay_ten(ten):
    tu = ten.split()
    return tu[-1]



danh_sach = [" nguYen vaN a ", "tRAn tHi b", "  le   van   c  ", "PHAM thi d"]

danh_sach_chuan = []
for ten in danh_sach:
    danh_sach_chuan.append(chuan_hoa(ten))


danh_sach_chuan.sort(key=lay_ten)


print("Danh sach ket qua:")
for ten in danh_sach_chuan:
    print(ten)