# Converts minutes to float format, i.e.: 7:30 => 7.5
def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    return hours + minutes / 60

def main():
    time = input("What time is it? ").strip()

    # converts hours from Int to String and minutes from Float to String
    # resultTime = str(int(hours) + float(convert(minutes)))
    resultTime = convert(time)

    # output check
    # print(resultTime)

    # checking time intervals
    if 7 <= resultTime <= 8:
        print("breakfast time")
    elif 12 <= resultTime <= 13:
        print("lunch time")
    elif 18 <= resultTime <= 19:
        print("dinner time")

if __name__ == "__main__":
    main()
