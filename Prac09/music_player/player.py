import pygame

class MusicPlayer:
    def __init__(self,playlist):
        self.playlist = playlist
        self.current_index = 0
    
    def load_current_track(self):
        pygame.mixer.music.load(self.playlist[self.current_index])
    
    def play(self):
        self.load_current_track()
        pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.stop()

    def next_track(self):
        self.current_index = (self.current_index + 1) % len(self.playlist)
        self.play()

    def previous_track(self):
        self.current_index = (self.current_index - 1) % len(self.playlist)
        self.play()
    def get_current_track_name(self):
        return self.playlist[self.current_index]