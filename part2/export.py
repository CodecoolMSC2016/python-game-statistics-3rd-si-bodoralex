import reports as r


def main():
    input_file = 'game_stat.txt'
    export_file = open('reports.txt', 'w')

    export_file.write('What is the title of the most played game?\n')
    export_file.write(str(r.get_most_played(input_file)) + '\n\n')

    export_file.write('How many copies have been sold total?\n')
    export_file.write(str(r.sum_sold(input_file)) + '\n\n')

    export_file.write('What is the average selling?\n')
    export_file.write(str(r.get_selling_avg(input_file)) + '\n\n')

    export_file.write('How many characters long is the longest title?\n')
    export_file.write(str(r.count_longest_title(input_file)) + '\n\n')

    export_file.write('What is the average of the release dates?\n')
    export_file.write(str(r.get_date_avg(input_file)) + '\n\n')

    export_file.write('What properties has a game?\n')
    export_file.write(str(r.get_game(input_file, 'The Sims 3')) + '\n\n')

    export_file.write('How many games are there grouped by genre?\n')
    genre_count = r.count_grouped_by_genre(input_file)
    for genre in genre_count.items():
        export_file.write(str(genre))
        export_file.write('\n')

    export_file.close()

main()
