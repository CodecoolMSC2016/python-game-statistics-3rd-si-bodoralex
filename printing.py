import reports as r


def main():

    input_file = 'game_stat.txt'

    print(r.count_games(input_file), '\n')
    print(r.decide(input_file, 2000), '\n')
    print(r.get_latest(input_file), '\n')
    print(r.count_by_genre(input_file, 'First-person shooter'), '\n')
    print(r.get_line_number_by_title(input_file, 'Counter-Strike'), '\n')

    shoretd_titles = r.sort_abc(input_file)
    for title in shoretd_titles:
        print(title)
    print()
    genres = r.get_genres(input_file)

    for genre in genres:
        print(genre)
    print('\n' + str(r.when_was_top_sold_fps(input_file)))


main()
