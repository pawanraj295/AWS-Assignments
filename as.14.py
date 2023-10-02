#NameError and a TypeError
def name_error_example():

    try:

        print(undefined_variable)
    except NameError as e:
        print(f"NameError: {e}")
        print("A NameError occurred.")

def type_error_example():
    try:
        result = "hello" + 42
    except TypeError as e:
        print(f"TypeError: {e}")
        print("A TypeError occurred.")

if __name__ == "__main__":
    print("Handling NameError:")
    name_error_example()

    print("\nHandling TypeError:")
    type_error_example()
