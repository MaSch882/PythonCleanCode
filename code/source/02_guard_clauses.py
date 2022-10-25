def check_id_wrong(name: str, age: int, birthplace: str) -> bool:
    if name == 'Max Mustermann':
        if age == 24:
            if birthplace == 'Musterstadt':
                return True
    return False


def check_id_correct(name: str, age: int, birthplace: str) -> bool:
    if name != 'Max Mustermann':
        return False
    if age != 24:
        return False
    if birthplace != 'Musterstadt':
        return False
    return True


def main():
    name = 'Max Mustermann'
    age = 24
    birthplace = 'Musterstadt'

    print(check_id_wrong(name, age, birthplace))
    print(check_id_correct(name, age, birthplace))


if __name__ == '__main__':
    main()