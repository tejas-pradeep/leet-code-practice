
def reorderLogFiles(self, logs: List[str]) -> List[str]:
    letter_logs = []
    digit_logs = []
    temp_arr = []
    for i in logs:
        temp_arr = i.split(" ")
        if temp_arr[1].isnumeric():
            digit_logs.append(i)
        else:
            letter_logs.append(i)
    letter_logs.sort(key=lambda n: (n.split()[1:],n.split()[0]))
    return letter_logs + digit_logs
    