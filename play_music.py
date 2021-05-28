from pygame import mixer        
from pydub import AudioSegment  
from os.path import join
from os import listdir, mkdir
from time import  sleep
from shutil import copyfile, rmtree

# MUSIC_DIR = '/home/nikhil/Music/Hindi'

class MusicPlayer:
    """Class consisting of methods to handle music
    """    
    def __init__(self):
        mixer.init()
        self.music_dir = '/home/nikhil/Music/Hindi'
        try:
            mkdir("AudioFiles")
        except FileExistsError:
            print("AudioFiles already exists")
        except:
            print("Error encountered")
        self.local_music_dir = 'AudioFiles'
        self.stop = False
        self.iterator = 0
        # self.current_music = "music.wav"
    
    def start_music_player(self):
        """Imports list of songs present in default directory

        And starts playing music!!!
        """        
        self.songs = listdir(self.music_dir)
        self.stop = False
        while not self.stop:
            song_path = join(self.music_dir,self.songs[self.iterator])   
            self.play_music()
            sleep(self.get_duration(self.songs[self.iterator], song_path))
            self.iterator += 1

    def stop_music_player(self):
        self.stop_music()
        self.stop = True

    def play_music(self):
        """Plays the music

        Args:

            music (string): music from default music directory
        """        
        # self.convert_mp3_to_wav(music, path)
        # mixer.music.load(musciPath)
        mixer.music.load(self.current_music)
        mixer.music.play()

    def stop_music(self):
        """Stops playing music

        Returns:

            bool: true if music is stopped
        """        
        if(self.isPlaying()):
            mixer.music.stop()
        mixer.music.unload()
        # Remove the local music file
        return True;

    def resume_music(self):
        """Resumes music
        """        
        mixer.music.unpause()

    def pause_music(self):
        """Pauses music
        """        
        mixer.music.pause()

    def skip_to_next(self):
        pass

    def replay_music(self):
        """Replays music
        """        
        mixer.music.rewind()

    def get_volume(self):
        """Returns current volume of music player

        Returns:

            float: volume value between 0.0 and 1.0
        """        
        return mixer.music.get_volume()

    def set_volume(self, volume_level):
        """Sets the volume of music player

        Args:
            volume_level (float): value to be set
        """        
        mixer.music.set_volume(volume_level)
        print("Volume Level Set to {0}".format(self.get_volume()))

    def isPlaying(self):
        """Returns True if Music Player is playing some music

        Returns:
            [bool]
        """        
        return mixer.music.get_busy()

    def played_time(self):
        """Returns time for which music has been played

        Returns:
            [int]: time in seconds
        """        
        return mixer.music.get_pos()

    def convert_mp3_to_wav(self, music, path):
        """Converts .MP3 file to .WAV

        Args:
            music (string): name of music file
        """    
        sound = AudioSegment.from_mp3(path)
        self.current_music = join(self.local_music_dir, music[:-3] + "wav")
        sound.export(self.current_music, format="wav")    
        # if(music[-3:] == "wav"):
        #     self.current_music = music
        #     copyfile(path, join(self.local_music_dir, self.current_music))
        # else:

    def gideon_speech(self):
        sound = AudioSegment.from_mp3("gideon_audio.mp3")
        speech = join(self.local_music_dir, "gideon_audio.wav")
        sound.export(speech, format="wav")
        if(self.isPlaying()):
            self.stop_music()
        mixer.music.load(speech)
        mixer.music.play()
        audio = MP3(speech)
        sleep(audio.info.length)

    def get_duration(self, music, path):
        if(music[-3:] == "wav"):
            self.current_music = join(self.local_music_dir, music)
            copyfile(path, self.current_music)
        elif(music[-3:] == ".mp3"):
            self.convert_mp3_to_wav(music, path)
        else:
            print("Unrecognized File format")
            return
        
        try:
            import wave  
            import contextlib
            with contextlib.closing(wave.open(self.current_music, 'r')) as f:
                frames = f.getnframes()
                rate = f.getframerate()
                return frames/(float(rate))
        except:
            print("Error encountered while getting music duration")

    def __del__(self):
        print("Exiting music player")
        rmtree("AudioFiles", ignore_errors=True)
        # try:
        #     del self.songs
        # except:

