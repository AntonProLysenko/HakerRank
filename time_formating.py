def timeConversion(s):
    # stripped= s.strip()
    # arr_s = stripped.split(":")
    # is_am = "AM" in arr_s[len(arr_s)-1]
    # is_pm = "PM" in arr_s[len(arr_s)-1]

    # testing = s[8:10]
    # print(testing)

    # if is_pm:
    #     if arr_s[0]=="12":
    #         milit_hours = int(arr_s[0])
    #     else:
    #         milit_hours = int(arr_s[0])+12
    # else:
    #     if arr_s[0]=="12":
    #         milit_hours = "00"
    #     else:  
    #         milit_hours = int(arr_s[0])

    # secs=arr_s[len(arr_s)-1]
    # print(secs[:2])
    # # milit_hours = str(milit_hours)
    
    # return (f"{milit_hours}:{arr_s[1]}:{secs[:2]}")
    hours = s[0:2]
    minutes = s[3:5]
    secs = s[6:8]
    am_pm = s[8:10]

    if am_pm == "PM":
        if hours == "12":
            milit = hours
        else:
            milit = str(int(hours)+12)
    else:
        if hours =="12":
            milit = "00"
        else:
            milit = hours
    
    return(f"{milit}:{minutes}:{secs}")
        

print(timeConversion("06:59:59AM"))