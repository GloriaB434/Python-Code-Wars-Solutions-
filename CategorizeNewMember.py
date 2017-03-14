def openOrSenior(data):
#Create empty list to store each member type as either "Senior" or "Open" based on the data
    member_types = []
#Data is of the form [age, handicap] if the age greater than or equal to 55 and the handicap is greater than 7 then they are a senior 
#Otherwise they are an open member
    for member in data:
        if member[0] >= 55 and 7 < member[1] <=27 :
#Store information in the member_types list 
            member_types.append("Senior")
        else:
            member_types.append ("Open")
    return member_types 
