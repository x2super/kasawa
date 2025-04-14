# Kasawa Modules
- สวัสดีครับ โมดูลนี้เป็นโมดูลส่วนตัวที่เปิดให้คนทั้วไปสามารถใช้งานได้เลย
  - ซึ่งเราสามารถลงโมดูล ได้สองแบบเลยแบบแรกจะใช้ git ในการลง
  -  สามารถพิมพ์ชื่อลงโมดูลได้ปกติ ซึ่งตอนนี้ยังใช้ได้แบบแรก

> ใครที่ต้องการลงขั้นตอนแรกให้ทำการลง git กันก่อน
```
# windows os
https://git-scm.com/downloads

# linux os
sudo apt install git -y

# mac os
brew install git
````


> Example Install Module
 - อันนี้จะเป็นคำสั่งสำหรับลงโมดูลของเรานะครับผม
```
# git install [work]
pip install git+https://github.com/x2super/kasawa.git

#pypi install [not work]
pip install kasawa
```

> Example coding 

- Wallet topup
  - รับเงินซองอั่งเปาของคุณแบบ อัติโนมัติ ใช้งานง่ายไม่ย่งยาก
```py 
from  kasawa  import  topup
# สามารถใส่ทั้งลิ้งค์อั่งเปาได้เลย มีระบบเช็คอัติโนมัติ
# ไม่ต้องกลัวว่าผู้ใช้จะส่งลิ้งค์ที่ผิดพลาด
money  =  topup("phone(เบอร์มือถือ)", "vouch(ลิ้งค์ซองอั่งเปา)")
print(money.json())
```
🟢 Successfully	
```json
{
  "status": true,
  "message": {
    "voucher": {
      "voucher_id": "54720433906870018",
      "amount_baht": "10.00",
      "redeemed_amount_baht": "10.00",
      "member": 1,
      "status": "active",
      "link": "xxxxxxxxxxxxxxxx",
      "detail": "",
      "expire_date": 1739702702858,
      "type": "F",
      "redeemed": 1,
      "available": 0
    },
    "owner_profile": {
      "full_name": "xxxx ***"
    },
    "redeemer_profile": {
      "mobile_number": "0000000000"
    },
    "my_ticket": {
      "mobile": "0000000000",
      "update_date": 1739616394250,
      "amount_baht": "10.00",
      "full_name": "xxxx ***",
      "profile_pic": null
    },
    "tickets": [
      {
        "mobile": "000000-000",
        "update_date": 1739616394250,
        "amount_baht": "10.00",
        "full_name": "xxxx ***",
        "profile_pic": "https://profile-images-cdn.truemoney.com/tmn.10043578308_0d14ec5919fa3bebc42dd754afeb5.jpg"
      }
    ]
  }
}
```
🔴 Failed
```py
# ลิ้งค์ซองอั่งเปาผิด
{
	'status': False, 
	'message': 'INVALID_VOUCHER'
}

# เบอร์มือถือผิด
{
	'status': False, 
	'message': 'INVALID_PHONE'
}
# หรืออีกอย่างนึงถ้าหาก รันแล้ว รับซองช้ามาก ก็คือใช้ไม่ได้เหมือนกัน
```
