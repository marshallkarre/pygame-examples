#Slightly-modified to run on Python 3, based on code by Joe P (https://www.youtube.com/channel/UC6QzpZxCD8sxndOJBQvbGPg)

# I hope that this code is any help at all for your game!
# if it has I would love to see your project, so send me a
# message/link at https://www.youtube.com/channel/UC6QzpZxCD8sxndOJBQvbGPg


# import and initialize pygame
import pygame
pygame.init()
# import random for random.randint and random.choice
import random

# define width and height of the window and screen object
WIDTH = 800
HEIGHT = 600

# create the window for the game. This is where images will "blit" to
# fill the surface with black in RGB form
main_s = pygame.display.set_mode((WIDTH, HEIGHT))
main_s.fill((0, 0, 0))

# create clock object used to set frame rate
clock = pygame.time.Clock()

# create an empty list to hold particle objects
particle_list = []

# create a screen for particles to collide with
# look at the "remove_particles" function for why
# this would be needed
screen = pygame.sprite.Sprite()
screen.rect = pygame.Surface((WIDTH, HEIGHT)).get_rect()
screen.rect.x = 0
screen.rect.y = 0

# create a class for Particles derived from pygame.sprite.Sprite
# pygame.sprite.Sprite allows us to collide objects easily
class Particle(pygame.sprite.Sprite):
    # constructor that takes starting x and y positions
    # change in x and y which provides speed and direction of the particle
    # size of the particle
    def __init__(self, x, y, dx, dy, size):
        # create a displayable surface to represent the particle and
        # create a rect object from the image
        self.image = pygame.Surface((size, size))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()

        # assign the passed values to the class objects own values
        self.x_velocity = dx
        self.y_velocity = dy
        self.rect.x = x
        self.rect.y = y

        # create gravity effect (optional in the class update function)
        self.gravity = 0.25

    def update(self):
        # add gravity effect (optional but cool)
        self.y_velocity += self.gravity

        # move the rect based on the current velocity of the particle
        self.rect.x += self.x_velocity
        self.rect.y += self.y_velocity

    def display(self, main_surface):
        # display the particles image to the main surface at the particles coordinates
        main_surface.blit(self.image, (self.rect.x, self.rect.y))

def create_particles(p_list, position):

    # define an amount of particles to create
    particle_count = 20

    # create a range of numbers that exculdes 0, if 0 is included then
    # there is a chance both x and y velocity will be 0 and then the
    # particle will just be stationary
    numbers = list(set(range(-5, 5)) - {0})

    # loop for the particle count
    for i in range(0, particle_count):

        # create a particle using the position passed in the function,
        # random velocity in x and random velocity in y
        # random size from 1 to 5
        p = Particle(position[0], position[1], random.choice(numbers), random.choice(numbers), random.randint(1, 5))

        # add the particle to the list
        p_list.append(p)

    # return the new list
    return p_list

def remove_particles(p_list):
    # loop for the size of the particle list, elements are checked moving backwards through the list size
    # this is because removing an element from a python list just shifts everything back so in a list of
    # [2, 5, 7, 3, 6] lets say elements 0 and 4 need to be removed if element 0 is removed the list
    # becomes [5, 7, 3, 6] now trying to remove element 4 would class as iterating out of range. removing
    # list elements backwards avoids this issue.
    for x in range(0, len(p_list)):
        try:
            # check if the particle is no longer colliding with the screen
            if not pygame.sprite.collide_rect(screen, p_list[len(p_list) - x - 1]):
                # remove the particle from the list
                del p_list[len(p_list) - x - 1]
        except:
            # break in case [len(p_list) - x - 1] is out of range
            # I'm not entirely sure why it gets out of range but maybe one of you
            # could tell me! Please let me know becasue it is bothering me!
            # the missed particle will be removed on the next update anyway
            # because the particle will just get tested next update as it
            # is still in the list
            break

    # return the new list
    return p_list

def update_all(u_list):
    # loop for the length of the list
    for i in range(0, len(u_list)):
        # call the update function of each list element
        u_list[i].update()

def display_all(d_list, main_surface):
    # fill the screen again with black
    main_s.fill((0, 0, 0))

    # loop for the length of the list
    for i in range(0, len(d_list)):
        # call the display function for each list element and pass the main surface to it
        d_list[i].display(main_surface)

RUN = True
while RUN:
    # set the desired frame rate to 60
    # to see actual frame rate you can use
    # print(str(clock.get_fps()))
    clock.tick(60)

    # loop for all events picked up by pygame, this
    # includes all keyboard, mouse and window events
    for event in pygame.event.get():
        # if the window x is pressed
        if event.type == pygame.QUIT:
            RUN = False
        # if the mouse is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            # create particles from the point it was clicked
            particle_list = create_particles(particle_list, pygame.mouse.get_pos())

    # update and display the particle list
    update_all(particle_list)
    display_all(particle_list, main_s)

    # check if any particles need to be removed
    particle_list = remove_particles(particle_list)

    # tell pygame that changes have been made to the screen and needs to be displayed
    pygame.display.flip()

# exit all pygame modules
pygame.quit()