"""
author rochanaph
October 23 2017"""

import w3,w4,w5, os
import math

def main():
    path = './text files'
    this_path = os.path.split(__file__)[0]
    path = os.path.join(this_path, path)

    # membaca sekaligus pre-processing semua artikel simpan ke dictionary
    articles = {}
    for item in os.listdir(path):
        if item.endswith(".txt"):
            with open(path + "/" + item, 'r') as file:
                articles[item] = w3.prepro_base(file.read())

    # representasi bow
    list_of_bow = [] # membuat list kosong
    for key, value in articles.items(): # iterasi pasangan key, value
        # print key, value
        list_token = value.split() # cari kata2 dengan men-split
        dic = w4.bow(list_token)   # membuat bow
        list_of_bow.append(dic)    # append bow ke list kosong yg di atas

    # membuat matrix
    matrix_akhir = w4.matrix(list_of_bow) # jalankan fungsi matrix ke list_of_bow

    # mencari jarak
    jarak = {}
    for key, vektor in zip(articles.keys(), matrix_akhir):
        jarak[key] = w5.euclidean(matrix_akhir[0], vektor) # simpan nama file sbg key, jarak sbg value
    return jarak

# print main()


def findSim(pathfile, pathcorpus):
    """
    mencari jarak/similarity antara suatu file dengan sekumpulan file/corpus dalam folder.
    :param pathfile: path tempat artikel yg dicari
    :param pathcorpus: path tempat folder
    :return: nama file, jarak terdekat
    """

    # this_path = os.path.split(__file__)[0]
    # pathcorpus = os.path.join(this_path, pathcorpus)
    # pathfile   = os.path.join(this_path, pathfile)
    # membaca sekaligus pre-processing semua artikel corpus simpan ke dictionary
    articles = {}
    for item in os.listdir(pathcorpus):
        if item.endswith(".txt"):
            with open(pathcorpus + "/" + item, 'r') as file:
                articles[item] = w3.prepro_base(file.read())

    # memasukan kata kunci kedalam dictionary dengan nama item/index(keyword_index)
    # kemudian dimasukan ke dictionary articles dengan value keyword yang dimasukan
    findname = 'index'
    articles[findname] = w3.prepro_base(pathfile)

    # tambahkan artikel yg dicari ke dictionary
    # findname = pathfile.split("/")[-1]
    # try:
    #     articles[findname]
    # except:
    #     with open(pathfile, 'r') as file:
    #         articles[findname] = w3.prepro_base(file.read())

    # representasi bow
    list_of_bow = []
    for key, value in articles.items():
        list_token = value.split()
        dic = w4.bow(list_token)
        list_of_bow.append(dic)

    # matrix
    matrix_akhir = w4.matrix(list_of_bow)

    # jarak
    # id_file = articles.keys().index(findname)    # index findname dalam articles.keys() = index dalam matrix
    id_keyword = articles.keys().index(findname)
    kategori = {}
    for item in os.listdir(pathcorpus):
        if item.endswith(".txt"):
            with open(pathcorpus + "/" + item, 'r') as file:
                kategori[item] = " "
    # kategori = {}
    jarak = {}
    for key, vektor in zip(articles.keys(), matrix_akhir):
        if key != findname:
            jarak[key] = w5.euclidean(matrix_akhir[id_keyword], vektor)
    # kategori
        if key[:2] == "ed":
            kategori[key]=("edukasi")
        elif key[:2] == "bk":
            kategori[key]=("ekonomi")
        elif key[:2] == "bl":
            kategori[key]=("bola")
        elif key[:2] == "en":
            kategori[key]=("entertaiment")
        elif key[:2] == "ot":
            kategori[key]=("otomotif")
        elif key[:2] == "lf":
            kategori[key]=("lifestyle")
        elif key[:2] == "tk":
            kategori[key]=("teknologi")
    # return w4.sortdic(jarak, descending=False, n=5)
    return w4.sortdic(jarak, kategori, descending=False, n=5)

# print findSim('./text files/ot_2.txt','./text files')

def findCosine(pathfile, pathcorpus):
    """
    mencari jarak/similarity antara suatu file dengan sekumpulan file/corpus dalam folder.
    :param pathfile: path tempat artikel yg dicari
    :param pathcorpus: path tempat folder
    :return: nama file, jarak terdekat
    """

    # this_path = os.path.split(__file__)[0]
    # pathcorpus = os.path.join(this_path, pathcorpus)
    # pathfile   = os.path.join(this_path, pathfile)
    # membaca sekaligus pre-processing semua artikel corpus simpan ke dictionary
    articles = {}
    for item in os.listdir(pathcorpus):
        if item.endswith(".txt"):
            with open(pathcorpus + "/" + item, 'r') as file:
                articles[item] = w3.prepro_base(file.read())

    # memasukan kata kunci kedalam dictionary dengan nama item/index(keyword_index)
    # kemudian dimasukan ke dictionary articles dengan value keyword yang dimasukan
    findname = 'index'
    articles[findname] = w3.prepro_base(pathfile)

    # tambahkan artikel yg dicari ke dictionary
    # findname = pathfile.split("/")[-1]
    # try:
    #     articles[findname]
    # except:
    #     with open(pathfile, 'r') as file:
    #         articles[findname] = w3.prepro_base(file.read())

    # representasi bow
    list_of_bow = []
    for key, value in articles.items():
        list_token = value.split()
        dic = w4.bow(list_token)
        list_of_bow.append(dic)

    # matrix
    matrix_akhir = w4.matrix(list_of_bow)

    # jarak
    # id_file = articles.keys().index(findname)    # index findname dalam articles.keys() = index dalam matrix
    id_keyword = articles.keys().index(findname)
    kategori = {}
    for item in os.listdir(pathcorpus):
        if item.endswith(".txt"):
            with open(pathcorpus + "/" + item, 'r') as file:
                kategori[item] = " "
    # kategori = {}
    jarak = {}
    for key, vektor in zip(articles.keys(), matrix_akhir):
        if key != findname:
            jarak[key] = w5.cosine(matrix_akhir[id_keyword], vektor)
    # kategori
        if key[:2] == "ed":
            kategori[key]=("edukasi")
        elif key[:2] == "bk":
            kategori[key]=("ekonomi")
        elif key[:2] == "bl":
            kategori[key]=("bola")
        elif key[:2] == "en":
            kategori[key]=("entertaiment")
        elif key[:2] == "ot":
            kategori[key]=("otomotif")
        elif key[:2] == "lf":
            kategori[key]=("lifestyle")
        elif key[:2] == "tk":
            kategori[key]=("teknologi")
    # return w4.sortdic(jarak, descending=False, n=5)
    return w4.sortdic(jarak, kategori, descending=False, n=5)

def findManhattan_distance(pathfile, pathcorpus):
    """
    mencari jarak/similarity antara suatu file dengan sekumpulan file/corpus dalam folder.
    :param pathfile: path tempat artikel yg dicari
    :param pathcorpus: path tempat folder
    :return: nama file, jarak terdekat
    """

    # this_path = os.path.split(__file__)[0]
    # pathcorpus = os.path.join(this_path, pathcorpus)
    # pathfile   = os.path.join(this_path, pathfile)
    # membaca sekaligus pre-processing semua artikel corpus simpan ke dictionary
    articles = {}
    for item in os.listdir(pathcorpus):
        if item.endswith(".txt"):
            with open(pathcorpus + "/" + item, 'r') as file:
                articles[item] = w3.prepro_base(file.read())

    # memasukan kata kunci kedalam dictionary dengan nama item/index(keyword_index)
    # kemudian dimasukan ke dictionary articles dengan value keyword yang dimasukan
    findname = 'index'
    articles[findname] = w3.prepro_base(pathfile)

    # tambahkan artikel yg dicari ke dictionary
    # findname = pathfile.split("/")[-1]
    # try:
    #     articles[findname]
    # except:
    #     with open(pathfile, 'r') as file:
    #         articles[findname] = w3.prepro_base(file.read())

    # representasi bow
    list_of_bow = []
    for key, value in articles.items():
        list_token = value.split()
        dic = w4.bow(list_token)
        list_of_bow.append(dic)

    # matrix
    matrix_akhir = w4.matrix(list_of_bow)

    # jarak
    # id_file = articles.keys().index(findname)    # index findname dalam articles.keys() = index dalam matrix
    id_keyword = articles.keys().index(findname)
    kategori = {}
    for item in os.listdir(pathcorpus):
        if item.endswith(".txt"):
            with open(pathcorpus + "/" + item, 'r') as file:
                kategori[item] = " "
    # kategori = {}
    jarak = {}
    for key, vektor in zip(articles.keys(), matrix_akhir):
        if key != findname:
            jarak[key] = w5.manhattan_distance(matrix_akhir[id_keyword], vektor)
    # kategori
        if key[:2] == "ed":
            kategori[key]=("edukasi")
        elif key[:2] == "bk":
            kategori[key]=("ekonomi")
        elif key[:2] == "bl":
            kategori[key]=("bola")
        elif key[:2] == "en":
            kategori[key]=("entertaiment")
        elif key[:2] == "ot":
            kategori[key]=("otomotif")
        elif key[:2] == "lf":
            kategori[key]=("lifestyle")
        elif key[:2] == "tk":
            kategori[key]=("teknologi")
    # return w4.sortdic(jarak, descending=False, n=5)
    return w4.sortdic(jarak, kategori, descending=False, n=5)

def findJaccard_similarity(pathfile, pathcorpus):
    """
    mencari jarak/similarity antara suatu file dengan sekumpulan file/corpus dalam folder.
    :param pathfile: path tempat artikel yg dicari
    :param pathcorpus: path tempat folder
    :return: nama file, jarak terdekat
    """

    # this_path = os.path.split(__file__)[0]
    # pathcorpus = os.path.join(this_path, pathcorpus)
    # pathfile   = os.path.join(this_path, pathfile)
    # membaca sekaligus pre-processing semua artikel corpus simpan ke dictionary
    articles = {}
    for item in os.listdir(pathcorpus):
        if item.endswith(".txt"):
            with open(pathcorpus + "/" + item, 'r') as file:
                articles[item] = w3.prepro_base(file.read())

    # memasukan kata kunci kedalam dictionary dengan nama item/index(keyword_index)
    # kemudian dimasukan ke dictionary articles dengan value keyword yang dimasukan
    findname = 'index'
    articles[findname] = w3.prepro_base(pathfile)

    # tambahkan artikel yg dicari ke dictionary
    # findname = pathfile.split("/")[-1]
    # try:
    #     articles[findname]
    # except:
    #     with open(pathfile, 'r') as file:
    #         articles[findname] = w3.prepro_base(file.read())

    # representasi bow
    list_of_bow = []
    for key, value in articles.items():
        list_token = value.split()
        dic = w4.bow(list_token)
        list_of_bow.append(dic)

    # matrix
    matrix_akhir = w4.matrix(list_of_bow)

    # jarak
    # id_file = articles.keys().index(findname)    # index findname dalam articles.keys() = index dalam matrix
    id_keyword = articles.keys().index(findname)
    kategori = {}
    for item in os.listdir(pathcorpus):
        if item.endswith(".txt"):
            with open(pathcorpus + "/" + item, 'r') as file:
                kategori[item] = " "
    # kategori = {}
    jarak = {}
    for key, vektor in zip(articles.keys(), matrix_akhir):
        if key != findname:
            jarak[key] = w5.jaccard_similarity(matrix_akhir[id_keyword], vektor)
    # kategori
        if key[:2] == "ed":
            kategori[key]=("edukasi")
        elif key[:2] == "bk":
            kategori[key]=("ekonomi")
        elif key[:2] == "bl":
            kategori[key]=("bola")
        elif key[:2] == "en":
            kategori[key]=("entertaiment")
        elif key[:2] == "ot":
            kategori[key]=("otomotif")
        elif key[:2] == "lf":
            kategori[key]=("lifestyle")
        elif key[:2] == "tk":
            kategori[key]=("teknologi")
    # return w4.sortdic(jarak, descending=False, n=5)
    return w4.sortdic(jarak, kategori, descending=False, n=5)

def findPearson_correlation(pathfile, pathcorpus):
    """
    mencari jarak/similarity antara suatu file dengan sekumpulan file/corpus dalam folder.
    :param pathfile: path tempat artikel yg dicari
    :param pathcorpus: path tempat folder
    :return: nama file, jarak terdekat
    """

    # this_path = os.path.split(__file__)[0]
    # pathcorpus = os.path.join(this_path, pathcorpus)
    # pathfile   = os.path.join(this_path, pathfile)
    # membaca sekaligus pre-processing semua artikel corpus simpan ke dictionary
    articles = {}
    for item in os.listdir(pathcorpus):
        if item.endswith(".txt"):
            with open(pathcorpus + "/" + item, 'r') as file:
                articles[item] = w3.prepro_base(file.read())

    # memasukan kata kunci kedalam dictionary dengan nama item/index(keyword_index)
    # kemudian dimasukan ke dictionary articles dengan value keyword yang dimasukan
    findname = 'index'
    articles[findname] = w3.prepro_base(pathfile)

    # tambahkan artikel yg dicari ke dictionary
    # findname = pathfile.split("/")[-1]
    # try:
    #     articles[findname]
    # except:
    #     with open(pathfile, 'r') as file:
    #         articles[findname] = w3.prepro_base(file.read())

    # representasi bow
    list_of_bow = []
    for key, value in articles.items():
        list_token = value.split()
        dic = w4.bow(list_token)
        list_of_bow.append(dic)

    # matrix
    matrix_akhir = w4.matrix(list_of_bow)

    # jarak
    # id_file = articles.keys().index(findname)    # index findname dalam articles.keys() = index dalam matrix
    id_keyword = articles.keys().index(findname)
    kategori = {}
    for item in os.listdir(pathcorpus):
        if item.endswith(".txt"):
            with open(pathcorpus + "/" + item, 'r') as file:
                kategori[item] = " "
    # kategori = {}
    jarak = {}
    for key, vektor in zip(articles.keys(), matrix_akhir):
        if key != findname:
            jarak[key] = w5.pearson_correlation(matrix_akhir[id_keyword], vektor)
    # kategori
        if key[:2] == "ed":
            kategori[key]=("edukasi")
        elif key[:2] == "bk":
            kategori[key]=("ekonomi")
        elif key[:2] == "bl":
            kategori[key]=("bola")
        elif key[:2] == "en":
            kategori[key]=("entertaiment")
        elif key[:2] == "ot":
            kategori[key]=("otomotif")
        elif key[:2] == "lf":
            kategori[key]=("lifestyle")
        elif key[:2] == "tk":
            kategori[key]=("teknologi")
    # return w4.sortdic(jarak, descending=False, n=5)
    return w4.sortdic(jarak, kategori, descending=False, n=5)
