from src.playerService import Player
from src.playerService import AcademicTalent
from src.playerService import GameEvent

if __name__ == "__main__":
    player = Player("Alex", AcademicTalent())
    
    # study example
    player.study(3)
    
    # work example
    player.job_manager.set_job("Tutor")
    player.work()
    
    # social example
    player.interact_with_npc("John", "compliment")
    
    # investigation example
    print(player.ask_for_clue("John"))
    
    # event example
    print(GameEvent.survive_night(player))
    
    # save game
    player.save_game()