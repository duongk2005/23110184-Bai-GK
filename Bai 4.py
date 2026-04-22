import random

def file_ky_luc():
    try:
        f = open("kyluc.txt", "r")
        diem = int(f.read())
        f.close()
        return diem
    except:
        return None

def ghi_ky_luc(diem):
    f = open("kyluc.txt", "w")
    f.write(str(diem))
    f.close()

so_may = random.randint(1, 100)
so_lan_doan = 0
gioi_han = 7

kyluc = file_ky_luc()

print("tro choi doan so tu 1 den 100")
print("ban co 7 luot de doan")

if so_may % 2 == 0:
    print("goi y: so nay la so chan")
else:
    print("goi y: so nay la so le")

while so_lan_doan < gioi_han:
    try:
        doan = int(input("nhap so ban muon doan: "))
        so_lan_doan += 1

        if doan == so_may:
            print("chuc mung! ban da doan dung")
            print("so lan doan:", so_lan_doan)

            
            if kyluc is None or so_lan_doan < kyluc:
                print("ban da dat ky luc moi!")
                ghi_ky_luc(so_lan_doan)
            else:
                print("ky luc hien tai la:", kyluc)

            break

        elif doan < so_may:
            print("so can tim lon hon")
        else:
            print("so can tim nho hon")

    except:
        print("loi: ban phai nhap so!")

if so_lan_doan == gioi_han and doan != so_may:
    print("ban da thua!")
    print("so dung la:", so_may)