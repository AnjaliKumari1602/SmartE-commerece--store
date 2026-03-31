import pandas as pd
from collections import Counter

Categories={'Cosmetics':['Lakme','M.A.C','Sugar Cosmetics',"L'Oreal Paris",'Colorbar'],
            'Electronics':['Samsung','Sony','Huawei','Panasonic','LG'],
            'Clothing':['Louis Vuitton','H&M','Zara','Chanel','Nike']}

Products={
    101: ['Absolute Foundation','Lakme',850,15],
    102: ['Enrich Matte Lipstick','Lakme',295,24],
    103: ['Eyeconic Kajal','Lakme',190,10],
    104: ['Sun Expert SPF 50','Lakme',450,5],
    105: ['Prep + Prime Fix+','M.A.C',2100,18],
    106: ['Studio Fix Fluid','M.A.C',3300,12],
    107: ['Ruby Woo Lipstick','M.A.C',1950,8],
    108: ['Smudge Me Not Liquid Lipstick','Sugar Cosmetics',499,20],
    109: ['Contour De Force Face Palette','Sugar Cosmetics',799,14],
    110: ['Kohl Of Honour Intense Kajal','Sugar Cosmetics',249,25],
    111: ['Revitalift Hyaluronic Acid Serum',"L'Oreal Paris",999,11],
    112: ['Excellence Creme Hair Color',"L'Oreal Paris",650,22],
    113: ['Lash Paradise Mascara',"L'Oreal Paris",849,16],
    114: ['Velvet Matte Lipstick','Colorbar',350,19],
    115: ['Perfect Match Primer','Colorbar',899,7],
    116: ['Intenso Eyeliner','Colorbar',550,13],
    
    117: ['Galaxy S24 Ultra','Samsung',129999,5],
    118: ['55" Neo QLED 4K TV','Samsung',85000,8],
    119: ['Galaxy Watch 6','Samsung', 29999,15],
    120: ['253L Double Door Refrigerator','Samsung',26500,10],
    121: ['WH-1000XM5 Headphones','Sony',29990,12],
    122: ['PlayStation 5 Console','Sony',54990,4],
    123: ['Bravia 65" OLED TV','Sony',145000,3],
    124: ['Alpha a7 IV Camera','Sony',215000,2],
    125: ['P60 Pro Smartphone','Huawei',85000,6],
    126: ['MateBook X Pro','Huawei',120000,4],
    127: ['Watch GT 4','Huawei',18000,14],
    128: ['1.5 Ton 5 Star Split AC','Panasonic',42000,9],
    129: ['27L Convection Microwave','Panasonic',12500,11],
    130: ['Lumix S5 II','Panasonic',165000,5],
    131: ['8kg Front Load Washing Machine','LG',35000,7],
    132: ['27" 4K UHD Monitor','LG',28000,16],
    133: ['OLED C3 55" TV','LG',135000,4],
    
    134: ['Neverfull MM Tote Bag','Louis Vuitton',155000,3],
    135: ['Multiple Wallet','Louis Vuitton',45000,6],
    136: ['Initiales 40mm Reversible Belt','Louis Vuitton',55000,4],
    137: ['Basic Cotton T-Shirt','H&M',499,25],
    138: ['Slim Fit Denim Jeans','H&M',1999,21],
    139: ['Relaxed Fit Hoodie','H&M',2299,18],
    140: ['Faux Leather Biker Jacket','Zara',4990,10],
    141: ['Pleated Wide-Leg Trousers','Zara',2990,15],
    142: ['Printed Midi Dress','Zara',3590,12],
    143: ['Men’s Bomber Jacket','Zara',5990,8],
    144: ['No. 5 Eau de Parfum 100ml','Chanel',14500,7],
    145: ['Classic Flap Bag','Chanel',850000,2],
    146: ['Cat Eye Sunglasses','Chanel',35000,5],
    147: ['Air Force 1 Sneakers','Nike',7495,14],
    148: ['Dri-FIT Training T-Shirt','Nike',1595,23],
    149: ['Pro Women’s Leggings','Nike',2495,20],
    150: ['Air Max 270 Shoes','Nike',12995,9]
}

customers={}
Purhistory = {}

def custdetails():
    try:
        Cho=int(input("New Customer:-\n1)Yes\n2)No\n"))
        if Cho==1:
            while True:
                try:
                    custid=100+len(customers)+1
                    name=input("Enter your name:-")
                    age=int(input("Enter your age:-"))
                    cont=int(input("Enter you contact:-"))
                    add=input("Enter your address")
                    lst=[name,age,cont,add]
                    customers.setdefault(custid,lst)
                    break
                except ValueError:
                    print("Invalid Input.Retry...\n")
            return custid
        
        elif Cho==2:
            custid=int(input("Enter your customer id"))
            for i in customers:
                if i==custid:
                    print("Details matched successfully")
                    return custid
                else:
                    print("Details not matched")
    except ValueError:
        print("Invalid Input.\n")

def history(custid,details,field2):
    if field2=='purchase':
        for i in Purhistory:
            if i==custid:
                Purhistory[i].append(details)
        else:
            Purhistory.setdefault(custid,[details])

def purchase(field2,custid,buy):
    amt=0
    for i in Products:
        found=i in buy
        if found==True:
            amt+=Products[i][2]
            Products[i][3]-=1
            details=[Products[i][0],Products[i][1],field2,Products[i][2]]
            history(custid,details,'purchase')
    print("Total amount=",amt)

def Display(field2,custid):
    print("\nProduct id [Product name,Brand,Price,Stock]")
    for i in Products:
        found=Products[i][1] in Categories[field2]
        if found==True:
            print(i,Products[i])
    buy=[]
    try:
        ask=int(input("\nDo you want to buy:-\n1)Yes\n2)No\n"))
        if ask==1:
            try:
                while True:
                    pur=int(input("\nEnter product id to purchase"))
                    if pur in Products:
                        buy.append(pur)
                        cond=int(input("\nDo you want to change?\n1)Yes\n2)No\n"))
                        if cond==1:
                            cho3=int(input("\nDo you want to:-\n1)Add\n2)Remove\n"))
                            if cho3==1:
                                continue
                            elif cho3==2:
                                rem=int(input("\nEnter product id to remove:-/n"))
                                buy.remove(rem)
                            else:
                                print("Invalid input")
                        if cond==2:
                            break
                    else:
                        print("Inavalid product id")
                purchase(field2,custid,buy)
            except ValueError:
                print("Invalid Input.\n")
            print("Your order list:-",buy)
        elif ask==2:
            pass
        else:
            print("Invalid Choice\n")
    except ValueError:
                print("Invalid Input.\n")

def Brand(field2,custid):
    for i in Categories:
        if i==field2:
            print("\nAvailable brands are:-")
            for j in Categories[i]:
                print(j)
    try:
        while True:
            br = input("\nEnter your preferred brand:- ")
            print()
            brand_found = False 
            for i in Products:
                if br.lower() == Products[i][1].lower():
                    print(i, Products[i])
                    brand_found = True
            if not brand_found:
                print("Wrong brand entered. Please try again.")
            else:
                break
        
        buy=[]
        while True:
            pur=int(input("\nEnter product id to purchase"))
            if pur in Products:
                buy.append(pur)
                cond=int(input("\nDo you change?\n1)Yes\n2)No"))
                if cond==1:
                    while True:
                        cho3=int(input("\nDo you want to:-\n1)Add\n2)Remove"))
                        if cho3==1:
                            break
                        elif cho3==2:
                            rem=int(input("\nEnter product id to remove"))
                            buy.remove(rem)
                            break
                        else:
                            print("Invalid input\n")
                elif cond==2:
                    break
            else:
                print("Invalid product id")
        print("\nYour order list:-",buy)
        purchase(field2,custid,buy)
    except ValueError:
        print("Invalid Input.\n")
            

def viewhistory(custid):
    found=custid in Purhistory
    if found==True:
        for i in Purhistory[custid]:
            print(i)
    else:
        print("No purchase history exists")
    airecommend(custid)

def airecommend(custid):
    print("\nAI SHOPPING ASSISTANT INSIGHTS")
    brinterest=[]
    if custid in Purhistory:
        for record in Purhistory[custid]:
            brinterest.append(record[1])

    else:
        print("\nAI INSIGHT: You are a new customer! Since you have no history yet")

    brmost=Counter(brinterest).most_common(1)[0][0]
    print(f"\nAI INSIGHT: I noticed you are highly interested in '{brmost}'.")
    print("Here are some more products you might like:\n")
    for i in Products:
        if Products[i][1].lower()==brmost.lower():
            print(i,Products[i])



print('='*80)
print('\t\t\tWELCOME TO THE SMART E-COMMERCE STORE')
cid=custdetails()
print('='*80)

while True:
    try:
        print("\n____________MAIN MENU____________")
        cho1=int(input("Select a category:-\n1)Cosmetics\n2)Electronics\n3)Clothing\n4)View purchase history\n5)Exit\n"))
        if cho1==1:
            cho2=int(input("\nWhat do you want to see:-\n1)All cosmetic products\n2)Specific brand\n"))
            if cho2==1:
                Display('Cosmetics',cid)
            elif cho2==2:
                Brand('Cosmetics',cid)
            else:
                print("Invalid Choice")
        elif cho1==2:
            cho2=int(input("\nDo you want to see:-\n1)All cosmetic products\n2)Specific brand\n"))
            if cho2==1:
                Display('Electronics',cid)
            elif cho2==2:
                Brand('Electronics',cid)
            else:
                print("Invalid Choice")
        elif cho1==3:
            cho2=int(input("\nDo you want to see:-\n1)All cosmetic products\n2)Specific brand\n"))
            if cho2==1:
                Display('Clothing',cid)
            elif cho2==2:
                Brand('Clothing',cid)
            else:
                print("Invalid Choice")
        elif cho1==4:
            viewhistory(cid)
        elif cho1==5:
            print("Quitting...\n")
            break
        else:
            print("Invalid Choice.\n")
    except ValueError:
        print("Invalid Input.Please enter numbers only.\n")
