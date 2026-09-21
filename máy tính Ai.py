import time 

print("chào bn tôi là máy tính AI")
time.sleep(1.0)
print("tôi cs thể làm các bài toàn như + - * :")
time.sleep(1.0)
while True:  
    print("chương trình đang chạy")
    time.sleep(1.0)
    tra_loi = input("bạn cs muốn chạy máy tính AI (tiếp tục) ko ( muốn thì ghi yes nếu ko muốn thì ghi no):  ")
    
    if tra_loi == "no":
        print("tắt máy tính Ai thành công")
        break  
        
    if tra_loi == "yes":
        print("máy tính đã khởi động xong")
        so_thu_nhat = float(input("Nhập số thứ nhất: "))
        phep_tinh = input("nhập phép tính: ")
        so_thu_hai = float(input("Nhập số thứ hai: "))
        if (phep_tinh == "+"):
            print(so_thu_nhat + so_thu_hai)
        elif (phep_tinh =="-"):
            print(so_thu_nhat - so_thu_hai)
        elif (phep_tinh =="*"):
            print(so_thu_nhat * so_thu_hai)
        elif (phep_tinh =="/"):
            print(so_thu_nhat / so_thu_hai)
        else:
            print("bạn nhập sai cú pháp")
            
    
   
    
    

        
