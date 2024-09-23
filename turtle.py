import turtle

class MyTurtle:
    def __init__(self, color, shape, size=(1, 1, 1)):
        # membuat objek turtle
        self.t = turtle.Turtle()
        self.t.color(color) 
        self.t.shape(shape)
        self.t.turtlesize(stretch_wid=size[0], stretch_len=size[1], outline=size[2])
        # strecth wid untuk lebar turtle
        # strecth len untuk panjang turtle
        # outline untuk ketebalan garis luar turtle

    def maju(self, jarak):
        # method untuk menggerakkan turtle maju sesuai jarak yang ditentukan
        self.t.forward(jarak)

    def belok_kiri(self, sudut):
        # method untuk memutar turtle ke kiri
        self.t.left(sudut) 

    def buat_segitiga(self, ukuran):
        # method untuk menggambar persegi
        for _ in range(3): # untuk pengulangan
            self.maju(ukuran)
            self.belok_kiri(120)

    def selesai(self):
        # method untuk menyelesaikan gambar
        turtle.done()

# membuat objek turtle dengan warna dan bentuk
turtle1 = MyTurtle("red", "turtle", size=(2,2,2))

# menggambar dengan ukuran sisi 250
turtle1.buat_segitiga(250)

# menyelesaikan gambar
turtle1.selesai()
