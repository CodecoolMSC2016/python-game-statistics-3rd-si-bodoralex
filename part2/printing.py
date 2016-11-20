import reports as r


def main():

    input_file = 'game_stat.txt'

    print(r.get_most_played(input_file), '\n')
    print(r.sum_sold(input_file), '\n')
    print(r.get_selling_avg(input_file), '\n')
    print(r.count_longest_title(input_file), '\n')
    print(r.get_date_avg(input_file), '\n')
    print(r.get_game(input_file, 'The Sims 3'), '\n')

    genre_count = r.count_grouped_by_genre(input_file)
    for genre in genre_count.items():
        print(genre)

    print()


main()
