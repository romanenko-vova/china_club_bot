FormData(
    #     [
    #         ("TransactionId", "3541977847"),
    #         ("Amount", "1490.00"),
    #         ("Currency", "RUB"),
    #         ("PaymentAmount", "1490.00"),
    #         ("PaymentCurrency", "RUB"),
    #         ("OperationType", "Payment"),
    #         ("InvoiceId", "efef06ce-ec69-471d-9235-f06415a562eb"),
    #         ("AccountId", "1"),
    #         ("SubscriptionId", "sc_d7dd2bee6a1ceb1bf2b83aa17eab6"),
    #         ("Name", ""),
    #         ("Email", "test@test.ru"),
    #         ("DateTime", "2026-05-28 12:55:43"),
    #         ("IpAddress", "1.52.35.139"),
    #         ("IpCountry", "VN"),
    #         ("IpCity", "Хошимин"),
    #         ("IpRegion", "Хошимин"),
    #         ("IpDistrict", "Хошимин"),
    #         ("IpLatitude", "10.82302"),
    #         ("IpLongitude", "106.62965"),
    #         ("CardId", "656861528d5f00f7a54bee28"),
    #         ("CardFirstSix", "424242"),
    #         ("CardLastFour", "4242"),
    #         ("CardType", "Visa"),
    #         ("CardExpDate", "01/30"),
    #         ("Issuer", "TINKOFF"),
    #         ("IssuerBankCountry", "RU"),
    #         ("Description", "Оплата подписки на 1 месяц"),
    #         ("AuthCode", "A1B2C3"),
    #         ("Token", "tk_32fd70c672118d25112b28f02259a"),
    #         ("TestMode", "1"),
    #         ("Status", "Completed"),
    #         ("GatewayName", "Test"),
    #         (
    #             "Data",
    #             '{\n  "CloudPayments": {\n    "recurrent": {\n      "interval": "Month",\n      "period": 1\n    }\n  }\n}',
    #         ),
    #         ("TotalFee", "0.00"),
    #         ("CardProduct", ""),
    #         ("PaymentMethod", ""),
    #         ("InstallmentTerm", ""),
    #         ("InstallmentMonthlyPayment", ""),
    #         ("CustomFields", ""),
    #         ("VatAboveTotalFee", ""),
    #         ("ProcessorAndPartnerFee", ""),
    #         ("VatWithinProcessorFee", ""),
    #     ]
    # )


Request: #101 V2 POST https://pythonfication.romanenko-coding.ru/cp/pay
TransactionId=3503689911&Amount=1490.00&Currency=RUB&PaymentAmount=1490.00&PaymentCurrency=RUB&OperationType=Payment&AccountId=tochilovalarisa@gmail.com&SubscriptionId=sc_a2fb47fd5fe1eaf4406478274f48b&Name=&Email=tochilovalarisa@gmail.com&DateTime=2026-05-10 15:59:23&IpAddress=172.18.10.73&IpCountry=&IpCity=&IpRegion=&IpDistrict=&IpLatitude=&IpLongitude=&CardId=64d7edf8d7421ff0c13393c4&CardFirstSix=546912&CardLastFour=4914&CardType=MasterCard&CardExpDate=12/22&Issuer=Sberbank&IssuerBankCountry=RU&Description=Оплата подписки&AuthCode=625506&Token=tk_5aa37b9829b89b38ad3fc00f24f5a&TestMode=0&Status=Completed&GatewayName=Tbank&TotalFee=70.89&CardProduct=SAP&PaymentMethod=&Rrn=613015333510&InstallmentTerm=&InstallmentMonthlyPayment=&CustomFields=&VatAboveTotalFee=12.78&ProcessorAndPartnerFee=&VatWithinProcessorFee=
Response: {"code":10,"message":"Missing required fields"}