from csv import reader
# import pickle


initial_list = []
with open("codes.csv") as file:
    csv_reader = reader(file)
    next(csv_reader)
    for row in csv_reader:
        # data = list(csv_reader)
        initial_list.append(row)

codes_list = []
for sublist in initial_list:
    for item in sublist:
        codes_list.append(item)

def get_codes():
    initial_list = []
    with open("codes.csv") as file:
        csv_reader = reader(file)
        next(csv_reader)
        for row in csv_reader:
            # data = list(csv_reader)
            initial_list.append(row)

    codes_list = []
    for sublist in initial_list:
        for item in sublist:
            codes_list.append(item)

    return codes_list

#     with open("codes.pickle", "wb") as file:
#         pickle.dump(codes_list, file)
#
# def unpickle_codes():
#     with open("codes.pickle", "rb") as file:
#         codes_list = pickle.load(file)
#     return codes_list
