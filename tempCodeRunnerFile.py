                gameover = False
                    gamestarted = False
                    sprites.empty()
                    bird, game_start_message, score = create_sprites()  # Update the score variable to reference the new Score object
                    score.value = 0  # Reset the current score
                    score.highscore = load_highscore()  # Update the high score from the file