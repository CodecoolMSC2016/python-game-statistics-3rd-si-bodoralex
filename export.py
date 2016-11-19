import reports

input_file = 'game_stat.txt'
export_file = open('reports.txt', 'w')

genres = []
ordered_titles = []
ordered_titles = reports.sort_abc(input_file)

export_file.write(str('How many games are in the file?\n'))
export_file.write(str(reports.count_games(input_file)) + '\n\n')

export_file.write(str('Is there a game from 2000?\n'))
export_file.write(str(reports.decide(input_file, 2000)) + '\n\n')

export_file.write(str('Which was the latest game?\n'))
export_file.write(str(reports.get_latest(input_file)) + '\n\n')

export_file.write(
    str('How many games do we have by the First-person shooter genre?\n'))
export_file.write(str(reports.count_by_genre(
    input_file, 'First-person shooter')) + '\n\n')

export_file.write(str('What is the line number of Counter-Strike?') + '\n')
export_file.write(str(reports.get_line_number_by_title(
    input_file, 'Counter-Strike')) + '\n\n')

export_file.write(
    str('What is the alphabetical ordered list of the titles?\n'))
ordered_titles = reports.sort_abc(input_file)
for title in ordered_titles:
    export_file.write(title)
    export_file.write('\n')

export_file.write(str('\nWhat are the genres?\n'))
genres = reports.get_genres(input_file)
for genre in genres:
    export_file.write(genre)
    export_file.write('\n')

export_file.write(
    str('\nWhat is the release date of the top sold "First-person shooter" game?\n'))
export_file.write(str(reports.when_was_top_sold_fps(input_file)))

export_file.close()
