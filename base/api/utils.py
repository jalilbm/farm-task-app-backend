def validate_animals_data(animal_data):
    """
    Validates incoming animal data.

    Args:
        animal_data (list): A list of dictionaries, each containing animal data.

    Returns:
        A list of validated animal data or dictionary with a message in case of error.
    """
    required_keys = ["id", "name", "quantity"]
    ids_seen = set()

    if not animal_data:
        return {"ok": False, "message": "Animals list is required"}

    for animal in animal_data:
        if not all(key in animal for key in required_keys):
            return {"ok": False, "message": "Invalid data structure"}

        try:
            # Check if id can be converted to int and is unique
            id = int(animal["id"])
            if id in ids_seen:
                return {"ok": False, "message": "Id is not unique"}
            ids_seen.add(id)

            # Check if quantity can be converted to int
            quantity = int(animal["quantity"])
        except ValueError:
            return {
                "ok": False,
                "message": "Id or quantity cannot be converted to integer",
            }

    return {"ok": True, "message": "Successful"}


def filter_valid_animals(animals):
    """
    Returns valid animals from given list. A valid animal is supposed to have keys 'id', 'name', and 'quantity'
    where 'id' is unique and can be convertible to int, 'quantity' can also be convertible to int.

    Args:
    animals (list): A list of dictionaries where each dictionary represents an animal and contains its 'id', 'name' and 'quantity'.

    Returns:
    list: Returns a list of valid animal dictionaries. If no valid animal is found, the returned list will be empty.
    """
    ids_seen = set()
    output = []

    for animal in animals:
        try:
            id = int(animal["id"])
            quantity = int(animal["quantity"])
            if (
                all(key in animal for key in ["id", "name", "quantity"])
                and id not in ids_seen
            ):
                animal["id"] = id
                animal["quantity"] = quantity
                output.append(animal)
                ids_seen.add(id)
        except ValueError:
            continue
    return output
