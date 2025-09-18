from datetime import datetime, date, time, timezone, tzinfo, timedelta


class TZ2(tzinfo):
    def utcoffset(self, dt):
        return timedelta(hours=2)

    def dst(self, dt):
        return timedelta(0)

    def tzname(self, dt):
        return "+02:00"

    def datetime(self, dt):
        return

    def __repr__(self):
        return f"{self.__class__.__name__}()"


# test
tt = datetime.today()
print(datetime.now())
print(tt)
