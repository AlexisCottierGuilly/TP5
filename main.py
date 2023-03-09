"""
Fait par Alexis Cottier-Guilly
Fait le 18 janvier 2023
Ce programme teste les dessins avec arcade en dessinant quelque chose
que l'on peut reconnaitre avec différentes formes
"""
import math
import random

import arcade

SCREEN_WIDTH = 800 * 2
SCREEN_HEIGHT = 600 * 2
SCREEN_TITLE = "Les forêts magnifiques"

COLORS = [arcade.color.ROCKET_METALLIC, arcade.color.DARK_BROWN, arcade.color.DARK_GREEN,
          arcade.color.RED, arcade.color.YELLOW, arcade.color.BAKER_MILLER_PINK, arcade.color.SKY_BLUE,
          arcade.color.BLACK, arcade.color.WHITE]

CIRCLE = 0
SQUARE = 1

SHAPES = [CIRCLE, SQUARE]
SHAPE_NUMBER_KEY = [arcade.key.KEY_1, arcade.key.KEY_2, arcade.key.KEY_3]
SHAPE_COLORS_KEY = [arcade.key.KEY_1, arcade.key.KEY_2, arcade.key.KEY_3,
                    arcade.key.KEY_4, arcade.key.KEY_5, arcade.key.KEY_6, arcade.key.KEY_7,
                    arcade.key.KEY_8, arcade.key.KEY_9]


class DessinMagnifique(arcade.Window):
    """
    La classe principale de l'application

    NOTE : Vous pouvez effacer les méthodes que vous n'avez pas besoin.
    Si vous en avez besoin, remplacer le mot clé "pass" par votre propre code.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.dessin_custom = arcade.SpriteList()
        self.mouse_pressed = False
        self.mouse_position = -100, -100
        self.mouse_color = COLORS[0]
        self.mouse_size = 1.0
        self.shape = CIRCLE
        self.mouse_alpha = 255
        self.mouse_middle_click = False
        self.shift_pressed = False
        self.map_seed = 1
        self.load_new_terrain()

    def setup(self):
        """
        Configurer les variables de votre jeu ici. Il faut appeler la méthode une nouvelle
        fois si vous recommencez une nouvelle partie.
        """
        # C'est ici que vous allez créer vos listes de sprites et vos sprites.
        # C'est aussi ici que vous chargez les sons de votre jeu.
        pass

    def get_current_shape(self, x, y):
        """
        Créer une forme qui correspond au type de forme et à la bonne couleur
        :param x : position en x du sprite
        :param y : position en y du sprite
        :return: redonne le sprite -- qui va ensuite être ajouté à la liste des sprites du dessin
        """
        shape = arcade.Sprite()

        if self.shape == CIRCLE:
            shape = arcade.SpriteCircle(round(SCREEN_WIDTH // 50 * self.mouse_size), self.mouse_color)
            shape.position = x, y

        elif self.shape == SQUARE:
            shape = arcade.SpriteSolidColor(round(SCREEN_WIDTH // 25 * self.mouse_size),
                                            round(SCREEN_WIDTH // 25 * self.mouse_size), self.mouse_color)
            shape.position = x, y

        shape.alpha = self.mouse_alpha

        return shape

    def load_new_terrain(self):
        self.map_seed = random.randint(1, 1_000_000_000_000_000)

    @staticmethod
    def draw_tree(position, size):
        arcade.draw_rectangle_filled(position[0], position[1], size[0], size[1], arcade.color.WOOD_BROWN)
        arcade.draw_ellipse_filled(position[0], position[1] + size[1] / 1.2, size[0] * random.uniform(2, 3),
                                   size[1] * random.uniform(1.5, 2.5), arcade.color.DARK_GREEN)

    @staticmethod
    def draw_rock(position, size):
        arcade.draw_circle_filled(position[0], position[1], size[0] / 2.5, num_segments=random.randint(5, 8), color=arcade.color.COOL_GREY)

    @staticmethod
    def draw_grass(position, size):
        arcade.draw_arc_outline(position[0], position[1], size[0] * 0.5, size[1] * 0.75, (0, 100, 0), 0, random.uniform(45, 130), SCREEN_WIDTH / 150)

    @staticmethod
    def get_object_setup():
        position = random.uniform(0, SCREEN_WIDTH), random.uniform(0, SCREEN_HEIGHT / 3)
        size = random.uniform(SCREEN_WIDTH / 50, SCREEN_WIDTH / 25), random.uniform(SCREEN_HEIGHT / 35,
                                                                                    SCREEN_HEIGHT / 15)
        return position, size

    def draw_background(self):
        arcade.draw_rectangle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 6,
                                     SCREEN_WIDTH, SCREEN_HEIGHT / 3, arcade.color.ARMY_GREEN)
        random.seed(self.map_seed)
        for i in range(random.randint(25, 150)):
            self.draw_grass(*self.get_object_setup())

        for i in range(random.randint(3, 5)):
            self.draw_rock(*self.get_object_setup())

        for i in range(random.randint(5, 20)):
            self.draw_tree(*self.get_object_setup())

        sun_position = random.randint(round(SCREEN_WIDTH / 15), round(SCREEN_WIDTH / 15 * 14)), SCREEN_HEIGHT / 8 * 7

        arcade.draw_circle_filled(sun_position[0], sun_position[1], SCREEN_WIDTH / 20, arcade.color.SUNGLOW)

        number_of_radius = 10
        for angle in range(number_of_radius):
            # Dessiner les rayons du soleil
            angle = 360 / number_of_radius * (angle + 1)
            distance_from_center = SCREEN_WIDTH / 20
            start_position = sun_position[0] + math.cos(math.radians(angle)) * distance_from_center, \
                                sun_position[1] + math.sin(math.radians(angle)) * distance_from_center
            end_position = sun_position[0] + math.cos(math.radians(angle)) * distance_from_center * 2, \
                                sun_position[1] + math.sin(math.radians(angle)) * distance_from_center * 2
            arcade.draw_line(start_position[0], start_position[1], end_position[0], end_position[1], arcade.color.SUNGLOW)

        nom_foret = ''.join([random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(random.randint(3, 7))]).capitalize()
        arcade.draw_text(f'La forêt de {nom_foret}', 0, round(SCREEN_HEIGHT / 3 * 2),
                         arcade.color.MIDNIGHT_BLUE, width=SCREEN_WIDTH, bold=True,
                         font_size=round(SCREEN_WIDTH / 15), align='center', font_name='Garamond')
        arcade.draw_text(f'Seed de génération : {self.map_seed}', 0, round(SCREEN_HEIGHT / 3 * 1.8),
                         arcade.color.MIDNIGHT_BLUE, width=SCREEN_WIDTH,
                         font_size=round(SCREEN_WIDTH / 75), align='center')

        random.seed()

    def on_draw(self):
        """
        C'est la méthode qu'Arcade invoque à chaque "frame" pour afficher les éléments
        de votre jeu à l'écran.
        """

        # Cette commande permet d'effacer l'écran avant de dessiner. Elle va dessiner l'arrière-plan
        # selon la couleur spécifiée avec la méthode "set_background_color".
        arcade.start_render()
        self.draw_background()
        self.dessin_custom.draw()
        self.get_current_shape(self.mouse_position[0], self.mouse_position[1]).draw()

    def on_update(self, delta_time):
        """
        Toute la logique pour déplacer les objets de votre jeu et de
        simuler sa logique vont ici. Normalement, c'est ici que
        vous allez invoquer la méthode "update()" sur vos listes de sprites.
        Paramètre :
            - delta_time : le nombre de millisecondes depuis le dernier update.
        """
        pass

    def on_key_press(self, key, key_modifiers):
        """
        Cette méthode est invoquée à chaque fois que l'usager tape une touche
        sur le clavier.
        Paramètres :
            - key: la touche enfoncée
            - key_modifiers : est-ce que l'usager appuie sur "shift" ou "ctrl" ?
        """

        if key == arcade.key.LSHIFT:
            self.shift_pressed = True

        if key_modifiers & arcade.key.LSHIFT:
            if key in SHAPE_COLORS_KEY:
                self.mouse_color = COLORS[SHAPE_COLORS_KEY.index(key)]

        elif key == arcade.key.ENTER:
            self.load_new_terrain()

        else:
            if key in SHAPE_NUMBER_KEY:
                self.shape = SHAPES[SHAPE_NUMBER_KEY.index(key)]

        if key == arcade.key.R:
            self.dessin_custom = arcade.SpriteList()

    def on_key_release(self, key, key_modifiers):
        """
        Méthode invoquée à chaque fois que l'usager enlève son doigt d'une touche.
        Paramètres :
            - key: la touche relâchée
            - key_modifiers : est-ce que l'usager appuie sur "shift" ou "ctrl" ?
        """
        if key == arcade.key.LSHIFT:
            self.shift_pressed = False

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Méthode invoquée lorsque le curseur de la souris se déplace dans la fenêtre.
        Paramètres:
            - x, y : les coordonnées de l'emplacement actuel de la sourir
            - delta_X, delta_y : le changement (x et y) depuis la dernière fois que la méthode a été invoqué.
        """
        self.mouse_position = x, y
        if self.mouse_pressed:
            self.dessin_custom.append(self.get_current_shape(self.mouse_position[0], self.mouse_position[1]))

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Méthode invoquée lorsque l'usager clique un bouton de la souris.
        Paramètres:
            - x, y: coordonnées où le bouton a été cliqué
            - button : le bouton de la souris appuyé
            - key_modifiers : est-ce que l'usager appuie sur "shift" ou "ctrl" ?
        """

        if button == arcade.MOUSE_BUTTON_LEFT:
            self.mouse_pressed = True
            self.mouse_position = x, y
            self.dessin_custom.append(self.get_current_shape(self.mouse_position[0], self.mouse_position[1]))
        elif button == arcade.MOUSE_BUTTON_MIDDLE:
            self.mouse_middle_click = True

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Méthode invoquée lorsque l'usager relâche le bouton cliqué de la souris.
        Paramètres:
            - x, y: coordonnées où le bouton a été relâché
            - button : le bouton de la souris relâché
            - key_modifiers : est-ce que l'usager appuie sur "shift" ou "ctrl" ?
        """

        if button == arcade.MOUSE_BUTTON_LEFT:
            self.mouse_pressed = False
            self.mouse_position = x, y
        elif button == arcade.MOUSE_BUTTON_MIDDLE:
            self.mouse_middle_click = False

    def on_mouse_scroll(self, x: int, y: int, scroll_x: int, scroll_y: int):
        multiplier = 0.8 if scroll_y == -1 else 1.3

        if self.shift_pressed:
            self.mouse_alpha *= multiplier
            self.mouse_alpha = min(max(self.mouse_alpha, 1), 255)
        else:
            self.mouse_size *= multiplier
            self.mouse_size = min(max(self.mouse_size, 0.1), 10)


def main():
    """ Main method """
    game = DessinMagnifique(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
