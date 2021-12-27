def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")

    fruit_list.reverse()
    fruit_list.append("orange")
    inde_apple = fruit_list.index("apple")
    fruit_list.insert(inde_apple, "cherry")
    print(f"original: {inde_apple}")
    print(f"original: {fruit_list}")

    fruit_list.remove("banana")
    print(f"original: {fruit_list}")

    poped_item=fruit_list.pop()
    print(poped_item)

    fruit_list.sort()
    print(f"original: {fruit_list}")

    fruit_list.clear()
    print(f"original: {fruit_list}")


main()