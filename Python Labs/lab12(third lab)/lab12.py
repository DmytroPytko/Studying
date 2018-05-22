import re


def calc_number_of_php():
    file = open('logs')
    pattern = "23/Mar/2009:((02:00:0[0-3]|0[3-4]:[0-5][0-9])|(05:[0-5][0-5]:0[0-2])).*GET.*\.php.*3[0-9][0-9]\s"
    total_number_of_php = 0
    # current_size = 0
    for line in file:
        match = re.search(pattern, line)
        if match:
            print(match.group())
            total_number_of_php += 1
    print("The total number of .php files that was returned is: " + str(total_number_of_php))
    file.close()


if __name__ == "__main__":
    calc_number_of_php()
