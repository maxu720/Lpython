# 定义函数findall，实现对字符串find方法的进一步封装，要求返回符合要求的所有位置的起始下标，如字符串"helloworldhellopythonhelloc++hellojava"，需要找出里面所有的
# "hello"的位置，最后将返回一个元组(0, 10, 21, 29)，即将h的下标全部返回出来，而find方法只能返回第一个
def findall(string, s):
    ret = []
        return tuple(ret)
    while True:
        index = string.find(s)
        # 如果能找到对应的子字符串
        if index != -1:
            if len(ret)!=0:
                # 如果之前已经找到对应字符的索引，再次找到时，需要拿出上次的索引值加上本次索引值再加一，得到在整个字符串中的索引位置
                ret.append(ret[-1]+index+1)
            else:
                # 第一次找到对应索引，直接存储位置
                ret.append(index)
            # 每次找到对应位置后，截取剩余部分，再进行查找
            string = string[index+len(s)::]
        else:
            break
    return tuple(ret)
a = findall("helloworldhellopythonhelloc++hellojava","h")
print(a)