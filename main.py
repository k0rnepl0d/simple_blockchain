import json
import os
import hashlib


if not os.path.exists('blockchain'):
    os.mkdir('blockchain')


blockchain = os.curdir + '/blockchain/'

# ---Hash generation---
def hash_gen(filename):
    file_ = open(blockchain + filename, 'rb').read()
    return hashlib.sha256(file_).hexdigest()

# ---Getting the number of the last block in the chain---
def get_files():
    files = os.listdir(blockchain)
    return sorted([int(i) for i in files])

# ---Checking the integrity of the block chain---
def check_chain():
    files = get_files()
    print(' ')
    for file_ in files[1:]:
        f = open(blockchain + str(file_))
        h = json.load(f)['hash']

        prev_file = str(file_ - 1)

        actual_hash = hash_gen(prev_file)

        if h == actual_hash:
            res = 'Ok'
        else:
            res = 'Corrupted'

        print(f'Block {prev_file} is: {res}')

# ---Generation of a new block---
def new_block(prev_hash=''):
    files = get_files()
    len_files = len(files)

    if len_files == 0:
        filename = str('0')
        data = {
            'sender': 'none',
            'amount': 0,
            'recipient': 'none',
            'hash': ''
        }
        with open(blockchain + filename, 'w') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print('\nGenesis block genegate')


    else:
        prev_file = files[-1]

        filename = str(prev_file + 1)

        prev_hash = hash_gen(str(prev_file))

        sender = input(str('\nSender: '))
        amount = int(input('\nAmount: '))
        recipient = input(str('\nRecipient: '))

        data = {
            'sender': sender,
            'amount': amount,
            'recipient': recipient,
            'hash': prev_hash
        }
        with open(blockchain + filename, 'w') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print('\nBlock generate')

# ---Dialogue with the user---
def main():
    while True:
        action = input('\nNew block(1) / Check chain(2): ')

        if action == '1':
            new_block()

        elif action == '2':
            check_chain()


if __name__ == '__main__':
    main()
