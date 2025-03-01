import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock

class TicTacToeApp(App):
    def build(self):
        self.title = "Tic Tac Toe"
        self.mode = None
        self.close_event = None

        # Welcome screen
        self.welcome_screen = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.welcome_label = Label(text="Welcome to Digital Tic Tac Toe", font_size=52, color=(0, 1, 0, 1))
        self.start_button = Button(text="Click here to start", size_hint=(0.5, 0.9), font_size=50, color=(0.5, 0, 0, 1), background_color=(0, 0, 0, 1), pos_hint={'center_x': 0.5})
        self.close_button_welcome = Button(text="X", size_hint=(0.1, 0.1), pos_hint={'right': 1, 'top': 1}, color=(1, 0, 0, 1), background_color=(0.5, 0, 0, 1), on_press=self.close_app)
        self.made_by_label = Label(text="Made by Chitraaksh", font_size=30, color=(0, 1, 1, 0.5))

        self.start_button.bind(on_press=self.show_mode_selection)

        self.welcome_screen.add_widget(self.welcome_label)
        self.welcome_screen.add_widget(self.made_by_label)
        self.welcome_screen.add_widget(self.start_button)
        self.welcome_screen.add_widget(self.close_button_welcome)

        # Mode selection screen
        self.mode_selection_screen = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.mode_selection_label = Label(text="Select Mode", font_size=52, color=(0, 1, 0, 1))
        self.button_single_player = Button(text='Single Player', size_hint=(0.5, 0.2), font_size=40, color=(0, 1, 1, 1), background_color=(0, 0, 0.5, 0.8), pos_hint={'center_x': 0.5})
        self.button_single_player.bind(on_press=self.set_mode('single'))
        self.button_multiplayer = Button(text='Multiplayer', size_hint=(0.5, 0.2), font_size=40, color=(1, 0, 1, 1), background_color=(0.5, 0, 0.5, 0.8), pos_hint={'center_x': 0.5})
        self.button_multiplayer.bind(on_press=self.set_mode('multi'))
        self.close_button_mode = Button(text="X", size_hint=(0.1, 0.1), pos_hint={'right': 1, 'top': 1}, color=(1, 0, 0, 1), background_color=(0.5, 0, 0, 1), on_press=self.close_app)

        self.mode_selection_screen.add_widget(self.mode_selection_label)
        self.mode_selection_screen.add_widget(self.button_single_player)
        self.mode_selection_screen.add_widget(self.button_multiplayer)
        self.mode_selection_screen.add_widget(self.close_button_mode)

        # Game screen setup
        self.game_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.button_layout = BoxLayout(size_hint=(1, 0.2), padding=10, spacing=10)
        self.grid = GridLayout(cols=3, padding=10, spacing=10)
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.turn = 'X'
        self.status_label = Label(text="", size_hint=(1, 0.1), font_size=50, color=(0, 1, 0, 1))

        self.close_button_game = Button(text="X", size_hint=(0.1, 0.1), pos_hint={'right': 1, 'top': 1}, color=(1, 0, 0, 1), background_color=(0.5, 0, 0, 1), on_press=self.close_app)

        self.game_layout.add_widget(self.close_button_game)
        self.game_layout.add_widget(self.status_label)
        self.game_layout.add_widget(self.grid)

        for i in range(3):
            for j in range(3):
                button = Button(on_press=self.make_move(i, j), font_size=160, background_color=(0.2, 0.2, 0.2, 5))
                self.grid.add_widget(button)
                self.buttons[i][j] = button

        return self.welcome_screen  # Start with the welcome screen

    def show_mode_selection(self, instance):
        self.root.clear_widgets()
        self.root.add_widget(self.mode_selection_screen)

    def set_mode(self, mode):
        def callback(instance):
            self.mode = mode
            self.reset_board()
            self.status_label.text = f"Mode: {mode.capitalize()} - Player X's turn"
            self.status_label.color = (0, 0, 1, 1)
            self.root.clear_widgets()
            self.root.add_widget(self.game_layout)

        return callback

    def reset_board(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.turn = 'X'
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].text = ''
                self.buttons[i][j].color = (0, 0, 0, 1)
        self.status_label.text = "Player X's turn"
        self.status_label.color = (0, 0, 1, 1)

    def make_move(self, i, j):
        def callback(instance):
            if not instance.text and not self.check_winner() and self.mode:
                instance.text = self.turn
                instance.color = (0, 0, 1, 1) if self.turn == 'X' else (1, 0, 0, 1)
                self.board[i][j] = self.turn
                if self.check_winner():
                    self.status_label.text = f"Player {self.turn} wins!"
                    self.status_label.color = (0, 0, 1, 1) if self.turn == 'X' else (1, 0, 0, 1)
                    Clock.schedule_once(self.show_end_screen, 5)  # Delay of 5 seconds
                elif all(all(row) for row in self.board):
                    self.status_label.text = "It's a draw!"
                    self.status_label.color = (0, 1, 0, 1)
                    Clock.schedule_once(self.show_end_screen, 5)  # Delay of 5 seconds
                else:
                    self.turn = 'O' if self.turn == 'X' else 'X'
                    self.status_label.text = f"Player {self.turn}'s turn"
                    self.status_label.color = (0, 0, 1, 1) if self.turn == 'X' else (1, 0, 0, 1)
                    if self.mode == 'single' and self.turn == 'O':
                        self.status_label.text = "Computer's move..."
                        self.status_label.color = (1, 0, 0, 1)
                        Clock.schedule_once(self.computer_move, 1.5)

        return callback

    def show_end_screen(self, dt):  # Added dt parameter for Clock.schedule_once
        self.button_single_player.disabled = False
        self.button_multiplayer.disabled = False
        self.root.clear_widgets()
        self.root.add_widget(self.mode_selection_screen)

    def computer_move(self, dt):
        best_score = float('-inf')
        best_move = None
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '':
                    self.board[i][j] = 'O'
                    score = self.minimax(self.board, 0, False)
                    self.board[i][j] = ''
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)

        if best_move:
            i, j = best_move
            self.board[i][j] = 'O'
            self.buttons[i][j].text = 'O'
            self.buttons[i][j].color = (1, 0, 0, 1)
            if self.check_winner():
                self.status_label.text = "Player O wins!"
                self.status_label.color = (1, 0, 0, 1)
                Clock.schedule_once(self.show_end_screen, 5)  # Delay of 5 seconds
            elif all(all(row) for row in self.board):
                self.status_label.text = "It's a draw!"
                self.status_label.color = (0, 1, 0, 1)
                Clock.schedule_once(self.show_end_screen, 5)  # Delay of 5 seconds
            else:
                self.turn = 'X'
                self.status_label.text = "Player X's turn"
                self.status_label.color = (0, 0, 1, 1)

    def minimax(self, board, depth, is_maximizing):
        winner = self.check_winner()
        if winner == 'O':
            return 1
        elif winner == 'X':
            return -1
        elif all(all(row) for row in board):
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == '':
                        board[i][j] = 'O'
                        score = self.minimax(board, depth + 1, False)
                        board[i][j] = ''
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == '':
                        board[i][j] = 'X'
                        score = self.minimax(board, depth + 1, True)
                        board[i][j] = ''
                        best_score = min(score, best_score)
            return best_score

    def check_winner(self):
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] and self.board[row][0] != '':
                return self.board[row][0]
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] != '':
                return self.board[0][col]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != '':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != '':
            return self.board[0][2]
        return None

    def close_app(self, instance):
        App.get_running_app().stop()

if __name__ == '__main__':
    TicTacToeApp().run()