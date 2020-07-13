import youtube_dl

# TODO rename file to: search_links.py

# mock input data -> don't need to run gui to check
mock_gui_output_1 = {0: None, 10: 'skrillex', 11: 2, 12: '1: Without Separation : Whole track',
                     '-DEFAULT_FOLDER-': 'C:\\!\\git\\youtube_instrumentals\\!download', 'Browse': ''}

mock_gui_output_flume_skrillex_tameimpala_10 = {0: None, 10: 'flume', 11: 2, 12: '1: Without Separation : Whole track',
                                                20: 'skrillex', 21: '3',
                                                22: '1: Without Separation : Whole track', 30: 'tame impala ', 31: '4',
                                                32: '1: Without Separation : Whole track', 40: '', 41: 0,
                                                42: '1: Without Separation : Whole track',
                                                50: '', 51: 0, 52: '1: Without Separation : Whole track', 60: '', 61: 0,
                                                62: '1: Without Separation : Whole track', 70: '', 71: 0,
                                                72: '1: Without Separation : Whole track',
                                                80: '', 81: 0, 82: '1: Without Separation : Whole track', 90: '', 91: 0,
                                                92: '1: Without Separation : Whole track', 100: '', 101: 0,
                                                102: '1: Without Separation : Whole track',
                                                '-DEFAULT_FOLDER-': 'C:\\!\\git\\youtube_instrumentals\\!download',
                                                'Browse': ''}

mock_gui_output_banks_audioslave_sonlux_jamesblake = {0: None, 10: 'banks', 11: 10,
                                                      12: '1: Without Separation : Whole track',
                                                      20: 'audioslave', 21: '3',
                                                      22: '1: Without Separation : Whole track', 30: 'son lux', 31: '4',
                                                      32: '1: Without Separation : Whole track', 40: 'james blake',
                                                      41: 5,
                                                      42: '1: Without Separation : Whole track',
                                                      50: '', 51: 0, 52: '1: Without Separation : Whole track', 60: '',
                                                      61: 0,
                                                      62: '1: Without Separation : Whole track', 70: '', 71: 0,
                                                      72: '1: Without Separation : Whole track',
                                                      80: '', 81: 0, 82: '1: Without Separation : Whole track', 90: '',
                                                      91: 0,
                                                      92: '1: Without Separation : Whole track', 100: '', 101: 0,
                                                      102: '1: Without Separation : Whole track',
                                                      '-DEFAULT_FOLDER-': 'C:\\!\\git\\youtube_instrumentals\\!download',
                                                      'Browse': ''}
# options for youtube_dl
# simulate: true -> this will only gather information
ydl_opts_wav = {
    'format': 'bestaudio/best',
    'outtmpl': '!download/%(uploader)s/%(title)s.%(ext)s',
    'min_views': 10000,
    'max_views': 10000000000000,
    'max_length': 1000,
    'ignoreerrors': True,
    'simulate': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '320',
    }],
}


def tracks_combined_number(data):
    """
    :return: number of all tracks from all artists,
    for ex flume 2, skrillex 3 -> this will return 5 (int)
    """
    return int(len(data) / 3 - 1)


def remove_ydl_cache():
    """
    unfinished downloads from past may cause errors,
    it's safer to remove cache downloads - this remove possibility of continue downloads that was unfinished
    """
    # youtube_dl require some arguments, this won't be passed further
    ydl_opts_wav = {}
    # remove cache
    youtube_dl.YoutubeDL(ydl_opts_wav).cache.remove()


global_artists_name = []


def ydl(gui_output):
    iterations = tracks_combined_number(gui_output)

    # remove cache
    youtube_dl.YoutubeDL(ydl_opts_wav).cache.remove()

    for k in range(iterations):
        # get id for every line of gui
        index_nr = k
        k = k + 1
        id_name = k * 10 + 0
        id_how_much = k * 10 + 1
        id_method = k * 10 + 2

        # parse for every iteration (line), corresponding value
        name = gui_output[id_name]
        how_much = gui_output[id_how_much]
        method = gui_output[id_method]

        # ignore lines when there isn't any input (from gui10 line window)
        if name == "":
            break

        print("name", name, "how_much", how_much, "method", method)

        query = "ytsearch" + str(how_much) + ":" + name

        one_artist_link_list = []
        one_artist_link_list.append(name),
        global_artists_name.append(one_artist_link_list)

        print(query)
        # for p in range(how_much):
        #     links = youtube_dl_info_parser['entries'][p]['id']
        #     one_artist_link_list[index_nr].append(links)
        try:
            youtube_dl_info_parser = youtube_dl.YoutubeDL(ydl_opts_wav).extract_info(query)
            number_links = len(youtube_dl_info_parser['entries'])
            print("\n\n\n", number_links)
            for m in range(number_links):
                global_artists_name[index_nr].append(youtube_dl_info_parser['entries'][m]['id'])
            # links = youtube_dl_info_parser['entries'][0]['id']
            # print("this is links: ", links)
        except:
            print('************** EXCEPT: youtube-dl unsupported keyword')

    return global_artists_name

# output_backend = ydl(mock_gui_output_1)
# print(output_backend)
# searching_results.get_info_all_list(output_backend)
