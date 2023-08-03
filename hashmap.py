import ctypes


def create_list():
    size = 0
    capacity = 10
    data = (ctypes.py_object * capacity)()

    def append(value):
        nonlocal size, capacity, data
        if size == capacity:
            new_data = (ctypes.py_object * (capacity * 2))()
            for i in range(size):
                new_data[i] = data[i]
            data = new_data
            capacity = capacity * 2
        data[size] = value
        size += 1

    def get(index):
        if 0 <= index < size:
            return data[index]
        else:
            raise IndexError("Index out of range")

    def set(index, value):
        if 0 <= index < size:
            data[index] = value
        else:
            raise IndexError("Index out of range")

    def remove(index):
        if 0 <= index < size:
            for i in range(index, size - 1):
                data[i] = data[i + 1]
            data[size - 1] = None
            size -= 1
        else:
            raise IndexError("Index out of range")

    def display():
        for i in range(size):
            print(data[i], end=" ")
        print()

    return append, get, set, remove, display

# Example usage:
append, get, set, remove, display = create_list()

append(10)
append(20)
append(30)
display()

set(1, 25)
display()

remove(0)
display()

print(get(1))


def hashmap(size):
    map = [None] * size

    def add(key, value):
        key_hash = hash(key) % size
        key_value = (key, value)

        if map[key_hash] is None:
            map[key_hash] = [key_value]
        else:
            for i, (existing_key, _) in enumerate(map[key_hash]):
                if existing_key == key:
                    map[key_hash][i] = key_value
                    break
            else:
                map[key_hash].append(key_value)

    def get(key):
        key_hash = hash(key) % size
        key_value_list = map[key_hash]

        if key_value_list is not None:
            for existing_key, value in key_value_list:
                if existing_key == key:
                    return value

        return None

    def delete(key):
        key_hash = hash(key) % size
        key_value_list = map[key_hash]

        if key_value_list is not None:
            for i, (existing_key, _) in enumerate(key_value_list):
                if existing_key == key:
                    del map[key_hash][i]
                    break

    def display():
        for i, key_value_list in enumerate(map):
            if key_value_list is not None:
                print(f"Slot {i}: {key_value_list}")

    return add, get, delete, display

# Example usage:
add, get, delete, display = hashmap(10)

add("apple", 10)
add("banana", 5)
add("orange", 20)
display()

print("Get value for 'apple':", get("apple"))
print("Get value for 'banana':", get("banana"))

delete("orange")
print("After deleting 'orange':")
display()
