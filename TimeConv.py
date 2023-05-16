def main():
    time = input("Enter a time: ")
    if len(time) < 4:
        print("Invalid time")
        return
    hr = int(time[0:2])
    mi = int(time[2:4])
    ampm = "AM"

    if mi == 60:
        hr = hr + 1
        mi = 0
    if hr == 12:
        ampm = "PM"
    if hr == 0:
        hr = 12
        ampm = "AM"
    if hr == 24:
        ampm = "AM"
    if hr > 24 or mi > 60:
        print("Invalid time")
        return
    if hr > 12:
        hr = hr - 12
        ampm = "PM"
    if mi < 10:
        mi = f"0{mi}"
    print(f"{hr}:{mi} {ampm}")
    
while True:
    main()

