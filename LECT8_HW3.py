def lst_gen(list_, iter_num=None):
    if iter_num is not None:
        n = 0
        while n < iter_num:
            for x in list_:
                yield x
            n += 1
    else:
        n = 0
        while True:
            for x in list_:
                yield x
            n += 1


list_ = ["a", "b"]
for y in lst_gen(list_, 2):
    print(y)


# list_ = ["a", "b"]
# for y in lst_gen(list_, None):
#     print(y)
