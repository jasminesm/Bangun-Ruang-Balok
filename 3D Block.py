#Nama  = Jasmine Sarah Maqnolia
#NIM   = 20051397078
#Kelas = 2020B
#Prodi = Manajemen Informatika
#UAS Grafika Komputer

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

#mendefinisikan sudut/titik sudut
vertices = (
(1, -2, -3),
(1, 2, -3),
(-1, 2, -3),
(-1, -2, -3),
(1, -2, 3),
(1, 2, 3),
(-1, -2,3),
(-1, 2, 3)
)

#mendefinisikan garis/rusuk
edges = (
(0,1),
(0,3),
(0,4),
(2,1),
(2,3),
(2,7),
(6,3),
(6,4),
(6,7),
(5,1),
(5,4),
(5,7)
)

#mendefinisikan warna
colors = (
    (1,0,0),
    (1,0,1),
    (0,0,1),
    (1,0,1),
    (1,1,1),
    (0,1,1),
    (1,0,1),
    (1,0,1),
    (0,0,1),
    (1,0,1),
    (1,1,1),
    (0,1,1),
    )

#mendefisikan sisi
surfaces = (
(0,1,2,3),
(3,2,7,6),
(6,7,5,4),
(4,5,1,0),
(1,5,7,2),
(4,0,3,6)
)

#menggambar balok
def Block():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_QUADS)
    for surface in surfaces:
        x = 0
        for vertex in surface:
            x+=1
            glColor3fv(colors[x])
            glVertex3fv(vertices[vertex])
    glEnd()

#menambahkan layar untuk menampilkan balok
def main():
    #inisialisasi pygame
    pygame.init()
    #resolusi display layar
    display = (800,600)
    #mode layar double buffering
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    #mengubah perspektif, fov 30*, znear 0.1, zfar 50
    gluPerspective(30, (display[0]/display[1]), 0.1, 50.0)
    #memindahkan objek sesuai dengan matrix translate
    glTranslatef(0.0,0.0, -20)
    #infinite looping
    while True:
        #apabila ditekan tombol x, maka program akan berhenti.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #apabila ada tombol keyboard yang ditekan, 
        #maka akan dilakukan fungsi berikut
        if event.type == pygame.KEYDOWN:
            #bila yang di tekan tombol panah kiri
            #pindahkan balok ke kiri sebanyak 0.5
            if event.key == pygame.K_LEFT:
                glTranslatef(-0.5,0,0)
            if event.key == pygame.K_RIGHT:
                glTranslatef(0.5,0,0)

            if event.key == pygame.K_UP:
                glTranslatef(0,1,0)
            if event.key == pygame.K_DOWN:
                glTranslatef(0,-1,0)
        if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0,0,1.0)

                if event.button == 5:
                    glTranslatef(0,0,-1.0)
        
        glRotatef(1, 3, 1, 1)
        #menghapus semua kanvas/display
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Block()
        pygame.display.flip()
        #menunggu 20ms sebelum looping lagi
        pygame.time.wait(20) 
main ()