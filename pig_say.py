def pig_say(text):
    text_len = len(text)

    print('         {}'.format("_" * text_len))
    print('         <{}>'.format(text))
    print('         {}'.format('-' * text_len))
    print('         /')
    print('   ^..^ /')
    print('~( ( oo )')
    print('   ,, ,, ')


def main():
    text = input("Type here what you want the pig to say: ")
    pig_say(text)


if __name__ == "_main_":
    main()