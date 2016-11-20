def get_most_played(file_name):
    with open(file_name, encoding="utf-8") as database:
        stats = [row.strip().split('\t') for row in database.readlines()]
        most_played_game = ""
        most_played_copies = 0.
        for row in stats:
            if float(row[1]) > most_played_copies:
                most_played_copies = float(row[1])
                most_played_game = row[0]
        return most_played_game


def sum_sold(file_name):
    with open(file_name, encoding="utf-8") as database:
        stats = [float(row.strip().split('\t')[1])
                 for row in database.readlines()]
        return sum(stats)


def get_selling_avg(file_name):
    with open(file_name, encoding="utf-8") as database:
        stats = [float(row.strip().split('\t')[1])
                 for row in database.readlines()]
        return sum(stats) / (len(stats))


def count_longest_title(file_name):
    with open(file_name, encoding="utf-8") as database:
        lenghts = [len(row.strip().split('\t')[0])
                   for row in database.readlines()]
        return max(lenghts)


def get_date_avg(file_name):
    with open(file_name, encoding="utf-8") as database:
        release_dates = [int(row.strip().split('\t')[2])
                         for row in database.readlines()]
        return round(sum(release_dates) / len(release_dates) + 0.5)


def get_game(file_name, title):
    with open(file_name, encoding="utf-8") as database:
        game = [row.strip().split('\t')
                for row in database.readlines() if row.strip().split('\t')[0] == title]
        g = game[0]
        return [g[0], float(g[1]), int(g[2]), g[3], g[4]]


def count_grouped_by_genre(file_name):
    with open(file_name, encoding="utf-8") as database:
        game_genres = {}
        while True:
            row = database.readline().split("\t")
            if row == ['']:
                return game_genres
            elif not row[3] in game_genres:
                game_genres[row[3]] = 1
            else:
                game_genres[row[3]] += 1
