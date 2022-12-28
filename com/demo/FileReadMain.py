

file_loc = "C:\\surender\\hadoop_course\\4_inputfiles\\accounts_profile.txt"
trans_loc = "C:\\surender\\hadoop_course\\4_inputfiles\\atm_list.txt"
def read_file_as_list(loc):
    file = open(loc,"r")
    data_list = file.readlines()
    return data_list


def main():
    data_list = read_file_as_list(file_loc)
    print(data_list)
    for i in data_list:
        print(i)
    print(len(data_list))
    atm_list = read_file_as_list(trans_loc)
    print(atm_list)

if __name__ == "__main__":
    main()
    f = open("C:\\surender\\fastTrack.txt", "a+")
    f.write("\nWhat is your name ")
    f.write("\nHow are you  ")
    f.close()


