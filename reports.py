def count_games(file_name):
    with open(file_name, encoding="utf-8") as database:
        rows = 0
        stats = [row.strip().split('\t') for row in database.readlines()]
        for row in stats:
            if len(row) == 5:
                rows += 1
        return rows


def decide(file_name, year):
    with open(file_name, encoding="utf-8") as database:
        for row in database.readlines():
            if str(year) in row:
                return True
        return False


def get_latest(file_name):
    with open(file_name, encoding="utf-8") as database:
        year = 0
        stats = [row.strip().split('\t') for row in database.readlines()]
        for row in stats:
            if year < int(row[2]):
                year = int(row[2])
        for row in stats:
            if year == int(row[2]):
                return row[0]


def count_by_genre(file_name, genre):
    with open(file_name, encoding="utf-8") as database:
        genrecounter = 0
        stats = [row.strip().split('\t') for row in database.readlines()]
        for row in stats:
            if genre == row[3]:
                genrecounter += 1
        return genrecounter


def get_line_number_by_title(file_name, title):
    with open(file_name, encoding="utf-8") as database:
        try:
            stats = [row.strip().split('\t') for row in database.readlines()]
            title_row = 1
            for row in stats:
                if title == row[0]:
                    return title_row
                title_row += 1
            raise ValueError
        except ValueError:
            pass


def sort_abc(file_name):
    with open(file_name, encoding="utf-8") as database:
        titles = [row.strip().split('\t')[0] for row in database.readlines()]
        return sorted(titles, key=str.lower)


def get_genres(file_name):
    with open(file_name, encoding="utf-8") as database:
        stats = [row.strip().split('\t') for row in database.readlines()]
        genres = []
        for row in stats:
            if not row[3] in genres:
                genres.append(row[3])
        return sorted(genres, key=str.lower)


def when_was_top_sold_fps(file_name):
    try:
        with open(file_name, encoding="utf-8") as database:
            stats = [row.strip().split('\t') for row in database.readlines()
                     if row.strip().split('\t')[3] == 'First-person shooter']
            top_copies = 0
            release_date = 0
            for row in stats:
                if float(row[1]) > top_copies:
                    top_copies = float(row[1])
                    release_date = row[2]
            if release_date != 0:
                return int(release_date)
            raise ValueError
    except ValueError:
        pass
