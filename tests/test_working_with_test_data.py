import csv
import json


with open('test_data/users.json', encoding='utf-8') as file_users:
    users_list = json.load(file_users)
    if not isinstance(users_list, list):
        raise RuntimeError('Expected a JSON array of users in users.json')


result_users = []
for user in users_list:
    result_users.append({
        'name':    user['name'],
        'gender':  user['gender'],
        'address': user['address'],
        'age':     user['age'],
        'books':   []
    })


with open('test_data/books.csv', encoding='utf-8', newline='') as file_books:
    reader_books = csv.reader(file_books)

    header = next(reader_books, None)
    if header is None:
        raise RuntimeError('books.csv is empty')

    idx_title = header.index('Title')
    idx_author = header.index('Author')
    idx_pages = header.index('Pages')
    idx_genre = header.index('Genre')

    num_users = len(result_users)

    for i, row in enumerate(reader_books):
        title = row[idx_title]
        author = row[idx_author]
        pages = int(row[idx_pages])
        genre = row[idx_genre]

        user_index = i % num_users
        result_users[user_index]['books'].append({
            'title':  title,
            'author': author,
            'pages':  pages,
            'genre':  genre
        })


output_data = {'users': result_users}
with open('result.json', 'w', encoding='utf-8') as file_result:
    json.dump(output_data, file_result, ensure_ascii=False, indent=1)
