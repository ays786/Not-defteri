def not_ekle():
    not_metni = input("Notunuzu yazın: ")
    with open("notlar.txt", "a") as dosya:
        dosya.write(not_metni + "\n")
    print("Notunuz kaydedildi!")

if __name__ == "__main__":
    not_ekle()
