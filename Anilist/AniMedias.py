from __init__ import *

def reDate(DateJson):
    try:
        return date(DateJson["year"], DateJson["month"], DateJson["day"])
    except:
        return None


class AniMedia:
    def __init__(self, mediaType, json):
        self.id = json["id"]
        self.status = json["status"] #
        self.mediaType = mediaType
        self.format = json["format"] #
        self.description = json["description"] #
        self.endDate = reDate(json["endDate"])
        self.season = json["season"] #
        self.seasonYear = json["seasonYear"] #
        self.seasonInt = json["seasonInt"]
        self.duration = json["duration"] #
        self.countryOfOrigin = json["countryOfOrigin"]
        self.trailer = json["trailer"]
        self.coverImage = json["coverImage"] #
        self.bannerImage = json["bannerImage"]
        self.synonyms = json["synonyms"]
        self.meanScore = json["meanScore"]
        self.popularity = json["popularity"]
        self.trending = json["trending"]
        self.favourites = json["favourites"]
        self.isFavourite = json["isFavourite"]
        self.averageScore = json["averageScore"]
        self.episodes = json["episodes"] #
        self.isAdult = json["isAdult"]
        self.nextAiringEpisode = json["nextAiringEpisode"] #
        self.genres = json["genres"]
        self.startDate = reDate(json["startDate"])
        self.title = json["title"] #
        self.relations = json["relations"]
        self.chapters = json["chapters"]
        self.volumes = json["volumes"]

    def getAiredEpisodes(self):
        try:

            if (date.today() - self.startDate).total_seconds() >= 0:

                if self.nextAiringEpisode is None:
                    media_aired_episodes = self.episodes
                else:
                    media_aired_episodes = self.nextAiringEpisode["episode"] - 1
                return media_aired_episodes
            else:
                return 0
        except:
            pass
        return None


    def getTitle(self, romaji):
        if not romaji and self.title["english"] is not None:
            return self.title["english"]
        return self.title["romaji"]


class MyAniMedia(AniMedia):
    def __init__(self, mediaType, json):
        super().__init__(mediaType, json["media"])
        self.progress = json["progress"]
        self.score = json["score"]
        self.mystatus = json["status"]
