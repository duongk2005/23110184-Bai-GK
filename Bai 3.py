def c_sang_f(c):
    return c * 9/5 + 32


def f_sang_c(f):
    return (f - 32) * 5/9


def usd_sang_vnd(usd, ty_gia):
    return usd * ty_gia


while True:
    print("\n===== MENU =====")
    print("1. chuyen C sang F")
    print("2. chuyen F sang C")
    print("3. chuyen USD sang VND")
    print("4. thoat")
    
    chon = input("chon mot chuc nang: ")
    
    if chon == "1":
        try:
            c = float(input("nhap do C: "))
            print("ket qua:", c_sang_f(c),"F")
        except:
            print("loi: yeu cau phai nhap so!")
    
    elif chon == "2":
        try:
            f = float(input("nhap do F: "))
            print("ket qua:", f_sang_c(f),"C")
        except:
            print("loi: yeu cau phai nhap so!")
    
    elif chon == "3":
        try:
            usd = float(input("nhap so USD: "))
            ty_gia = float(input("nhap ty gia: "))
            print("ket qua:", usd_sang_vnd(usd, ty_gia), "VND")
        except:
            print("loi: yeu phai nhap so!")
    
    elif chon == "4":
        break
    else:
        print("lua chon khong hop le!")