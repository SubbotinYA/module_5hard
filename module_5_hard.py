import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self, users=[], videos=[]):
        self.users = users
        self.videos = videos
        self.current_user = None

    def log_in(self, nickname, password):
        for userUrTube in self.users:
            if userUrTube.nickname == nickname and userUrTube.password == password:
                self.current_user = userUrTube
                return print(f'Пользователь {nickname} сейчас текущий пользователь')

    def register(self, nickname, password, age):
        if nickname in [user.nickname for user in
                        self.users]:  # создаем список пользователей с атрибутом nickname в котором проверяем на наличие поступивший nickname
            return print(f'Пользователь {nickname} уже существует')  # котором проверяем на наличие поступивший nickname
        self.users.append(User(nickname, password, age))  # добавляем экземпляр с поступившими nickname, password, age
        self.current_user = (User(nickname, password, age))

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for movie in args:
            if movie.title in [video.title for video in self.videos]:
                return print(f'видео с названием {movie.title!r} уже существует')
            self.videos.append(movie)

    def get_videos(self, text: str):
        list_search_movie = []
        for video in self.videos:
            if text.lower() in video.title.lower():
                list_search_movie.append(video.title)
        return list_search_movie

    def watch_video(self, movie_title):
        if not self.current_user:
            return print('Войдите в аккаунт, чтобы смотреть видео')
        elif self.current_user and self.current_user.age < 18:
            return print('Вам нет 18 лет, пожалуйста покиньте страницу')
        elif movie_title not in [video.title for video in self.videos]:
            return print(f'К сожалению фильм {movie_title!r} отсутствует')
        for video in self.videos:
            if movie_title == video.title:
                for i in range(1, 11):
                    print(i, end=' ')
                    time.sleep(1)
                    video.time_now += 1
                    video.time_now = 0
                print('Конец видео')


if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)

    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
