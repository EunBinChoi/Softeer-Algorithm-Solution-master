# 3) progress the preprocessing string is ciphered
# 1. 만약 두 글자가 표에서 같은 행에 존재하면 오른쪽으로 한 칸 이동한 칸에 적힌 글자로 암호화

class Location:
    def __init__(self) -> None:
        self.__x = -1
        self.__y = -1

    def __eq__(self, _o: object) -> bool:
        return self.__x != -1 and _o.x != -1 and self.__x == _o.x and \
               self.__y != -1 and _o.y != -1 and self.__y == _o.y

    def __str__(self) -> str:
        return "<Location Class> x = {0}, y = {1}".format(self.__x, self.__y)


def getLocationOfMsg(_key: list, _target: str) -> list:
    _target_first_letter_loc = Location()
    _target_second_letter_loc = Location()

    for i in range(len(_key)):
        for j in range(len(_key[0])):
            if _key[i][j] == _target[0]:
                _target_first_letter_loc.x = i
                _target_first_letter_loc.y = j
                break

    for i in range(len(_key)):
        for j in range(len(_key[0])):
            if _key[i][j] == _target[1]:
                _target_second_letter_loc.x = i
                _target_second_letter_loc.y = j
                break

    if _target_first_letter_loc.x != -1 and _target_first_letter_loc.y != -1 and \
            _target_second_letter_loc.x != -1 and _target_second_letter_loc.y != -1:
        _loc = [_target_first_letter_loc, _target_second_letter_loc]
        return _loc
    else:
        return None


def isSameRow(_key: list, _target: str) -> bool:
    _target_first_x = -1
    _target_second_x = -1
    # print('key', key)
    # print('target', target, 'target[0]', target[0], 'target[1]', target[1])
    for i in range(len(_key)):
        for j in range(len(_key[0])):
            if _key[i][j] == _target[0]: _target_first_x = i; break

    for i in range(len(_key)):
        for j in range(len(_key[0])):
            if _key[i][j] == _target[1]: _target_second_x = i; break

    # print(target_first_x)
    # print(target_second_x)

    if _target_first_x != -1 and _target_second_x != -1 and _target_first_x == _target_second_x:
        return True
    else:
        return False


def isSameColumn(_key: list, _target: str) -> bool:
    _target_first_y = -1
    _target_second_y = -1

    for i in range(len(_key)):
        for j in range(len(_key[0])):
            if _key[i][j] == _target[0]: _target_first_y = j; break

    for i in range(len(_key)):
        for j in range(len(_key[0])):
            if _key[i][j] == _target[1]: _target_second_y = j; break

    # print(target_first_y)
    # print(target_second_y)

    if _target_first_y != -1 and _target_second_y != -1 and _target_first_y == _target_second_y:
        return True
    else:
        return False


if __name__ == '__main__':
    # 1) make the 5x5 array for making key
    dup = []
    msg_str = input()
    key_str = input().replace('J', 'I')

    key_str2lst = [[0] * 5 for _ in range(5)]
    alphabet = [chr(i) for i in range(65, 91) if chr(i) != 'J']
    checker = [False for i in range(65, 91) if chr(i) != 'J']
    # print(alphabet)

    i = 0
    k = 0
    while i < len(key_str2lst):  # row
        j = 0
        while j < len(key_str2lst[0]):  # col
            if k < len(key_str):
                if key_str[k] not in dup:
                    # push key_str[] into key_str2lst[i][j]
                    # push key_str[] into tmp
                    dup.append(key_str[k])
                    key_str2lst[i][j] = key_str[k]

                    # get ascii softeer-playfair of key_str[]: A => 65-65 = 0
                    # change checker False to True
                    key_ord = ord(key_str2lst[i][j]) if key_str2lst[i][j] <= 'J' else ord(key_str2lst[i][j]) - 1
                    checker[key_ord - ord('A')] = True
                    j += 1
                k += 1
            elif k == len(key_str):
                # fill with noused character
                for idx in range(len(checker)):
                    if not checker[idx]:
                        # print('idx', idx)
                        # print('alphabet[]', alphabet[idx])
                        key_str2lst[i][j] = alphabet[idx]
                        checker[idx] = True
                        break
                j += 1
        i += 1

    # 2) preprocessing the message before it is ciphered
    msg_str_pair = [msg_str[i:i + 2] for i in range(0, len(msg_str), 2)]

    i = 0
    new_msg_str_pair = []
    while i < len(msg_str_pair):
        if len(msg_str_pair[i]) == 2:
            if msg_str_pair[i][0] == msg_str_pair[i][1]:
                new_msg_str = msg_str_pair[i][0]
                new_msg_str += 'X' if msg_str_pair[i][0] != 'X' else 'Q'
                new_msg_str_pair.append(new_msg_str)

                left_msg_str = msg_str_pair[i][1]
                for k in range(i + 1, len(msg_str_pair)):
                    left_msg_str += msg_str_pair[k]

                msg_str_pair = [left_msg_str[j:j + 2] for j in range(0, len(left_msg_str), 2)]
                i = 0
            else:
                new_msg_str_pair.append(msg_str_pair[i])
                i += 1
        else:
            new_msg_str_pair.append(msg_str_pair[i] + 'X')
            i += 1

    ciphered_msg = [None for _ in range(len(new_msg_str_pair))]
    i = 0
    while i < len(new_msg_str_pair):
        target = new_msg_str_pair[i]
        if getLocationOfMsg(key_str2lst, target):
            loc = getLocationOfMsg(key_str2lst, target)

        if isSameRow(key_str2lst, target):
            first_letter = key_str2lst[loc[0].x][(loc[0].y + 1) % len(key_str2lst[0])]
            second_letter = key_str2lst[loc[1].x][(loc[1].y + 1) % len(key_str2lst[0])]
        elif isSameColumn(key_str2lst, target):
            first_letter = key_str2lst[(loc[0].x + 1) % len(key_str2lst)][loc[0].y]
            second_letter = key_str2lst[(loc[1].x + 1) % len(key_str2lst)][loc[1].y]
        else:
            first_letter = key_str2lst[loc[0].x][loc[1].y]
            second_letter = key_str2lst[loc[1].x][loc[0].y]

        ciphered_msg[i] = first_letter + second_letter
        i += 1

    print("".join(ciphered_msg))
