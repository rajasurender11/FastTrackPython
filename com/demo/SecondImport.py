from FirstImport import id,add

def process():
    print("This is process method  ")

def main():
    print("This is second import")
    print(id)
    print(__name__)
    r = add(8,9)
    print(r)
    process()


if __name__ == "__main__":
    main()

