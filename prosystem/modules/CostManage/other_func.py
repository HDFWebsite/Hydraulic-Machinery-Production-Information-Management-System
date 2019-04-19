from datetime import datetime
def get_boms_list(boms_list,year):
    boms_dict_list = []
    total_month01, total_month02, total_month03, total_month04 = 0, 0, 0, 0
    total_month05, total_month06, total_month07, total_month08 = 0, 0, 0, 0
    total_month09, total_month10, total_month11, total_month12 = 0, 0, 0, 0
    for data in boms_list:
        boms_dict_list.append(data.to_dict())
        total_month01+=data.month01
        total_month02+=data.month02
        total_month03+=data.month03
        total_month04+=data.month04
        total_month05+=data.month05
        total_month06+=data.month06
        total_month07+=data.month07
        total_month08+=data.month08
        total_month09+=data.month09
        total_month10+=data.month10
        total_month11+=data.month11
        total_month12+=data.month12
    data = {
        "year1": datetime.now().strftime("%Y"),
        "year2": int(datetime.now().strftime("%Y"))-1,
        "year3": int(datetime.now().strftime("%Y"))-2,
        "year4": int(datetime.now().strftime("%Y"))-3,
        "query_year": int(year),
        'boms_dict_list': boms_dict_list,
        "total_month01":total_month01,
        "total_month02":total_month02,
        "total_month03":total_month03,
        "total_month04":total_month04,
        "total_month05":total_month05,
        "total_month06":total_month06,
        "total_month07":total_month07,
        "total_month08":total_month08,
        "total_month09":total_month09,
        "total_month10":total_month10,
        "total_month11":total_month11,
        "total_month12":total_month12,
    }
    return data

def getAllneedModel1TP(current_month,plan,plans):
    if current_month == "month01":
        plan.month01 = plans.total_price
    elif current_month == "month02":
        plan.month02 = plans.total_price
    elif current_month == "month03":
        plan.month03 = plans.total_price
    elif current_month == "month04":
        plan.month04 = plans.total_price
    elif current_month == "month05":
        plan.month05 = plans.total_price
    elif current_month == "month06":
        plan.month06 = plans.total_price
    elif current_month == "month07":
        plan.month07 = plans.total_price
    elif current_month == "month08":
        plan.month08 = plans.total_price
    elif current_month == "month09":
        plan.month09 = plans.total_price
    elif current_month == "month10":
        plan.month10 = plans.total_price
    elif current_month == "month11":
        plan.month11 = plans.total_price
    elif current_month == "month12":
        plan.month12 = plans.total_price
    return plan


def getAllneedModel2TP(current_month, plan, plans):
    if current_month == "month01":
        plan.month01 += plans.total_price
    elif current_month == "month02":
        plan.month02 += plans.total_price
    elif current_month == "month03":
        plan.month03 += plans.total_price
    elif current_month == "month04":
        plan.month04 += plans.total_price
    elif current_month == "month05":
        plan.month05 += plans.total_price
    elif current_month == "month06":
        plan.month06 += plans.total_price
    elif current_month == "month07":
        plan.month07 += plans.total_price
    elif current_month == "month08":
        plan.month08 += plans.total_price
    elif current_month == "month09":
        plan.month09 += plans.total_price
    elif current_month == "month10":
        plan.month10 += plans.total_price
    elif current_month == "month11":
        plan.month11 += plans.total_price
    elif current_month == "month12":
        plan.month12 += plans.total_price
    return plan

def getAllneedModel1TC(current_month,plan,plans):
    if current_month == "month01":
        plan.month01 = plans.total_cost
    elif current_month == "month02":
        plan.month02 = plans.total_cost
    elif current_month == "month03":
        plan.month03 = plans.total_cost
    elif current_month == "month04":
        plan.month04 = plans.total_cost
    elif current_month == "month05":
        plan.month05 = plans.total_cost
    elif current_month == "month06":
        plan.month06 = plans.total_cost
    elif current_month == "month07":
        plan.month07 = plans.total_cost
    elif current_month == "month08":
        plan.month08 = plans.total_cost
    elif current_month == "month09":
        plan.month09 = plans.total_cost
    elif current_month == "month10":
        plan.month10 = plans.total_cost
    elif current_month == "month11":
        plan.month11 = plans.total_cost
    elif current_month == "month12":
        plan.month12 = plans.total_cost
    return plan


def getAllneedModel2TC(current_month, plan, plans):
    if current_month == "month01":
        plan.month01 += plans.total_cost
    elif current_month == "month02":
        plan.month02 += plans.total_cost
    elif current_month == "month03":
        plan.month03 += plans.total_cost
    elif current_month == "month04":
        plan.month04 += plans.total_cost
    elif current_month == "month05":
        plan.month05 += plans.total_cost
    elif current_month == "month06":
        plan.month06 += plans.total_cost
    elif current_month == "month07":
        plan.month07 += plans.total_cost
    elif current_month == "month08":
        plan.month08 += plans.total_cost
    elif current_month == "month09":
        plan.month09 += plans.total_cost
    elif current_month == "month10":
        plan.month10 += plans.total_cost
    elif current_month == "month11":
        plan.month11 += plans.total_cost
    elif current_month == "month12":
        plan.month12 += plans.total_cost
    return plan
