def sort_colors(sequence):
    colors = sequence.split('-')
    colors.sort()
    return '-'.join(colors)

if __name__ == "__main__":
    print(sort_colors("green-red-yellow-black-white"))
    print(sort_colors("PINK-BLUE-TAN-PURPLE"))
