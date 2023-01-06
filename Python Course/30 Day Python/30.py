class ListsNDictionary:

    print("____LIST____")
    class List:
        My_List = []


        My_Cart = [12.99, 312, 32, 142]
        print(f"My Cart consist of : {My_Cart}")
        print("Sum of My_Cart Is: ", sum(My_Cart)) # 498.99

        # append - adds item to the end of the list
        My_Cart.append(39.99)
        print("Append: 39.99" , My_Cart)

        # len - finds length of list
        print(f"Length of My_Cart is: {len(My_Cart)}") # 5
        
        # position []
        print(My_Cart) # [12.99, 312, 32, 142, 39.99]
        print(f"Position 3: {My_Cart[3]}") # 142
        print(f"Position 2: {My_Cart[2]}") # 32
        print(f"Position 1: {My_Cart[1]}") # 312
        print(f"Position 2 X 120: {My_Cart[2] * 120}") # 3840


        My_String = "hello world"
        print(f"Length of My_String: {len(My_String)}") # 11

        print(f"Position 4 Letter: {My_String[4]}") # 'o'


        My_Items = ["mouse", "laptop", "mic", "screen", "snack"]
        print(My_Items)

        print(f"Position 1 in list: {My_Items[1]}") # 'laptop'
        
        My_Products = [My_Items, My_Cart]
        print(My_Products) # [['mouse', 'laptop', 'mic', 'screen', 'snack'], [12.99, 312, 32, 142, 39.99]]
    
    print("____DICTIONARIES____")
    class Dictionaries:
        My_List = [1,2,3,4,5]
        My_Data = {"name": "Justin Mitchel"}
        print(My_Data["name"]) # 'Justin Mitchel'

        My_Data = {"name": "Justin Mitchel", "location": "California"}
        # My_Data[0] # Traceback Error Dictionary cannot identify positions

        print(My_Data.keys()) # Dict_Keys(['name', 'location']))
        
        print(f"Dictionary to List - {list(My_Data.keys())}")  # ['name', 'location']
        print(f" List position 0: {list(My_Data.keys())[0]}") # 'name'

        # My_Data.append({"occ": "coder"}) # Traceback Error

        My_Data["occ"] = "Coder"
        print(f"New Dictionary: {My_Data}") # {'name': 'Justin Mitchel', 'location': 'California', 'occ': 'Coder'}
        
        User_1 = {"name": "James bond"}
        User_2 = {"name": "Ned Stark"}
        My_Users = [User_1, User_2]
        print(f"My users: {My_Users}\n") # [{'name': 'James bond'}, {'name': 'Ned Stark'}]