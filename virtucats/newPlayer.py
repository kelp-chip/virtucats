import csv

class NewPlayer:
    def __init__(self, player_name, infile):

        self.name = player_name
        self.game_tracker = 0
        self.chapt_tracker = 0

        file = open(infile, newline='')
        reader = csv.reader(file)
        header = next(reader)  # skips over first line since  header

        data = [row for row in reader]
        id_list = []
        for line in data:
            id_list.append(int(line[0]))
        id_list.sort()
        player_id = id_list[-1] + 1

        self.id = player_id

        new_player = [self.id, self.name, self.game_tracker, self.chapt_tracker]

        file = open(infile, 'a', newline='')
        writer = csv.writer(file)
        writer.writerow(new_player)
