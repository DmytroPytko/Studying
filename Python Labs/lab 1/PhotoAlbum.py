class PhotoAlbum:

    total_number_of_lists = 0

    def __init__(self, heading="Photo Album", color="Blue", price=140, number_of_lists=250, type="Classical Album"):
        self.heading = heading
        self.color = color
        self.price = price
        self.number_of_lists = number_of_lists
        self.type = type
        PhotoAlbum.total_number_of_lists += self.number_of_lists

    def to_string(self):
        print("Heading: " + self.heading + ", Color: " + str(self.color)
              + ", Price: " + str(self.price) + " Number of lists: "
              + str(self.number_of_lists) + " lists, Type: " + str(self.type))

    def print_sum(self):
        print("Album called " + self.heading + " has number of lists " + str(self.number_of_lists))

    @staticmethod
    def print_static_sum():
        print("Total number of lists of all Albums = " + str(PhotoAlbum.total_number_of_lists))


if __name__ == "__main__":
    classical_album = PhotoAlbum()
    transparent_album = PhotoAlbum("Photoalbum with transparent pocket", "white", 50, 370, "Family Album")
    photo_book = PhotoAlbum("Photobook with artistic elements", "yellow", 290, 180, "Custom")
    classical_album.to_string()
    transparent_album.to_string()
    photo_book.to_string()
    PhotoAlbum.print_static_sum()
    transparent_album.print_sum()
    photo_book.print_sum()
