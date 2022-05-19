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
                        print(item)
                    else:
                        swapped_dict.update({item: k})
            else:
                swapped_dict.update({k: k})
        else:
            print(False,str(v), "is not list")
        k_list.append(k)
        v_list.append(v)

    print(swapped_dict)
    print(len(swapped_dict.items()))
    print(swapped_dict.keys())


parser(images_categories)