def format_announcement_for_combined_post(announcement):
    return ("## " + announcement.title + "\n" +
            "[Link to the " + announcement.title + " announcement](" + announcement.url + ") \n")