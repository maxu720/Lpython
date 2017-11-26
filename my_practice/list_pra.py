'''
从键盘中输入5个学生的名字，存储到列表中，然后打印出每个学生名字中的第二个字符

'''


def get_students():
    student_list = []
    num = 0

    num = input('请输入要输入学生信息个数：')
    num = int(num)

    for i in range(num):
        stu = input("请输入第{}学生姓名：".format(i + 1))
        student_list.append(stu)
    print(student_list)
    return student_list

def get_varify_students():
    student_list = []
    num = 0

    num = input('请输入要输入学生信息个数：')
    num = int(num)

    while len(student_list) < num:
        stu = input("请输入第{}学生姓名：".format(len(student_list) + 1))
        if len(stu) < 2:
            print("请重新输入")
            continue

        student_list.append(stu)
    print(student_list)
    return student_list

def print_info(student_list):
    for i in student_list:
        a = i[1]
        print(a)

if __name__ == '__main__':
    student_list = get_varify_students()
    print_info(student_list)


