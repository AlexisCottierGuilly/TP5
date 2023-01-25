"""
Fait par Alexis Cottier-Guilly
Fait le 18 janvier 2023
Ce programme teste les dessins avec arcade en dessinant quelque chose
que l'on peut reconnaitre avec différentes formes
"""

import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Modèle de départ"

COLORS = [arcade.color.ROCKET_METALLIC, arcade.color.DARK_BROWN, arcade.color.DARK_GREEN]

CIRCLE = 0
SQUARE = 1
TRIANGLE = 2
ARC = 3
LINE = 4
POLYGON = 5
ELLIPSE = 6

SHAPES = [CIRCLE, SQUARE, TRIANGLE, ARC, LINE, POLYGON, ELLIPSE]
SHAPE_NUMBER_KEY = [arcade.key.KEY_1, arcade.key.KEY_2, arcade.key.KEY_3,
                    arcade.key.KEY_4, arcade.key.KEY_5, arcade.key.KEY_6, arcade.key.KEY_7]


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
        self.mouse_size = 1
        self.shape = CIRCLE

    def setup(self):
        """
        Configurer les variables de votre jeu ici. Il faut appeler la méthode une nouvelle
        fois si vous recommencer une nouvelle partie.
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

        return shape

    def on_draw(self):
        """
        C'est la méthode qu'Arcade invoque à chaque "frame" pour afficher les éléments
        de votre jeu à l'écran.
        """

        # Cette commande permet d'effacer l'écran avant de dessiner. Elle va dessiner l'arrière-plan
        # selon la couleur spécifiée avec la méthode "set_background_color".
        arcade.start_render()
        arcade.draw_rectangle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 6,
                                     SCREEN_WIDTH, SCREEN_HEIGHT / 3, arcade.color.ARMY_GREEN)

        self.get_current_shape(self.mouse_position[0], self.mouse_position[1]).draw()
        self.dessin_custom.draw()

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

        if key in SHAPE_NUMBER_KEY:
            self.shape = SHAPES[SHAPE_NUMBER_KEY.index(key)]
        elif key == arcade.key.R:
            self.dessin_custom = arcade.SpriteList()

    def on_key_release(self, key, key_modifiers):
        """
        Méthode invoquée à chaque fois que l'usager enlève son doigt d'une touche.
        Paramètres :
            - key: la touche relâchée
            - key_modifiers : est-ce que l'usager appuie sur "shift" ou "ctrl" ?
        """
        pass

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
        self.mouse_pressed = True
        self.mouse_position = x, y
        self.dessin_custom.append(self.get_current_shape(self.mouse_position[0], self.mouse_position[1]))

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Méthode invoquée lorsque l'usager relâche le bouton cliqué de la souris.
        Paramètres:
            - x, y: coordonnées où le bouton a été relâché
            - button : le bouton de la souris relâché
            - key_modifiers : est-ce que l'usager appuie sur "shift" ou "ctrl" ?
        """
        self.mouse_pressed = False
        self.mouse_position = x, y

    def on_mouse_scroll(self, x: int, y: int, scroll_x: int, scroll_y: int):
        self.mouse_size *= (1.3 if scroll_y == -1 else 0.8)
        self.mouse_size = min(max(self.mouse_size, 0.1), 10)


def main():
    """ Main method """
    game = DessinMagnifique(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
