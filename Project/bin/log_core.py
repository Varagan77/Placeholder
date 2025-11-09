#basic script for sms template

#vars
name = ""
R = ""
service_date = ""
ref = ""

#changes when variables are added
message = f"""
Dear {name},

Notice! R{R}, Service date: {service_date}, CHS Medical Services, Room 101, MediClinic 
BFN, FNB 62435637113, Branch 230134, Ref {ref}, Tel 051 5227146, bkotze@chs.bfnmcc.co.za

Regards,
Barbara Kotze
"""


print(message)


