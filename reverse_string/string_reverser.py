def reverse_string(s): 
    reversed_string = ""
    for char in s:
        reversed_string = char + reversed_string
    return reversed_string

def main():
    user_input = input("Ters çevrilecek metni girin: ")
    print("Ters çevrilmiş metin:", reverse_string(user_input))

if __name__ == "__main__":
    main()