from dict_key_categories import images_categories
import time
# result = dict((v,k) for k,v in images_categories.items())
# print(result)

def parser(dict_to_swap):
    k_list = []
    v_list = []
    swapped_dict = {}
    stupid = []
    for k,v in dict_to_swap.items():
        if isinstance(v, list): #sprawdzam czy value jest lista
            if len(v)>0:
                for item in v:
                    stupid = list(swapped_dict.keys())
                    if stupid.count(item):
                        new_val = swapped_dict[item]
                        if isinstance(new_val, list):
                            val_to_add = [k]
                            new_val.extend(val_to_add)
                            swapped_dict.update({item:new_val})
                        else:
                            new_val = [new_val]
                            val_to_add = [k]
                            new_val.extend(val_to_add)
                            swapped_dict.update({item:new_val})
                        #print(item)
                    else:
                        swapped_dict.update({item: k})
            else:
                swapped_dict.update({k: k})
        else:
            print(False,str(v), "is not list")
        k_list.append(k)
        v_list.append(v)

    # print("paste to : mapped_tags",swapped_dict)
    # print(len(swapped_dict.items()))
    # print("paste to categories",swapped_dict.values())
    # print("paste to: k_mapped_tags",swapped_dict.keys())


    s1 = str('"""'+time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime())+'"""'+"\n\n")
    s2 = str("mapped_tags = "+str(swapped_dict)+"\n")
    s3 = str("categories = " + str(dict_to_swap.keys())[10:-1]+"\n")
    s4 = str("k_mapped_tags = " + str(swapped_dict.keys())[10:-1]+"\n")
    s5 = str('\n\n'+'"""' +"File generated after parser function in dict_parser.py "+ '"""' + "\n")

    file = open("dict_key_tags.py", "w",encoding='UTF-8')
    file.write(s1)
    file.write(s2)
    file.write(s3)
    file.write(s4)
    file.write(s5)
    file.close()

def parser_run():
    parser(images_categories)

parser_run()