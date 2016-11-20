import reports as r


def main():
    input_file = 'game_stat.txt'
    export_file = open('reports.txt', 'w')

    export_file.write('How many games are in the file?\n')
    export_file.write(str(r.count_games(input_file)) + '\n\n')

    export_file.write('Is there a game from 2000?\n')
    export_file.write(str(r.decide(input_file, 2000)) + '\n\n')

    export_file.write('Which was the latest game?\n')
    export_file.write(str(r.get_latest(input_file)) + '\n\n')

    export_file.write(
        'How many games do we have by the First-person shooter genre?\n')
    export_file.write(str(r.count_by_genre(
        input_file, 'First-person shooter')) + '\n\n')

    export_file.write('What is the line number of Counter-Strike?\n')
    export_file.write(str(r.get_line_number_by_title(
        input_file, 'Counter-Strike')) + '\n\n')

    export_file.write('What is the alphabetical ordered list of the titles?\n')
    ordered_titles = r.sort_abc(input_file)
    for title in ordered_titles:
        export_file.write(title)
        export_file.write('\n')

    export_file.write('\nWhat are the genres?\n')
    genres = r.get_genres(input_file)
    for genre in genres:
        export_file.write(genre)
        export_file.write('\n')

    export_file.write(
        '\nWhat is the release date of the top sold "First-person shooter" game?\n')
    export_file.write(str(r.when_was_top_sold_fps(input_file)))

    export_file.close()

main()
